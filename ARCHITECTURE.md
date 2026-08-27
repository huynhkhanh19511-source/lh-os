# Architecture

## System Boundary

LH OS connects a knowledge layer to an execution layer and closes the loop through runtime evidence.

```text
                         LH OS
                           │
                ┌──────────┴──────────┐
                │                     │
             Notion                GitHub
         Knowledge Layer       Execution Layer
                                      │
                                      ▼
                           Sensemaking Runtime
                                      │
                                      ▼
                                   Feedback
                                      │
                                      ▼
                                    Notion
```

## Layers

| Layer | Primary responsibility |
|---|---|
| Notion | Knowledge, architecture, decisions, memory |
| GitHub | Skills, agents, code, artifacts, experiments, tests, versioning |
| Sensemaking Runtime | Execute reusable capabilities against reality |
| Feedback | Evidence, failures, observations, learning |

## Sensemaking Runtime

The runtime is the execution layer for Architectural Sensemaking.

```text
Reality
  ↓
Sensemaking Agent
  ↓
Skill Composition
  ↓
Structured Reality
  ↓
Decision
  ↓
Artifact
  ↓
Runtime Evidence
```

### Core abstractions

- **Agent** — thin orchestrator that selects and composes skills.
- **Skill** — reusable capability; analogous to a Unix utility.
- **Primitive** — building block used to represent a reality.
- **Pattern** — recognizable relationship or configuration among primitives.
- **Structure** — organized representation of reality.
- **Artifact** — persistent output that can be reused, tested, or communicated.
- **Case** — concrete reality used to test the runtime.

## First Runtime Case

Contract Analysis is the first case used to validate the Sensemaking Runtime. It is not the identity of the Agent.

```text
Contract Text
  ↓
Contract Primitives
  ↓
Contractual Relationships
  ↓
Risk / Rights / Constraints
  ↓
Decision
```

## Traceability

A mature workflow should allow a decision to be traced through implementation and runtime:

```text
Idea → Decision → Issue → Skill / Agent → Commit → Runtime → Observation → Learning
```

## Design Rule

Do not copy the entire knowledge base into GitHub. Link the systems and keep each artifact in the layer where it is most useful.

**Build the smallest executable capability that can produce useful runtime evidence.**
