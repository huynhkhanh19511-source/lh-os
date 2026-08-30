# structure

## Verb

**Structure** organizes explicit elements and relationships into a representation whose arrangement is useful for further judgment.

## Core transformation

```text
Elements + relationships
        ↓
     structure
        ↓
Organized representation
```

## Input

Explicit units, relationships, and optionally recognized patterns.

## Output

A structured representation, for example:

- graph
- hierarchy
- dependency map
- timeline
- constraint model
- capability map

The primitive does not prescribe one universal structure.

## Invariant

The resulting structure should preserve enough underlying elements and relationships to remain inspectable.

A structure should make some property easier to observe than the unstructured input did.

## What structure does not do

Structure does not:

- perform every kind of analysis
- decide what action to take
- claim that the representation is reality itself

It changes representation, not reality.

## Why not Structural Analysis?

Structural Analysis describes a broad multi-step activity.

**structure** is narrower:

> organize elements and relationships into a useful representation.

Analysis may use structure, but structure itself remains a composable transformation.

## Composition

```text
extract → structure
extract → relate → structure
extract → relate → recognize → structure
```

## Primitive test

A successful structure operation reveals an organization that makes downstream comparison, evaluation, or decision-making easier.