"""Contract analysis as the first domain runtime for Sensemaking."""

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
    """Create a minimal structural shell from contract text.

    Extraction logic is intentionally deferred. The MVP first establishes the
    domain model and runtime boundary before adding retrieval/LLM logic.
    """
    return {
        "input": contract_text,
        "primitives": list(CONTRACT_PRIMITIVES),
        "relationships": [],
        "risks": [],
        "decision": None,
    }
