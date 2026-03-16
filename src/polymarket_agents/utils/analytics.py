"""Edge scoring and Kelly criterion utilities."""


def calculate_edge(true_prob: float, implied_prob: float) -> float:
    """Edge = estimated true probability minus market implied probability."""
    return true_prob - implied_prob


def kelly_fraction(edge: float, odds: float = 1.0) -> float:
    """
    Full Kelly fraction.
    For binary YES bet: f* = edge / (1 - implied_prob)
    Simplified here as edge / odds with floor at 0.
    """
    if odds <= 0:
        return 0.0
    return max(0.0, edge / odds)


def expected_value(true_prob: float, implied_prob: float) -> float:
    """EV per dollar bet on YES: p_true * (1/p_implied) - 1."""
    if implied_prob <= 0:
        return 0.0
    return true_prob / implied_prob - 1.0


def score_market(
    true_prob: float,
    implied_prob: float,
    volume: float,
    min_edge: float = 0.03,
    min_volume: float = 5000.0,
    min_kelly: float = 0.01,
) -> dict:
    """Compute full edge scorecard for a market."""
    edge = calculate_edge(true_prob, implied_prob)
    ev = expected_value(true_prob, implied_prob)
    kelly = kelly_fraction(edge, 1.0 - implied_prob)

    if edge > min_edge and volume >= min_volume and kelly >= min_kelly:
        action = "BET"
    elif edge > 0:
        action = "WATCH"
    else:
        action = "PASS"

    return {
        "edge": round(edge, 4),
        "expected_value": round(ev, 4),
        "kelly_fraction": round(kelly, 4),
        "action": action,
        "implied_prob": implied_prob,
        "true_prob": true_prob,
        "volume": volume,
    }
