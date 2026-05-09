This repo contains a single skill: `idea-harness`.

The skill lives in `skills/idea-harness/`. Entry point is `SKILL.md`; it references four supporting files:

- `STATE-MACHINE.md` — four states and their transition rules
- `PRECISION-GATE.md` — four precision checks that gate the `ready` state
- `OUTPUTS.md` — output templates for each state
- `VOCABULARY.md` — internal terms and user-facing language rules
- `EXAMPLES.md` — full conversation examples (Chinese + English)

The skill clarifies vague app ideas via Socratic questioning. It does NOT generate code, choose tech stacks, or expand scope.

`scripts/verify.sh` runs static smoke checks (requires `ripgrep`). CI runs it on every push.

When editing skill files:

- `SKILL.md` must stay under 120 lines.
- User-visible outputs must never expose internal terms (state names, gate names, audit labels).
- Every "non-goal" line in `EXAMPLES.md` must include a reason after ` — `.
