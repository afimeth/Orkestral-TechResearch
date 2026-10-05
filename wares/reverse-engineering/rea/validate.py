"""Offline metadata checks only; never launches REA or writes an ingest record."""
import copy
import hashlib
import json
from pathlib import Path
import re
import sys

from jsonschema import Draft202012Validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def read(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_registration(registry, sources, security):
    Draft202012Validator(read("registry.schema.json")).validate(registry)
    pin = registry["source"]["commit"]
    require(re.fullmatch(r"[0-9a-f]{40}", pin), "invalid source commit")
    require(pin == sources["source_commit"] == security["source_commit"], "source pin mismatch")
    require(registry["install_run"]["runtime_gate"] == "HOLD", "runtime gate changed")
    require(registry["integration"]["ontology_conversion"] is False, "ontology conversion forbidden")
    require(registry["integration"]["canonical_architecture_claim"] is False, "canonical claim forbidden")
    require(registry["integration"]["ingest_endpoint"] is None, "invented ingest endpoint")
    require(registry["source"]["release_commit"] == sources["npm"]["git_head"], "release pin mismatch")
    require(registry["source"]["release_equals_reviewed_source"] == (pin == sources["npm"]["git_head"]), "release conflation")
    require(security["audit"]["production_counts"]["high"] > 0, "review finding unexpectedly changed")
    require(security["finding_status"] == "OPEN", "producer cannot close security finding")
    ids = {s["id"] for s in sources["files"]}
    require(len(ids) == len(sources["files"]), "duplicate source IDs")
    for s in sources["files"]:
        require(s["commit"] == pin, "mixed source generation")
        require(re.fullmatch(r"[0-9a-f]{64}", s["sha256"]), "invalid source digest")
        require(s["url"] == f"https://github.com/morluto/rea/blob/{pin}/{s['path']}", "mutable source URL")
    lock = next(s for s in sources["files"] if s["id"] == "lock")
    require(lock["sha256"] == security["audit"]["lock_sha256"], "audit lock mismatch")
    def refs(value):
        if isinstance(value, dict):
            for k, v in value.items():
                if k == "source_refs":
                    require(set(v) <= ids, "missing source reference")
                else:
                    refs(v)
        elif isinstance(value, list):
            for v in value:
                refs(v)
    refs(registry)


def main():
    for name in ["registry.schema.json", "contract.schema.json"]:
        Draft202012Validator.check_schema(read(name))
    registry, sources, security = map(read, ["registry.json", "sources.json", "security-review.json"])
    validate_registration(registry, sources, security)
    contract = Draft202012Validator(read("contract.schema.json"))
    example = read("handoff.example.json")
    contract.validate(example)
    require(example["result"]["status"] == "HOLD", "example must not invent a run")
    rejected = 0
    def reject(candidate, validate):
        nonlocal rejected
        try:
            validate(candidate)
        except (ValueError, __import__('jsonschema').ValidationError):
            rejected += 1
        else:
            raise ValueError("negative control was incorrectly accepted")
    for path, value in [
        (("authority", "canonical_promoted"), True),
        (("authority", "alexandria_ingested"), True),
        (("request", "target", "owner_authorized"), False),
        (("request", "target", "sha256"), "bad"),
        (("request", "effects", "execute_target"), True),
        (("result", "status"), "OBSERVED"),
        (("result", "bundle_sha256"), "a" * 64),
        (("result", "ingest"), "ACCEPTED"),
        (("source_commit",), "f" * 40),
    ]:
        candidate = copy.deepcopy(example)
        target = candidate
        for part in path[:-1]:
            target = target[part]
        target[path[-1]] = value
        reject(candidate, contract.validate)
    for path, value in [
        (("roles", "REA"), "New4 ontology"),
        (("source", "release_equals_reviewed_source"), True),
        (("install_run", "runtime_gate"), "READY"),
    ]:
        candidate = copy.deepcopy(registry)
        candidate[path[0]][path[1]] = value
        reject(candidate, lambda r: validate_registration(r, sources, security))
    receipt = read("receipt.json")
    expected = {p.relative_to(ROOT).as_posix() for p in HERE.iterdir()
                if p.is_file() and p.name != "receipt.json"} | {"README.md"}
    require(set(receipt["files"]) == expected, "receipt scope mismatch")
    for name, digest in receipt["files"].items():
        path = (ROOT / name).resolve()
        require(path.is_relative_to(ROOT), "receipt path escapes repo")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, "file hash mismatch: " + name)
    print(json.dumps({"status": "PASS", "schemas": 2, "negative_controls": rejected,
                      "hashed_files": len(expected), "runtime": "NOT_RUN",
                      "independent_review": "NOT_PERFORMED"}))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}))
        sys.exit(1)
