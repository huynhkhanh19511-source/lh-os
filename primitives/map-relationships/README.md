# Map Relationships

## Purpose
Transform isolated primitives into explicit relationships.

## Input
Primitive list.

## Output
Relationships expressed as:

`subject → predicate → object`

## Relationship Types v0.1
- owes
- pays
- must
- may
- limited_by
- valid_during
- terminates_if
- survives

## Validation
Each relationship must reference existing primitives.
