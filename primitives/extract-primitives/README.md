# Extract Primitives

## Purpose
Transform raw contract text into explicit semantic primitives.

## Input
A contract document.

## Output
A list of primitives with:
- id
- type
- subject
- object
- predicate
- source

## Primitive Types v0.1
- Party
- Obligation
- Right
- Constraint
- Time
- Payment
- Condition

## Validation
Every extracted primitive must be traceable to source text.
