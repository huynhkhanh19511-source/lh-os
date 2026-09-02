import json
from pathlib import Path

from cases.demand_node_scout.run.main import extract_mission


CASE_DIR = Path(__file__).resolve().parents[1] / "cases" / "demand-node-scout"


def test_demand_node_extracts_mission_without_losing_evidence():
    data = json.loads((CASE_DIR / "input" / "node.json").read_text(encoding="utf-8"))

    mission = extract_mission(data["node"])

    assert mission["origin"] == "Newbridge"
    assert mission["node_type"] == "bridge_node"
    assert mission["evidence"] == data["node"]["evidence"]
    assert mission["observed_signals"] == data["node"]["signals"]
    assert mission["inference"]["status"] == "inferred"
    assert "solution architecture" in mission["required_capabilities"]
    assert mission["access_surface"] == data["node"]["access_vectors"]
