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

## Architectural Sensemaking Model

Architectural Sensemaking is the progression of the same person through three cognitive states while entering and understanding a reality:

```text
Reality
  ↓
Reality Orientation
  ↓
Relationship Sensemaking
  ↓
System Formation
  ↓
Architecture
  ↓
Runtime
  ↓
Feedback
```

See [Sensemaking Model](docs/sensemaking-model.md) for the detailed model.

The three states correspond to increasing depth of observation rather than fixed job ranks:

| State | Core question | Primary view |
|---|---|---|
| Junior State — Reality Orientation | What is this? | Objects / Structure |
| Senior State — Relationship Sensemaking | How does it relate? | Relationships / Workflow |
| Architect State — System Formation | What system should exist? | System / Architecture |

A person may move through all three states when entering a new reality. The state is determined by depth of understanding, not title.

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

Contract Analysis can also be used to validate the three sensemaking states:

```text
Contract
  ↓
L1 — Structure Map
"What is this?"
  ↓
L2 — Relationship / Workflow Map
"How does it relate?"
  ↓
L3 — System / Architecture Map
"What system does this create?"
```

## Traceability

A mature workflow should allow a decision to be traced through implementation and runtime:

```text
Idea → Decision → Issue → Skill / Agent → Commit → Runtime → Observation → Learning
```

## Design Rule

Do not copy the entire knowledge base into GitHub. Link the systems and keep each artifact in the layer where it is most useful.

**Build the smallest executable capability that can produce useful runtime evidence.**
