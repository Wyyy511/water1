from __future__ import annotations
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent

GROUPS = {
    "tools": [
        "data_tool.py","query_adapter.py","baseline_tool.py","scenario_tool.py",
        "export_tool.py","qa_tool.py","field_governance.py","material_tool.py"
    ],
    "agent": ["router.py","deepseek_client.py","llm_adapter.py","risk_brief.py"],
    "core": ["logging_utils.py","paths.py"],
    "engines": ["baseline_api.py","baseline_calculator.py","baseline_water_risk_v2.py","scenario_engine.py"],
    "static": ["index.html","app.js","styles.css","Water_Risk_Input_Template.xlsx"],
    "data": [
        "data_registry.json","exposure_weights.csv","extreme_drought.csv","field_dictionary.csv",
        "field_gap_register.csv","future_ws_sv.csv","hazard_baseline.csv","material_params.csv",
        "monthly_ws.csv","scenario_params.json"
    ],
}

GOLDEN = [
    "example_1_complete_input.json","example_1_complete_output.json",
    "example_2_proxy_input.json","example_2_proxy_output.json",
    "example_3_partial_input.json","example_3_partial_output.json",
    "example_4_insufficient_input.json","example_4_insufficient_output.json",
    "example_5_conflict_input.json","example_5_conflict_output.json",
    "example_6_error_input.json","example_6_error_output.json",
]

def _copy_if_needed(source: Path, target: Path) -> None:
    if target.exists():
        return
    if not source.exists():
        raise RuntimeError(f"Required deployment file is missing: {source.name}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)

def ensure_layout() -> dict:
    # Rebuild Python packages and static/data folders from root-level files.
    for folder, names in GROUPS.items():
        dest = ROOT / folder
        dest.mkdir(parents=True, exist_ok=True)
        if folder in {"tools","agent","core","engines"}:
            (dest / "__init__.py").touch(exist_ok=True)
        for name in names:
            _copy_if_needed(ROOT / name, dest / name)

    golden = ROOT / "qa" / "golden"
    golden.mkdir(parents=True, exist_ok=True)
    for name in GOLDEN:
        _copy_if_needed(ROOT / name, golden / name)

    # Runtime writable folders.
    for name in ["logs","outputs","sample_inputs"]:
        (ROOT / name).mkdir(parents=True, exist_ok=True)

    required = [
        ROOT / "server.py",
        ROOT / "tools" / "data_tool.py",
        ROOT / "agent" / "deepseek_client.py",
        ROOT / "core" / "paths.py",
        ROOT / "engines" / "baseline_api.py",
        ROOT / "static" / "index.html",
        ROOT / "data" / "field_dictionary.csv",
        ROOT / "data" / "field_gap_register.csv",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        raise RuntimeError("Bootstrap failed; still missing: " + ", ".join(missing))

    return {
        "root": str(ROOT),
        "reconstructed": True,
        "tools": len(GROUPS["tools"]),
        "data_files": len(GROUPS["data"]),
        "golden_files": len(GOLDEN),
    }

if __name__ == "__main__":
    print(ensure_layout())
