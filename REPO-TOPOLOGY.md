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
├── runtime/
│   └── sensemaking/
│
├── cases/
│   └── contract-analysis/
│       ├── input/
│       ├── run/
│       ├── artifacts/
│       └── evidence/
│
├── tests/
└── docs/
```

## Organization Principle

LH OS separates the repository into two primary boundaries:

### Shared Capabilities

```text
agent/
skills/
runtime/
tests/
```

These represent reusable system capabilities that may serve multiple reality cases.

### Reality Cases

```text
cases/
└── <case>/
    ├── input/
    ├── run/
    ├── artifacts/
    └── evidence/
```

A **Case** is a self-contained reality experiment. Opening one case should reveal its full lifecycle:

```text
Reality Input
    ↓
Execution
    ↓
Artifact
    ↓
Evidence
```

This keeps case-specific material colocated while preserving shared capabilities at the system level.

## Current Case

`contract-analysis` is the first runtime case:

```text
cases/contract-analysis/
├── input/
│   └── sample-contract.md
├── run/
│   └── run.md
├── artifacts/
│   └── sample-analysis.md
└── evidence/
    └── M0.1-first-run.md
```

Contract Analysis is a **Case**, not an Agent, domain layer, or identity of LH OS.

## Future Extraction Candidates

- `kinh-architect` — if Kinh Architect becomes an independently versioned execution system.
- `labs` — if experiments become numerous enough to need a separate lifecycle.
- `hunter` — if Hunter becomes a standalone product/system rather than an LH OS validation project.

## Rule

**Split by lifecycle, not by imagination. Introduce structure only when runtime evidence justifies it.**
