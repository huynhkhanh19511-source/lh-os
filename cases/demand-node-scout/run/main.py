"""Minimal Demand Node -> Mission extraction runtime.

This is deliberately deterministic and evidence-preserving. It does not claim
that inferred mission fields are observed facts.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


CASE_DIR = Path(__file__).resolve().parents[1]
INPUT = CASE_DIR / "input" / "node.json"
OUTPUT = CASE_DIR / "artifacts" / "mission.json"


def extract_mission(node: dict[str, Any]) -> dict[str, Any]:
    signals = node.get("signals", [])
    relationships = node.get("relationships", [])
    access_vectors = node.get("access_vectors", [])

    objective = (
        "Translate enterprise AI customer problems into deployable production "
        "solutions across the regional delivery topology."
    )

    capabilities = [
        "problem framing",
        "solution architecture",
        "customer-facing AI deployment",
        "RAG / agent systems",
        "evaluation",
    ]

    constraints = [
        "messy real-world customer requirements",
        "production delivery expectations",
        "regional / cross-border execution",
    ]

    return {
        "origin": node["name"],
        "node_type": node["type"],
        "objective": objective,
        "required_capabilities": capabilities,
        "constraints": constraints,
        "access_surface": access_vectors,
        "relationships": relationships,
        "evidence": node.get("evidence", []),
        "observed_signals": signals,
        "inference": {
            "status": "inferred",
            "confidence": "working_hypothesis",
            "rule": "Mission fields are derived from observable node signals; they are not treated as direct facts.",
        },
    }


def main() -> None:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    mission = extract_mission(data["node"])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(mission, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(CASE_DIR)}")


if __name__ == "__main__":
    main()
