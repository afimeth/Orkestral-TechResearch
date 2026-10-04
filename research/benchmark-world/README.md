# benchmark.world

An owner-authored research primitive, normalized with AI assistance from public
benchmark documentation. This catalog makes benchmark environments, intended
capabilities, potential failure classes and source provenance machine-readable.
It is evidence-backed at the documentation level and **not independently
validated by a third party**. It contains no new benchmark runs or model scores.

**benchmark score != truth.** A score depends on a task distribution, harness,
prompt, sampling, tools, budget, model revision and verifier. It does not prove
universal competence, safety, factual truth, production readiness or authority.
The failure taxonomy is a derived candidate; benchmark coverage is not a causal
diagnosis of a particular worker's failure. Run trajectories may support later
analysis, but the catalog does not claim to have collected them.

**public access != unrestricted redistribution.** Source links, metadata,
schemas and derived summaries are preferred. No raw questions, reference
solutions, patches, media, copyrighted datasets, gated assets or private personal
corpus are vendored. A repository's code license does not clear all associated
dataset, media or inherited rights. Raw ingestion or redistribution requires a
separate artifact-specific license and terms check. This repository does not
grant rights to upstream assets or provide legal clearance.

## Files and contracts

| File | Purpose |
| --- | --- |
| `benchmark_registry.jsonl` | One catalog row per benchmark or framework, 30 rows |
| `benchmark_registry.schema.json` | Strict JSON Schema for catalog rows |
| `benchmark_world.schema.json` | Strict Draft 2020-12 ontology for an individual run |
| `benchmark_world.example.json` | Explicit `NOT_RUN` example, with null measurements |
| `capability_taxonomy.json` | Derived capability and potential failure labels |
| `validate.py` | Schema, coverage, taxonomy, provenance and rejection checks |
| `catalog.md` | Human-readable projection of the registry |
| `source_observations.json` | Source hashes and inspection scope |

The ontology preserves identity, world, task, worker, trajectory, outcome,
failure analysis and epistemics. `UNKNOWN` denotes an unchecked textual fact;
null numeric/boolean measurements are not zero or failure. An empty trajectory
with `NOT_RUN` means no capture occurred, not a successful run without actions.
`benchmark_version` is independent of the pinned documentation commit. Run
records must pin the actual task revision, model and verifier before comparison.
The example is a format demonstration, not execution evidence.

The registry includes MMLU, MMLU-Pro, GPQA, HLE, ARC-AGI-2, TruthfulQA, SimpleQA,
HumanEval, MBPP, LiveCodeBench, HumanEval-XL, mHumanEval, SWE-bench, Terminal-Bench,
BFCL, tau-bench, BrowseComp, GAIA, WebArena, OSWorld 2.x, RE-Bench, AgentBench,
RULER, LongBench, MMMU, Video-MME, HarmBench, JailbreakBench, HELM and lm-eval.
HELM and lm-eval are framework entries, not single datasets. Multi-environment
families use a dominant environment label; a real run must describe its subset.

## Evidence and limits

Each row points to an observed public README or dataset card at an immutable
source commit, with a SHA256 digest and line references. `evidence_backed` means
documentation was observed; it does not certify every derived classification.
`public_artifacts` contains links found in that documentation; those destinations
were not all separately accessed. `candidate_fields` describes documentation
level artifact/field candidates, not a verified payload schema. No upstream code
was executed. No dataset access gate was accepted or bypassed.

Geographic source affiliation is `UNKNOWN` because it has not been checked.
Language/domain projection is recorded separately and must not be mistaken for
nationality, universal validity, or cross-region equivalence. Most exact
benchmark versions and dataset license scopes remain `UNKNOWN`. A GitHub-reported
SPDX identifier is recorded only for the repository and is not dataset clearance.

Known boundaries observed in the pinned documentation:

- [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) restricts public
  crawlable redistribution. The public dataset card was read; gated payloads
  were not accessed. Private test answers remain distinct from public metadata.
- [OSWorld-V2](https://github.com/xlang-ai/OSWorld-V2) recommends `osworld-v2.1`
  and separates public code from gated task classes and complete assets.
- [Video-MME](https://github.com/MME-Benchmarks/Video-MME) restricts commercial
  use and redistribution without approval; video owners retain copyright.
- [tau-bench](https://github.com/sierra-research/tau-bench) marks its task
  versions outdated and directs readers to a successor repository.
- [simple-evals](https://github.com/openai/simple-evals) retains reference
  implementations while announcing deprecation of new model result updates.

## Validate locally

Requires Python 3.10+ and `jsonschema` with Draft 2020-12 support. It does not
require upstream benchmark runtimes, model credentials or network access.

```text
python research/benchmark-world/validate.py
```

Validation checks both schemas, all rows, required benchmark coverage, taxonomy
references, immutable source links, null `NOT_RUN` measurements and malformed
record rejection. Structural validation is self-validation, not independent
semantic, empirical or legal review. Source observation time and source revision
are stored in the registry; later updates must re-observe sources and preserve
version distinctions rather than silently replacing provenance.

This is a reviewable research candidate on a dedicated branch. Owner review,
merge, adoption and any operational deployment are separate decisions.
