# relate

## Verb

**Relate** makes connections between explicit units visible.

## Core transformation

```text
Isolated units
      ↓
    relate
      ↓
Explicit relationships
```

## Input

A collection of identifiable units.

## Output

A collection of relationships.

```text
Relationship
- source
- relation
- target
- basis
- provenance?
```

Conceptually:

```text
source → relation → target
```

## Invariant

A relationship should identify:

1. what is connected
2. how it is connected
3. what justifies the connection when inference is involved

## What relate does not do

Relate does not:

- prescribe a universal relationship vocabulary
- decide strategic importance
- infer an entire system structure
- produce a final decision

## Domain configuration

Relationship vocabularies belong to the case or domain.

Contract:

```text
owes
must
may
limited_by
valid_during
terminates_if
```

System:

```text
depends_on
causes
blocks
enables
constrains
```

The primitive remains:

> make a connection explicit.

## Primitive test

A successful relate operation produces connections that can be inspected independently of the original raw representation.