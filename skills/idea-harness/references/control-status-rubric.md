# Control Status Rubric

Use this rubric to decide the internal Idea Control Status. The state is determined by blocking gates, not by confidence.

Do not expose these internal states to ordinary users by default. Map them to the public statuses:

| Internal state | Public status |
|---|---|
| `Blocked` | `Need More Info` |
| `Draftable` | `Need More Info` |
| `Contract-Ready` | `Need More Info` |
| `Execution-Ready` | `Ready` |

## Evidence States

| Status | Meaning | Can unlock Execution-Ready |
|---|---|---|
| `Confirmed` | The user explicitly said it or confirmed it. | Yes |
| `Candidate` | The AI inferred it, but the user has not confirmed it. | No |
| `Missing` | There is no evidence. | No |
| `Conflict` | User statements conflict or point in incompatible directions. | No |

## Blocking Gates

The following fields unlock final execution only when `Confirmed`. `Candidate`, `Missing`, and `Conflict` all block `Execution-Ready`:

- Goal
- Primary user
- Core workflow
- MVP must-haves
- Explicit non-goals
- Data persistence, when the product records user input
- Acceptance criteria

## State Transition Rules

Apply these rules in order:

```text
If Goal is not Confirmed -> Blocked
Else if Primary user is not Confirmed -> Blocked
Else if Core workflow is not Confirmed -> at most Draftable
Else if MVP must-haves is not Confirmed -> at most Draftable
Else if Explicit non-goals is not Confirmed -> at most Draftable
Else if Data persistence is relevant and not Confirmed -> at most Contract-Ready
Else if Acceptance criteria is not Confirmed -> at most Contract-Ready
Else -> Execution-Ready
```

## Allowed User-Facing Outputs

### Need More Info

Use whenever the internal state is `Blocked`, `Draftable`, or `Contract-Ready`.

Allowed:

- `当前结论`
- `已确认`
- `不能先假设`
- Exactly 1 `下一步` question

Forbidden:

- `执行 Prompt`
- Internal audit headings such as `Evidence Ledger`, `Blocking Unknowns`, `Assumption Firewall`, and `Requirement Contract`
- Technical stack recommendation
- Implementation plan

### Ready

Use only when the internal state is `Execution-Ready`.

Allowed:

- `当前结论`
- `已确认`
- `不能先假设`
- `执行 Prompt`

Required:

- Every hard requirement in the prompt must map to confirmed user evidence.
- The prompt must include V1 non-goals and forbidden assumptions.
- The prompt must include observable acceptance criteria.

## Internal Allowed Outputs By State

Use this section only when the user explicitly asks for the audit view or when maintaining tests and internal documentation.

### Blocked

Use when the idea is too broad or a high-risk gate is missing or conflicting.

Allowed:

- Current understanding
- Evidence Ledger
- Blocking Unknowns
- Assumption Firewall
- Exactly 1 Next Best Question

Forbidden:

- Any `Requirement Contract` heading or content
- Final AI Execution Prompt
- Technical stack recommendation
- Implementation plan

### Draftable

Use when basic direction exists, but execution still requires AI guessing.

Allowed:

- Requirement draft
- Evidence Ledger
- Blocking Unknowns
- Assumption Firewall
- Up to 3 questions
- Requirement Contract draft only if every unconfirmed field is marked `[NEEDS CLARIFICATION]`

Forbidden:

- Final AI Execution Prompt
- Treating `Candidate` fields as requirements
- Filling unconfirmed contract fields as hard requirements

### Contract-Ready

Use when a contract draft can be formed but final execution still needs one confirmation or one non-critical blocking gate.

Allowed:

- Requirement Contract draft
- Acceptance criteria draft
- Final confirmation request or one last blocking question
- `[NEEDS CLARIFICATION]` placeholders for any field that still lacks confirmation

Forbidden:

- Final AI Execution Prompt
- Adding unconfirmed scope to hard requirements

### Execution-Ready

Use only when all blocking gates are `Confirmed`.

Allowed:

- Final Requirement Contract
- Acceptance criteria
- Assumption Firewall
- Final AI Execution Prompt

Required:

- Every hard requirement in the final prompt must map to a `Confirmed` Evidence Ledger row.
- The final prompt must include V1 non-goals and forbidden assumptions.

## Risk Defaults

Use these default risk levels unless the user evidence suggests otherwise:

| Situation | Risk |
|---|---|
| Goal missing or too broad | High |
| Primary user missing | High |
| Core workflow missing | High |
| MVP boundary missing | High |
| Explicit non-goals missing | High |
| Data persistence missing when user content exists | Medium |
| Acceptance criteria missing | High |
| Technical preference missing | Low |

## Common Dangerous Assumptions

Add unconfirmed items from this list to Assumption Firewall:

- Login or account system
- Database or long-term storage
- Multi-user collaboration
- Payment or subscription
- AI model calls or AI features
- Charts, analytics, dashboards
- Cloud sync
- Mobile app
- Notifications
- File upload
- Export formats
- Deployment target
- Admin panel
- Security architecture
