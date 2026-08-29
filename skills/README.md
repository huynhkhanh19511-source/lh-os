# LH OS Skills

Skills in LH OS are not imagined instructions or a collection of prompts.

> **A Skill is compressed experience: a reusable way of working extracted from repeated contact with Reality.**

## Architecture

```text
Theory
   ↓
Primitives
   ↓
Skills
   ↓
Runtime
   ↓
Evidence
   ↓
Skill Update
```

A Skill combines reusable primitives into a purposeful workflow.

It is not considered complete simply because documentation exists.

## Current Skill Set

| Skill | Status | Purpose |
|---|---|---|
| [Reality Scout](reality-scout/README.md) | Developing | Turn observations into a structured representation of Reality |
| [Capability Assessment](capability-assessment/README.md) | Developing | Evaluate demonstrated capability through evidence |
| [Gap Analysis](gap-analysis/README.md) | Developing | Identify meaningful gaps and prioritize intervention |
| [Runtime Review](runtime-review/README.md) | Developing | Compare intended and actual behavior to extract learning |
| [Solution Package Design](solution-package-design/README.md) | Future flagship | Bridge Reality, architecture, implementation, and Runtime |

## Skill Evolution Loop

```text
Experience
    ↓
Repeated Pattern
    ↓
Skill Extraction
    ↓
Skill Hypothesis
    ↓
Runtime
    ↓
Failure / Friction
    ↓
Evidence
    ↓
Skill Update
    ↺
```

## Maturity

A Skill may move through:

```text
Idea
↓
Candidate
↓
Developing
↓
Runtime-tested
↓
Evidence-backed
↓
Reusable
```

## When should a Skill be extracted?

A workflow becomes a Skill candidate when:

- the work has been repeated
- a recognizable workflow is emerging
- we do not want to rediscover the process next time
- an AI agent needs explicit instructions to perform the work consistently
- the output has a recognizable quality bar

## Standard Skill Structure

```text
skills/<skill-name>/
├── README.md
├── examples/
└── evidence/
```

As a Skill matures, its documentation should make explicit:

- Purpose
- Trigger
- Input
- Process
- Output
- Evaluation
- Runtime
- Failure Modes
- Evidence
- Version

## Principle

> **Runtime → Pattern → Skill**

Do not mistake a documented workflow for a proven capability.

> **Skills are compressed Runtime, not imagined instructions.**
