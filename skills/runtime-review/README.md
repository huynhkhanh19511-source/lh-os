# Runtime Review

> Compare what was intended with what actually happened.

## Purpose

Runtime Review turns execution results into learning.

It examines the difference between:

- intended behavior
- implementation
- expected behavior
- actual Runtime behavior

```text
Intent
   ↓
Implementation
   ↓
Runtime
   ↓
Expected vs Actual
   ↓
Failure / Difference
   ↓
Cause Hypothesis
   ↓
Learning
   ↓
Update
```

## Boundary

Runtime Review does not assume every failure is a bug.

A Runtime difference may challenge:

- implementation
- assumptions
- architecture
- problem framing
- evaluation criteria

## Core Principle

> Runtime can invalidate upstream abstraction.

## Workflow

1. Record the original intent.
2. Define expected behavior.
3. Observe actual Runtime behavior.
4. Compare expected vs actual.
5. Identify failures or unexpected outcomes.
6. Investigate possible causes.
7. Decide what should be updated.
8. Preserve evidence.

## Output

A Runtime Review containing:

- Intent
- Expected behavior
- Actual behavior
- Difference
- Evidence
- Cause hypotheses
- Decision
- Learning
- Next change

## Failure Modes

- jumping directly to a fix
- treating symptoms as causes
- changing multiple variables without evidence
- hiding negative results
- declaring success without verification

## Runtime

Developing. Intended for code, workflows, agents, system designs, and decision processes.

> **Abstraction cannot escape Runtime.**
