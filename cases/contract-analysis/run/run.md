# Contract Analysis Runtime v0.1

## Input
`cases/contract-analysis/input/sample-contract.md`

## Step 1 — Extract Primitives

| ID | Type | Subject | Predicate | Object |
|---|---|---|---|---|
| P1 | Party | Alpha Retail Co. | is | Client |
| P2 | Party | Beta Analytics Ltd. | is | Provider |
| P3 | Obligation | Provider | must deliver | monthly analytics report and dashboard |
| P4 | Payment | Client | must pay | USD 2,000/month |
| P5 | Time | Payment | due within | 15 days of invoice |
| P6 | Constraint | Information | must remain | confidential |
| P7 | Time | Confidentiality | survives termination | 2 years |
| P8 | Right | Either party | may terminate | for uncured material breach |
| P9 | Condition | Material breach | cure period | 30 days after notice |
| P10 | Constraint | Provider liability | limited to | 3 months of fees |

## Step 2 — Map Relationships

- Provider → must deliver → monthly analytics report and dashboard
- Client → must pay → USD 2,000/month
- Payment → due within → 15 days of invoice
- Information → must remain → confidential
- Confidentiality → survives termination → 2 years
- Either party → may terminate → uncured material breach
- Material breach → cure period → 30 days after notice
- Provider liability → limited to → 3 months of fees

## Step 3 — Structured Reality

The contract creates a service-for-payment relationship constrained by confidentiality, breach remediation, termination rights, and a capped liability boundary.

## Step 4 — Decision Signals

1. Payment obligation is explicit but depends on invoice receipt.
2. Termination right is conditional on material breach and a 30-day cure period.
3. Confidentiality survives termination for 2 years.
4. Provider's downside exposure is contractually capped at 3 months of fees.

## Output
`cases/contract-analysis/artifacts/sample-analysis.md`
