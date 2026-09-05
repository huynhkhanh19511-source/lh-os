# Process — Running one JD through JD Market Scout

## Steps

1. **Capture Source**
   - Save the JD (or a clean extract) into `input/jds/`.
   - Prefer original text over heavy rewriting.

2. **Create Evidence Record**
   - Copy `schema/evidence-record.md`.
   - Name it clearly, e.g. `evidence/records/2026-09-05-rwazi-decision-systems-architect.md`.
   - Fill in strict order:
     - Meta
     - Source (Observed only)
     - Inference
     - Hypothesis
     - My Evidence vs Gap
     - Decision EV
     - Decision
     - Proof Needed

3. **Force a Decision**
   - Must be one of: Apply / Watch / Reject.
   - Write a short rationale.

4. **Update Application Queue**
   - Add or update the row in `analysis/application-queue.md`.

5. **Act**
   - If Decision = Apply → submit the application.
   - Record the action in the Runtime Log section of the Evidence Record.

6. **Close the loop**
   - When any Runtime signal arrives (auto-reject, recruiter reply, interview, feedback, offer):
     - Update the Runtime Log.
     - Update Fit / Gap beliefs.
     - Update `analysis/fit-matrix.md` and `analysis/cross-jd-patterns.md` if the signal is meaningful.

## Anti-patterns

- Analyzing a JD and stopping at “interesting”.
- Mixing Source and Inference in the same paragraph.
- Inventing a numeric P(success).
- Creating new abstractions because the current ones feel incomplete.
- Leaving a JD without a Decision.
