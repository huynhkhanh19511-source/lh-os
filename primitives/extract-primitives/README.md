# extract

## Verb

**Extract** makes units that are implicit in a representation explicit.

## Core transformation

```text
Unstructured representation
        ↓
      extract
        ↓
Explicit units + provenance
```

## Input

Any representation containing potentially relevant units:

- contract text
- job descriptions
- incident reports
- meeting notes
- market observations

## Output

A collection of explicit units.

Minimal conceptual form:

```text
Unit
- id
- content
- type?       optional/domain-supplied
- source
- confidence? optional
```

## Invariant

Every extracted unit should remain traceable to the representation from which it was extracted.

## What extract does not do

Extract does not:

- determine relationships
- decide importance
- infer complete structure
- perform domain-specific analysis

## Domain configuration

Domain concepts belong outside the primitive.

Contract Analysis may configure:

```text
Party
Obligation
Right
Constraint
Time
Payment
Condition
```

The verb remains:

> make relevant units explicit.

## Composition

```text
Reality → extract → relate
Reality → extract → recognize
Reality → extract → structure
```

## Primitive test

A successful extract operation lets downstream transformations operate on explicit units without repeatedly parsing the entire original representation.