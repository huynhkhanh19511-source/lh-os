# Primitives

## The verb layer of LH OS

Primitives are the smallest reusable transformations currently discovered in LH OS.

They are not skills, domain ontologies, or stages in a fixed pipeline.

A primitive should behave more like a Unix command:

- do one transformation clearly
- have an explicit input/output boundary
- remain useful outside one domain
- compose with other primitives
- preserve enough traceability for downstream judgment

> What is the smallest operation that transforms one representation of reality into another?

## Current candidates

| Primitive | Core transformation |
|---|---|
| extract | reality → explicit units |
| relate | units → explicit relationships |
| recognize | observations → pattern instances |
| structure | elements + relationships → organized representation |

These are candidates, not a closed instruction set.

## Composition

Primitives are not a mandatory pipeline. A case may compose them differently.

```text
Reality → extract → relate → structure
Reality → extract → recognize → structure
```

The invariant is composability, not sequence.

## What does not belong here

- Domain ontology → case/domain configuration
- Multi-step workflows → skills
- Orchestration → agents/runtime
- Broad activities such as analysis → skills or case logic

## Discovery rule

```text
Reality Case
  ↓
Observed transformation
  ↓
Repeated across cases?
  ↓ yes
Candidate primitive
  ↓
Stable input/output boundary?
  ↓ yes
Reusable primitive
```

Do not invent primitives because the architecture looks incomplete.

## Primitive contract

Every primitive should define:

1. Verb
2. Input
3. Transformation
4. Output
5. Invariants
6. Traceability
7. Composition
8. Non-goals

## Design principle

> Local transformation. Explicit boundary. Global composition.

The goal is not a taxonomy of cognition. The goal is to discover a small, stable instruction set that repeatedly helps messy reality become usable representation.