"""Contract Analysis case for the Architectural Sensemaking runtime."""

CONTRACT_PRIMITIVES = (
    "party",
    "service",
    "payment",
    "term",
    "right",
    "obligation",
    "condition",
    "liability",
    "termination",
)


def analyze_contract(contract_text: str) -> dict:
    """Return the minimal structural shell used by the first runtime case.

    Extraction logic is intentionally deferred. The MVP first establishes the
    runtime boundary and structural model before adding retrieval/LLM logic.
    """
    return {
        "input": contract_text,
        "primitives": list(CONTRACT_PRIMITIVES),
        "relationships": [],
        "risks": [],
        "decision": None,
    }
