# LH OS

> **Turn messy reality into structured understanding, better decisions, reusable artifacts, and evidence that improves the system.**

## What is LH OS?

LH OS is an experimental **Decision & Sensemaking System**.

Its job is simple:

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
Better System
```

Most knowledge systems help us store information or understand ideas.

LH OS asks a further question:

> **Can understanding be turned into a reusable decision process, tested against reality, and improved through evidence?**

That is what this repository is exploring.

## The Problem

Complex reality is usually messy:

- information is fragmented
- relationships are hidden
- important constraints are easy to miss
- decisions depend on interpretation
- useful reasoning often disappears after the moment

The result is repeated sensemaking from scratch.

LH OS attempts to create a reusable loop:

```text
Messy Reality
    ↓
Make relationships visible
    ↓
Form a structured view
    ↓
Support a decision
    ↓
Leave a reusable artifact
    ↓
Observe what happened
    ↓
Improve the way we understand reality
```

## What LH OS is not

LH OS is **not primarily**:

- a note-taking system
- an AI agent framework
- a collection of automations
- a knowledge base
- a single domain application

Those can be parts of the system.

The identity of LH OS is the **loop that connects Reality → Understanding → Decision → Evidence**.

## How it works

The current sensemaking pipeline is:

```text
Reality
  ↓
Extract Primitives
  ↓
Map Relationships
  ↓
Form Structure
  ↓
Identify Decision Signals
  ↓
Produce Artifact
  ↓
Collect Evidence
```

### Core concepts

| Concept | Meaning |
|---|---|
| **Reality** | The situation, input, or environment being understood |
| **Primitive** | A basic unit extracted from reality |
| **Relationship** | A meaningful connection between primitives |
| **Structure** | An organized representation of the reality |
| **Decision Signal** | Information that changes or supports a decision |
| **Artifact** | A persistent output that can be reused, inspected, or communicated |
| **Evidence** | Observation from runtime that can update belief or system design |
| **Case** | A concrete reality used to test the system |

## System vs Case

LH OS is the **system**.

A Contract Analysis is only one **case used to test the system**.

```text
LH OS
│
├── Shared Sensemaking Capabilities
│
└── Reality Cases
    ├── Contract Analysis
    ├── JD Analysis
    ├── Market Scout
    └── ...
```

Each case asks:

> Can the same underlying sensemaking logic produce useful results when reality changes?

## Current Proof

The first runtime case is **Contract Analysis**:

```text
Contract Text
  ↓
Primitives
  ↓
Relationships
  ↓
Structured Contract
  ↓
Decision Signals
  ↓
Decision Artifact
  ↓
Runtime Evidence
```

This is not meant to prove that LH OS is a contract system.

It tests a more general hypothesis:

> **A messy reality can be transformed through explicit intermediate representations into a reusable decision artifact.**

## Repository Structure

```text
lh-os/
│
├── agent/       # shared orchestration
├── skills/      # reusable capabilities
├── runtime/     # shared execution mechanisms
├── tests/       # system validation
│
├── cases/       # reality experiments
│   └── <case>/
│       ├── input/
│       ├── run/
│       ├── artifacts/
│       └── evidence/
│
└── docs/        # supporting models
```

A case is a complete vertical slice:

```text
Input → Run → Artifact → Evidence
```

## Why GitHub?

This repository is the execution and proof layer of LH OS.

- **Notion** holds broader knowledge, theory, architecture, and decisions.
- **GitHub** holds executable capabilities, cases, artifacts, tests, and version history.
- **Runtime** creates observations that can challenge the theory.

```text
Theory
  ↓
System Design
  ↓
Runtime
  ↓
Evidence
  ↓
Theory Update
```

## Current Principle

> **Build the smallest executable capability that can produce evidence capable of changing the system.**
