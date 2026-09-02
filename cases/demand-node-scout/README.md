# Demand Node Scout

A reality case for testing whether LH OS can transform employment-market reality into a structured **Demand → Mission → Capability → Access** representation.

This case is intentionally small. It does not build a general Hunter framework. It pressure-tests one vertical slice:

```text
Node Evidence
    ↓
Demand Node
    ↓
Mission Extraction
    ↓
Capability / Constraint / Access
    ↓
Decision Artifact
    ↓
Evidence
```

## Why this case exists

The current strategic model distinguishes three execution surfaces:

```text
Architect / Decision
        ↓
Solution Package / Bridge
        ↓
Engineer / Deployment
```

The case therefore treats a role or JD as **evidence**, not as the primary object of search. The primary object is the node that generates, routes, or executes recurring missions.

## Input contract

`input/node.json` contains observable market evidence. The runtime extracts a minimal mission representation without pretending that inference is fact.

## Output contract

`artifacts/mission.json` contains:

- node identity and type
- inferred mission objective
- required capabilities
- constraints
- access surface
- evidence references
- inference confidence

## Runtime principle

Keep the smallest executable capability that can produce evidence capable of changing LH OS.
