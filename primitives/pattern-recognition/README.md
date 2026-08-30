# recognize

## Verb

**Recognize** identifies meaningful configurations within observations or representations.

## Core transformation

```text
Observations
      ↓
   recognize
      ↓
Pattern instances
```

## Input

Comparable observations, units, relationships, or structures.

## Output

Explicit pattern instances:

```text
Pattern
- members
- configuration
- basis
- reference?  optional
- confidence? optional
```

## What counts as a pattern?

Depending on the case:

- repetition
- similarity
- deviation
- anomaly
- recurring configuration
- match against a known pattern

The detection rule must be explicit.

## Invariant

Recognition must add a new explicit claim about a configuration present across one or more observations.

## What recognize does not do

Recognize does not:

- explain why a pattern exists
- determine strategic importance
- create a complete structural model
- make the final decision

It answers:

> What configuration is present?

not automatically:

> Why does it matter?

## Composition

```text
extract → recognize
relate → recognize
structure → recognize
```

## Primitive test

A successful recognize operation makes a configuration inspectable that was not explicit in the input representation.