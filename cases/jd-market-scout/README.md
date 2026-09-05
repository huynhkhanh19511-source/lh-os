# JD Market Scout

A Reality Scout field experiment.

Goal: turn real Job Descriptions into structured evidence, force a decision on every JD, and treat the application process itself as Runtime.

```text
Market Reality (JD)
       ↓
Reality Scout
  - Source (what the JD actually says)
  - Inference (what we derive)
  - Hypothesis (what we believe)
  - Fit / Gap
  - Decision EV
       ↓
Decision: Apply / Watch / Reject
       ↓
Runtime
  - Apply
  - Interview
  - Reject / Feedback / Offer
       ↓
Model Update
  - Fit ↑/↓
  - Gap ↑/↓
  - Market belief update
  - Strategy update
```

This case exists to stop architecture-only work and start generating real market evidence.

---

## Why this case exists

LH OS has strong internal models (Reality Scout, TERRAIN, decision discipline).

What it lacks is repeated contact with external market Reality that can confirm, contradict, or force updates to those models.

Job Descriptions are public, abundant, and high-signal fragments of market Reality. Using them as the first field experiment allows us to:

1. Practice Source → Inference discipline on real text
2. Force a decision on every observation (no pure analysis)
3. Turn applications and interviews into Runtime feedback
4. Build a living evidence base of the FDE / FDA / AI Deployment market
5. Later feed that evidence into a real CV and application strategy

---

## Core Rules (Non-negotiable)

1. **Every JD must end in a Decision**  
   Apply / Watch / Reject. No “analyze and store”.

2. **Strict epistemic separation**  
   - Source = what the JD literally says  
   - Inference = what we derive from it  
   - Hypothesis = what we currently believe  
   - Evidence (mine) = what we can already point to  
   - Gap = what is still missing

3. **Success is Information Gain or Outcome**, not a beautiful record.  
   Evidence Record is only memory of the experiment.

4. **Decision EV, not fake probability**  
   Ask: “Is it worth spending time and opportunity cost to test this Reality right now?”  
   Factors: Role relevance, Capability match, Evidence gap, Application cost, Information value, Career value, Access.

5. **No new abstraction until Runtime evidence requires it.**

---

## Folder Structure

```text
cases/jd-market-scout/
├── README.md                 # this file
├── schema/
│   └── evidence-record.md    # template for each JD
├── input/
│   └── jds/                  # raw JD text or links
├── evidence/
│   └── records/              # one Evidence Record per JD
├── analysis/
│   ├── cross-jd-patterns.md  # patterns across multiple JDs
│   ├── fit-matrix.md         # living capability vs market demand
│   └── application-queue.md  # ranked decisions
└── run/
    └── process.md            # how to run one JD through the loop
```

---

## Evidence Record Template (summary)

Each JD produces one record with clear layers:

**Meta**  
Company, Role, Location, Source link, Date

**Source (Observed)**  
Native vocabulary + direct claims from the JD (quote or paraphrase tightly)

**Inference**  
What demand / pressure / work function we derive

**Hypothesis**  
Current belief about the role’s real nature and fit

**My Evidence vs Gap**  
What we already have vs what is still missing

**Decision EV**  
Why Apply / Watch / Reject (including Information Value)

**Decision**  
Apply | Watch | Reject

**Proof Needed**  
If gap exists, what concrete proof should be created next

---

## Operating Loop

```text
1. Drop JD into input/jds/
2. Create Evidence Record (Source → Inference → Decision)
3. Update application-queue.md
4. If Decision = Apply → submit
5. Record Runtime outcome (auto-reject, interview, feedback, offer)
6. Update Fit / Gap / Market beliefs
7. Only then consider changing principles or abstractions
```

---

## Relationship to other cases

- `demand-node-scout` tested a smaller vertical slice (Node → Mission).
- `jd-market-scout` is the broader field experiment that feeds real market pressure into Reality Scout and into personal capability diagnosis.

---

## Current Status

- Case created.
- Schema and first Evidence Records to be added next.
- No JDs processed yet.

Next action: add the first real JD and produce its Evidence Record.
