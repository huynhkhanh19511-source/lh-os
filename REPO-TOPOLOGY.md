# Repository Topology

## Initial Strategy

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
└── NOTION-GITHUB-LINKING.md
```

As executable work grows, implementation directories can be introduced deliberately rather than pre-allocating a large hierarchy.

## Future Extraction Candidates

- `kinh-architect` — if Kinh Architect becomes an independently versioned execution system.
- `labs` — if experiments become numerous enough to need a separate lifecycle.
- `hunter` — if Hunter becomes a standalone product/system rather than an LH OS validation project.

## Rule

**Split by lifecycle, not by imagination.**
