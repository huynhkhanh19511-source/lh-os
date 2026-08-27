# Repository Topology

## Strategy

Start with one root repository: `lh-os`.

Do not split Kinh Architect, Hunter, or other projects into separate repositories until there is a concrete need for independent lifecycle, permissions, release cadence, or ownership.

## Current Model

```text
lh-os/
├── README.md
├── MISSION.md
├── ARCHITECTURE.md
├── REPO-TOPOLOGY.md
├── ISSUE-TAXONOMY.md
├── NOTION-GITHUB-LINKING.md
│
├── agent/
│   └── sensemaking/
│
├── skills/
│   ├── pattern_recognition/
│   └── structural_analysis/
│
├── domains/
│   └── contract/
│
├── artifacts/
├── tests/
└── docs/
```

## Runtime Organization

```text
Sensemaking Runtime
│
├── Agent
│   └── sensemaking/
│
├── Skills
│   ├── pattern_recognition/
│   └── structural_analysis/
│
├── Cases
│   └── Contract Analysis
│
├── Artifacts
└── Tests
```

`domains/` is retained for the current MVP implementation. Conceptually, Contract Analysis is a **Case** rather than an Agent or a top-level architectural layer. A future cleanup may move domain-specific runtime cases under `cases/` once the abstraction is validated by runtime evidence.

## Future Extraction Candidates

- `kinh-architect` — if Kinh Architect becomes an independently versioned execution system.
- `labs` — if experiments become numerous enough to need a separate lifecycle.
- `hunter` — if Hunter becomes a standalone product/system rather than an LH OS validation project.

## Rule

**Split by lifecycle, not by imagination. Introduce structure only when runtime evidence justifies it.**
