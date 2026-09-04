# Reality Scout

> Reconstruct fragmented Reality into a connected, inspectable Reality Map before judgment or intervention.

Reality Scout is a core skill in LH OS for making sense of fragmented customer Reality before other skills operate on it.

It does not primarily answer **what should we do?**

It first answers:

> **What world are we actually looking at, how are its pieces connected, and why does it look this way from the customer's position?**

---

## Why Reality Scout Exists

Reality rarely arrives as a coherent system.

A customer may send:

- documents
- presentations
- process descriptions
- architecture diagrams
- metrics
- screenshots
- logs
- requirements
- complaints
- meeting notes
- system information
- statements from different people

These are not a Reality yet.

They are **nodes scattered across a multi-dimensional Reality space**.

```text
                    PEOPLE
                       │
                       │
        PROCESS ───────┼────── SYSTEM
                       │
                       │
        DATA ──────────┼────── DECISION
                       │
                       │
                    OUTCOME
```

Each artifact exposes only a fragment of the world.

The meaning is often not inside an individual node.

**Meaning emerges from the relationships between nodes.**

Therefore:

```text
Fragmented Inputs
       ↓
    Nodes
       ↓
Relationships
       ↓
Patterns
       ↓
Meaning
       ↓
Shared Reality
```

Reality Scout exists to perform this reconstruction.

---

## Core Mission

> **Connect the dots before judging the dots.**

The first job is not to assess capability, identify gaps, review runtime, or design a solution.

The first job is to understand the structure that the customer's fragments collectively describe.

```text
Customer Reality
      ↓
[ Reality Scout ]
      ↓
Shared Reality Map
      ↓
┌──────────────┬──────────────┬──────────────┐
│ Capability   │ Gap          │ Runtime      │
│ Assessment   │ Analysis     │ Review       │
└──────────────┴──────────────┴──────────────┘
                     ↓
             Solution Package Design
```

The downstream skills should **consume a reconstructed Reality**, rather than each trying to rediscover the customer's world independently.

---

## The Reality Scout Question

Reality Scout continuously asks two questions.

### 1. Our Position — What do we feel?

When we encounter the material, observe our own signals:

- What feels clear?
- What feels confusing?
- What feels incomplete?
- What feels contradictory?
- What feels suspicious?
- What feels unusually emphasized?
- What seems to be missing?
- What creates the feeling that "something does not connect"?

These feelings are **signals, not facts**.

Intuition is used as a sensor for deciding where to investigate.

```text
Feeling
   ↓
Signal
   ↓
Hypothesis
   ↓
Evidence Check
   ↓
Confirm / Reject / Unknown
```

> **Trust intuition enough to investigate it, but never enough to call it Evidence.**

---

### 2. Customer Position — What are they feeling?

Then change seats.

Ask:

> **If I were the customer, why would I send these particular things?**

The material a customer chooses to provide is itself a signal about how they see Reality.

For example:

| What customer sends | Possible perspective |
|---|---|
| Strategy deck | Management / strategic perspective |
| Architecture diagram | Technology / system perspective |
| SOP | Intended process perspective |
| Incident logs | Failure / exception perspective |
| KPI dashboard | Measurement / management perspective |
| User complaints | Lived experience / consequence perspective |
| Meeting notes | Organizational / political perspective |

The artifact contains two layers:

```text
Artifact
├── Information
└── Perspective
```

Information tells us **what they know or claim**.

Perspective tells us **from where they are looking at Reality**.

Reality Scout must understand both.

---

## Perspective Gap

Our Reality and the customer's Reality may not initially be the same.

```text
              REALITY
                 │
       ┌─────────┴─────────┐
       ↓                   ↓
  OUR POSITION       CUSTOMER POSITION
       │                   │
  What we notice      What they notice
  What we feel       What they feel
  What we question   What they emphasize
       │                   │
       └─────────┬─────────┘
                 ↓
          Perspective Gap
                 ↓
           Investigation
                 ↓
          Shared Reality
```

A Perspective Gap is not automatically a problem.

It is a signal that two observers may be looking at different dimensions, levels, or consequences of the same system.

Sometimes the most important Problem is hidden precisely inside this gap.

---

## Reality as a Multi-Dimensional Graph

