# Architectural Sensemaking Runtime

## Purpose

The runtime is the execution layer for turning reality into structured reality and decision-support artifacts.

```text
Reality
  ↓
Pattern Recognition
  ↓
Primitives + Relationships
  ↓
Structural Analysis
  ↓
Risk / Strength
  ↓
Decision
  ↓
Artifact
```

## Abstraction boundary

- **Agent** — thin runtime/orchestrator that composes skills.
- **Skill** — reusable capability, analogous to a Unix utility.
- **Domain skill** — a composition or specialization for a reality type, such as Contract Analysis.
- **Artifact** — persistent output that can be reused, tested, or communicated.

## First runtime case

Contract Analysis is the first domain case, not the identity of the Agent.

```text
Contract Text
  → Contract Primitives
  → Contractual Relationships
  → Risk / Rights
  → Decision
```

The MVP deliberately starts with the runtime boundary and structural model. Extraction, retrieval, LLM orchestration, and richer decision logic can be added after runtime feedback exposes what is actually needed.
