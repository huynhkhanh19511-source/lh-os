# Customer Judgment

## Definition

**Customer Judgment is the ability to determine whether the system should be built before determining how the system should be built.**

Core question:

> **Is this worth building, and does it solve the real pain?**

Customer Judgment is the capability to understand the business context, people, workflow, constraints, and underlying pain behind surface-level requirements.

## Newbridge Bridge Capability

Newbridge exposes this capability through:

> **Customer embed + discovery under commercial pressure**

This is not simply customer interviewing. The practitioner must enter customer Reality, discover the actual bottleneck, scope an intervention, and make a build / test / don't-build decision while time, budget, revenue, and outcome pressure are real.

## Node → Network → Flow

### Node — What is this?

Identify actors, requirements, systems, data, constraints, and stated requests.

### Network — How is everything connected?

Map stakeholders, dependencies, handoffs, incentives, constraints, and causal relationships.

### Flow — How does the business actually move?

Model the current workflow, locate bottlenecks, and identify where an intervention could change the flow.

Architectural Sensemaking therefore moves from:

```text
NODE
  ↓
NETWORK
  ↓
FLOW
```

The Architect does not stop at observing the flow; the Architect asks how the flow should be redesigned.

## Customer Judgment Flow

```text
Customer Requirement
        ↓
Observed Reality
        ↓
Actors + Network
        ↓
Current Business Flow
        ↓
Pain / Bottleneck
        ↓
Business Impact
        ↓
Root Cause Hypothesis
        ↓
Intervention Hypothesis
        ↓
BUILD / TEST / DON'T BUILD
        ↓
Architecture
        ↓
Prototype → Runtime → Outcome
```

## Relationship to Other Judgments

| Judgment | Core question |
|---|---|
| **Customer Judgment** | Should we build this? Are we solving the real pain? |
| **Architecture Judgment** | If worth solving, how should the system be organized? |
| **Technical Judgment** | How should we implement it under the constraints? |

Customer Judgment therefore sits **upstream of Architecture Judgment**.

## Newbridge Mapping

| Newbridge signal | LH OS capability |
|---|---|
| Customer embed | Reality sensing |
| Discovery | Customer Judgment |
| Commercial pressure | Decision under constraints |
| Architecture | Flow / System design |
| Prototype | Artifact → Runtime |
| Production | Runtime capability |
| Own outcome | Evidence / Outcome measurement |

## Evidence Required

Close this gap through repeated cases that produce evidence:

1. Stated requirement
2. Observed Reality
3. Actors / stakeholders
4. Current Flow
5. Pain / bottleneck
6. Business impact
7. Root-cause hypothesis
8. Proposed intervention
9. Build / Test / Don't Build decision
10. Success metric
11. Runtime evidence
12. Outcome / belief update

## Runtime Principle

Do not close Customer Judgment by collecting “customer discovery knowledge”. Close it through:

```text
Reality
  ↓
Decision
  ↓
Artifact
  ↓
Runtime
  ↓
Outcome
  ↓
Belief Update
```

The purpose is to turn customer understanding into a decision that can be tested against Reality.

## Strategic Role in LH OS

The bridge is not only:

```text
Decision Architecture → Deployment
```

It is:

```text
Customer Reality
      ↓
Customer Judgment
      ↓
Architecture
      ↓
Prototype
      ↓
Runtime
      ↓
Outcome
```

Without Customer Judgment, LH can build a technically correct solution for the wrong problem.