Reality Scout should think in terms of **nodes and relationships**, not isolated documents.

### Possible node types

```text
Actor
Goal
Capability
Process
System
Data
Decision
Metric
Event
Constraint
Resource
Requirement
Outcome
Problem
Assumption
Evidence
Unknown
```

### Possible relationships

```text
Cause → Effect
Claim → Evidence
Problem → Consequence
Process → Bottleneck
System → Behavior
Decision → Input
Owner → Responsibility
Metric → Outcome
Requirement → Constraint
Event → Pattern
Exception → Failure Mode
Capability → Outcome
```

The exact ontology is not fixed.

The Scout should introduce structure only when the observed Reality requires it.

The central operation remains:

```text
Node
  ↓
Relationship
  ↓
Pattern
  ↓
Meaning
```

---

## Example — Reconstructing Meaning

Suppose the customer provides four artifacts:

1. An architecture diagram showing an automated AI workflow.
2. An SOP showing a human review step.
3. A KPI showing processing time remains high.
4. User complaints about inconsistent results.

Reading each artifact independently produces four disconnected facts.

Reality Scout connects them:

```text
Architecture
      │
      │ claims automation
      ▼
AI Capability
      │
      │ supposed to support
      ▼
Workflow
      │
      │ actual intervention
      ▼
Human Review
      │
      ▼
Processing Delay
      │
      ▼
Customer Complaint
```

Now the Reality has meaning.

The Scout still should not immediately declare the final Problem.

It should ask:

- Is the human review mandatory or exceptional?
- Why does it exist?
- Is the AI output trusted?
- Which stage creates the delay?
- Does inconsistency originate in the model, data, workflow, or human decision?

The connection creates the **investigation surface**.

---

## Observation vs Interpretation

Reality Scout must preserve the boundary between what is observed and what is inferred.

```text
Observed
   ↓
Connected
   ↓
Interpreted
   ↓
Hypothesized
   ↓
Validated / Rejected
```

Example:

**Observed**

> The SOP contains a mandatory human review step.

**Connected**

> The review occurs after AI output and before the final operational action.

**Interpretation**

> The workflow does not fully trust the AI output.

**Hypothesis**

> Human review may be a major constraint on scaling the workflow.

**Unknown**

> Whether review is required for every case or only high-risk cases.

The Scout must never collapse these layers into one statement.

---

## Workflow

### 1. Capture

Collect the available customer Reality without prematurely organizing it.

### 2. Sense

Read the material from our position.

Record what feels:

- clear
- unclear
- contradictory
- suspicious
- missing
- unusually emphasized

### 3. Re-position

Read the same material from the customer's position.

Ask:

- Why did they send this?
- What are they trying to communicate?
- What are they likely worried about?
- What perspective dominates their material?
- What perspective is absent?

### 4. Extract Nodes

Identify meaningful entities, facts, claims, events, constraints, actors, systems, and unknowns.

### 5. Connect Nodes

Search across documents and dimensions for meaningful relationships.

Do not stop at document boundaries.

### 6. Detect Structure

Look for:

- repeated relationships
- causal chains
- contradictions
- bottlenecks
- dependencies
- missing links
- isolated nodes
- perspective gaps

### 7. Form Meaning

Describe the emerging structure without pretending that every inference is confirmed.

### 8. Produce a Reality Map

Return a compact representation of:

- what is known
- how things connect
- what appears to matter
- what conflicts
- what is missing
- what remains uncertain
- what must be checked next

---

## Reality Map

The primary output is not a long report.

It is a **Reality Map**.

```markdown
# Reality Map

## Scope
What part of Reality is being reconstructed?

## Nodes
What meaningful entities / facts / signals were found?

## Relationships
How are the nodes connected?

## Observed Reality
What is directly supported?

## Perspectives
How are we and the customer looking at Reality?

## Emerging Patterns
What structure appears across multiple nodes?

## Contradictions
Which nodes disagree?

## Missing Links
Which relationships are required to understand the system but are not yet visible?

## Unknowns
What cannot yet be established?

## Hypotheses
What explanations are plausible but unconfirmed?

## Confidence
How stable is the current Reality model?

## Next Question
What single question would reduce the most uncertainty?
```

