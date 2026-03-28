"""
Polymarket CLOB trading connector.

Handles Web3 wallet setup, CLOB client initialization, order building,
and execution — all gated behind SAFE_MODE for dry-run capability.

Ported from polymarket_langchain reference and adapted to use onto-market's
config, retry, and logging utilities.
"""
from __future__ import annotations

import ast
import time
from typing import Any

import httpx
from web3 import Web3

from onto_market.config import config
from onto_market.utils.logger import get_logger
from onto_market.utils.retry import retry_with_backoff

logger = get_logger(__name__)

USDC_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
CTF_ADDRESS = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"
EXCHANGE_ADDRESS = "0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e"
NEG_RISK_EXCHANGE = "0xC5d563A36AE78145C45a50134d48A1215220f80a"

ERC20_APPROVE_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"}
        ],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]

ERC1155_APPROVAL_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "operator", "type": "address"},
            {"internalType": "bool", "name": "approved", "type": "bool"},
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    }
]


class PolymarketConnector:
    """
    CLOB trading connector for Polymarket.

    When safe_mode=True (default), order execution is logged but not posted.
    Set safe_mode=False and provide a funded wallet to trade live.
    """

    def __init__(self, safe_mode: bool | None = None):
        self.safe_mode = safe_mode if safe_mode is not None else config.SAFE_MODE

        self.gamma_url = "https://gamma-api.polymarket.com"
        self.clob_url = config.CLOB_API_URL
        self.chain_id = config.CHAIN_ID
        self.private_key = config.POLYGON_PRIVATE_KEY
        self.polygon_rpc = config.POLYGON_RPC_URL

        self.w3: Web3 | None = None
        self.account = None
        self.client = None
        self.usdc_contract = None
        self.ctf_contract = None

        if self.private_key:
            self._init_web3()
            self._init_clob_client()

    def _init_web3(self) -> None:
        self.w3 = Web3(Web3.HTTPProvider(self.polygon_rpc))

        # Inject POA middleware required for Polygon RPC compatibility
        try:
            from web3.middleware import ExtraDataToPOAMiddleware
            self.w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)
        except ImportError:
            try:
                from web3.middleware import geth_poa_middleware
                self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            except ImportError:
                logger.debug("POA middleware unavailable, skipping")

        if not self.w3.is_connected():
            logger.warning("Failed to connect to Polygon RPC: %s", self.polygon_rpc)
            return

        try:
            self.account = self.w3.eth.account.from_key(self.private_key)
            logger.info("Wallet loaded: %s", self.account.address)
        except Exception as exc:
            logger.error("Invalid private key: %s", exc)
            return

        self.usdc_contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(USDC_ADDRESS),
            abi=ERC20_APPROVE_ABI,
        )
        self.ctf_contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(CTF_ADDRESS),
            abi=ERC1155_APPROVAL_ABI,
        )

    def _init_clob_client(self) -> None:
        if not self.private_key:
            return
        try:
            from py_clob_client.client import ClobClient
            self.client = ClobClient(
                self.clob_url,
                key=self.private_key,
                chain_id=self.chain_id,
            )
            creds = self.client.create_or_derive_api_creds()
            self.client.set_api_creds(creds)
            logger.info("CLOB client initialized")
        except Exception as exc:
            logger.warning("CLOB client init failed (trading disabled): %s", exc)
            self.client = None

    def _init_approvals(self) -> None:
        """Approve CLOB exchange to spend USDC and CTF contract for conditional tokens.

        Required once per wallet before any live trade can settle on-chain.
        Safe to call on an already-approved wallet (no-op if allowance is max).
        """
        if not self.w3 or not self.account or self.safe_mode:
            return
        max_uint = 2**256 - 1
        try:
            # USDC approval for CLOB exchange
            tx = self.usdc_contract.functions.approve(
                Web3.to_checksum_address(EXCHANGE_ADDRESS), max_uint
            ).build_transaction({
                "from": self.account.address,
                "nonce": self.w3.eth.get_transaction_count(self.account.address),
            })
            signed = self.w3.eth.account.sign_transaction(tx, self.private_key)
            txh = self.w3.eth.send_raw_transaction(signed.raw_transaction)
            self.w3.eth.wait_for_transaction_receipt(txh)
            logger.info("USDC approval confirmed: %s", txh.hex())

            # CTF setApprovalForAll for the neg-risk exchange
            tx2 = self.ctf_contract.functions.setApprovalForAll(
                Web3.to_checksum_address(NEG_RISK_EXCHANGE), True
            ).build_transaction({
                "from": self.account.address,
                "nonce": self.w3.eth.get_transaction_count(self.account.address),
            })
            signed2 = self.w3.eth.account.sign_transaction(tx2, self.private_key)
            txh2 = self.w3.eth.send_raw_transaction(signed2.raw_transaction)
            self.w3.eth.wait_for_transaction_receipt(txh2)
            logger.info("CTF approval confirmed: %s", txh2.hex())
        except Exception as exc:
            logger.error("Approval transaction failed: %s", exc)

    @property
    def wallet_address(self) -> str | None:
        return self.account.address if self.account else None

    # ── Market data ────────────────────────────────────────────────────────

    @retry_with_backoff(attempts=3, min_wait=2, max_wait=30)
    def get_market(self, token_id: str) -> dict:
        params = {"clob_token_ids": token_id}
        resp = httpx.get(f"{self.gamma_url}/markets", params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if data:
            return self._map_market(data[0], token_id)
        return {}

    @retry_with_backoff(attempts=3, min_wait=2, max_wait=30)
    def get_events(self, active_only: bool = True) -> list[dict]:
        resp = httpx.get(f"{self.gamma_url}/events", timeout=30)
        resp.raise_for_status()
        events = []
        for evt in resp.json():
            try:
                mapped = self._map_event(evt)
                if active_only and not mapped.get("active"):
                    continue
                events.append(mapped)
            except Exception:
                continue
        return events

    def get_tradeable_events(self) -> list[dict]:
        return [
            e for e in self.get_events(active_only=True)
            if not e.get("restricted") and not e.get("archived") and not e.get("closed")
        ]

    def get_orderbook(self, token_id: str) -> dict:
        if not self.client:
            raise RuntimeError("CLOB client not initialized — set POLYGON_PRIVATE_KEY")
        ob = self.client.get_order_book(token_id)
        return {
            "market": ob.market if hasattr(ob, "market") else "",
            "asset_id": ob.asset_id if hasattr(ob, "asset_id") else token_id,
            "bids": [{"price": b.price, "size": b.size} for b in (ob.bids or [])],
            "asks": [{"price": a.price, "size": a.size} for a in (ob.asks or [])],
        }

    def get_orderbook_price(self, token_id: str) -> float:
        if not self.client:
            raise RuntimeError("CLOB client not initialized")
        return float(self.client.get_price(token_id))

    def get_usdc_balance(self) -> float:
        if not self.account or not self.usdc_contract:
            raise RuntimeError("Web3 not initialized — set POLYGON_PRIVATE_KEY")
        raw = self.usdc_contract.functions.balanceOf(self.account.address).call()
        return raw / 1e6

    # ── Order building & execution ─────────────────────────────────────────

    def build_order(
        self,
        token_id: str,
        price: float,
        size: float,
        side: str = "BUY",
    ) -> dict:
        """Build an order dict. In safe_mode, returns the spec without posting."""
        order_spec = {
            "token_id": token_id,
            "price": price,
            "size": size,
            "side": side,
            "timestamp": time.time(),
        }

        if self.safe_mode:
            order_spec["dry_run"] = True
            logger.info(
                "DRY RUN order: %s %s @ %.4f (size=%.2f)",
                side, token_id[:16] + "...", price, size,
            )
            return order_spec

        if not self.client:
            raise RuntimeError("CLOB client not initialized for live trading")

        from py_clob_client.clob_types import OrderArgs
        resp = self.client.create_and_post_order(
            OrderArgs(price=price, size=size, side=side, token_id=token_id)
        )
        order_spec["response"] = resp
        order_spec["dry_run"] = False
        logger.info("LIVE order posted: %s", resp)
        return order_spec

    def execute_market_order(self, token_id: str, amount: float, side: str = "BUY") -> dict:
        """Execute a market (FOK) order. Gated by safe_mode."""
        order_spec = {
            "token_id": token_id,
            "amount": amount,
            "side": side,
            "order_type": "MARKET",
            "timestamp": time.time(),
        }

        if self.safe_mode:
            order_spec["dry_run"] = True
            logger.info(
                "DRY RUN market order: %s token=%s amount=%.2f",
                side, token_id[:16] + "...", amount,
            )
            return order_spec

        if not self.client:
            raise RuntimeError("CLOB client not initialized for live trading")

        from py_clob_client.clob_types import MarketOrderArgs, OrderType
        signed = self.client.create_market_order(
            MarketOrderArgs(token_id=token_id, amount=amount, side=side)
        )
        resp = self.client.post_order(signed, orderType=OrderType.FOK)
        order_spec["response"] = resp
        order_spec["dry_run"] = False
        logger.info("LIVE market order: %s", resp)
        return order_spec

    # ── Mapping helpers ────────────────────────────────────────────────────

    @staticmethod
    def _map_market(raw: dict, token_id: str = "") -> dict:
        mapped = {
            "id": int(raw.get("id", 0)),
            "question": raw.get("question", ""),
            "end": raw.get("endDate"),
            "description": raw.get("description", ""),
            "active": raw.get("active", False),
            "funded": raw.get("funded", False),
            "rewards_min_size": float(raw.get("rewardsMinSize", 0)),
            "rewards_max_spread": float(raw.get("rewardsMaxSpread", 0)),
            "spread": float(raw.get("spread", 0)),
            "outcomes": str(raw.get("outcomes", "[]")),
            "outcome_prices": str(raw.get("outcomePrices", "[]")),
            "clob_token_ids": str(raw.get("clobTokenIds", "[]")),
        }
        if token_id:
            mapped["clob_token_ids"] = token_id
        return mapped

    @staticmethod
    def _map_event(evt: dict) -> dict:
        return {
            "id": int(evt.get("id", 0)),
            "ticker": evt.get("ticker", ""),
            "slug": evt.get("slug", ""),
            "title": evt.get("title", ""),
            "description": evt.get("description", ""),
            "active": evt.get("active", False),
            "closed": evt.get("closed", False),
            "archived": evt.get("archived", False),
            "new": evt.get("new", False),
            "featured": evt.get("featured", False),
            "restricted": evt.get("restricted", False),
            "end": evt.get("endDate"),
            "markets": ",".join(
                str(m.get("id", "")) for m in evt.get("markets", [])
            ),
        }
