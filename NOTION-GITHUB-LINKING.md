# Notion ↔ GitHub Linking Convention

Notion and GitHub are complementary layers.

## Notion owns

- Knowledge
- Architecture
- Principles
- Long-form reasoning
- Strategic decisions

## GitHub owns

- Implementation
- Code
- Experiments
- Issues
- Pull requests
- Version history

## Traceability

When practical, link artifacts across both systems:

```text
Notion decision
    ↓
GitHub issue
    ↓
Pull request / commit
    ↓
Runtime result
    ↓
Notion observation or updated decision
```

## Rule

Keep the canonical version of each artifact in its natural system. Do not maintain duplicate copies merely for symmetry.

The goal is traceability, not duplication.