---

## Boundary

Reality Scout is responsible for:

- sensing Reality
- extracting nodes
- connecting nodes
- mapping relationships
- reconstructing context
- detecting emerging patterns
- identifying contradictions
- exposing missing links
- preserving uncertainty
- making perspective visible

Reality Scout is **not** responsible for:

- final capability assessment
- formal gap analysis
- runtime review
- solution design
- final decision
- forcing a clean narrative

```text
Reality Scout
      ↓
Reconstructed Reality
      ↓
Capability Assessment
Gap Analysis
Runtime Review
      ↓
Solution Package Design
```

---

## Downstream Contract

The downstream skills should not have to start from raw customer material whenever a Reality Map already exists.

### Capability Assessment asks

> What capabilities exist within this Reality?

### Gap Analysis asks

> Where does current Reality differ from required Reality?

### Runtime Review asks

> How does this Reality actually behave when the system runs?

### Solution Package Design asks

> Where and how can we intervene in this Reality?

Reality Scout prepares the common substrate.

---

## Core Principles

### 1. Connect before judging

> **Do not evaluate a node before understanding the structure it participates in.**

### 2. Feeling is a sensor, not Evidence

> Use intuition to find where to look; use evidence to decide what to believe.

### 3. Customer material is also a perspective signal

> What the customer sends tells us not only what they know, but how they are looking at Reality.

### 4. Meaning lives in relationships

> A collection of facts is not necessarily understanding.

### 5. Preserve uncertainty

> Unknown is a valid state of Reality.

### 6. Do not solve too early

> A good Scout makes the next skill more accurate; it does not steal the next skill's job.

### 7. Reality must remain inspectable

Every important interpretation should be traceable back to the nodes and relationships that produced it.

---

## Runtime

Reality Scout is designed as a fast first-pass runtime skill.

### Target

**15–30 minutes to create a first Reality Map from a messy customer input set.**

The first pass does not need to be complete.

It needs to be **good enough to expose the structure and the highest-value unknowns**.

```text
0–5 min
Capture + Sense

5–15 min
Extract + Connect

15–25 min
Patterns + Perspective Gaps

25–30 min
Reality Map + Next Question
```

Then send the Reality Map back into the human feedback loop:

```text
Scout
  ↓
Reality Map
  ↓
Customer: Correct / Reject / Add
  ↓
Reality Update
  ↓
Downstream Skill
```

The goal is not to be perfectly right alone.

The goal is to reach **shared Reality faster**.

---

## Failure Modes

Reality Scout fails when:

- isolated facts are mistaken for Reality
- relationships are invented without evidence
- intuition is presented as fact
- customer perspective is ignored
- contradictions are smoothed away
- missing links are treated as irrelevant
- AI-generated assumptions become Reality
- the Scout jumps directly into solution design
- the output becomes a beautiful narrative that cannot be traced back to evidence

A particularly dangerous failure mode is:

> **Premature coherence** — making fragmented Reality look complete before it actually is.

The Scout must prefer an incomplete but inspectable Reality Map over a complete-looking fiction.

---

## Evolution

Reality Scout improves through runtime.

```text
Runtime
   ↓
Reality Map
   ↓
Customer Correction
   ↓
Failure / Friction
   ↓
New Pattern
   ↓
Skill Update
```

The skill should become better at **seeing connections**, not merely better at producing reports.

---

## Position in LH OS

Reality Scout is the first blade of the LH OS Runtime Toolbox.

```text
                 MESSY REALITY
                      ↓
              ┌───────────────┐
              │ REALITY SCOUT │
              └───────┬───────┘
                      ↓
               REALITY MAP
                      ↓
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
 Capability        Gap          Runtime
 Assessment       Analysis       Review
        │             │             │
        └─────────────┼─────────────┘
                      ↓
             Solution Package
                 Design
                      ↓
                   Runtime
                      ↓
                  Evidence
```

The Scout is therefore not just another analysis skill.

It is the **Reality reconstruction layer** that allows the rest of the toolbox to operate on the same world.

---

> **Reality enters LH OS as fragments.**
>
> **Reality Scout connects the fragments until meaning becomes inspectable.**
>
> **Connect the dots before judging the dots.**
