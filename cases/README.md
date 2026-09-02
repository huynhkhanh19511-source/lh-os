# Reality Cases

Cases are concrete reality experiments used to pressure-test LH OS.

They are **not product modules**. Each case asks whether the current sensemaking system still works when applied to a different reality.

## Structure

```text
cases/
└── <case>/
    ├── input/      # Reality entering the case
    ├── run/        # Case-specific execution
    ├── artifacts/  # Outputs produced
    └── evidence/   # Observations that may change the system
```

## Current Cases

- `contract-analysis` — tests structured reasoning over messy contract reality.
- `demand-node-scout` — tests whether market reality can be transformed into actionable demand topology.

## Rule

> **Reality creates pressure. Evidence decides whether LH OS should change.**

Do not generalize a case into shared architecture until repeated cases create a real need for reuse.
