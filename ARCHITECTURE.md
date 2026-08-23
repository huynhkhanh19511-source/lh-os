# Architecture

## System Boundary

LH OS connects a knowledge layer to an execution layer and closes the loop through runtime evidence.

```text
                 LH OS
                   │
          ┌────────┴────────┐
          │                 │
       Notion            GitHub
   Knowledge Layer    Execution Layer
          │                 │
          └────────┬────────┘
                   ↓
                Runtime
                   ↓
                Feedback
                   ↓
                Notion
```

## Layers

| Layer | Primary responsibility |
|---|---|
| Notion | Knowledge, architecture, decisions, memory |
| GitHub | Code, artifacts, experiments, versioning |
| Runtime | Execution and observable behavior |
| Feedback | Evidence, failures, observations, learning |

## Traceability

A mature workflow should allow a decision to be traced through implementation and runtime:

```text
Idea → Decision → Issue → Code → Commit → Runtime → Observation → Learning
```

## Design Rule

Do not copy the entire knowledge base into GitHub. Link the systems and keep each artifact in the layer where it is most useful.
