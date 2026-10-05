# REA — Reverse Engineering Ware

REA is registered here as a **domain-specific plug/ware candidate** for the
New4 / Orkestral Tech Treasury. Runtime is **HOLD**. This branch supplies the
registry and boundary contract; it does not install a runtime adapter, modify
New4's ontology, or claim canonical architecture/state or Alexandria ingestion.

| Component | Contract role |
| --- | --- |
| REA | Reverse Engineering Ware; CLI/MCP plug |
| Ghidra / Hopper | Analysis providers, selected explicitly |
| New4 | Socket/environment; retains its own authority and routing |
| Alexandria | Evidence ingest target; existing writer/schema must be verified |

The integration contract is owner-requested design. It is not evidence that
these connections already exist in a running New4 installation.

## Decision and evidence

Reviewed source: [`348323dd23360bbac3841a9632ffcd08290566d2`](https://github.com/morluto/rea/tree/348323dd23360bbac3841a9632ffcd08290566d2).
The source LICENSE and package manifest declare MIT. Preserve the copyright
and permission notice when copying substantial REA code. Native analysis may
use free/open-source Ghidra; Hopper has a separate commercial license/demo.
No REA code is vendored in this registration. Target rights and dependency
licenses are separate from REA's license.

The source implements CLI dispatch and MCP stdio. Documentation describes
local analysis, and the code has typed, provider-bound evidence with semantic
IDs. Local-first does not mean network-free: package acquisition, optional
setup, browser/process operations, and the consuming agent have their own
effects. REA and Ghidra are not sandboxes.

**REA-DEPS-001 remains OPEN:** a lockfile-only npm production audit reported
four high-severity package entries: `@toon-format/toon`, `@xmldom/xmldom`,
`brace-expansion`, and `smol-toml`. These are dependency advisory matches,
not four proven REA exploits. Reachability is UNKNOWN. The complete dependency
audit reported ten package entries (six high, four moderate). No auto-fix was
applied. Independent review has not been performed.

Published `rea-agents@3.2.1` points to
`0356f7677f57898c5291658d7d4995784533ba6d`, which differs from the reviewed
source above. Downloaded release bytes matched npm's SHA-512 integrity value;
package signatures and provenance attestations were not independently verified.
The current-source review must not be transferred to the older package.
CI for the reviewed source was pending at observation, not passed.

Windows Ghidra is currently **unavailable**, not merely reduced-feature:
the source returns `unsupported_host` until native process ownership, private
DACLs and reparse-safe path admission exist. Manual MCP setup does not bypass
that gate. Linux/WSL2 is the planned route; it is not a runtime acceptance claim.

## Files and use

- [`registry.json`](registry.json): capabilities, inputs/outputs, interfaces,
  providers, realms, limitations and update/invalidation rules.
- [`registry.schema.json`](registry.schema.json): registration shape and
  fixed role/authority boundary for this candidate generation.
- [`contract.schema.json`](contract.schema.json): connector-neutral request and
  result envelope; preserves REA payloads and does not redefine either ontology.
- [`handoff.example.json`](handoff.example.json): synthetic HOLD example; no
  target, result, evidence or ingest receipt is claimed.
- [`RUNBOOK.md`](RUNBOOK.md): pinned installation/run path and WSL2 fallback,
  held until its security and prerequisite gates pass.
- [`sources.json`](sources.json): immutable source links and raw Git blob hashes,
  package/release metadata and bounded CI observation.
- [`security-review.json`](security-review.json): audit findings, source limits
  and explicit release conditions.
- [`receipt.json`](receipt.json): scope, hashes, validation and open acceptance.

Run from the repository root with Python and `jsonschema` already available:

```text
python -X utf8 wares/reverse-engineering/rea/validate.py
```

The validator checks schemas, role/authority separation, source pins, file
integrity and malformed-contract rejection. It neither contacts upstream nor
runs REA. Passing it validates this registration, not security or runtime.

## Evidence handoff and authority

Discover current capabilities for the exact target/provider/host. Default to
static, read-only analysis of an owner-authorized immutable copy. No target
execution, browser/process scenario, cloud upload, or provider substitution is
implicitly enabled. Ghidra itself needs local process launch and temporary
writes; the boundary must mediate these separately from target mutation.

Retain the raw REA bundle, evidence IDs, subject digest, provider version,
operation/parameters, analysis profile, environment, locations, limitations and
`observed` / `derived` / `inferred` classifications. Validate upstream semantic
IDs with the matching REA parser as well as transport SHA-256. If redaction is
needed, retain the private original and record a separately hashed derivative.
Do not edit a raw record and retain its former identity.

An adapter stages a local bundle and verifies its digest before asking the
existing Alexandria writer to validate/import it. No endpoint is invented here.
The candidate envelope permits only `NOT_ATTEMPTED` or `STAGED_LOCAL` ingest;
durable ingest acknowledgement is a separate future receipt. Unknown provider,
schema, capability, target integrity or authorization stops dispatch.

An upstream update, lockfile/advisory change, provider/Node/JDK/realm change,
contract change, target digest change or operation/profile change invalidates
affected readiness and cache reuse. Keep historical receipts. Re-pin and review
through a new branch/PR; never use `latest`, automatic `rea upgrade`, or automatic
merge to turn this candidate into a live integration.
