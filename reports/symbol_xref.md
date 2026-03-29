# Symbol Cross-Reference

Each symbol shows where it is imported or used.

## `devtools.repo_tools._common.find_python_files` (24 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/config_surface.py` | 24 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files` |
| `src/devtools/repo_tools/config_surface.py` | 128 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/dead_weight.py` | 117 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/entrypoint_map.py` | 23 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, mod` |
| `src/devtools/repo_tools/entrypoint_map.py` | 153 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/import_graph.py` | 26 | usage | `files = find_python_files(root)` |
| `src/devtools/repo_tools/symbol_index.py` | 14 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, mod` |
| `src/devtools/repo_tools/symbol_index.py` | 115 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/symbol_xref.py` | 17 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files` |
| `src/devtools/repo_tools/symbol_xref.py` | 88 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/test_map.py` | 43 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/test_map.py` | 56 | usage | `return [p for p in find_python_files(root) if _is_test_file(p)]` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 22 | import | `from ._common import find_python_files` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 102 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 24 | import | `from ._common import find_python_files, module_name` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 83 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 25 | import | `from ._common import find_python_files, module_name, should_skip` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 123 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 16 | import | `from ._common import find_python_files, module_name` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 100 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 18 | import | `from ._common import find_python_files` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 69 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 18 | import | `from ._common import find_python_files, module_name, parse_imports` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 43 | usage | `all_files = find_python_files(repo_root)` |

## `devtools.repo_tools._common.is_internal` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 34 | usage | `if is_internal(imported, known_modules):` |

## `devtools.repo_tools._common.load_import_graph_json` (7 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 41 | import | `from devtools.repo_tools._common import OUTPUT_DIR, load_import_graph_json` |
| `src/devtools/repo_tools/architecture_drift.py` | 169 | usage | `data = load_import_graph_json()` |
| `src/devtools/repo_tools/boundary_matrix.py` | 14 | import | `from devtools.repo_tools._common import OUTPUT_DIR, load_import_graph_json` |
| `src/devtools/repo_tools/boundary_matrix.py` | 92 | usage | `data = load_import_graph_json()` |
| `src/devtools/repo_tools/cycle_detector.py` | 16 | import | `from devtools.repo_tools._common import OUTPUT_DIR, load_import_graph_json` |
| `src/devtools/repo_tools/cycle_detector.py` | 139 | usage | `data = load_import_graph_json()` |
| `src/devtools/repo_tools/dead_weight.py` | 112 | usage | `data = load_import_graph_json()` |

## `devtools.repo_tools._common.module_name` (16 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/dead_weight.py` | 118 | usage | `mod = module_name(path, root)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 23 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, mod` |
| `src/devtools/repo_tools/entrypoint_map.py` | 154 | usage | `mod = module_name(path, root)` |
| `src/devtools/repo_tools/import_graph.py` | 27 | usage | `known_modules: set[str] = {module_name(p, root) for p in files}` |
| `src/devtools/repo_tools/import_graph.py` | 31 | usage | `src = module_name(path, root)` |
| `src/devtools/repo_tools/symbol_index.py` | 14 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, mod` |
| `src/devtools/repo_tools/symbol_index.py` | 55 | usage | `mod = module_name(path, root)` |
| `src/devtools/repo_tools/test_map.py` | 44 | usage | `mod = module_name(path, root)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 24 | import | `from ._common import find_python_files, module_name` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 84 | usage | `mod = module_name(path, repo_root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 25 | import | `from ._common import find_python_files, module_name, should_skip` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 124 | usage | `mod = module_name(path, repo_root)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 16 | import | `from ._common import find_python_files, module_name` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 54 | usage | `mod = module_name(path, root)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 18 | import | `from ._common import find_python_files, module_name, parse_imports` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 49 | usage | `mod = module_name(path, repo_root)` |

## `devtools.repo_tools._common.normalize_internal_target` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 35 | usage | `dst = normalize_internal_target(imported, known_modules)` |

## `devtools.repo_tools._common.parse_imports` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 32 | usage | `imports = parse_imports(path)` |
| `src/devtools/repo_tools/test_map.py` | 70 | usage | `test_imports[str(tp)] = parse_imports(tp)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 18 | import | `from ._common import find_python_files, module_name, parse_imports` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 59 | usage | `test_imports: dict[str, set[str]] = {str(tp): parse_imports(tp) for tp in test_f` |

## `devtools.repo_tools._common.should_skip` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/_common.py` | 38 | usage | `if should_skip(path):` |
| `src/devtools/repo_tools/census.py` | 8 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, SKIP_DIRS, should_skip` |
| `src/devtools/repo_tools/census.py` | 81 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/_common.py` | 43 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/census.py` | 101 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 25 | import | `from ._common import find_python_files, module_name, should_skip` |

## `devtools.repo_tools.architecture_drift.Violation` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 76 | usage | `def find_violations(data: dict) -> list[Violation]:` |
| `src/devtools/repo_tools/architecture_drift.py` | 77 | usage | `violations: list[Violation] = []` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 122 | usage | `violations: list[Violation] = field(default_factory=list)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 129 | usage | `violations: list[Violation] = []` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 146 | usage | `Violation(` |

## `devtools.repo_tools.architecture_drift.find_violations` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 76 | usage | `def find_violations(data: dict) -> list[Violation]:` |
| `src/devtools/repo_tools/architecture_drift.py` | 170 | usage | `violations = find_violations(data)` |

## `devtools.repo_tools.architecture_drift.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.architecture_drift.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.architecture_drift.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `devtools.repo_tools.boundary_matrix.build_matrix` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/boundary_matrix.py` | 93 | usage | `pairs = build_matrix(data)` |

## `devtools.repo_tools.boundary_matrix.domain_of` (5 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |

## `devtools.repo_tools.boundary_matrix.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.boundary_matrix.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.boundary_matrix.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `devtools.repo_tools.cartography.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.census.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.census.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `devtools.repo_tools.census.write_outputs` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/census.py` | 170 | usage | `json_path, md_path = write_outputs(report)` |

