# Architecture

## System Identity

LH OS is a **Decision & Sensemaking System**.

Its system boundary is defined by one loop:

```text
Reality
  ↓
Sensemaking
  ↓
Structured Reality
  ↓
Decision
  ↓
Artifact
  ↓
Evidence
  ↓
System Update
```

Everything inside LH OS should support at least one part of this loop.

## System Boundary

```text
                     LH OS
                       │
        ┌──────────────┴──────────────┐
        │                             │
 Shared Sensemaking System       Reality Cases
        │                             │
 Agent / Skills / Runtime       Concrete situations
        │                             │
        └───────────┬─────────────────┘
                    ↓
              Decision Artifact
                    ↓
                 Evidence
                    ↓
               System Update
```

## Shared System

Shared capabilities should be reusable across multiple cases.

```text
agent/
skills/
runtime/
tests/
```

They answer:

> **How does LH OS perform sensemaking?**

## Reality Cases

Cases are concrete situations used to pressure-test the system.

```text
cases/
└── <case>/
    ├── input/
    ├── run/
    ├── artifacts/
    └── evidence/
```

They answer:

> **Does the system still work when reality changes?**

A case is therefore not a product module. It is a **reality experiment**.

## Sensemaking Runtime

The current runtime hypothesis is:

```text
Reality
  ↓
Primitives
  ↓
Relationships
  ↓
Structure
  ↓
Decision Signals
  ↓
Artifact
  ↓
Evidence
```

### Core abstractions

| Abstraction | Role |
|---|---|
| Reality | What is being understood |
| Primitive | Basic unit extracted from reality |
| Relationship | Connection between primitives |
| Pattern | Repeated or meaningful configuration |
| Structure | Organized model of the reality |
| Skill | Reusable transformation capability |
| Agent | Orchestrates capability composition |
| Decision Signal | Output relevant to judgment |
| Artifact | Persistent result |
| Evidence | Runtime observation capable of changing belief |
| Case | Concrete pressure test |

## Architectural Sensemaking

Architectural Sensemaking describes increasing depth of engagement with a reality:

```text
Reality Orientation
    ↓
Relationship Sensemaking
    ↓
System Formation
    ↓
Architecture
```

The states answer progressively deeper questions:

| State | Question |
|---|---|
| Reality Orientation | What is this? |
| Relationship Sensemaking | How does it relate? |
| System Formation | What system is operating or should exist? |

The runtime attempts to make parts of this progression explicit and reusable.

## Evidence Boundary

An output is not automatically evidence.

Evidence must be able to answer:

```text
What did we expect?
What actually happened?
What differed?
What does that change?
```

The important loop is therefore:

```text
Runtime
  ↓
Observation
  ↓
Belief Update
  ↓
System Change
```

## First Case: Contract Analysis

Contract Analysis is the first reality case.

```text
Contract Text
  ↓
Extract Parties / Obligations / Rights / Constraints
  ↓
Map Relationships
  ↓
Form Structured Contract
  ↓
Identify Decision Signals
  ↓
Produce Decision Artifact
  ↓
Record Evidence
```

Its purpose is not to define LH OS.

Its purpose is to test this hypothesis:

> **Can explicit intermediate representations transform messy reality into a useful decision artifact?**

## Traceability

A mature LH OS workflow should preserve a path from reasoning to evidence:

```text
Reality
→ Representation
→ Decision
→ Implementation
→ Runtime
→ Observation
→ Evidence
→ Architecture Update
```

## Design Rule

> **Do not add architecture because it looks complete. Add it when reality creates pressure for it.**

And:

> **Build the smallest executable capability that can produce evidence capable of changing the system.**
