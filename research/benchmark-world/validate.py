"""Validate the catalog and ontology locally; never runs upstream benchmark code."""
import copy
import json
from pathlib import Path
import re
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent
EXPECTED = set('mmlu mmlu-pro gpqa hle arc-agi-2 truthfulqa simpleqa humaneval mbpp livecodebench humaneval-xl mhumaneval swe-bench terminal-bench bfcl tau-bench browsecomp gaia webarena osworld-2.x re-bench agentbench ruler longbench mmmu video-mme harmbench jailbreakbench helm lm-eval'.split())

def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def run():
    world_schema = load('benchmark_world.schema.json')
    registry_schema = load('benchmark_registry.schema.json')
    for schema in [world_schema, registry_schema]:
        Draft202012Validator.check_schema(schema)
    world = Draft202012Validator(world_schema, format_checker=FormatChecker())
    registry = Draft202012Validator(registry_schema, format_checker=FormatChecker())
    rows = [json.loads(line) for line in (ROOT / 'benchmark_registry.jsonl').read_text(encoding='utf-8').splitlines()]
    taxonomy = load('capability_taxonomy.json')
    assert len(rows) == len(EXPECTED)
    assert {r['benchmark_id'] for r in rows} == EXPECTED
    for row in rows:
        registry.validate(row)
        assert set(row['capabilities']) <= set(taxonomy['capabilities'])
        assert set(row['failure_classes']) <= set(taxonomy['failure_classes'])
        assert row['assurance']['evidence_backed']
        assert re.fullmatch('[a-f0-9]{40}', row['provenance']['commit_sha'])
        assert re.fullmatch('[a-f0-9]{64}', row['provenance']['readme_sha256'])
        assert row['provenance']['commit_sha'] in row['provenance']['readme_url']
        assert all(e['line_end'] >= e['line_start'] for e in row['documentation_evidence'])
    example = load('benchmark_world.example.json')
    world.validate(example)
    assert example['outcome']['measurement_status'] == 'NOT_RUN'
    assert all(example['outcome'][k] is None for k in ['score', 'success', 'partial_success', 'latency_seconds', 'tokens', 'retries'])
    # Meaningful rejection checks: missing provenance, untyped outcomes, extra claims,
    # and accidental raw vendoring must fail instead of silently passing.
    bad_examples = []
    bad = copy.deepcopy(example)
    bad['outcome']['success'] = 'true'
    bad_examples.append((world, bad))
    bad = copy.deepcopy(example)
    bad['outcome']['score'] = 0
    bad_examples.append((world, bad))
    bad = copy.deepcopy(example)
    bad['epistemics']['confidence'] = 1.1
    bad_examples.append((world, bad))
    bad = copy.deepcopy(rows[0])
    del bad['provenance']
    bad_examples.append((registry, bad))
    bad = copy.deepcopy(rows[0])
    bad['available_public_data_fields']['raw_payload_vendored'] = True
    bad_examples.append((registry, bad))
    bad = copy.deepcopy(rows[0])
    bad['score'] = 100
    bad_examples.append((registry, bad))
    for validator, bad in bad_examples:
        assert list(validator.iter_errors(bad)), 'Malformed fixture was accepted'
    result = {'status': 'PASS', 'registry_rows': len(rows), 'source_pins_checked': len(rows),
              'schemas_valid': 2, 'example_valid': True, 'rejection_cases_passed': len(bad_examples),
              'dataset_license_unknown': [r['benchmark_id'] for r in rows if r['license_reuse']['dataset_license'] == 'UNKNOWN'],
              'redistribution_unknown': [r['benchmark_id'] for r in rows if r['license_reuse']['redistribution_permission'] == 'UNKNOWN'],
              'scope': 'LOCAL_STRUCTURAL_VALIDATION_NOT_INDEPENDENT_SEMANTIC_OR_LEGAL_VALIDATION'}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result

if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        print(f'VALIDATION_FAILED: {type(exc).__name__}: {exc}', file=sys.stderr)
        sys.exit(1)
