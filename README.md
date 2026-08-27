# LH OS

LH OS is an executable system for **Architectural Sensemaking**: turning knowledge, architecture, and decisions into runtime feedback.

## Mission

Connect thinking to execution: ideas and decisions become executable capabilities, are tested against reality, and feed evidence back into the architecture.

## System Model

```text
Notion → GitHub → Sensemaking Runtime → Feedback → Notion
```

- **Notion** — memory, knowledge, architecture, decisions
- **GitHub** — execution, skills, artifacts, experiments, tests, versioning
- **Sensemaking Runtime** — executes reusable capabilities against reality
- **Feedback** — runtime evidence that updates the system

## Sensemaking Model

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

- **Agent** — thin orchestrator that selects and composes skills
- **Skill** — reusable capability; analogous to a Unix utility
- **Primitive** — building block used to represent a reality
- **Pattern** — recognizable relationship/configuration among primitives
- **Structure** — organized representation of reality
- **Artifact** — persistent output that can be reused, tested, or communicated
- **Case** — a concrete reality used to test the runtime

## First Runtime Case

**Contract Analysis** is the first case, not the identity of the Agent.

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

## Repository Role

This repository is the execution home of LH OS. It contains executable capabilities, implementation work, experiments, tests, artifacts, and version history. It does not duplicate the knowledge base.
