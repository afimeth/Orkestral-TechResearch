"""Rebuild the human catalog and source observation projection from local metadata."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def project():
    rows = [json.loads(line) for line in (ROOT / 'benchmark_registry.jsonl').read_text(encoding='utf-8').splitlines()]
    reviews = [json.loads(line) for line in (ROOT / 'source_reviews.jsonl').read_text(encoding='utf-8').splitlines()]
    lines = ['# Benchmark catalog', '',
             'Generated from `benchmark_registry.jsonl`; regenerate with `project_catalog.py`.', '',
             'Capability/failure mappings are owner-directed derived candidates. No model scores are recorded.', '',
             '| Benchmark | Environment | Intended capabilities | Potential failures | Dataset declaration | Source |',
             '| --- | --- | --- | --- | --- | --- |']
    for row in rows:
        lines.append(f'| {row["name"]} | {row["environment_type"]} | {", ".join(row["capabilities"])} | '
                     f'{", ".join(row["failure_classes"])} | {row["license_reuse"]["dataset_license"]} | '
                     f'[pinned documentation]({row["provenance"]["readme_url"]}) |')
    (ROOT / 'catalog.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    observation = {'scope': 'PUBLIC_DOCUMENTATION_ONLY_NO_DATASET_PAYLOADS_OR_EXECUTION',
                   'assurance': 'SELF_OBSERVED_NOT_INDEPENDENT_THIRD_PARTY_VALIDATION',
                   'sources': [{'benchmark_id': row['benchmark_id'], **row['provenance']} for row in rows],
                   'supplemental_reviews': reviews}
    (ROOT / 'source_observations.json').write_text(json.dumps(observation, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    project()
