# Benchmark catalog

Generated from `benchmark_registry.jsonl`; edit the registry and regenerate this projection.

All capability and failure mappings are owner-directed derived candidates. No model scores are recorded.

| Benchmark | Environment | Intended capabilities | Potential failures | Dataset license | Source |
| --- | --- | --- | --- | --- | --- |
| MMLU | STATIC | knowledge, reasoning | knowledge_error | UNKNOWN | [pinned documentation](https://github.com/hendrycks/test/blob/4450500f923c49f1fb1dd3d99108a0bd9717b660/README.md) |
| MMLU-Pro | STATIC | knowledge, reasoning | reasoning_error | UNKNOWN | [pinned documentation](https://github.com/TIGER-AI-Lab/MMLU-Pro/blob/f418b116db00b065c2aea046518d8fcf74d39872/README.md) |
| GPQA | STATIC | expert_reasoning | reasoning_error | UNKNOWN | [pinned documentation](https://github.com/idavidrein/gpqa/blob/56686c06f5e19865c153de0fdb11be3890014df7/README.md) |
| HLE | STATIC | expert_reasoning, multimodal | reasoning_error | UNKNOWN | [pinned documentation](https://github.com/centerforaisafety/hle/blob/22ed3074b1e7b134bcbc09028d0ba320839b0655/README.md) |
| ARC-AGI-2 | STATIC | abstract_reasoning | generalization_failure | UNKNOWN | [pinned documentation](https://github.com/arcprize/ARC-AGI-2/blob/f3283f727488ad98fe575ea6a5ac981e4a188e49/readme.md) |
| TruthfulQA | STATIC | truthfulness | false_claim | Apache-2.0_UPSTREAM_DECLARED | [pinned documentation](https://github.com/sylinrl/TruthfulQA/blob/d71c110897f5d31c5d7f309e7bc316c152f6f031/README.md) |
| SimpleQA | STATIC | factuality, calibration | false_claim, miscalibration | MIT_UPSTREAM_DECLARED | [pinned documentation](https://github.com/openai/simple-evals/blob/652c89d0ca9df547706735883097e9537d40dc47/README.md) |
| HumanEval | EXECUTABLE | code_generation | test_failure | UNKNOWN | [pinned documentation](https://github.com/openai/human-eval/blob/6d43fb980f9fee3c892a914eda09951f772ad10d/README.md) |
| MBPP | EXECUTABLE | code_generation | test_failure | UNKNOWN | [pinned documentation](https://github.com/google-research/google-research/blob/e49bbfe381c9c0e564b937f1c4e163a2273c65cc/mbpp/README.md) |
| LiveCodeBench | EXECUTABLE | code_generation | test_failure, temporal_leakage | UNKNOWN | [pinned documentation](https://github.com/LiveCodeBench/LiveCodeBench/blob/28fef95ea8c9f7a547c8329f2cd3d32b92c1fa24/README.md) |
| HumanEval-XL | EXECUTABLE | code_generation, cross_lingual | semantic_drift, test_failure | UNKNOWN | [pinned documentation](https://github.com/floatai/HumanEval-XL/blob/1e9301f6cfc2d3481a7f7e44569982285238ac99/README.md) |
| mHumanEval | EXECUTABLE | code_generation, cross_lingual | semantic_drift, test_failure | UNKNOWN | [pinned documentation](https://github.com/mraihan-gmu/mHumanEval-Benchmark/blob/b4ac5b3f59bb8a9b27fabd2d63080963995b1388/README.md) |
| SWE-bench | REPOSITORY | software_engineering | test_failure, wrong_reference | UNKNOWN | [pinned documentation](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/README.md) |
| Terminal-Bench | SHELL_OS | terminal_use, planning | tool_misuse, premature_completion | UNKNOWN | [pinned documentation](https://github.com/harbor-framework/terminal-bench-1/blob/d28711d0da2675d0bb1d56de45ae5df6082438a3/README.md) |
| BFCL | TOOL_DB | tool_calling | tool_misuse, argument_error | UNKNOWN | [pinned documentation](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/README.md) |
| tau-bench | TOOL_DB | tool_calling, policy_compliance | authority_error, state_error | UNKNOWN | [pinned documentation](https://github.com/sierra-research/tau-bench/blob/59a200c6d575d595120f1cb70fea53cef0632f6b/README.md) |
| BrowseComp | WEB | web_research | wrong_reference, verification_failure | MIT_UPSTREAM_DECLARED | [pinned documentation](https://github.com/openai/simple-evals/blob/652c89d0ca9df547706735883097e9537d40dc47/README.md) |
| GAIA | INTERACTIVE | general_assistance, tool_calling, multimodal | tool_misuse, verification_failure | UNKNOWN | [pinned documentation](https://huggingface.co/datasets/gaia-benchmark/GAIA/blob/682dd723ee1e1697e00360edccf2366dc8418dd9/README.md) |
| WebArena | WEB | web_navigation, planning | state_error, premature_completion | UNKNOWN | [pinned documentation](https://github.com/web-arena-x/webarena/blob/dce04686a56253aefba7b18a4fa0937cf1dc987b/README.md) |
| OSWorld-2.x | DESKTOP | computer_use, planning | stale_state, tool_misuse, premature_completion | UNKNOWN | [pinned documentation](https://github.com/xlang-ai/OSWorld-V2/blob/acdd3493808e716825975b0f0208194bb2faf3c3/README.md) |
| RE-Bench | RESEARCH | research_engineering | verification_failure, budget_overrun | UNKNOWN | [pinned documentation](https://github.com/METR/RE-Bench/blob/93b98062e55f6945d4a7e213a3226dd419896170/README.md) |
| AgentBench | INTERACTIVE | agent_planning, tool_calling | state_error, tool_misuse | UNKNOWN | [pinned documentation](https://github.com/THUDM/AgentBench/blob/d1e4a10db08c87075c78972e48ecc182be03e2d5/README.md) |
| RULER | STATIC | long_context | context_loss | UNKNOWN | [pinned documentation](https://github.com/NVIDIA/RULER/blob/c3f5e3b4f87f97e048793bb510a3a6b19a46bf3a/README.md) |
| LongBench | STATIC | long_context, reading | context_loss | UNKNOWN | [pinned documentation](https://github.com/THUDM/LongBench/blob/2e00731f8d0bff23dc4325161044d0ed8af94c1e/README.md) |
| MMMU | STATIC | multimodal, expert_reasoning | visual_grounding_error, reasoning_error | UNKNOWN | [pinned documentation](https://github.com/MMMU-Benchmark/MMMU/blob/268471d0d488258990025331c7528359c324aa25/README.md) |
| Video-MME | STATIC | video_understanding | temporal_reasoning_error, visual_grounding_error | CUSTOM_ACADEMIC_ONLY_NO_COMMERCIAL_USE | [pinned documentation](https://github.com/MME-Benchmarks/Video-MME/blob/06c2315b892f88578f81d73205d07cf576f292b9/README.md) |
| HarmBench | ADVERSARIAL | safety_behavior | unsafe_compliance | UNKNOWN | [pinned documentation](https://github.com/centerforaisafety/HarmBench/blob/8e1604d1171fe8a48d8febecd22f600e462bdcdd/README.md) |
| JailbreakBench | ADVERSARIAL | safety_behavior | unsafe_compliance | UNKNOWN | [pinned documentation](https://github.com/JailbreakBench/jailbreakbench/blob/23dbdf6b19650521604456229bc1d9c4156c85c1/README.md) |
| HELM | SUITE | multi_scenario_evaluation | metric_misinterpretation | UNKNOWN | [pinned documentation](https://github.com/stanford-crfm/helm/blob/63754d05db6f874e41a395880fb573890a13e791/README.md) |
| lm-eval | SUITE | multi_scenario_evaluation | metric_misinterpretation | UNKNOWN | [pinned documentation](https://github.com/EleutherAI/lm-evaluation-harness/blob/d6de81643928d653435c431bae19945d41d32520/README.md) |