## `devtools.repo_tools.config_surface.ConfigRef` (17 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/config_surface.py` | 62 | usage | `def extract_config_refs(path: Path, root: Path) -> list[ConfigRef]:` |
| `src/devtools/repo_tools/config_surface.py` | 70 | usage | `refs: list[ConfigRef] = []` |
| `src/devtools/repo_tools/config_surface.py` | 83 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 87 | usage | `refs.append(ConfigRef(".env", "dotenv_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 91 | usage | `refs.append(ConfigRef("*.yaml", "yaml_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 95 | usage | `refs.append(ConfigRef("*.json", "json_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 99 | usage | `refs.append(ConfigRef("*.toml", "toml_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 106 | usage | `refs.append(ConfigRef(key, "path_read", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 120 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 58 | usage | `def _extract(path: Path, root: Path) -> list[ConfigRef]:` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 66 | usage | `refs: list[ConfigRef] = []` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 73 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 75 | usage | `refs.append(ConfigRef(".env", "dotenv_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 77 | usage | `refs.append(ConfigRef("*.yaml", "yaml_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 79 | usage | `refs.append(ConfigRef("*.json", "json_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 81 | usage | `refs.append(ConfigRef("*.toml", "toml_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 94 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |

## `devtools.repo_tools.config_surface.extract_config_refs` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/config_surface.py` | 62 | usage | `def extract_config_refs(path: Path, root: Path) -> list[ConfigRef]:` |
| `src/devtools/repo_tools/config_surface.py` | 129 | usage | `for ref in extract_config_refs(path, root):` |

## `devtools.repo_tools.config_surface.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.config_surface.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `devtools.repo_tools.config_surface.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.config_surface.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `devtools.repo_tools.cycle_detector.build_adj` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/cycle_detector.py` | 82 | usage | `adj = build_adj(data)` |

## `devtools.repo_tools.cycle_detector.find_cycles` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/cycle_detector.py` | 140 | usage | `cycles = find_cycles(data)` |

## `devtools.repo_tools.cycle_detector.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.cycle_detector.strongconnect` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/cycle_detector.py` | 69 | usage | `strongconnect(v)` |

## `devtools.repo_tools.cycle_detector.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.cycle_detector.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `devtools.repo_tools.dead_weight.DeadFile` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 115 | usage | `dead: list[DeadFile] = []` |
| `src/devtools/repo_tools/dead_weight.py` | 136 | usage | `dead.append(DeadFile(mod, file_str, flags))` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 152 | usage | `by_flag: dict[str, list[DeadFile]] = {}` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 82 | usage | `dead: list[DeadFile] = []` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 97 | usage | `dead.append(DeadFile(mod, file_str, flags))` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 103 | usage | `dead: list[DeadFile],` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 119 | usage | `by_flag: dict[str, list[DeadFile]] = {}` |

## `devtools.repo_tools.dead_weight.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.dead_weight.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `devtools.repo_tools.dead_weight.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.dead_weight.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `devtools.repo_tools.entrypoint_map.Entrypoint` (31 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/entrypoint_map.py` | 59 | usage | `) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 60 | usage | `found: list[Entrypoint] = []` |
| `src/devtools/repo_tools/entrypoint_map.py` | 75 | usage | `Entrypoint("typer/click", mod, file_str, node.lineno, func_str)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 79 | usage | `Entrypoint("langgraph", mod, file_str, node.lineno, func_str)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 83 | usage | `Entrypoint("web-app", mod, file_str, node.lineno, func_str)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 96 | usage | `Entrypoint(` |
| `src/devtools/repo_tools/entrypoint_map.py` | 108 | usage | `Entrypoint(` |
| `src/devtools/repo_tools/entrypoint_map.py` | 120 | usage | `def _pyproject_scripts(root: Path) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 127 | usage | `entries: list[Entrypoint] = []` |
| `src/devtools/repo_tools/entrypoint_map.py` | 139 | usage | `Entrypoint(` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 151 | usage | `results: list[Entrypoint] = []` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 172 | usage | `deduped: list[Entrypoint] = []` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 74 | usage | `def _detect_frameworks(tree: ast.Module, mod: str, file_str: str) -> list[Entryp` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 75 | usage | `found: list[Entrypoint] = []` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 80 | usage | `found.append(Entrypoint("typer/click", mod, file_str, node.lineno, fname))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 82 | usage | `found.append(Entrypoint("web-app", mod, file_str, node.lineno, fname))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 84 | usage | `found.append(Entrypoint("langgraph", mod, file_str, node.lineno, fname))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 90 | usage | `found.append(Entrypoint("langgraph", mod, file_str, node.lineno, f".{attr}()"))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 92 | usage | `found.append(Entrypoint("scheduler", mod, file_str, node.lineno, f".{attr}()"))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 96 | usage | `def _pyproject_scripts(root: Path) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 102 | usage | `entries: list[Entrypoint] = []` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 114 | usage | `Entrypoint("console-script", target.split(":")[0], "pyproject.toml", i, f"{cmd} ` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 121 | usage | `results: list[Entrypoint] = []` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 139 | usage | `deduped: list[Entrypoint] = []` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `entries: list[Entrypoint],` |

## `devtools.repo_tools.entrypoint_map.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.entrypoint_map.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `devtools.repo_tools.entrypoint_map.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.entrypoint_map.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `devtools.repo_tools.import_graph.build_graph` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 85 | usage | `graph = build_graph()` |
| `src/onto_market/devtools/repo_tools/__init__.py` | 8 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 38 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 173 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 26 | import | `from .import_graph import PACKAGE_NAME, build_graph` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 103 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 27 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 71 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 26 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 77 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 169 | usage | `g = build_graph(repo_root)` |

## `devtools.repo_tools.import_graph.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.import_graph.write_dot` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 88 | usage | `dot_path = write_dot(graph)` |

## `devtools.repo_tools.import_graph.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.import_graph.write_mermaid` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 87 | usage | `mmd_path = write_mermaid(graph)` |

## `devtools.repo_tools.symbol_index.Symbol` (19 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/symbol_index.py` | 54 | usage | `def extract_symbols(path: Path, root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 63 | usage | `symbols: list[Symbol] = []` |
| `src/devtools/repo_tools/symbol_index.py` | 76 | usage | `Symbol(node.name, kind, mod, file_str, node.lineno, _base_names(node.bases))` |
| `src/devtools/repo_tools/symbol_index.py` | 84 | usage | `Symbol(` |
| `src/devtools/repo_tools/symbol_index.py` | 98 | usage | `symbols.append(Symbol(node.name, "function", mod, file_str, node.lineno))` |
| `src/devtools/repo_tools/symbol_index.py` | 103 | usage | `deduped: list[Symbol] = []` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 114 | usage | `all_symbols: list[Symbol] = []` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 53 | usage | `def _extract(path: Path, root: Path) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 62 | usage | `symbols: list[Symbol] = []` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 71 | usage | `symbols.append(Symbol(node.name, kind, mod, file_str, node.lineno, _base_names(n` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 76 | usage | `symbols.append(Symbol(f"{node.name}.{item.name}", "method", mod, file_str, item.` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 83 | usage | `symbols.append(Symbol(node.name, "function", mod, file_str, node.lineno, []))` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 87 | usage | `deduped: list[Symbol] = []` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 99 | usage | `all_symbols: list[Symbol] = []` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 106 | usage | `symbols: list[Symbol],` |

## `devtools.repo_tools.symbol_index.extract_symbols` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/symbol_index.py` | 54 | usage | `def extract_symbols(path: Path, root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 116 | usage | `all_symbols.extend(extract_symbols(path, root))` |

## `devtools.repo_tools.symbol_index.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.symbol_index.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `devtools.repo_tools.symbol_index.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.symbol_index.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `devtools.repo_tools.symbol_xref.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.symbol_xref.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `devtools.repo_tools.symbol_xref.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.symbol_xref.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `devtools.repo_tools.test_map.build_map` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/test_map.py` | 154 | usage | `coverage = build_map()` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 127 | usage | `coverage = build_map(args.root)` |

## `devtools.repo_tools.test_map.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `devtools.repo_tools.test_map.write_json` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 171 | usage | `json_path = write_json(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 95 | usage | `json_path = write_json(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 185 | usage | `json_path = write_json(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 141 | usage | `json_path = write_json(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 196 | usage | `json_path = write_json(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 216 | usage | `json_path = write_json(entries)` |
| `src/devtools/repo_tools/import_graph.py` | 86 | usage | `json_path = write_json(graph)` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 158 | usage | `json_path = write_json(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 147 | usage | `json_path = write_json(xref)` |
| `src/devtools/repo_tools/test_map.py` | 155 | usage | `json_path = write_json(coverage)` |

## `devtools.repo_tools.test_map.write_md` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 172 | usage | `md_path = write_md(violations)` |
| `src/devtools/repo_tools/boundary_matrix.py` | 96 | usage | `md_path = write_md(pairs)` |
| `src/devtools/repo_tools/config_surface.py` | 186 | usage | `md_path = write_md(surface)` |
| `src/devtools/repo_tools/cycle_detector.py` | 142 | usage | `md_path = write_md(cycles)` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 197 | usage | `md_path = write_md(dead)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 217 | usage | `md_path = write_md(entries)` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 159 | usage | `md_path = write_md(symbols)` |
| `src/devtools/repo_tools/symbol_xref.py` | 148 | usage | `md_path = write_md(xref)` |
| `src/devtools/repo_tools/test_map.py` | 156 | usage | `md_path = write_md(coverage)` |

## `onto_market.agents.memory_agent.create_memory_agent` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/__init__.py` | 1 | import | `from .memory_agent import create_memory_agent` |
| `src/onto_market/agents/memory_agent.py` | 126 | usage | `agent = create_memory_agent()` |

## `onto_market.agents.memory_agent.decide_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/memory_agent.py` | 83 | usage | `def decide_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 111 | usage | `g.add_node("decide", decide_node)` |

## `onto_market.agents.memory_agent.enrichment_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/memory_agent.py` | 35 | usage | `def enrichment_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 109 | usage | `g.add_node("enrichment", enrichment_node)` |

## `onto_market.agents.memory_agent.memory_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/memory_agent.py` | 28 | usage | `def memory_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 108 | usage | `g.add_node("memory", memory_node)` |

## `onto_market.agents.memory_agent.reasoning_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/memory_agent.py` | 63 | usage | `def reasoning_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 110 | usage | `g.add_node("reasoning", reasoning_node)` |

## `onto_market.agents.ontology_agent.ontology_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 21 | import | `from onto_market.agents.ontology_agent import ontology_node` |
| `src/onto_market/agents/planning_agent.py` | 379 | usage | `g.add_node("ontology", ontology_node)` |

## `onto_market.agents.planning_agent.create_planning_agent` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 28 | import | `from onto_market.agents.planning_agent import create_planning_agent` |
| `scripts/cli.py` | 32 | usage | `agent = create_planning_agent()` |
| `src/onto_market/agents/__init__.py` | 2 | import | `from .planning_agent import create_planning_agent` |
| `src/onto_market/agents/planning_agent.py` | 402 | usage | `agent = create_planning_agent()` |
| `src/onto_market/main.py` | 37 | import | `from onto_market.agents.planning_agent import create_planning_agent` |
| `src/onto_market/main.py` | 40 | usage | `agent = create_planning_agent()` |

## `onto_market.agents.planning_agent.decision_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 256 | usage | `def decision_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 383 | usage | `g.add_node("decision", decision_node)` |

## `onto_market.agents.planning_agent.probability_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 169 | usage | `def probability_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 381 | usage | `g.add_node("probability", probability_node)` |

## `onto_market.agents.planning_agent.research_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 94 | usage | `def research_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 378 | usage | `g.add_node("research", research_node)` |

## `onto_market.agents.planning_agent.stats_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 134 | usage | `def stats_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 380 | usage | `g.add_node("stats", stats_node)` |

## `onto_market.agents.planning_agent.swarm_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 220 | usage | `def swarm_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 382 | usage | `g.add_node("swarm", swarm_node)` |

## `onto_market.agents.planning_agent.trade_node` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 317 | usage | `def trade_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 384 | usage | `g.add_node("trade", trade_node)` |

## `onto_market.agents.state.AgentState` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/__init__.py` | 3 | import | `from .state import AgentState, MemoryAgentState, PlanningState` |
| `src/onto_market/agents/memory_agent.py` | 11 | import | `from onto_market.agents.state import MemoryAgentState` |
| `src/onto_market/agents/memory_agent.py` | 28 | usage | `def memory_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 35 | usage | `def enrichment_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 63 | usage | `def reasoning_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 83 | usage | `def decide_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 107 | usage | `g = StateGraph(MemoryAgentState)` |
| `src/onto_market/core/agent_base.py` | 8 | import | `from onto_market.core.state import AgentState` |
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.agents.state.MemoryAgentState` (7 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/__init__.py` | 3 | import | `from .state import AgentState, MemoryAgentState, PlanningState` |
| `src/onto_market/agents/memory_agent.py` | 11 | import | `from onto_market.agents.state import MemoryAgentState` |
| `src/onto_market/agents/memory_agent.py` | 28 | usage | `def memory_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 35 | usage | `def enrichment_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 63 | usage | `def reasoning_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 83 | usage | `def decide_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 107 | usage | `g = StateGraph(MemoryAgentState)` |

## `onto_market.agents.state.PlanningState` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/__init__.py` | 3 | import | `from .state import AgentState, MemoryAgentState, PlanningState` |
| `src/onto_market/agents/planning_agent.py` | 22 | import | `from onto_market.agents.state import PlanningState` |
| `src/onto_market/agents/planning_agent.py` | 94 | usage | `def research_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 134 | usage | `def stats_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 169 | usage | `def probability_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 220 | usage | `def swarm_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 256 | usage | `def decision_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 317 | usage | `def trade_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 377 | usage | `g = StateGraph(PlanningState)` |

## `onto_market.config.config.Config` (27 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/config_surface.py` | 62 | usage | `def extract_config_refs(path: Path, root: Path) -> list[ConfigRef]:` |
| `src/devtools/repo_tools/config_surface.py` | 70 | usage | `refs: list[ConfigRef] = []` |
| `src/devtools/repo_tools/config_surface.py` | 83 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 87 | usage | `refs.append(ConfigRef(".env", "dotenv_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 91 | usage | `refs.append(ConfigRef("*.yaml", "yaml_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 95 | usage | `refs.append(ConfigRef("*.json", "json_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 99 | usage | `refs.append(ConfigRef("*.toml", "toml_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 106 | usage | `refs.append(ConfigRef(key, "path_read", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 120 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/onto_market/config/__init__.py` | 1 | import | `from .config import config, Config` |
| `src/onto_market/config/config.py` | 52 | usage | `config = Config()` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 58 | usage | `def _extract(path: Path, root: Path) -> list[ConfigRef]:` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 66 | usage | `refs: list[ConfigRef] = []` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 73 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 75 | usage | `refs.append(ConfigRef(".env", "dotenv_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 77 | usage | `refs.append(ConfigRef("*.yaml", "yaml_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 79 | usage | `refs.append(ConfigRef("*.json", "json_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 81 | usage | `refs.append(ConfigRef("*.toml", "toml_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 94 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/onto_market/swarm/archetypes.py` | 42 | usage | `ARCHETYPE_REGISTRY: dict[Archetype, ArchetypeConfig] = {` |
| `src/onto_market/swarm/archetypes.py` | 43 | usage | `Archetype.BULL: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 51 | usage | `Archetype.BEAR: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 59 | usage | `Archetype.ANALYST: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 67 | usage | `Archetype.CONTRARIAN: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 75 | usage | `Archetype.NOISE_TRADER: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 83 | usage | `Archetype.INSIDER: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 105 | usage | `def from_config(cls, agent_id: int, cfg: ArchetypeConfig) -> SwarmAgent:` |

## `onto_market.connectors.gamma.GammaConnector` (21 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 67 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `scripts/cli.py` | 75 | usage | `gamma = GammaConnector()` |
| `scripts/refresh_markets.py` | 9 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `scripts/refresh_markets.py` | 25 | usage | `gamma = GammaConnector()` |
| `src/onto_market/agents/memory_agent.py` | 13 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/agents/memory_agent.py` | 20 | usage | `gamma = GammaConnector()` |
| `src/onto_market/agents/planning_agent.py` | 25 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/agents/planning_agent.py` | 36 | usage | `gamma = GammaConnector()` |
| `src/onto_market/connectors/__init__.py` | 1 | import | `from .gamma import GammaConnector` |
| `src/onto_market/context.py` | 46 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/context.py` | 47 | usage | `self._gamma = GammaConnector()` |
| `src/onto_market/trading/executor.py` | 12 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/trading/executor.py` | 32 | usage | `gamma: GammaConnector \| None = None,` |
| `src/onto_market/trading/executor.py` | 36 | usage | `self.gamma = gamma or GammaConnector()` |
| `src/onto_market/trading/trader.py` | 11 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/trading/trader.py` | 47 | usage | `gamma: GammaConnector \| None = None,` |
| `src/onto_market/trading/trader.py` | 51 | usage | `self.gamma = gamma or GammaConnector()` |
| `tests/test_planning_agent.py` | 121 | import | `from onto_market.connectors.gamma import GammaConnector, _parse_market` |
| `tests/test_planning_agent.py` | 142 | usage | `gc = GammaConnector()` |
| `tests/test_planning_agent.py` | 156 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `tests/test_planning_agent.py` | 158 | usage | `gc = GammaConnector()` |

## `onto_market.connectors.gamma.GammaConnector.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.connectors.gamma.GammaConnector.close` (0 refs)
_No references found._

## `onto_market.connectors.gamma.GammaConnector.get_market_by_id` (0 refs)
_No references found._

## `onto_market.connectors.gamma.GammaConnector.get_markets` (0 refs)
_No references found._

## `onto_market.connectors.gamma.GammaConnector.iter_markets` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/connectors/gamma.py` | 79 | usage | `def iter_markets(self, max_markets: int = 500, **kwargs) -> list[Market]:` |

## `onto_market.connectors.gamma.GammaConnector.search_markets` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/connectors/gamma.py` | 110 | usage | `def search_markets(self, query: str, limit: int = 10) -> list[Market]:` |

## `onto_market.connectors.gamma.close` (0 refs)
_No references found._

## `onto_market.connectors.gamma.get_market_by_id` (0 refs)
_No references found._

## `onto_market.connectors.gamma.get_markets` (0 refs)
_No references found._

## `onto_market.connectors.gamma.iter_markets` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/connectors/gamma.py` | 79 | usage | `def iter_markets(self, max_markets: int = 500, **kwargs) -> list[Market]:` |

## `onto_market.connectors.gamma.search_markets` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/connectors/gamma.py` | 110 | usage | `def search_markets(self, query: str, limit: int = 10) -> list[Market]:` |

## `onto_market.connectors.news.NewsConnector` (3 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 26 | import | `from onto_market.connectors.news import NewsConnector` |
| `src/onto_market/agents/planning_agent.py` | 38 | usage | `news = NewsConnector()` |
| `src/onto_market/connectors/__init__.py` | 2 | import | `from .news import NewsConnector` |

## `onto_market.connectors.news.NewsConnector.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.connectors.news.NewsConnector.get_headlines` (0 refs)
_No references found._

## `onto_market.connectors.news.NewsConnector.headlines_text` (0 refs)
_No references found._

## `onto_market.connectors.news.get_headlines` (0 refs)
_No references found._

## `onto_market.connectors.news.headlines_text` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector` (26 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 105 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `scripts/cli.py` | 110 | usage | `polymarket = PolymarketConnector(safe_mode=not live)` |
| `src/onto_market/agents/planning_agent.py` | 344 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/agents/planning_agent.py` | 349 | usage | `connector = PolymarketConnector()` |
| `src/onto_market/context.py` | 52 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/context.py` | 53 | usage | `self._polymarket = PolymarketConnector(safe_mode=self.safe_mode)` |
| `src/onto_market/trading/executor.py` | 13 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/trading/executor.py` | 33 | usage | `polymarket: PolymarketConnector \| None = None,` |
| `src/onto_market/trading/executor.py` | 37 | usage | `self.polymarket = polymarket or PolymarketConnector()` |
| `src/onto_market/trading/trader.py` | 12 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/trading/trader.py` | 48 | usage | `polymarket: PolymarketConnector \| None = None,` |
| `src/onto_market/trading/trader.py` | 52 | usage | `self.polymarket = polymarket or PolymarketConnector()` |
| `tests/test_integration.py` | 13 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `tests/test_integration.py` | 23 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 34 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 39 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 44 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_trading.py` | 5 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `tests/test_trading.py` | 13 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 17 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 21 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 35 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 44 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 55 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 73 | usage | `result = PolymarketConnector._map_market(raw)` |
| `tests/test_trading.py` | 94 | usage | `result = PolymarketConnector._map_event(raw)` |

## `onto_market.connectors.polymarket.PolymarketConnector.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.connectors.polymarket.PolymarketConnector.build_order` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector.execute_market_order` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector.get_events` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector.get_market` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector.get_orderbook` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector.get_orderbook_price` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector.get_tradeable_events` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector.get_usdc_balance` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.PolymarketConnector.wallet_address` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.build_order` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.execute_market_order` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.get_events` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.get_market` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.get_orderbook` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.get_orderbook_price` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.get_tradeable_events` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.get_usdc_balance` (0 refs)
_No references found._

## `onto_market.connectors.polymarket.wallet_address` (0 refs)
_No references found._

## `onto_market.connectors.search.SearchConnector` (3 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 27 | import | `from onto_market.connectors.search import SearchConnector` |
| `src/onto_market/agents/planning_agent.py` | 37 | usage | `search = SearchConnector()` |
| `src/onto_market/connectors/__init__.py` | 3 | import | `from .search import SearchConnector` |

## `onto_market.connectors.search.SearchConnector.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.connectors.search.SearchConnector.search` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 27 | import | `from onto_market.connectors.search import SearchConnector` |
| `src/onto_market/agents/planning_agent.py` | 37 | usage | `search = SearchConnector()` |
| `src/onto_market/agents/planning_agent.py` | 94 | usage | `def research_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 113 | usage | `research_context = search.search_text(query, max_results=3)` |
| `src/onto_market/agents/planning_agent.py` | 378 | usage | `g.add_node("research", research_node)` |
| `src/onto_market/connectors/__init__.py` | 3 | import | `from .search import SearchConnector` |
| `src/onto_market/connectors/gamma.py` | 110 | usage | `def search_markets(self, query: str, limit: int = 10) -> list[Market]:` |
| `src/onto_market/polymarket_agents/utils/__init__.py` | 3 | import | `from .objects import Market, ResearchNote` |

## `onto_market.connectors.search.SearchConnector.search_text` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 113 | usage | `research_context = search.search_text(query, max_results=3)` |

## `onto_market.connectors.search.search` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 27 | import | `from onto_market.connectors.search import SearchConnector` |
| `src/onto_market/agents/planning_agent.py` | 37 | usage | `search = SearchConnector()` |
| `src/onto_market/agents/planning_agent.py` | 94 | usage | `def research_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 113 | usage | `research_context = search.search_text(query, max_results=3)` |
| `src/onto_market/agents/planning_agent.py` | 378 | usage | `g.add_node("research", research_node)` |
| `src/onto_market/connectors/__init__.py` | 3 | import | `from .search import SearchConnector` |
| `src/onto_market/connectors/gamma.py` | 110 | usage | `def search_markets(self, query: str, limit: int = 10) -> list[Market]:` |
| `src/onto_market/polymarket_agents/utils/__init__.py` | 3 | import | `from .objects import Market, ResearchNote` |

## `onto_market.connectors.search.search_text` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 113 | usage | `research_context = search.search_text(query, max_results=3)` |

## `onto_market.context.AppContext` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/context.py` | 69 | usage | `_context: Optional[AppContext] = None` |
| `src/onto_market/context.py` | 72 | usage | `def get_context() -> AppContext:` |
| `src/onto_market/context.py` | 75 | usage | `_context = AppContext()` |
| `src/onto_market/context.py` | 79 | usage | `def set_context(ctx: AppContext) -> None:` |

## `onto_market.context.AppContext.get_gamma` (0 refs)
_No references found._

## `onto_market.context.AppContext.get_llm` (0 refs)
_No references found._

## `onto_market.context.AppContext.get_memory_manager` (0 refs)
_No references found._

## `onto_market.context.AppContext.get_polymarket` (0 refs)
_No references found._

## `onto_market.context.AppContext.reset` (0 refs)
_No references found._

## `onto_market.context.get_context` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/context.py` | 72 | usage | `def get_context() -> AppContext:` |

## `onto_market.context.get_gamma` (0 refs)
_No references found._

## `onto_market.context.get_llm` (0 refs)
_No references found._

## `onto_market.context.get_memory_manager` (0 refs)
_No references found._

## `onto_market.context.get_polymarket` (0 refs)
_No references found._

## `onto_market.context.reset` (0 refs)
_No references found._

## `onto_market.context.reset_context` (0 refs)
_No references found._

## `onto_market.context.set_context` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/context.py` | 79 | usage | `def set_context(ctx: AppContext) -> None:` |

## `onto_market.core.agent_base.AgentProtocol` (0 refs)
_No references found._

## `onto_market.core.agent_base.AgentProtocol.compile` (0 refs)
_No references found._

## `onto_market.core.agent_base.AgentProtocol.invoke` (0 refs)
_No references found._

## `onto_market.core.agent_base.BaseAgent` (0 refs)
_No references found._

## `onto_market.core.agent_base.BaseAgent.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.core.agent_base.BaseAgent.build_graph` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 85 | usage | `graph = build_graph()` |
| `src/onto_market/devtools/repo_tools/__init__.py` | 8 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 38 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 173 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 26 | import | `from .import_graph import PACKAGE_NAME, build_graph` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 103 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 27 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 71 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 26 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 77 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 169 | usage | `g = build_graph(repo_root)` |

## `onto_market.core.agent_base.BaseAgent.compile` (0 refs)
_No references found._

## `onto_market.core.agent_base.build_graph` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 85 | usage | `graph = build_graph()` |
| `src/onto_market/devtools/repo_tools/__init__.py` | 8 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 38 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 173 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 26 | import | `from .import_graph import PACKAGE_NAME, build_graph` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 103 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 27 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 71 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 26 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 77 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 169 | usage | `g = build_graph(repo_root)` |

## `onto_market.core.agent_base.compile` (0 refs)
_No references found._

## `onto_market.core.agent_base.invoke` (0 refs)
_No references found._

## `onto_market.core.graph.decorator` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/graph.py` | 14 | usage | `return decorator` |

## `onto_market.core.graph.get_graph` (0 refs)
_No references found._

## `onto_market.core.graph.list_graphs` (0 refs)
_No references found._

## `onto_market.core.graph.register_graph` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/memory_agent.py` | 102 | import | `from onto_market.core.graph import register_graph` |
| `src/onto_market/agents/memory_agent.py` | 105 | usage | `@register_graph("memory_agent")` |
| `src/onto_market/agents/planning_agent.py` | 24 | import | `from onto_market.core.graph import register_graph` |
| `src/onto_market/agents/planning_agent.py` | 375 | usage | `@register_graph("planning_agent")` |

## `onto_market.core.llm_router.get_xai_client` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/llm_router.py` | 72 | usage | `client = get_xai_client()` |

## `onto_market.core.llm_router.llm_completion` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/__init__.py` | 1 | import | `from .llm_router import llm_completion, llm_json` |
| `src/onto_market/core/llm_router.py` | 108 | usage | `raw = llm_completion(` |
| `src/onto_market/utils/llm_client.py` | 8 | import | `from onto_market.core.llm_router import llm_completion, llm_json` |
| `src/onto_market/utils/llm_client.py` | 17 | usage | `return llm_completion(` |
| `tests/test_integration.py` | 15 | import | `from onto_market.core.llm_router import llm_completion, llm_json, _LITELLM_MODEL` |
| `tests/test_integration.py` | 170 | usage | `result = llm_completion([{"role": "user", "content": "hi"}])` |
| `tests/test_integration.py` | 209 | usage | `result = llm_completion([{"role": "user", "content": "test"}])` |
| `tests/test_integration.py` | 221 | usage | `llm_completion([{"role": "user", "content": "test"}])` |

## `onto_market.core.llm_router.llm_json` (5 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/__init__.py` | 1 | import | `from .llm_router import llm_completion, llm_json` |
| `src/onto_market/utils/llm_client.py` | 8 | import | `from onto_market.core.llm_router import llm_completion, llm_json` |
| `src/onto_market/utils/llm_client.py` | 24 | usage | `return llm_json(` |
| `tests/test_integration.py` | 15 | import | `from onto_market.core.llm_router import llm_completion, llm_json, _LITELLM_MODEL` |
| `tests/test_integration.py` | 187 | usage | `result = llm_json([{"role": "user", "content": "return JSON"}])` |

## `onto_market.core.state.AgentState` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/__init__.py` | 3 | import | `from .state import AgentState, MemoryAgentState, PlanningState` |
| `src/onto_market/agents/memory_agent.py` | 11 | import | `from onto_market.agents.state import MemoryAgentState` |
| `src/onto_market/agents/memory_agent.py` | 28 | usage | `def memory_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 35 | usage | `def enrichment_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 63 | usage | `def reasoning_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 83 | usage | `def decide_node(state: MemoryAgentState) -> dict:` |
| `src/onto_market/agents/memory_agent.py` | 107 | usage | `g = StateGraph(MemoryAgentState)` |
| `src/onto_market/core/agent_base.py` | 8 | import | `from onto_market.core.state import AgentState` |
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.devtools.repo_tools._common.find_python_files` (24 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/config_surface.py` | 24 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files` |
| `src/devtools/repo_tools/config_surface.py` | 128 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/dead_weight.py` | 117 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/entrypoint_map.py` | 23 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, mod` |
| `src/devtools/repo_tools/entrypoint_map.py` | 153 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/import_graph.py` | 26 | usage | `files = find_python_files(root)` |
| `src/devtools/repo_tools/symbol_index.py` | 14 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, mod` |
| `src/devtools/repo_tools/symbol_index.py` | 115 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/symbol_xref.py` | 17 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files` |
| `src/devtools/repo_tools/symbol_xref.py` | 88 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/test_map.py` | 43 | usage | `for path in find_python_files(root):` |
| `src/devtools/repo_tools/test_map.py` | 56 | usage | `return [p for p in find_python_files(root) if _is_test_file(p)]` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 22 | import | `from ._common import find_python_files` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 102 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 24 | import | `from ._common import find_python_files, module_name` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 83 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 25 | import | `from ._common import find_python_files, module_name, should_skip` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 123 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 16 | import | `from ._common import find_python_files, module_name` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 100 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 18 | import | `from ._common import find_python_files` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 69 | usage | `for path in find_python_files(repo_root):` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 18 | import | `from ._common import find_python_files, module_name, parse_imports` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 43 | usage | `all_files = find_python_files(repo_root)` |

## `onto_market.devtools.repo_tools._common.module_name` (16 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/dead_weight.py` | 118 | usage | `mod = module_name(path, root)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 23 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, mod` |
| `src/devtools/repo_tools/entrypoint_map.py` | 154 | usage | `mod = module_name(path, root)` |
| `src/devtools/repo_tools/import_graph.py` | 27 | usage | `known_modules: set[str] = {module_name(p, root) for p in files}` |
| `src/devtools/repo_tools/import_graph.py` | 31 | usage | `src = module_name(path, root)` |
| `src/devtools/repo_tools/symbol_index.py` | 14 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, mod` |
| `src/devtools/repo_tools/symbol_index.py` | 55 | usage | `mod = module_name(path, root)` |
| `src/devtools/repo_tools/test_map.py` | 44 | usage | `mod = module_name(path, root)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 24 | import | `from ._common import find_python_files, module_name` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 84 | usage | `mod = module_name(path, repo_root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 25 | import | `from ._common import find_python_files, module_name, should_skip` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 124 | usage | `mod = module_name(path, repo_root)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 16 | import | `from ._common import find_python_files, module_name` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 54 | usage | `mod = module_name(path, root)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 18 | import | `from ._common import find_python_files, module_name, parse_imports` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 49 | usage | `mod = module_name(path, repo_root)` |

## `onto_market.devtools.repo_tools._common.parse_imports` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 32 | usage | `imports = parse_imports(path)` |
| `src/devtools/repo_tools/test_map.py` | 70 | usage | `test_imports[str(tp)] = parse_imports(tp)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 18 | import | `from ._common import find_python_files, module_name, parse_imports` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 59 | usage | `test_imports: dict[str, set[str]] = {str(tp): parse_imports(tp) for tp in test_f` |

## `onto_market.devtools.repo_tools._common.should_skip` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/_common.py` | 38 | usage | `if should_skip(path):` |
| `src/devtools/repo_tools/census.py` | 8 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, SKIP_DIRS, should_skip` |
| `src/devtools/repo_tools/census.py` | 81 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/_common.py` | 43 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/census.py` | 101 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 25 | import | `from ._common import find_python_files, module_name, should_skip` |

## `onto_market.devtools.repo_tools._paths.resolve_output_path` (27 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 37 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 232 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 25 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 141 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 23 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 60 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/census.py` | 9 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/census.py` | 190 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 23 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 116 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 26 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 123 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 25 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 108 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 26 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 155 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 23 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 233 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 9 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 410 | usage | `destination = resolve_output_path(repo_root, output_path, "REPO_MAP.md")` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 17 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 111 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 19 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 58 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 96 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 19 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 84 | usage | `output_dir = resolve_output_path(repo_root, reports_dir, "reports")` |

## `onto_market.devtools.repo_tools._paths.resolve_repo_root` (44 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `reports/streamlit_app.py` | 31 | import | `from onto_market.devtools.repo_tools._paths import resolve_repo_root  # noqa: E4` |
| `src/onto_market/devtools/repo_tools/_common.py` | 11 | import | `from ._paths import resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/_common.py` | 40 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 37 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 172 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 231 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 25 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 102 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 140 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 23 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 59 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/census.py` | 9 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/census.py` | 90 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/census.py` | 189 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 23 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 100 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 115 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 26 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 70 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 122 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 25 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 76 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 107 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 26 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 120 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 154 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 23 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 127 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 168 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 232 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 10 | import | `from ._paths import resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 12 | usage | `DEFAULT_PATH = resolve_repo_root() / "data" / "ontology.json"` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 63 | usage | `root = resolve_repo_root(path.parent.parent)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 9 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 316 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 17 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 98 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 110 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 19 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 57 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 95 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 19 | import | `from ._paths import resolve_output_path, resolve_repo_root` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 42 | usage | `repo_root = resolve_repo_root(root)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 83 | usage | `repo_root = resolve_repo_root(root)` |

## `onto_market.devtools.repo_tools.architecture_drift.ArchitectureDriftSnapshot` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 161 | usage | `return ArchitectureDriftSnapshot(` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 171 | usage | `def analyze(root: str \| Path \| None = None) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 182 | usage | `def _verdict(snapshot: ArchitectureDriftSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 191 | usage | `def render_markdown(snapshot: ArchitectureDriftSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 227 | usage | `snapshot: ArchitectureDriftSnapshot,` |

## `onto_market.devtools.repo_tools.architecture_drift.Violation` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/architecture_drift.py` | 76 | usage | `def find_violations(data: dict) -> list[Violation]:` |
| `src/devtools/repo_tools/architecture_drift.py` | 77 | usage | `violations: list[Violation] = []` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 104 | usage | `def write_json(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/architecture_drift.py` | 120 | usage | `def write_md(violations: list[Violation], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 122 | usage | `violations: list[Violation] = field(default_factory=list)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 129 | usage | `violations: list[Violation] = []` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 146 | usage | `Violation(` |

## `onto_market.devtools.repo_tools.architecture_drift.analyze` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 171 | usage | `def analyze(root: str \| Path \| None = None) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 174 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 264 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 101 | usage | `def analyze(root: str \| Path \| None = None) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 104 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 163 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 69 | usage | `def analyze(root: str \| Path \| None = None) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 72 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 145 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 167 | usage | `def analyze(root: str \| Path \| None = None) -> tuple[ImportGraphSnapshot, nx.D` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 258 | usage | `snapshot, _ = analyze(root=root)` |

## `onto_market.devtools.repo_tools.architecture_drift.analyze_from_graph` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 174 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 104 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 72 | usage | `return analyze_from_graph(g, repo_root)` |

## `onto_market.devtools.repo_tools.architecture_drift.build_parser` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 56 | usage | `args = build_parser().parse_args()` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 283 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 177 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/census.py` | 223 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 164 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 277 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 284 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 425 | usage | `args = build_parser().parse_args(argv)` |

## `onto_market.devtools.repo_tools.architecture_drift.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.architecture_drift.render_markdown` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 191 | usage | `def render_markdown(snapshot: ArchitectureDriftSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 256 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 107 | usage | `def render_markdown(snapshot: BoundaryMatrixSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 155 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/census.py` | 197 | usage | `md_path.write_text(render_markdown(report), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 90 | usage | `def render_markdown(snapshot: CycleSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 137 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 194 | usage | `def render_markdown(snapshot: ImportGraphSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 250 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |

## `onto_market.devtools.repo_tools.architecture_drift.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.architecture_drift.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.boundary_matrix.BoundaryMatrixSnapshot` (5 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 92 | usage | `return BoundaryMatrixSnapshot(` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 101 | usage | `def analyze(root: str \| Path \| None = None) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 107 | usage | `def render_markdown(snapshot: BoundaryMatrixSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 136 | usage | `snapshot: BoundaryMatrixSnapshot,` |

## `onto_market.devtools.repo_tools.boundary_matrix.analyze` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 171 | usage | `def analyze(root: str \| Path \| None = None) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 174 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 264 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 101 | usage | `def analyze(root: str \| Path \| None = None) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 104 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 163 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 69 | usage | `def analyze(root: str \| Path \| None = None) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 72 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 145 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 167 | usage | `def analyze(root: str \| Path \| None = None) -> tuple[ImportGraphSnapshot, nx.D` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 258 | usage | `snapshot, _ = analyze(root=root)` |

## `onto_market.devtools.repo_tools.boundary_matrix.analyze_from_graph` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 174 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 104 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 72 | usage | `return analyze_from_graph(g, repo_root)` |

## `onto_market.devtools.repo_tools.boundary_matrix.build_parser` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 56 | usage | `args = build_parser().parse_args()` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 283 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 177 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/census.py` | 223 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 164 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 277 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 284 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 425 | usage | `args = build_parser().parse_args(argv)` |

## `onto_market.devtools.repo_tools.boundary_matrix.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.boundary_matrix.render_markdown` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 191 | usage | `def render_markdown(snapshot: ArchitectureDriftSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 256 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 107 | usage | `def render_markdown(snapshot: BoundaryMatrixSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 155 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/census.py` | 197 | usage | `md_path.write_text(render_markdown(report), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 90 | usage | `def render_markdown(snapshot: CycleSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 137 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 194 | usage | `def render_markdown(snapshot: ImportGraphSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 250 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |

## `onto_market.devtools.repo_tools.boundary_matrix.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.boundary_matrix.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.cartography.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.cartography.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.census.build_parser` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 56 | usage | `args = build_parser().parse_args()` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 283 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 177 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/census.py` | 223 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 164 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 277 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 284 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 425 | usage | `args = build_parser().parse_args(argv)` |

## `onto_market.devtools.repo_tools.census.build_report` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/census.py` | 206 | usage | `report = build_report(root=root)` |

## `onto_market.devtools.repo_tools.census.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.census.render_markdown` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 191 | usage | `def render_markdown(snapshot: ArchitectureDriftSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 256 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 107 | usage | `def render_markdown(snapshot: BoundaryMatrixSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 155 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/census.py` | 197 | usage | `md_path.write_text(render_markdown(report), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 90 | usage | `def render_markdown(snapshot: CycleSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 137 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 194 | usage | `def render_markdown(snapshot: ImportGraphSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 250 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |

## `onto_market.devtools.repo_tools.census.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.census.should_skip` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/_common.py` | 38 | usage | `if should_skip(path):` |
| `src/devtools/repo_tools/census.py` | 8 | import | `from devtools.repo_tools._common import OUTPUT_DIR, ROOT, SKIP_DIRS, should_skip` |
| `src/devtools/repo_tools/census.py` | 81 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/_common.py` | 43 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/census.py` | 101 | usage | `if should_skip(path):` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 25 | import | `from ._common import find_python_files, module_name, should_skip` |

## `onto_market.devtools.repo_tools.census.top_level_category` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/census.py` | 112 | usage | `category = top_level_category(path, repo_root)` |

## `onto_market.devtools.repo_tools.census.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.config_surface.ConfigRef` (17 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/config_surface.py` | 62 | usage | `def extract_config_refs(path: Path, root: Path) -> list[ConfigRef]:` |
| `src/devtools/repo_tools/config_surface.py` | 70 | usage | `refs: list[ConfigRef] = []` |
| `src/devtools/repo_tools/config_surface.py` | 83 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 87 | usage | `refs.append(ConfigRef(".env", "dotenv_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 91 | usage | `refs.append(ConfigRef("*.yaml", "yaml_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 95 | usage | `refs.append(ConfigRef("*.json", "json_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 99 | usage | `refs.append(ConfigRef("*.toml", "toml_load", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 106 | usage | `refs.append(ConfigRef(key, "path_read", file_str, node.lineno))` |
| `src/devtools/repo_tools/config_surface.py` | 120 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 58 | usage | `def _extract(path: Path, root: Path) -> list[ConfigRef]:` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 66 | usage | `refs: list[ConfigRef] = []` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 73 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 75 | usage | `refs.append(ConfigRef(".env", "dotenv_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 77 | usage | `refs.append(ConfigRef("*.yaml", "yaml_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 79 | usage | `refs.append(ConfigRef("*.json", "json_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 81 | usage | `refs.append(ConfigRef("*.toml", "toml_load", file_str, node.lineno))` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 94 | usage | `refs.append(ConfigRef(key, "env_var", file_str, node.lineno))` |

## `onto_market.devtools.repo_tools.config_surface.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.config_surface.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.config_surface.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.cycle_detector.CycleSnapshot` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 60 | usage | `return CycleSnapshot(` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 69 | usage | `def analyze(root: str \| Path \| None = None) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 80 | usage | `def _verdict(snapshot: CycleSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 90 | usage | `def render_markdown(snapshot: CycleSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 118 | usage | `snapshot: CycleSnapshot,` |

## `onto_market.devtools.repo_tools.cycle_detector.analyze` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 171 | usage | `def analyze(root: str \| Path \| None = None) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 174 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 264 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 101 | usage | `def analyze(root: str \| Path \| None = None) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 104 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 163 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 69 | usage | `def analyze(root: str \| Path \| None = None) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 72 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 145 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 167 | usage | `def analyze(root: str \| Path \| None = None) -> tuple[ImportGraphSnapshot, nx.D` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 258 | usage | `snapshot, _ = analyze(root=root)` |

## `onto_market.devtools.repo_tools.cycle_detector.analyze_from_graph` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 174 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 104 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 72 | usage | `return analyze_from_graph(g, repo_root)` |

## `onto_market.devtools.repo_tools.cycle_detector.build_parser` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 56 | usage | `args = build_parser().parse_args()` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 283 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 177 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/census.py` | 223 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 164 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 277 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 284 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 425 | usage | `args = build_parser().parse_args(argv)` |

## `onto_market.devtools.repo_tools.cycle_detector.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.cycle_detector.render_markdown` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 191 | usage | `def render_markdown(snapshot: ArchitectureDriftSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 256 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 107 | usage | `def render_markdown(snapshot: BoundaryMatrixSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 155 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/census.py` | 197 | usage | `md_path.write_text(render_markdown(report), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 90 | usage | `def render_markdown(snapshot: CycleSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 137 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 194 | usage | `def render_markdown(snapshot: ImportGraphSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 250 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |

## `onto_market.devtools.repo_tools.cycle_detector.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.cycle_detector.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.dead_weight.DeadFile` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 115 | usage | `dead: list[DeadFile] = []` |
| `src/devtools/repo_tools/dead_weight.py` | 136 | usage | `dead.append(DeadFile(mod, file_str, flags))` |
| `src/devtools/repo_tools/dead_weight.py` | 141 | usage | `def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 151 | usage | `def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/dead_weight.py` | 152 | usage | `by_flag: dict[str, list[DeadFile]] = {}` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 82 | usage | `dead: list[DeadFile] = []` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 97 | usage | `dead.append(DeadFile(mod, file_str, flags))` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 103 | usage | `dead: list[DeadFile],` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 119 | usage | `by_flag: dict[str, list[DeadFile]] = {}` |

## `onto_market.devtools.repo_tools.dead_weight.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.dead_weight.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.dead_weight.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.entrypoint_map.Entrypoint` (31 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/entrypoint_map.py` | 59 | usage | `) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 60 | usage | `found: list[Entrypoint] = []` |
| `src/devtools/repo_tools/entrypoint_map.py` | 75 | usage | `Entrypoint("typer/click", mod, file_str, node.lineno, func_str)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 79 | usage | `Entrypoint("langgraph", mod, file_str, node.lineno, func_str)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 83 | usage | `Entrypoint("web-app", mod, file_str, node.lineno, func_str)` |
| `src/devtools/repo_tools/entrypoint_map.py` | 96 | usage | `Entrypoint(` |
| `src/devtools/repo_tools/entrypoint_map.py` | 108 | usage | `Entrypoint(` |
| `src/devtools/repo_tools/entrypoint_map.py` | 120 | usage | `def _pyproject_scripts(root: Path) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 127 | usage | `entries: list[Entrypoint] = []` |
| `src/devtools/repo_tools/entrypoint_map.py` | 139 | usage | `Entrypoint(` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 151 | usage | `results: list[Entrypoint] = []` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 172 | usage | `deduped: list[Entrypoint] = []` |
| `src/devtools/repo_tools/entrypoint_map.py` | 182 | usage | `def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 198 | usage | `def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 74 | usage | `def _detect_frameworks(tree: ast.Module, mod: str, file_str: str) -> list[Entryp` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 75 | usage | `found: list[Entrypoint] = []` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 80 | usage | `found.append(Entrypoint("typer/click", mod, file_str, node.lineno, fname))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 82 | usage | `found.append(Entrypoint("web-app", mod, file_str, node.lineno, fname))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 84 | usage | `found.append(Entrypoint("langgraph", mod, file_str, node.lineno, fname))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 90 | usage | `found.append(Entrypoint("langgraph", mod, file_str, node.lineno, f".{attr}()"))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 92 | usage | `found.append(Entrypoint("scheduler", mod, file_str, node.lineno, f".{attr}()"))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 96 | usage | `def _pyproject_scripts(root: Path) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 102 | usage | `entries: list[Entrypoint] = []` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 114 | usage | `Entrypoint("console-script", target.split(":")[0], "pyproject.toml", i, f"{cmd} ` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 121 | usage | `results: list[Entrypoint] = []` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 139 | usage | `deduped: list[Entrypoint] = []` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `entries: list[Entrypoint],` |

## `onto_market.devtools.repo_tools.entrypoint_map.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.entrypoint_map.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.entrypoint_map.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.import_graph.ImportGraphSnapshot` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/import_graph.py` | 167 | usage | `def analyze(root: str \| Path \| None = None) -> tuple[ImportGraphSnapshot, nx.D` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 176 | usage | `snapshot = ImportGraphSnapshot(` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 194 | usage | `def render_markdown(snapshot: ImportGraphSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 228 | usage | `snapshot: ImportGraphSnapshot,` |

## `onto_market.devtools.repo_tools.import_graph.analyze` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 171 | usage | `def analyze(root: str \| Path \| None = None) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 174 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 264 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 101 | usage | `def analyze(root: str \| Path \| None = None) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 104 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 163 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 69 | usage | `def analyze(root: str \| Path \| None = None) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 72 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 145 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 167 | usage | `def analyze(root: str \| Path \| None = None) -> tuple[ImportGraphSnapshot, nx.D` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 258 | usage | `snapshot, _ = analyze(root=root)` |

## `onto_market.devtools.repo_tools.import_graph.build_graph` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/import_graph.py` | 85 | usage | `graph = build_graph()` |
| `src/onto_market/devtools/repo_tools/__init__.py` | 8 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 38 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 173 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 26 | import | `from .import_graph import PACKAGE_NAME, build_graph` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 103 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 27 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 71 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 26 | import | `from .import_graph import build_graph` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 77 | usage | `g = build_graph(repo_root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 169 | usage | `g = build_graph(repo_root)` |

## `onto_market.devtools.repo_tools.import_graph.build_parser` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 56 | usage | `args = build_parser().parse_args()` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 283 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 177 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/census.py` | 223 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 164 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 277 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 284 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 425 | usage | `args = build_parser().parse_args(argv)` |

## `onto_market.devtools.repo_tools.import_graph.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.import_graph.render_markdown` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 191 | usage | `def render_markdown(snapshot: ArchitectureDriftSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 256 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 107 | usage | `def render_markdown(snapshot: BoundaryMatrixSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 155 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/census.py` | 197 | usage | `md_path.write_text(render_markdown(report), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 90 | usage | `def render_markdown(snapshot: CycleSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 137 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 194 | usage | `def render_markdown(snapshot: ImportGraphSnapshot) -> str:` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 250 | usage | `md_path.write_text(render_markdown(snapshot), encoding="utf-8")` |

## `onto_market.devtools.repo_tools.import_graph.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.import_graph.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.ontology_audit.audit` (3 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `src/onto_market/devtools/repo_tools/__init__.py` | 9 | import | `from .ontology_audit import audit` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 285 | usage | `audit(` |

## `onto_market.devtools.repo_tools.ontology_audit.build_parser` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 56 | usage | `args = build_parser().parse_args()` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 283 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 177 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/census.py` | 223 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 164 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 277 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 284 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 425 | usage | `args = build_parser().parse_args(argv)` |

## `onto_market.devtools.repo_tools.ontology_audit.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.repo_map.build_parser` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 56 | usage | `args = build_parser().parse_args()` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 283 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 177 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/census.py` | 223 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 164 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 277 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 284 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 425 | usage | `args = build_parser().parse_args(argv)` |

## `onto_market.devtools.repo_tools.repo_map.generate` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |

## `onto_market.devtools.repo_tools.repo_map.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.symbol_index.Symbol` (19 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/symbol_index.py` | 54 | usage | `def extract_symbols(path: Path, root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 63 | usage | `symbols: list[Symbol] = []` |
| `src/devtools/repo_tools/symbol_index.py` | 76 | usage | `Symbol(node.name, kind, mod, file_str, node.lineno, _base_names(node.bases))` |
| `src/devtools/repo_tools/symbol_index.py` | 84 | usage | `Symbol(` |
| `src/devtools/repo_tools/symbol_index.py` | 98 | usage | `symbols.append(Symbol(node.name, "function", mod, file_str, node.lineno))` |
| `src/devtools/repo_tools/symbol_index.py` | 103 | usage | `deduped: list[Symbol] = []` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 114 | usage | `all_symbols: list[Symbol] = []` |
| `src/devtools/repo_tools/symbol_index.py` | 120 | usage | `def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/devtools/repo_tools/symbol_index.py` | 137 | usage | `def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 53 | usage | `def _extract(path: Path, root: Path) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 62 | usage | `symbols: list[Symbol] = []` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 71 | usage | `symbols.append(Symbol(node.name, kind, mod, file_str, node.lineno, _base_names(n` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 76 | usage | `symbols.append(Symbol(f"{node.name}.{item.name}", "method", mod, file_str, item.` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 83 | usage | `symbols.append(Symbol(node.name, "function", mod, file_str, node.lineno, []))` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 87 | usage | `deduped: list[Symbol] = []` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 99 | usage | `all_symbols: list[Symbol] = []` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 106 | usage | `symbols: list[Symbol],` |

## `onto_market.devtools.repo_tools.symbol_index.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.symbol_index.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.symbol_index.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.symbol_xref.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.symbol_xref.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.devtools.repo_tools.symbol_xref.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.devtools.repo_tools.test_map.build_map` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/devtools/repo_tools/test_map.py` | 154 | usage | `coverage = build_map()` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 127 | usage | `coverage = build_map(args.root)` |

## `onto_market.devtools.repo_tools.test_map.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.devtools.repo_tools.test_map.write_report` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 265 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 164 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 207 | usage | `return write_report(report=report, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 158 | usage | `json_path, md_path = write_report(surface, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 146 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 162 | usage | `json_path, md_path = write_report(dead, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 186 | usage | `json_path, md_path = write_report(entries, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 259 | usage | `return write_report(snapshot, root=root, reports_dir=reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 143 | usage | `json_path, md_path = write_report(symbols, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 127 | usage | `json_path, md_path = write_report(xref, args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 128 | usage | `json_path, md_path = write_report(coverage, args.root, args.reports_dir)` |

## `onto_market.main.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `onto_market.memory.manager.MemoryManager` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/refresh_markets.py` | 10 | import | `from onto_market.memory.manager import MemoryManager` |
| `scripts/refresh_markets.py` | 26 | usage | `memory = MemoryManager(config.DATABASE_PATH)` |
| `src/onto_market/agents/memory_agent.py` | 14 | import | `from onto_market.memory.manager import MemoryManager` |
| `src/onto_market/agents/memory_agent.py` | 19 | usage | `memory = MemoryManager(config.DATABASE_PATH)` |
| `src/onto_market/agents/planning_agent.py` | 28 | import | `from onto_market.memory.manager import MemoryManager` |
| `src/onto_market/agents/planning_agent.py` | 35 | usage | `memory = MemoryManager(config.DATABASE_PATH)` |
| `src/onto_market/context.py` | 40 | import | `from onto_market.memory.manager import MemoryManager` |
| `src/onto_market/context.py` | 41 | usage | `self._memory_manager = MemoryManager(self.db_path)` |
| `src/onto_market/memory/__init__.py` | 1 | import | `from .manager import MemoryManager` |
| `tests/test_memory.py` | 2 | import | `from onto_market.memory.manager import MemoryManager` |
| `tests/test_memory.py` | 7 | usage | `mem = MemoryManager(db_path)` |
| `tests/test_memory.py` | 14 | usage | `mem = MemoryManager(db_path)` |
| `tests/test_memory.py` | 22 | usage | `mem = MemoryManager(db_path)` |

## `onto_market.memory.manager.MemoryManager.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.memory.manager.MemoryManager.get_research` (0 refs)
_No references found._

## `onto_market.memory.manager.MemoryManager.search_markets` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/connectors/gamma.py` | 110 | usage | `def search_markets(self, query: str, limit: int = 10) -> list[Market]:` |

## `onto_market.memory.manager.MemoryManager.store_analytics` (0 refs)
_No references found._

## `onto_market.memory.manager.MemoryManager.store_research` (0 refs)
_No references found._

## `onto_market.memory.manager.MemoryManager.upsert_market` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/memory/manager.py` | 18 | usage | `def upsert_market(self, market: Market) -> None:` |
| `tests/test_memory.py` | 8 | usage | `mem.upsert_market(sample_market)` |

## `onto_market.memory.manager.get_research` (0 refs)
_No references found._

## `onto_market.memory.manager.search_markets` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/connectors/gamma.py` | 110 | usage | `def search_markets(self, query: str, limit: int = 10) -> list[Market]:` |

## `onto_market.memory.manager.store_analytics` (0 refs)
_No references found._

## `onto_market.memory.manager.store_research` (0 refs)
_No references found._

## `onto_market.memory.manager.upsert_market` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/memory/manager.py` | 18 | usage | `def upsert_market(self, market: Market) -> None:` |
| `tests/test_memory.py` | 8 | usage | `mem.upsert_market(sample_market)` |

## `onto_market.memory.zep_reader.ZepEntityReader` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/memory/__init__.py` | 2 | import | `from .zep_reader import ZepEntityReader` |

## `onto_market.memory.zep_reader.ZepEntityReader.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.memory.zep_reader.ZepEntityReader.get_facts` (0 refs)
_No references found._

## `onto_market.memory.zep_reader.ZepEntityReader.store_fact` (0 refs)
_No references found._

## `onto_market.memory.zep_reader.get_facts` (0 refs)
_No references found._

## `onto_market.memory.zep_reader.store_fact` (0 refs)
_No references found._

## `onto_market.ontology.graph.OntologyGraph` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `reports/streamlit_app.py` | 117 | import | `from onto_market.ontology.graph import OntologyGraph` |
| `reports/streamlit_app.py` | 118 | usage | `og = OntologyGraph(persist_path=str(onto_path))` |
| `reports/streamlit_app.py` | 415 | import | `from onto_market.ontology.graph import OntologyGraph` |
| `reports/streamlit_app.py` | 416 | usage | `og = OntologyGraph(persist_path=str(onto_path))` |
| `src/onto_market/agents/ontology_agent.py` | 15 | import | `from onto_market.ontology.graph import OntologyGraph, Triple` |
| `src/onto_market/agents/ontology_agent.py` | 23 | usage | `onto = OntologyGraph()` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 43 | import | `from onto_market.ontology.graph import OntologyGraph` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 45 | usage | `return OntologyGraph` |
| `src/onto_market/main.py` | 72 | import | `from onto_market.ontology.graph import OntologyGraph` |
| `src/onto_market/main.py` | 73 | usage | `onto = OntologyGraph()          # loads same persisted graph` |
| `src/onto_market/ontology/__init__.py` | 1 | import | `from .graph import OntologyGraph, Triple` |

## `onto_market.ontology.graph.OntologyGraph.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.ontology.graph.OntologyGraph.add_triple` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/ontology/graph.py` | 71 | usage | `def add_triple(self, triple: Triple) -> None:` |
| `src/onto_market/ontology/graph.py` | 103 | usage | `def add_triples(self, triples: list[Triple], persist: bool = True) -> None:` |

## `onto_market.ontology.graph.OntologyGraph.add_triples` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/ontology/graph.py` | 103 | usage | `def add_triples(self, triples: list[Triple], persist: bool = True) -> None:` |

## `onto_market.ontology.graph.OntologyGraph.context_for` (0 refs)
_No references found._

## `onto_market.ontology.graph.OntologyGraph.get_entity` (0 refs)
_No references found._

## `onto_market.ontology.graph.OntologyGraph.prune` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |

## `onto_market.ontology.graph.OntologyGraph.stats` (10 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `reports/streamlit_app.py` | 119 | usage | `stats = og.stats()` |
| `reports/streamlit_app.py` | 130 | usage | `"nodes": stats["nodes"],` |
| `reports/streamlit_app.py` | 131 | usage | `"edges": stats["edges"],` |
| `reports/streamlit_app.py` | 132 | usage | `"top_entities": stats["top_entities"],` |
| `src/onto_market/agents/planning_agent.py` | 134 | usage | `def stats_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 380 | usage | `g.add_node("stats", stats_node)` |
| `src/onto_market/main.py` | 74 | usage | `stats = onto.stats()` |
| `src/onto_market/main.py` | 77 | usage | `f"({stats['nodes']} nodes, {stats['edges']} edges)")` |
| `src/onto_market/main.py` | 79 | usage | `if stats["top_entities"]:` |
| `src/onto_market/main.py` | 83 | usage | `for entity, degree in stats["top_entities"][:8]:` |

## `onto_market.ontology.graph.Triple` (7 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/ontology_agent.py` | 15 | import | `from onto_market.ontology.graph import OntologyGraph, Triple` |
| `src/onto_market/agents/ontology_agent.py` | 43 | usage | `def _extract_triples(text: str, query: str, source: str) -> list[Triple]:` |
| `src/onto_market/agents/ontology_agent.py` | 59 | usage | `triples: list[Triple] = []` |
| `src/onto_market/agents/ontology_agent.py` | 63 | usage | `Triple(` |
| `src/onto_market/ontology/__init__.py` | 1 | import | `from .graph import OntologyGraph, Triple` |
| `src/onto_market/ontology/graph.py` | 71 | usage | `def add_triple(self, triple: Triple) -> None:` |
| `src/onto_market/ontology/graph.py` | 103 | usage | `def add_triples(self, triples: list[Triple], persist: bool = True) -> None:` |

## `onto_market.ontology.graph.add_triple` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/ontology/graph.py` | 71 | usage | `def add_triple(self, triple: Triple) -> None:` |
| `src/onto_market/ontology/graph.py` | 103 | usage | `def add_triples(self, triples: list[Triple], persist: bool = True) -> None:` |

## `onto_market.ontology.graph.add_triples` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/ontology/graph.py` | 103 | usage | `def add_triples(self, triples: list[Triple], persist: bool = True) -> None:` |

## `onto_market.ontology.graph.context_for` (0 refs)
_No references found._

## `onto_market.ontology.graph.get_entity` (0 refs)
_No references found._

## `onto_market.ontology.graph.prune` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |

## `onto_market.ontology.graph.stats` (10 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `reports/streamlit_app.py` | 119 | usage | `stats = og.stats()` |
| `reports/streamlit_app.py` | 130 | usage | `"nodes": stats["nodes"],` |
| `reports/streamlit_app.py` | 131 | usage | `"edges": stats["edges"],` |
| `reports/streamlit_app.py` | 132 | usage | `"top_entities": stats["top_entities"],` |
| `src/onto_market/agents/planning_agent.py` | 134 | usage | `def stats_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 380 | usage | `g.add_node("stats", stats_node)` |
| `src/onto_market/main.py` | 74 | usage | `stats = onto.stats()` |
| `src/onto_market/main.py` | 77 | usage | `f"({stats['nodes']} nodes, {stats['edges']} edges)")` |
| `src/onto_market/main.py` | 79 | usage | `if stats["top_entities"]:` |
| `src/onto_market/main.py` | 83 | usage | `for entity, degree in stats["top_entities"][:8]:` |

## `onto_market.polymarket_agents.utils.analytics.calculate_edge` (5 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/polymarket_agents/utils/__init__.py` | 1 | import | `from .analytics import calculate_edge, expected_value, kelly_fraction, score_mar` |
| `src/onto_market/polymarket_agents/utils/analytics.py` | 36 | usage | `edge = calculate_edge(true_prob, implied_prob)` |
| `src/onto_market/trading/trader.py` | 13 | import | `from onto_market.polymarket_agents.utils.analytics import score_market, calculat` |
| `tests/test_analytics.py` | 12 | usage | `assert calculate_edge(0.60, 0.50) == pytest.approx(0.10, abs=1e-6)` |
| `tests/test_analytics.py` | 16 | usage | `assert calculate_edge(0.40, 0.55) < 0` |

## `onto_market.polymarket_agents.utils.analytics.expected_value` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/state.py` | 41 | usage | `expected_value: float` |
| `src/onto_market/polymarket_agents/utils/__init__.py` | 1 | import | `from .analytics import calculate_edge, expected_value, kelly_fraction, score_mar` |
| `src/onto_market/polymarket_agents/utils/analytics.py` | 37 | usage | `ev = expected_value(true_prob, implied_prob)` |
| `tests/test_analytics.py` | 20 | usage | `ev = expected_value(0.60, 0.50)` |

## `onto_market.polymarket_agents.utils.analytics.kelly_fraction` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/state.py` | 42 | usage | `kelly_fraction: float` |
| `src/onto_market/polymarket_agents/utils/__init__.py` | 1 | import | `from .analytics import calculate_edge, expected_value, kelly_fraction, score_mar` |
| `src/onto_market/polymarket_agents/utils/analytics.py` | 38 | usage | `kelly = kelly_fraction(edge, 1.0 - implied_prob)` |
| `src/onto_market/trading/executor.py` | 123 | usage | `half_kelly = kelly_fraction / 2.0` |
| `src/onto_market/trading/executor.py` | 136 | usage | `edge * 100, kelly_fraction * 100, half_kelly * 100,` |
| `tests/test_analytics.py` | 25 | usage | `assert kelly_fraction(0.0, 0.5) == 0.0` |

## `onto_market.polymarket_agents.utils.analytics.score_market` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/planning_agent.py` | 29 | import | `from onto_market.polymarket_agents.utils.analytics import score_market` |
| `src/onto_market/agents/planning_agent.py` | 267 | usage | `scorecard = score_market(` |
| `src/onto_market/polymarket_agents/utils/__init__.py` | 1 | import | `from .analytics import calculate_edge, expected_value, kelly_fraction, score_mar` |
| `src/onto_market/trading/trader.py` | 13 | import | `from onto_market.polymarket_agents.utils.analytics import score_market, calculat` |
| `src/onto_market/trading/trader.py` | 102 | usage | `scorecard = score_market(` |
| `tests/test_analytics.py` | 29 | usage | `result = score_market(0.65, 0.50, volume=10_000)` |
| `tests/test_analytics.py` | 35 | usage | `result = score_market(0.48, 0.50, volume=10_000)` |
| `tests/test_analytics.py` | 41 | usage | `result = score_market(0.60, 0.50, volume=100)` |

## `onto_market.polymarket_agents.utils.database.Database` (3 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/memory/manager.py` | 8 | import | `from onto_market.polymarket_agents.utils.database import Database` |
| `src/onto_market/memory/manager.py` | 14 | usage | `self.db = Database(db_path)` |
| `src/onto_market/polymarket_agents/utils/__init__.py` | 2 | import | `from .database import Database` |

## `onto_market.polymarket_agents.utils.database.Database.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.polymarket_agents.utils.database.Database.conn` (30 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 67 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `scripts/cli.py` | 105 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `scripts/refresh_markets.py` | 9 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/devtools/repo_tools/cycle_detector.py` | 69 | usage | `strongconnect(v)` |
| `src/onto_market/agents/memory_agent.py` | 13 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/agents/planning_agent.py` | 25 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/agents/planning_agent.py` | 26 | import | `from onto_market.connectors.news import NewsConnector` |
| `src/onto_market/agents/planning_agent.py` | 27 | import | `from onto_market.connectors.search import SearchConnector` |
| `src/onto_market/agents/planning_agent.py` | 344 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/agents/planning_agent.py` | 349 | usage | `connector = PolymarketConnector()` |
| `src/onto_market/context.py` | 46 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/context.py` | 52 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/trading/executor.py` | 12 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/trading/executor.py` | 13 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/trading/trader.py` | 11 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/trading/trader.py` | 12 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `tests/test_integration.py` | 13 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `tests/test_integration.py` | 23 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 34 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 39 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 44 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_planning_agent.py` | 121 | import | `from onto_market.connectors.gamma import GammaConnector, _parse_market` |
| `tests/test_planning_agent.py` | 156 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `tests/test_trading.py` | 5 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `tests/test_trading.py` | 13 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 17 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 21 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 35 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 44 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 55 | usage | `connector = PolymarketConnector(safe_mode=True)` |

## `onto_market.polymarket_agents.utils.database.Database.execute` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/oracle.py` | 158 | usage | `def _aggregate(self, rounds_executed: int) -> OracleResult:` |

## `onto_market.polymarket_agents.utils.database.Database.execute_one` (0 refs)
_No references found._

## `onto_market.polymarket_agents.utils.database.conn` (30 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 67 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `scripts/cli.py` | 105 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `scripts/refresh_markets.py` | 9 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/devtools/repo_tools/cycle_detector.py` | 69 | usage | `strongconnect(v)` |
| `src/onto_market/agents/memory_agent.py` | 13 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/agents/planning_agent.py` | 25 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/agents/planning_agent.py` | 26 | import | `from onto_market.connectors.news import NewsConnector` |
| `src/onto_market/agents/planning_agent.py` | 27 | import | `from onto_market.connectors.search import SearchConnector` |
| `src/onto_market/agents/planning_agent.py` | 344 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/agents/planning_agent.py` | 349 | usage | `connector = PolymarketConnector()` |
| `src/onto_market/context.py` | 46 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/context.py` | 52 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/trading/executor.py` | 12 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/trading/executor.py` | 13 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `src/onto_market/trading/trader.py` | 11 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `src/onto_market/trading/trader.py` | 12 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `tests/test_integration.py` | 13 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `tests/test_integration.py` | 23 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 34 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 39 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_integration.py` | 44 | usage | `connector = PolymarketConnector(safe_mode=False)` |
| `tests/test_planning_agent.py` | 121 | import | `from onto_market.connectors.gamma import GammaConnector, _parse_market` |
| `tests/test_planning_agent.py` | 156 | import | `from onto_market.connectors.gamma import GammaConnector` |
| `tests/test_trading.py` | 5 | import | `from onto_market.connectors.polymarket import PolymarketConnector` |
| `tests/test_trading.py` | 13 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 17 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 21 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 35 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 44 | usage | `connector = PolymarketConnector(safe_mode=True)` |
| `tests/test_trading.py` | 55 | usage | `connector = PolymarketConnector(safe_mode=True)` |

## `onto_market.polymarket_agents.utils.database.execute` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/oracle.py` | 158 | usage | `def _aggregate(self, rounds_executed: int) -> OracleResult:` |

## `onto_market.polymarket_agents.utils.database.execute_one` (0 refs)
_No references found._

## `onto_market.polymarket_agents.utils.objects.Market` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/connectors/gamma.py` | 6 | import | `from onto_market.polymarket_agents.utils.objects import Market` |
| `src/onto_market/connectors/gamma.py` | 79 | usage | `def iter_markets(self, max_markets: int = 500, **kwargs) -> list[Market]:` |
| `src/onto_market/connectors/gamma.py` | 81 | usage | `markets: list[Market] = []` |
| `src/onto_market/connectors/gamma.py` | 110 | usage | `def search_markets(self, query: str, limit: int = 10) -> list[Market]:` |
| `src/onto_market/connectors/gamma.py` | 119 | usage | `markets: list[Market] = []` |
| `src/onto_market/connectors/gamma.py` | 133 | usage | `def _parse_market(raw: dict) -> Market:` |
| `src/onto_market/connectors/gamma.py` | 150 | usage | `return Market(` |
| `src/onto_market/memory/manager.py` | 9 | import | `from onto_market.polymarket_agents.utils.objects import Market` |
| `src/onto_market/memory/manager.py` | 18 | usage | `def upsert_market(self, market: Market) -> None:` |
| `src/onto_market/polymarket_agents/utils/__init__.py` | 3 | import | `from .objects import Market, ResearchNote` |
| `tests/conftest.py` | 4 | import | `from onto_market.polymarket_agents.utils.objects import Market` |
| `tests/conftest.py` | 8 | usage | `def sample_market() -> Market:` |
| `tests/conftest.py` | 9 | usage | `return Market(` |
| `tests/test_memory.py` | 3 | import | `from onto_market.polymarket_agents.utils.objects import Market` |

## `onto_market.polymarket_agents.utils.objects.Market.implied_probability` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/state.py` | 33 | usage | `implied_probability: float` |

## `onto_market.polymarket_agents.utils.objects.Market.no_token_id` (0 refs)
_No references found._

## `onto_market.polymarket_agents.utils.objects.Market.yes_token_id` (0 refs)
_No references found._

## `onto_market.polymarket_agents.utils.objects.ResearchNote` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/polymarket_agents/utils/__init__.py` | 3 | import | `from .objects import Market, ResearchNote` |

## `onto_market.polymarket_agents.utils.objects.implied_probability` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/agents/state.py` | 33 | usage | `implied_probability: float` |

## `onto_market.polymarket_agents.utils.objects.no_token_id` (0 refs)
_No references found._

## `onto_market.polymarket_agents.utils.objects.yes_token_id` (0 refs)
_No references found._

## `onto_market.swarm.archetypes.Archetype` (24 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/__init__.py` | 3 | import | `from onto_market.swarm.archetypes import SwarmAgent, Archetype, ARCHETYPE_REGIST` |
| `src/onto_market/swarm/archetypes.py` | 28 | usage | `name: Archetype` |
| `src/onto_market/swarm/archetypes.py` | 42 | usage | `ARCHETYPE_REGISTRY: dict[Archetype, ArchetypeConfig] = {` |
| `src/onto_market/swarm/archetypes.py` | 43 | usage | `Archetype.BULL: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 44 | usage | `name=Archetype.BULL,` |
| `src/onto_market/swarm/archetypes.py` | 51 | usage | `Archetype.BEAR: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 52 | usage | `name=Archetype.BEAR,` |
| `src/onto_market/swarm/archetypes.py` | 59 | usage | `Archetype.ANALYST: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 60 | usage | `name=Archetype.ANALYST,` |
| `src/onto_market/swarm/archetypes.py` | 67 | usage | `Archetype.CONTRARIAN: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 68 | usage | `name=Archetype.CONTRARIAN,` |
| `src/onto_market/swarm/archetypes.py` | 75 | usage | `Archetype.NOISE_TRADER: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 76 | usage | `name=Archetype.NOISE_TRADER,` |
| `src/onto_market/swarm/archetypes.py` | 83 | usage | `Archetype.INSIDER: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 84 | usage | `name=Archetype.INSIDER,` |
| `src/onto_market/swarm/archetypes.py` | 97 | usage | `archetype: Archetype` |
| `src/onto_market/swarm/archetypes.py` | 105 | usage | `def from_config(cls, agent_id: int, cfg: ArchetypeConfig) -> SwarmAgent:` |
| `src/onto_market/swarm/oracle.py` | 112 | usage | `if agent.archetype == Archetype.ANALYST and analyst_idx < len(analyst_estimates)` |
| `src/onto_market/swarm/oracle.py` | 127 | usage | `1 for a in self.agents if a.archetype == Archetype.ANALYST` |
| `tests/test_swarm.py` | 17 | usage | `for archetype in Archetype:` |
| `tests/test_swarm.py` | 38 | usage | `cfg = ARCHETYPE_REGISTRY[Archetype.BULL]` |
| `tests/test_swarm.py` | 40 | usage | `assert agent.archetype == Archetype.BULL` |
| `tests/test_swarm.py` | 44 | usage | `cfg = ARCHETYPE_REGISTRY[Archetype.NOISE_TRADER]` |
| `tests/test_swarm.py` | 50 | usage | `cfg = ARCHETYPE_REGISTRY[Archetype.CONTRARIAN]` |

## `onto_market.swarm.archetypes.ArchetypeConfig` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/archetypes.py` | 42 | usage | `ARCHETYPE_REGISTRY: dict[Archetype, ArchetypeConfig] = {` |
| `src/onto_market/swarm/archetypes.py` | 43 | usage | `Archetype.BULL: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 51 | usage | `Archetype.BEAR: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 59 | usage | `Archetype.ANALYST: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 67 | usage | `Archetype.CONTRARIAN: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 75 | usage | `Archetype.NOISE_TRADER: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 83 | usage | `Archetype.INSIDER: ArchetypeConfig(` |
| `src/onto_market/swarm/archetypes.py` | 105 | usage | `def from_config(cls, agent_id: int, cfg: ArchetypeConfig) -> SwarmAgent:` |

## `onto_market.swarm.archetypes.ArchetypeConfig.sample_bias` (0 refs)
_No references found._

## `onto_market.swarm.archetypes.ArchetypeConfig.sample_confidence` (0 refs)
_No references found._

## `onto_market.swarm.archetypes.SwarmAgent` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/__init__.py` | 3 | import | `from onto_market.swarm.archetypes import SwarmAgent, Archetype, ARCHETYPE_REGIST` |
| `src/onto_market/swarm/archetypes.py` | 105 | usage | `def from_config(cls, agent_id: int, cfg: ArchetypeConfig) -> SwarmAgent:` |
| `src/onto_market/swarm/archetypes.py` | 132 | usage | `def spawn_agents(swarm_size: int) -> list[SwarmAgent]:` |
| `src/onto_market/swarm/archetypes.py` | 134 | usage | `agents: list[SwarmAgent] = []` |
| `src/onto_market/swarm/archetypes.py` | 140 | usage | `agents.append(SwarmAgent.from_config(agent_id, cfg))` |
| `src/onto_market/swarm/archetypes.py` | 146 | usage | `agents.append(SwarmAgent.from_config(agent_id, cfg))` |
| `src/onto_market/swarm/dynamics.py` | 14 | import | `from onto_market.swarm.archetypes import SwarmAgent` |
| `src/onto_market/swarm/dynamics.py` | 34 | usage | `agents: list[SwarmAgent],` |
| `src/onto_market/swarm/dynamics.py` | 66 | usage | `agents: list[SwarmAgent],` |
| `src/onto_market/swarm/dynamics.py` | 75 | usage | `agents: list[SwarmAgent],` |
| `src/onto_market/swarm/oracle.py` | 65 | usage | `self.agents: list[SwarmAgent] = spawn_agents(self.swarm_size)` |
| `tests/test_swarm.py` | 39 | usage | `agent = SwarmAgent.from_config(0, cfg)` |
| `tests/test_swarm.py` | 45 | usage | `agent = SwarmAgent.from_config(0, cfg)` |

## `onto_market.swarm.archetypes.SwarmAgent.from_config` (5 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/archetypes.py` | 105 | usage | `def from_config(cls, agent_id: int, cfg: ArchetypeConfig) -> SwarmAgent:` |
| `src/onto_market/swarm/archetypes.py` | 140 | usage | `agents.append(SwarmAgent.from_config(agent_id, cfg))` |
| `src/onto_market/swarm/archetypes.py` | 146 | usage | `agents.append(SwarmAgent.from_config(agent_id, cfg))` |
| `tests/test_swarm.py` | 39 | usage | `agent = SwarmAgent.from_config(0, cfg)` |
| `tests/test_swarm.py` | 45 | usage | `agent = SwarmAgent.from_config(0, cfg)` |

## `onto_market.swarm.archetypes.SwarmAgent.seed_estimate` (0 refs)
_No references found._

## `onto_market.swarm.archetypes.SwarmAgent.update_from_neighbors` (0 refs)
_No references found._

## `onto_market.swarm.archetypes.from_config` (5 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/archetypes.py` | 105 | usage | `def from_config(cls, agent_id: int, cfg: ArchetypeConfig) -> SwarmAgent:` |
| `src/onto_market/swarm/archetypes.py` | 140 | usage | `agents.append(SwarmAgent.from_config(agent_id, cfg))` |
| `src/onto_market/swarm/archetypes.py` | 146 | usage | `agents.append(SwarmAgent.from_config(agent_id, cfg))` |
| `tests/test_swarm.py` | 39 | usage | `agent = SwarmAgent.from_config(0, cfg)` |
| `tests/test_swarm.py` | 45 | usage | `agent = SwarmAgent.from_config(0, cfg)` |

## `onto_market.swarm.archetypes.sample_bias` (0 refs)
_No references found._

## `onto_market.swarm.archetypes.sample_confidence` (0 refs)
_No references found._

## `onto_market.swarm.archetypes.seed_estimate` (0 refs)
_No references found._

## `onto_market.swarm.archetypes.spawn_agents` (11 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/archetypes.py` | 132 | usage | `def spawn_agents(swarm_size: int) -> list[SwarmAgent]:` |
| `src/onto_market/swarm/oracle.py` | 65 | usage | `self.agents: list[SwarmAgent] = spawn_agents(self.swarm_size)` |
| `tests/test_swarm.py` | 25 | usage | `agents = spawn_agents(100)` |
| `tests/test_swarm.py` | 29 | usage | `agents = spawn_agents(5000)` |
| `tests/test_swarm.py` | 33 | usage | `agents = spawn_agents(200)` |
| `tests/test_swarm.py` | 54 | usage | `agents = spawn_agents(1000)` |
| `tests/test_swarm.py` | 70 | usage | `agents = spawn_agents(50)` |
| `tests/test_swarm.py` | 81 | usage | `agents = spawn_agents(50)` |
| `tests/test_swarm.py` | 87 | usage | `agents = spawn_agents(50)` |
| `tests/test_swarm.py` | 93 | usage | `agents = spawn_agents(100)` |
| `tests/test_swarm.py` | 102 | usage | `agents = spawn_agents(10)` |

## `onto_market.swarm.archetypes.update_from_neighbors` (0 refs)
_No references found._

## `onto_market.swarm.dynamics.build_network` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 66 | usage | `self.network = build_network(self.swarm_size)` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 61 | usage | `g = build_network(100)` |
| `tests/test_swarm.py` | 65 | usage | `g = build_network(10)` |
| `tests/test_swarm.py` | 71 | usage | `network = build_network(50)` |
| `tests/test_swarm.py` | 94 | usage | `network = build_network(100)` |
| `tests/test_swarm.py` | 103 | usage | `network = build_network(10)` |

## `onto_market.swarm.dynamics.check_convergence` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/dynamics.py` | 95 | usage | `if check_convergence(agents, convergence_threshold):` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 84 | usage | `assert check_convergence(agents, threshold=0.01)` |
| `tests/test_swarm.py` | 90 | usage | `assert not check_convergence(agents, threshold=0.01)` |

## `onto_market.swarm.dynamics.propagate_influence` (3 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/dynamics.py` | 87 | usage | `propagate_influence(agents, network)` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 75 | usage | `propagate_influence(agents, network)` |

## `onto_market.swarm.dynamics.run_dynamics` (5 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `onto_market.swarm.oracle.OracleResult` (6 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/__init__.py` | 2 | import | `from onto_market.swarm.oracle import SocialSentimentOracle, OracleResult` |
| `src/onto_market/swarm/oracle.py` | 74 | usage | `) -> OracleResult:` |
| `src/onto_market/swarm/oracle.py` | 158 | usage | `def _aggregate(self, rounds_executed: int) -> OracleResult:` |
| `src/onto_market/swarm/oracle.py` | 192 | usage | `return OracleResult(` |
| `tests/test_swarm.py` | 12 | import | `from onto_market.swarm.oracle import SocialSentimentOracle, OracleResult` |
| `tests/test_swarm.py` | 114 | usage | `assert isinstance(result, OracleResult)` |

## `onto_market.swarm.oracle.SocialSentimentOracle` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 142 | import | `from onto_market.swarm.oracle import SocialSentimentOracle` |
| `scripts/cli.py` | 152 | usage | `oracle = SocialSentimentOracle(` |
| `src/onto_market/agents/planning_agent.py` | 30 | import | `from onto_market.swarm.oracle import SocialSentimentOracle` |
| `src/onto_market/agents/planning_agent.py` | 229 | usage | `oracle = SocialSentimentOracle()` |
| `src/onto_market/swarm/__init__.py` | 2 | import | `from onto_market.swarm.oracle import SocialSentimentOracle, OracleResult` |
| `tests/test_swarm.py` | 12 | import | `from onto_market.swarm.oracle import SocialSentimentOracle, OracleResult` |
| `tests/test_swarm.py` | 112 | usage | `oracle = SocialSentimentOracle(swarm_size=100, max_rounds=3)` |
| `tests/test_swarm.py` | 117 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |
| `tests/test_swarm.py` | 122 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |
| `tests/test_swarm.py` | 127 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |
| `tests/test_swarm.py` | 132 | usage | `oracle = SocialSentimentOracle(swarm_size=150, max_rounds=2)` |
| `tests/test_swarm.py` | 138 | usage | `oracle = SocialSentimentOracle(swarm_size=500, max_rounds=5)` |
| `tests/test_swarm.py` | 143 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |
| `tests/test_swarm.py` | 148 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |

## `onto_market.swarm.oracle.SocialSentimentOracle.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.swarm.oracle.SocialSentimentOracle.estimate` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/archetypes.py` | 101 | usage | `estimate: float = 0.5` |
| `src/onto_market/swarm/oracle.py` | 112 | usage | `if agent.archetype == Archetype.ANALYST and analyst_idx < len(analyst_estimates)` |

## `onto_market.swarm.oracle.estimate` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/swarm/archetypes.py` | 101 | usage | `estimate: float = 0.5` |
| `src/onto_market/swarm/oracle.py` | 112 | usage | `if agent.archetype == Archetype.ANALYST and analyst_idx < len(analyst_estimates)` |

## `onto_market.trading.executor.TradeExecutor` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/trading/__init__.py` | 3 | import | `from onto_market.trading.executor import TradeExecutor` |
| `src/onto_market/trading/trader.py` | 14 | import | `from onto_market.trading.executor import TradeExecutor` |
| `src/onto_market/trading/trader.py` | 53 | usage | `self.executor = TradeExecutor(` |
| `tests/test_trading.py` | 6 | import | `from onto_market.trading.executor import TradeExecutor` |
| `tests/test_trading.py` | 111 | usage | `executor = TradeExecutor(llm=mock_llm)` |
| `tests/test_trading.py` | 126 | usage | `executor = TradeExecutor(llm=mock_llm)` |
| `tests/test_trading.py` | 134 | usage | `executor = TradeExecutor(polymarket=mock_poly)` |
| `tests/test_trading.py` | 142 | usage | `executor = TradeExecutor(polymarket=mock_poly)` |
| `tests/test_trading.py` | 153 | usage | `executor = TradeExecutor(llm=mock_llm)` |

## `onto_market.trading.executor.TradeExecutor.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.trading.executor.TradeExecutor.filter_events` (0 refs)
_No references found._

## `onto_market.trading.executor.TradeExecutor.size_trade` (0 refs)
_No references found._

## `onto_market.trading.executor.TradeExecutor.superforecast` (0 refs)
_No references found._

## `onto_market.trading.executor.filter_events` (0 refs)
_No references found._

## `onto_market.trading.executor.size_trade` (0 refs)
_No references found._

## `onto_market.trading.executor.superforecast` (0 refs)
_No references found._

## `onto_market.trading.trader.Trader` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 104 | import | `from onto_market.trading.trader import Trader` |
| `scripts/cli.py` | 111 | usage | `trader = Trader(polymarket=polymarket)` |
| `src/onto_market/trading/__init__.py` | 2 | import | `from onto_market.trading.trader import Trader` |
| `tests/test_integration.py` | 14 | import | `from onto_market.trading.trader import Trader` |
| `tests/test_integration.py` | 83 | usage | `trader = Trader(llm=mock_llm, gamma=mock_gamma, polymarket=mock_poly)` |
| `tests/test_integration.py` | 113 | usage | `trader = Trader(gamma=mock_gamma)` |
| `tests/test_integration.py` | 127 | usage | `trader = Trader(gamma=mock_gamma)` |
| `tests/test_integration.py` | 137 | usage | `trader = Trader(gamma=mock_gamma)` |
| `tests/test_integration.py` | 149 | usage | `trader = Trader(gamma=mock_gamma)` |
| `tests/test_trading.py` | 7 | import | `from onto_market.trading.trader import Trader` |
| `tests/test_trading.py` | 164 | usage | `trader = Trader(polymarket=mock_poly)` |
| `tests/test_trading.py` | 182 | usage | `trader = Trader(llm=mock_llm, gamma=mock_gamma, polymarket=mock_poly)` |
| `tests/test_trading.py` | 197 | usage | `trader = Trader(gamma=mock_gamma)` |

## `onto_market.trading.trader.Trader.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.trading.trader.Trader.one_best_trade` (0 refs)
_No references found._

## `onto_market.trading.trader.one_best_trade` (0 refs)
_No references found._

## `onto_market.utils.file_parser.parse_csv` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/utils/file_parser.py` | 40 | usage | `return parse_csv(path)` |

## `onto_market.utils.file_parser.parse_file` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/utils/__init__.py` | 1 | import | `from .file_parser import parse_file` |

## `onto_market.utils.file_parser.parse_txt` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/utils/file_parser.py` | 38 | usage | `return parse_txt(path)` |

## `onto_market.utils.llm_client.LLMClient` (17 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 143 | import | `from onto_market.utils.llm_client import LLMClient` |
| `scripts/cli.py` | 156 | usage | `llm = LLMClient()` |
| `src/onto_market/agents/memory_agent.py` | 15 | import | `from onto_market.utils.llm_client import LLMClient` |
| `src/onto_market/agents/memory_agent.py` | 21 | usage | `llm = LLMClient()` |
| `src/onto_market/agents/ontology_agent.py` | 16 | import | `from onto_market.utils.llm_client import LLMClient` |
| `src/onto_market/agents/ontology_agent.py` | 20 | usage | `llm = LLMClient()` |
| `src/onto_market/agents/planning_agent.py` | 31 | import | `from onto_market.utils.llm_client import LLMClient` |
| `src/onto_market/agents/planning_agent.py` | 39 | usage | `llm = LLMClient()` |
| `src/onto_market/context.py` | 58 | import | `from onto_market.utils.llm_client import LLMClient` |
| `src/onto_market/context.py` | 59 | usage | `self._llm = LLMClient()` |
| `src/onto_market/trading/executor.py` | 14 | import | `from onto_market.utils.llm_client import LLMClient` |
| `src/onto_market/trading/executor.py` | 31 | usage | `llm: LLMClient \| None = None,` |
| `src/onto_market/trading/executor.py` | 35 | usage | `self.llm = llm or LLMClient()` |
| `src/onto_market/trading/trader.py` | 15 | import | `from onto_market.utils.llm_client import LLMClient` |
| `src/onto_market/trading/trader.py` | 46 | usage | `llm: LLMClient \| None = None,` |
| `src/onto_market/trading/trader.py` | 50 | usage | `self.llm = llm or LLMClient()` |
| `src/onto_market/utils/__init__.py` | 2 | import | `from .llm_client import LLMClient` |

## `onto_market.utils.llm_client.LLMClient.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.utils.llm_client.LLMClient.chat` (0 refs)
_No references found._

## `onto_market.utils.llm_client.LLMClient.chat_json` (0 refs)
_No references found._

## `onto_market.utils.llm_client.LLMClient.strip_think_tags` (0 refs)
_No references found._

## `onto_market.utils.llm_client.LLMClient.system` (0 refs)
_No references found._

## `onto_market.utils.llm_client.LLMClient.user` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `tests/test_integration.py` | 170 | usage | `result = llm_completion([{"role": "user", "content": "hi"}])` |
| `tests/test_integration.py` | 187 | usage | `result = llm_json([{"role": "user", "content": "return JSON"}])` |
| `tests/test_integration.py` | 209 | usage | `result = llm_completion([{"role": "user", "content": "test"}])` |
| `tests/test_integration.py` | 221 | usage | `llm_completion([{"role": "user", "content": "test"}])` |

## `onto_market.utils.llm_client.chat` (0 refs)
_No references found._

## `onto_market.utils.llm_client.chat_json` (0 refs)
_No references found._

## `onto_market.utils.llm_client.strip_think_tags` (0 refs)
_No references found._

## `onto_market.utils.llm_client.system` (0 refs)
_No references found._

## `onto_market.utils.llm_client.user` (4 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `tests/test_integration.py` | 170 | usage | `result = llm_completion([{"role": "user", "content": "hi"}])` |
| `tests/test_integration.py` | 187 | usage | `result = llm_json([{"role": "user", "content": "return JSON"}])` |
| `tests/test_integration.py` | 209 | usage | `result = llm_completion([{"role": "user", "content": "test"}])` |
| `tests/test_integration.py` | 221 | usage | `llm_completion([{"role": "user", "content": "test"}])` |

## `onto_market.utils.logger.get_logger` (27 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/refresh_markets.py` | 11 | import | `from onto_market.utils.logger import get_logger` |
| `scripts/refresh_markets.py` | 14 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/agents/memory_agent.py` | 16 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/agents/memory_agent.py` | 18 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/agents/ontology_agent.py` | 17 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/agents/ontology_agent.py` | 19 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/agents/planning_agent.py` | 32 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/agents/planning_agent.py` | 34 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/connectors/gamma.py` | 7 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/connectors/gamma.py` | 10 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/connectors/news.py` | 4 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/connectors/news.py` | 7 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/connectors/polymarket.py` | 20 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/connectors/polymarket.py` | 23 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/connectors/search.py` | 4 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/connectors/search.py` | 7 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/main.py` | 16 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/main.py` | 19 | usage | `logger = get_logger("onto-market")` |
| `src/onto_market/swarm/dynamics.py` | 15 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/swarm/dynamics.py` | 17 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/swarm/oracle.py` | 25 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/swarm/oracle.py` | 27 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/trading/executor.py` | 15 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/trading/executor.py` | 17 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/trading/trader.py` | 16 | import | `from onto_market.utils.logger import get_logger` |
| `src/onto_market/trading/trader.py` | 18 | usage | `logger = get_logger(__name__)` |
| `src/onto_market/utils/__init__.py` | 3 | import | `from .logger import get_logger` |

## `onto_market.utils.logger.setup_logger` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/utils/logger.py` | 41 | usage | `return setup_logger(name, level)` |

## `onto_market.utils.retry.RetryableAPIClient` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/utils/__init__.py` | 4 | import | `from .retry import RetryableAPIClient, retry_with_backoff` |

## `onto_market.utils.retry.RetryableAPIClient.__init__` (1 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/core/agent_base.py` | 24 | usage | `def __init__(self, state_schema: type[AgentState] = AgentState):` |

## `onto_market.utils.retry.retry_with_backoff` (13 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/connectors/gamma.py` | 8 | import | `from onto_market.utils.retry import retry_with_backoff` |
| `src/onto_market/connectors/gamma.py` | 32 | usage | `@retry_with_backoff(attempts=3, min_wait=2, max_wait=30)` |
| `src/onto_market/connectors/gamma.py` | 60 | usage | `@retry_with_backoff(attempts=3, min_wait=2, max_wait=30)` |
| `src/onto_market/connectors/gamma.py` | 109 | usage | `@retry_with_backoff(attempts=3, min_wait=2, max_wait=30)` |
| `src/onto_market/connectors/news.py` | 5 | import | `from onto_market.utils.retry import retry_with_backoff` |
| `src/onto_market/connectors/news.py` | 14 | usage | `@retry_with_backoff(attempts=3, min_wait=2, max_wait=20)` |
| `src/onto_market/connectors/polymarket.py` | 21 | import | `from onto_market.utils.retry import retry_with_backoff` |
| `src/onto_market/connectors/polymarket.py` | 186 | usage | `@retry_with_backoff(attempts=3, min_wait=2, max_wait=30)` |
| `src/onto_market/connectors/polymarket.py` | 196 | usage | `@retry_with_backoff(attempts=3, min_wait=2, max_wait=30)` |
| `src/onto_market/connectors/search.py` | 5 | import | `from onto_market.utils.retry import retry_with_backoff` |
| `src/onto_market/connectors/search.py` | 23 | usage | `@retry_with_backoff(attempts=3, min_wait=2, max_wait=20)` |
| `src/onto_market/utils/__init__.py` | 4 | import | `from .retry import RetryableAPIClient, retry_with_backoff` |
| `src/onto_market/utils/retry.py` | 40 | usage | `fn = retry_with_backoff(**self._retry_kwargs)(self._client)` |

## `scripts._bootstrap.run` (38 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/audit_ontology.py` | 4 | import | `from _bootstrap import run` |
| `scripts/audit_ontology.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.ontology_audit"))` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/generate_repo_map.py` | 4 | import | `from _bootstrap import run` |
| `scripts/generate_repo_map.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.repo_map"))` |
| `scripts/repo_census.py` | 5 | import | `from _bootstrap import run` |
| `scripts/repo_census.py` | 8 | usage | `raise SystemExit(run("onto_market.devtools.repo_tools.census"))` |
| `src/devtools/repo_tools/census.py` | 169 | usage | `report = run()` |
| `src/devtools/repo_tools/config_surface.py` | 184 | usage | `surface = run()` |
| `src/devtools/repo_tools/dead_weight.py` | 111 | usage | `def run(root: Path = ROOT) -> list[DeadFile]:` |
| `src/devtools/repo_tools/dead_weight.py` | 195 | usage | `dead = run()` |
| `src/devtools/repo_tools/entrypoint_map.py` | 150 | usage | `def run(root: Path = ROOT) -> list[Entrypoint]:` |
| `src/devtools/repo_tools/entrypoint_map.py` | 215 | usage | `entries = run()` |
| `src/devtools/repo_tools/symbol_index.py` | 113 | usage | `def run(root: Path = ROOT) -> list[Symbol]:` |
| `src/devtools/repo_tools/symbol_index.py` | 157 | usage | `symbols = run()` |
| `src/devtools/repo_tools/symbol_xref.py` | 146 | usage | `xref = run()` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 284 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 178 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 110 | usage | `return run(args.root, args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/census.py` | 224 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 157 | usage | `surface = run(args.root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 165 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 75 | usage | `def run(root: Path \| None = None) -> list[DeadFile]:` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 161 | usage | `dead = run(args.root)` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 119 | usage | `def run(root: Path \| None = None) -> list[Entrypoint]:` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 185 | usage | `entries = run(args.root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 278 | usage | `json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 232 | usage | `if to_prune and prune:` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 426 | usage | `generate(root=args.root, dry_run=args.dry, output_path=args.output)` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 97 | usage | `def run(root: Path \| None = None) -> list[Symbol]:` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 142 | usage | `symbols = run(args.root)` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 126 | usage | `xref = run(args.root, args.reports_dir)` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 86 | usage | `rounds = run_dynamics(` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 98 | usage | `rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05` |
| `tests/test_swarm.py` | 106 | usage | `rounds = run_dynamics(agents, network, max_rounds=0)` |

## `scripts.cli.analyze` (14 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 127 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 171 | usage | `def analyze(root: str \| Path \| None = None) -> ArchitectureDriftSnapshot:` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 174 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 264 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 70 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 101 | usage | `def analyze(root: str \| Path \| None = None) -> BoundaryMatrixSnapshot:` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 104 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 163 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 46 | usage | `def analyze_from_graph(g: nx.DiGraph, root: Path) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 69 | usage | `def analyze(root: str \| Path \| None = None) -> CycleSnapshot:` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 72 | usage | `return analyze_from_graph(g, repo_root)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 145 | usage | `snapshot = analyze(root=root)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 167 | usage | `def analyze(root: str \| Path \| None = None) -> tuple[ImportGraphSnapshot, nx.D` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 258 | usage | `snapshot, _ = analyze(root=root)` |

## `scripts.cli.scan` (0 refs)
_No references found._

## `scripts.cli.swarm` (23 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 142 | import | `from onto_market.swarm.oracle import SocialSentimentOracle` |
| `src/onto_market/agents/planning_agent.py` | 30 | import | `from onto_market.swarm.oracle import SocialSentimentOracle` |
| `src/onto_market/agents/planning_agent.py` | 220 | usage | `def swarm_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 382 | usage | `g.add_node("swarm", swarm_node)` |
| `src/onto_market/swarm/__init__.py` | 2 | import | `from onto_market.swarm.oracle import SocialSentimentOracle, OracleResult` |
| `src/onto_market/swarm/__init__.py` | 3 | import | `from onto_market.swarm.archetypes import SwarmAgent, Archetype, ARCHETYPE_REGIST` |
| `src/onto_market/swarm/archetypes.py` | 132 | usage | `def spawn_agents(swarm_size: int) -> list[SwarmAgent]:` |
| `src/onto_market/swarm/dynamics.py` | 14 | import | `from onto_market.swarm.archetypes import SwarmAgent` |
| `src/onto_market/swarm/oracle.py` | 19 | import | `from onto_market.swarm.archetypes import (` |
| `src/onto_market/swarm/oracle.py` | 24 | import | `from onto_market.swarm.dynamics import build_network, run_dynamics` |
| `src/onto_market/swarm/oracle.py` | 65 | usage | `self.agents: list[SwarmAgent] = spawn_agents(self.swarm_size)` |
| `src/onto_market/swarm/oracle.py` | 66 | usage | `self.network = build_network(self.swarm_size)` |
| `tests/test_swarm.py` | 4 | import | `from onto_market.swarm.archetypes import (` |
| `tests/test_swarm.py` | 11 | import | `from onto_market.swarm.dynamics import build_network, propagate_influence, check` |
| `tests/test_swarm.py` | 12 | import | `from onto_market.swarm.oracle import SocialSentimentOracle, OracleResult` |
| `tests/test_swarm.py` | 112 | usage | `oracle = SocialSentimentOracle(swarm_size=100, max_rounds=3)` |
| `tests/test_swarm.py` | 117 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |
| `tests/test_swarm.py` | 122 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |
| `tests/test_swarm.py` | 127 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |
| `tests/test_swarm.py` | 132 | usage | `oracle = SocialSentimentOracle(swarm_size=150, max_rounds=2)` |
| `tests/test_swarm.py` | 138 | usage | `oracle = SocialSentimentOracle(swarm_size=500, max_rounds=5)` |
| `tests/test_swarm.py` | 143 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |
| `tests/test_swarm.py` | 148 | usage | `oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)` |

## `scripts.cli.trade` (23 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/cli.py` | 53 | usage | `trade = result.get("trade_result", {})` |
| `scripts/cli.py` | 54 | usage | `if trade and not trade.get("skipped"):` |
| `scripts/cli.py` | 55 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `scripts/cli.py` | 56 | usage | `console.print(f"\n  [bold]Trade:[/] [{dry}] {trade.get('side', 'BUY')} @ {trade.` |
| `scripts/cli.py` | 104 | import | `from onto_market.trading.trader import Trader` |
| `scripts/cli.py` | 111 | usage | `trader = Trader(polymarket=polymarket)` |
| `src/onto_market/agents/planning_agent.py` | 317 | usage | `def trade_node(state: PlanningState) -> dict:` |
| `src/onto_market/agents/planning_agent.py` | 384 | usage | `g.add_node("trade", trade_node)` |
| `src/onto_market/agents/planning_agent.py` | 415 | usage | `trade = result.get("trade_result", {})` |
| `src/onto_market/agents/planning_agent.py` | 416 | usage | `if trade and not trade.get("skipped"):` |
| `src/onto_market/agents/planning_agent.py` | 417 | usage | `dry = "DRY RUN" if trade.get("dry_run") else "LIVE"` |
| `src/onto_market/agents/planning_agent.py` | 418 | usage | `print(f"  Trade:  [{dry}] {trade.get('side', '')} @ {trade.get('price', '')}")` |
| `src/onto_market/trading/__init__.py` | 2 | import | `from onto_market.trading.trader import Trader` |
| `tests/test_integration.py` | 14 | import | `from onto_market.trading.trader import Trader` |
| `tests/test_integration.py` | 83 | usage | `trader = Trader(llm=mock_llm, gamma=mock_gamma, polymarket=mock_poly)` |
| `tests/test_integration.py` | 113 | usage | `trader = Trader(gamma=mock_gamma)` |
| `tests/test_integration.py` | 127 | usage | `trader = Trader(gamma=mock_gamma)` |
| `tests/test_integration.py` | 137 | usage | `trader = Trader(gamma=mock_gamma)` |
| `tests/test_integration.py` | 149 | usage | `trader = Trader(gamma=mock_gamma)` |
| `tests/test_trading.py` | 7 | import | `from onto_market.trading.trader import Trader` |
| `tests/test_trading.py` | 164 | usage | `trader = Trader(polymarket=mock_poly)` |
| `tests/test_trading.py` | 182 | usage | `trader = Trader(llm=mock_llm, gamma=mock_gamma, polymarket=mock_poly)` |
| `tests/test_trading.py` | 197 | usage | `trader = Trader(gamma=mock_gamma)` |

## `scripts.import_graph.build_parser` (8 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 56 | usage | `args = build_parser().parse_args()` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 283 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 177 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/census.py` | 223 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 164 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 277 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 284 | usage | `args = build_parser().parse_args(argv)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 425 | usage | `args = build_parser().parse_args(argv)` |

## `scripts.import_graph.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `scripts.refresh_markets.main` (59 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `scripts/import_graph.py` | 76 | usage | `raise SystemExit(main())` |
| `scripts/refresh_markets.py` | 37 | usage | `main()` |
| `scripts/repo_tools/architecture_drift.py` | 9 | import | `from onto_market.devtools.repo_tools.architecture_drift import main` |
| `scripts/repo_tools/architecture_drift.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/boundary_matrix.py` | 9 | import | `from onto_market.devtools.repo_tools.boundary_matrix import main` |
| `scripts/repo_tools/boundary_matrix.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cartography.py` | 9 | import | `from onto_market.devtools.repo_tools.cartography import main` |
| `scripts/repo_tools/cartography.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/config_surface.py` | 9 | import | `from onto_market.devtools.repo_tools.config_surface import main` |
| `scripts/repo_tools/config_surface.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/cycle_detector.py` | 9 | import | `from onto_market.devtools.repo_tools.cycle_detector import main` |
| `scripts/repo_tools/cycle_detector.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/dead_weight.py` | 9 | import | `from onto_market.devtools.repo_tools.dead_weight import main` |
| `scripts/repo_tools/dead_weight.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/entrypoint_map.py` | 9 | import | `from onto_market.devtools.repo_tools.entrypoint_map import main` |
| `scripts/repo_tools/entrypoint_map.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/import_graph.py` | 9 | import | `from onto_market.devtools.repo_tools.import_graph import main` |
| `scripts/repo_tools/import_graph.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_index.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_index import main` |
| `scripts/repo_tools/symbol_index.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/symbol_xref.py` | 9 | import | `from onto_market.devtools.repo_tools.symbol_xref import main` |
| `scripts/repo_tools/symbol_xref.py` | 12 | usage | `raise SystemExit(main())` |
| `scripts/repo_tools/test_map.py` | 9 | import | `from onto_market.devtools.repo_tools.test_map import main` |
| `scripts/repo_tools/test_map.py` | 12 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/architecture_drift.py` | 42 | import | `from devtools.repo_tools.boundary_matrix import DOMAINS, TIER, domain_of` |
| `src/devtools/repo_tools/architecture_drift.py` | 83 | usage | `src_domain = domain_of(src_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 84 | usage | `dst_domain = domain_of(dst_mod)` |
| `src/devtools/repo_tools/architecture_drift.py` | 98 | usage | `Violation(src_domain, dst_domain, src_mod, dst_mod, rule)` |
| `src/devtools/repo_tools/architecture_drift.py` | 189 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/boundary_matrix.py` | 48 | usage | `src = domain_of(edge["source"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 49 | usage | `dst = domain_of(edge["target"])` |
| `src/devtools/repo_tools/boundary_matrix.py` | 110 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cartography.py` | 96 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/census.py` | 178 | usage | `main()` |
| `src/devtools/repo_tools/config_surface.py` | 197 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/cycle_detector.py` | 156 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/dead_weight.py` | 212 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/entrypoint_map.py` | 164 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/devtools/repo_tools/entrypoint_map.py` | 231 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/import_graph.py` | 100 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_index.py` | 173 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/symbol_xref.py` | 161 | usage | `raise SystemExit(main())` |
| `src/devtools/repo_tools/test_map.py` | 170 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/architecture_drift.py` | 291 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/boundary_matrix.py` | 185 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cartography.py` | 114 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/census.py` | 231 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/config_surface.py` | 168 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/cycle_detector.py` | 172 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/dead_weight.py` | 177 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 133 | usage | `results.append(Entrypoint("__main__", mod, file_str, line))` |
| `src/onto_market/devtools/repo_tools/entrypoint_map.py` | 200 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/import_graph.py` | 285 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/ontology_audit.py` | 296 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 431 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_index.py` | 157 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/symbol_xref.py` | 138 | usage | `raise SystemExit(main())` |
| `src/onto_market/devtools/repo_tools/test_map.py` | 140 | usage | `raise SystemExit(main())` |
| `src/onto_market/main.py` | 91 | usage | `main()` |

## `tests.conftest.db_path` (9 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `src/onto_market/context.py` | 22 | usage | `db_path: str = field(` |
| `src/onto_market/context.py` | 41 | usage | `self._memory_manager = MemoryManager(self.db_path)` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 197 | usage | `db_path = root / "data" / "memory.db"` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 198 | usage | `if not db_path.exists():` |
| `src/onto_market/devtools/repo_tools/repo_map.py` | 200 | usage | `return {"size_kb": db_path.stat().st_size // 1024, "exists": True}` |
| `src/onto_market/memory/manager.py` | 14 | usage | `self.db = Database(db_path)` |
| `tests/test_memory.py` | 7 | usage | `mem = MemoryManager(db_path)` |
| `tests/test_memory.py` | 14 | usage | `mem = MemoryManager(db_path)` |
| `tests/test_memory.py` | 22 | usage | `mem = MemoryManager(db_path)` |

## `tests.conftest.sample_market` (2 refs)

| File | Line | Kind | Context |
|------|-----:|------|---------|
| `tests/conftest.py` | 8 | usage | `def sample_market() -> Market:` |
| `tests/test_memory.py` | 8 | usage | `mem.upsert_market(sample_market)` |

## `tests.test_analytics.test_edge_negative` (0 refs)
_No references found._

## `tests.test_analytics.test_edge_positive` (0 refs)
_No references found._

## `tests.test_analytics.test_expected_value` (0 refs)
_No references found._

## `tests.test_analytics.test_kelly_zero_when_no_edge` (0 refs)
_No references found._

## `tests.test_analytics.test_score_market_bet` (0 refs)
_No references found._

## `tests.test_analytics.test_score_market_pass` (0 refs)
_No references found._

## `tests.test_analytics.test_score_market_watch_low_volume` (0 refs)
_No references found._

## `tests.test_integration.TestEventIdFallback` (0 refs)
_No references found._

## `tests.test_integration.TestEventIdFallback.test_fallback_failure_is_logged_not_raised` (0 refs)
_No references found._

## `tests.test_integration.TestEventIdFallback.test_fallback_skipped_when_event_has_no_id` (0 refs)
_No references found._

## `tests.test_integration.TestEventIdFallback.test_fallback_triggered_when_per_id_returns_none` (0 refs)
_No references found._

## `tests.test_integration.TestEventIdFallback.test_no_fallback_when_per_id_succeeds` (0 refs)
_No references found._

## `tests.test_integration.TestLLMProviderRouting` (0 refs)
_No references found._

## `tests.test_integration.TestLLMProviderRouting.test_grok_disables_tools_for_json` (0 refs)
_No references found._

## `tests.test_integration.TestLLMProviderRouting.test_grok_uses_xai_client` (0 refs)
_No references found._

## `tests.test_integration.TestLLMProviderRouting.test_litellm_model_map_is_complete` (0 refs)
_No references found._

## `tests.test_integration.TestLLMProviderRouting.test_non_grok_providers_use_litellm` (0 refs)
_No references found._

## `tests.test_integration.TestLLMProviderRouting.test_unknown_provider_raises` (0 refs)
_No references found._

## `tests.test_integration.TestLiveOrderPath` (0 refs)
_No references found._

## `tests.test_integration.TestLiveOrderPath.test_build_order_live_raises_without_clob_client` (0 refs)
_No references found._

## `tests.test_integration.TestLiveOrderPath.test_full_trade_pipeline_live_mode` (0 refs)
_No references found._

## `tests.test_integration.TestLiveOrderPath.test_get_orderbook_raises_without_clob_client` (0 refs)
_No references found._

## `tests.test_integration.TestLiveOrderPath.test_get_usdc_balance_raises_without_web3` (0 refs)
_No references found._

## `tests.test_integration.TestLiveOrderPath.test_market_order_live_raises_without_clob_client` (0 refs)
_No references found._

## `tests.test_integration.test_build_order_live_raises_without_clob_client` (0 refs)
_No references found._

## `tests.test_integration.test_fallback_failure_is_logged_not_raised` (0 refs)
_No references found._

## `tests.test_integration.test_fallback_skipped_when_event_has_no_id` (0 refs)
_No references found._

## `tests.test_integration.test_fallback_triggered_when_per_id_returns_none` (0 refs)
_No references found._

## `tests.test_integration.test_full_trade_pipeline_live_mode` (0 refs)
_No references found._

## `tests.test_integration.test_get_orderbook_raises_without_clob_client` (0 refs)
_No references found._

## `tests.test_integration.test_get_usdc_balance_raises_without_web3` (0 refs)
_No references found._

## `tests.test_integration.test_grok_disables_tools_for_json` (0 refs)
_No references found._

## `tests.test_integration.test_grok_uses_xai_client` (0 refs)
_No references found._

## `tests.test_integration.test_litellm_model_map_is_complete` (0 refs)
_No references found._

## `tests.test_integration.test_market_order_live_raises_without_clob_client` (0 refs)
_No references found._

## `tests.test_integration.test_no_fallback_when_per_id_succeeds` (0 refs)
_No references found._

## `tests.test_integration.test_non_grok_providers_use_litellm` (0 refs)
_No references found._

## `tests.test_integration.test_unknown_provider_raises` (0 refs)
_No references found._

## `tests.test_memory.test_store_analytics` (0 refs)
_No references found._

## `tests.test_memory.test_store_and_get_research` (0 refs)
_No references found._

## `tests.test_memory.test_upsert_and_search` (0 refs)
_No references found._

## `tests.test_planning_agent.TestMarketFromObj` (0 refs)
_No references found._

## `tests.test_planning_agent.TestMarketFromObj.test_converts_market_object` (0 refs)
_No references found._

## `tests.test_planning_agent.TestNormalizeMarket` (0 refs)
_No references found._

## `tests.test_planning_agent.TestNormalizeMarket.test_db_row_with_json_strings` (0 refs)
_No references found._

## `tests.test_planning_agent.TestNormalizeMarket.test_empty_string_token_ids` (0 refs)
_No references found._

## `tests.test_planning_agent.TestNormalizeMarket.test_live_market_already_has_implied` (0 refs)
_No references found._

## `tests.test_planning_agent.TestNormalizeMarket.test_malformed_json_string_falls_back` (0 refs)
_No references found._

## `tests.test_planning_agent.TestNormalizeMarket.test_missing_prices_defaults_to_half` (0 refs)
_No references found._

## `tests.test_planning_agent.TestScoreMarketMatch` (0 refs)
_No references found._

## `tests.test_planning_agent.TestScoreMarketMatch.test_case_insensitive` (0 refs)
_No references found._

## `tests.test_planning_agent.TestScoreMarketMatch.test_empty_tokens` (0 refs)
_No references found._

## `tests.test_planning_agent.TestScoreMarketMatch.test_full_overlap_beats_volume` (0 refs)
_No references found._

## `tests.test_planning_agent.TestScoreMarketMatch.test_zero_overlap_gets_volume_only` (0 refs)
_No references found._

## `tests.test_planning_agent.TestSearchMarketsIntegration` (0 refs)
_No references found._

## `tests.test_planning_agent.TestSearchMarketsIntegration.test_gamma_search_empty_results` (0 refs)
_No references found._

## `tests.test_planning_agent.TestSearchMarketsIntegration.test_gamma_search_returns_market_objects` (0 refs)
_No references found._

## `tests.test_planning_agent.TestStopwords` (0 refs)
_No references found._

## `tests.test_planning_agent.TestStopwords.test_common_words_filtered` (0 refs)
_No references found._

## `tests.test_planning_agent.TestStopwords.test_meaningful_tokens_not_filtered` (0 refs)
_No references found._

## `tests.test_planning_agent.test_case_insensitive` (0 refs)
_No references found._

## `tests.test_planning_agent.test_common_words_filtered` (0 refs)
_No references found._

## `tests.test_planning_agent.test_converts_market_object` (0 refs)
_No references found._

## `tests.test_planning_agent.test_db_row_with_json_strings` (0 refs)
_No references found._

## `tests.test_planning_agent.test_empty_string_token_ids` (0 refs)
_No references found._

## `tests.test_planning_agent.test_empty_tokens` (0 refs)
_No references found._

## `tests.test_planning_agent.test_full_overlap_beats_volume` (0 refs)
_No references found._

## `tests.test_planning_agent.test_gamma_search_empty_results` (0 refs)
_No references found._

## `tests.test_planning_agent.test_gamma_search_returns_market_objects` (0 refs)
_No references found._

## `tests.test_planning_agent.test_live_market_already_has_implied` (0 refs)
_No references found._

## `tests.test_planning_agent.test_malformed_json_string_falls_back` (0 refs)
_No references found._

## `tests.test_planning_agent.test_meaningful_tokens_not_filtered` (0 refs)
_No references found._

## `tests.test_planning_agent.test_missing_prices_defaults_to_half` (0 refs)
_No references found._

## `tests.test_planning_agent.test_zero_overlap_gets_volume_only` (0 refs)
_No references found._

## `tests.test_repo_tools.test_architecture_drift_allows_legal_import` (0 refs)
_No references found._

## `tests.test_repo_tools.test_architecture_drift_catches_violation` (0 refs)
_No references found._

## `tests.test_repo_tools.test_architecture_drift_connectors_cannot_import_swarm` (0 refs)
_No references found._

## `tests.test_repo_tools.test_architecture_drift_on_real_repo` (0 refs)
_No references found._

## `tests.test_repo_tools.test_architecture_drift_write_reports` (0 refs)
_No references found._

## `tests.test_repo_tools.test_boundary_matrix_counts_cross_domain_edges` (0 refs)
_No references found._

## `tests.test_repo_tools.test_boundary_matrix_ignores_intra_domain` (0 refs)
_No references found._

## `tests.test_repo_tools.test_boundary_matrix_on_real_repo` (0 refs)
_No references found._

## `tests.test_repo_tools.test_cycle_detector_dag_has_no_cycles` (0 refs)
_No references found._

## `tests.test_repo_tools.test_cycle_detector_finds_cycle` (0 refs)
_No references found._

## `tests.test_repo_tools.test_cycle_detector_on_real_repo` (0 refs)
_No references found._

## `tests.test_repo_tools.test_cycle_detector_write_reports` (0 refs)
_No references found._

## `tests.test_repo_tools.test_import_graph_discovers_edge` (0 refs)
_No references found._

## `tests.test_repo_tools.test_import_graph_no_self_loops` (0 refs)
_No references found._

## `tests.test_repo_tools.test_import_graph_on_real_repo` (0 refs)
_No references found._

## `tests.test_repo_tools.test_import_graph_relative_import` (0 refs)
_No references found._

## `tests.test_repo_tools.test_import_graph_snapshot_counts` (0 refs)
_No references found._

## `tests.test_repo_tools.test_import_graph_write_reports` (0 refs)
_No references found._

## `tests.test_repo_tools.test_ontology_audit_runs_on_simple_graph` (0 refs)
_No references found._

## `tests.test_repo_tools.test_repo_census_builds_and_writes_reports` (0 refs)
_No references found._

## `tests.test_repo_tools.test_repo_map_generates_markdown` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_agent_from_config` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_all_archetypes_registered` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_archetype_diversity` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_contrarian_has_negative_alpha` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_fractions_sum_to_one` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_seed_estimate_clamped` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_spawn_correct_count` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_spawn_large_swarm` (0 refs)
_No references found._

## `tests.test_swarm.TestArchetypes.test_unique_ids` (0 refs)
_No references found._

## `tests.test_swarm.TestDynamics` (0 refs)
_No references found._

## `tests.test_swarm.TestDynamics.test_build_network_correct_size` (0 refs)
_No references found._

## `tests.test_swarm.TestDynamics.test_build_network_small` (0 refs)
_No references found._

## `tests.test_swarm.TestDynamics.test_convergence_uniform_swarm` (0 refs)
_No references found._

## `tests.test_swarm.TestDynamics.test_no_convergence_diverse` (0 refs)
_No references found._

## `tests.test_swarm.TestDynamics.test_propagate_preserves_bounds` (0 refs)
_No references found._

## `tests.test_swarm.TestDynamics.test_run_dynamics_converges` (0 refs)
_No references found._

## `tests.test_swarm.TestDynamics.test_run_dynamics_zero_rounds` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle.test_oracle_confidence_in_range` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle.test_oracle_consensus_in_range` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle.test_oracle_consensus_near_base` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle.test_oracle_dissent_in_range` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle.test_oracle_high_base_prob` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle.test_oracle_low_base_prob` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle.test_oracle_returns_result` (0 refs)
_No references found._

## `tests.test_swarm.TestOracle.test_oracle_swarm_size_respected` (0 refs)
_No references found._

## `tests.test_swarm.test_agent_from_config` (0 refs)
_No references found._

## `tests.test_swarm.test_all_archetypes_registered` (0 refs)
_No references found._

## `tests.test_swarm.test_archetype_diversity` (0 refs)
_No references found._

## `tests.test_swarm.test_build_network_correct_size` (0 refs)
_No references found._

## `tests.test_swarm.test_build_network_small` (0 refs)
_No references found._

## `tests.test_swarm.test_contrarian_has_negative_alpha` (0 refs)
_No references found._

## `tests.test_swarm.test_convergence_uniform_swarm` (0 refs)
_No references found._

## `tests.test_swarm.test_fractions_sum_to_one` (0 refs)
_No references found._

## `tests.test_swarm.test_no_convergence_diverse` (0 refs)
_No references found._

## `tests.test_swarm.test_oracle_confidence_in_range` (0 refs)
_No references found._

## `tests.test_swarm.test_oracle_consensus_in_range` (0 refs)
_No references found._

## `tests.test_swarm.test_oracle_consensus_near_base` (0 refs)
_No references found._

## `tests.test_swarm.test_oracle_dissent_in_range` (0 refs)
_No references found._

## `tests.test_swarm.test_oracle_high_base_prob` (0 refs)
_No references found._

## `tests.test_swarm.test_oracle_low_base_prob` (0 refs)
_No references found._

## `tests.test_swarm.test_oracle_returns_result` (0 refs)
_No references found._

## `tests.test_swarm.test_oracle_swarm_size_respected` (0 refs)
_No references found._

## `tests.test_swarm.test_propagate_preserves_bounds` (0 refs)
_No references found._

## `tests.test_swarm.test_run_dynamics_converges` (0 refs)
_No references found._

## `tests.test_swarm.test_run_dynamics_zero_rounds` (0 refs)
_No references found._

## `tests.test_swarm.test_seed_estimate_clamped` (0 refs)
_No references found._

## `tests.test_swarm.test_spawn_correct_count` (0 refs)
_No references found._

## `tests.test_swarm.test_spawn_large_swarm` (0 refs)
_No references found._

## `tests.test_swarm.test_unique_ids` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector.test_build_order_dry_run` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector.test_build_order_has_timestamp` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector.test_execute_market_order_dry_run` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector.test_map_event` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector.test_map_market` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector.test_no_wallet_graceful` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector.test_safe_mode_default` (0 refs)
_No references found._

## `tests.test_trading.TestPolymarketConnector.test_safe_mode_explicit` (0 refs)
_No references found._

## `tests.test_trading.TestTradeExecutor` (0 refs)
_No references found._

## `tests.test_trading.TestTradeExecutor.test_filter_events_fallback` (0 refs)
_No references found._

## `tests.test_trading.TestTradeExecutor.test_size_trade_half_kelly` (0 refs)
_No references found._

## `tests.test_trading.TestTradeExecutor.test_size_trade_max_cap` (0 refs)
_No references found._

## `tests.test_trading.TestTradeExecutor.test_superforecast_clamps_probability` (0 refs)
_No references found._

## `tests.test_trading.TestTradeExecutor.test_superforecast_returns_dict` (0 refs)
_No references found._

## `tests.test_trading.TestTrader` (0 refs)
_No references found._

## `tests.test_trading.TestTrader.test_events_to_markets_uses_get_market_by_id` (0 refs)
_No references found._

## `tests.test_trading.TestTrader.test_one_best_trade_no_events` (0 refs)
_No references found._

## `tests.test_trading.TestTrader.test_one_best_trade_no_markets` (0 refs)
_No references found._

## `tests.test_trading.test_build_order_dry_run` (0 refs)
_No references found._

## `tests.test_trading.test_build_order_has_timestamp` (0 refs)
_No references found._

## `tests.test_trading.test_events_to_markets_uses_get_market_by_id` (0 refs)
_No references found._

## `tests.test_trading.test_execute_market_order_dry_run` (0 refs)
_No references found._

## `tests.test_trading.test_filter_events_fallback` (0 refs)
_No references found._

## `tests.test_trading.test_map_event` (0 refs)
_No references found._

## `tests.test_trading.test_map_market` (0 refs)
_No references found._

## `tests.test_trading.test_no_wallet_graceful` (0 refs)
_No references found._

## `tests.test_trading.test_one_best_trade_no_events` (0 refs)
_No references found._

## `tests.test_trading.test_one_best_trade_no_markets` (0 refs)
_No references found._

## `tests.test_trading.test_safe_mode_default` (0 refs)
_No references found._

## `tests.test_trading.test_safe_mode_explicit` (0 refs)
_No references found._

## `tests.test_trading.test_size_trade_half_kelly` (0 refs)
_No references found._

## `tests.test_trading.test_size_trade_max_cap` (0 refs)
_No references found._

## `tests.test_trading.test_superforecast_clamps_probability` (0 refs)
_No references found._

## `tests.test_trading.test_superforecast_returns_dict` (0 refs)
_No references found._
