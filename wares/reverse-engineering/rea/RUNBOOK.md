# Installation and run path — HOLD

This is an operator runbook, not an executed installation. **Do not run the
installation/analysis steps while REA-DEPS-001 is open.** The registry is usable
now; runtime remains disabled until the security review, prerequisites and
independent review are recorded for one exact generation. No agent config or
system package is modified by this PR.

## 1. Select a realm and exact source

Use a Linux x86_64 realm (documented Ubuntu 24.04+, Fedora 41+, or 64-bit Arch).
The proposed Windows fallback is WSL2 with Linux-native tools and a workspace
on the Linux filesystem. A distro appearing in `wsl --list --verbose` proves
registration only. Check actual architecture, distro, tool paths and versions:

```sh
uname -m
cat /etc/os-release
command -v node npm java javac
node --version
npm --version
java -version
javac -version
```

Node must satisfy `^22.19.0 || >=24.11.0`; Ghidra must be 12.1.4 with a full
64-bit JDK 21 according to this source. A Windows `npm` found through `/mnt/c`
does not satisfy Linux readiness. Ghidra and Java are operator-managed; REA
does not install them. Verify official distribution hashes and retain each
artifact's license before use. Hopper is optional and is not the free default.

The reviewed source pin is `348323dd23360bbac3841a9632ffcd08290566d2`.
Its production dependency advisories must be resolved/reviewed before running.
If an upstream fix is selected, create a new registry generation with that
commit and lock hash; do not silently replace this pin. The older npm package
`3.2.1` is not an equivalent installation source.

## 2. Isolated, source-pinned installation after gate release

The following template requires `APPROVED_REA_COMMIT` to be set to the exact
commit in the reviewed replacement registry. An unset variable aborts. First
pass every outbound URL/command through the environment's sensitive-data gate;
if the gate is unavailable, do not fetch. No cloud target upload is needed.

```sh
set -eu
: "${APPROVED_REA_COMMIT:?Set from the reviewed registry generation}"
case "$APPROVED_REA_COMMIT" in *[!0-9a-f]*|'') exit 2;; esac
[ "${#APPROVED_REA_COMMIT}" -eq 40 ]
TASK_REA_ROOT="$HOME/.local/share/rea-ware/$APPROVED_REA_COMMIT"
test ! -e "$TASK_REA_ROOT"
git clone --no-checkout https://github.com/morluto/rea.git "$TASK_REA_ROOT"
git -C "$TASK_REA_ROOT" checkout --detach "$APPROVED_REA_COMMIT"
[ "$(git -C "$TASK_REA_ROOT" rev-parse HEAD)" = "$APPROVED_REA_COMMIT" ]
cd "$TASK_REA_ROOT"
sha256sum package-lock.json LICENSE
# Compare hashes to the replacement sources.json before proceeding.
npm ci --ignore-scripts --no-audit --no-fund
npm audit --package-lock-only --ignore-scripts --omit=dev --json
# Review every needed lifecycle/native dependency before explicitly enabling it.
# Build only after that review; no global install, setup, or shell installer.
HUSKY=0 npm run build
node scripts/rea.mjs --help
```

`--ignore-scripts` avoids automatic lifecycle hooks, but is not a sandbox or a
complete dependency review. Native/optional capabilities may need separately
reviewed build steps. Do not remove the flag and retry blindly. A failed build
is a recorded failure, not runtime readiness. The path above is proposed and
has not been created by this integration.

## 3. Explicit Ghidra diagnostics and benign fixture

After prerequisites and the source gate pass, set actual absolute Linux paths:

```sh
export GHIDRA_INSTALL_DIR=/opt/ghidra_12.1.4_PUBLIC
export JAVA_HOME=/opt/jdk-21
export REA_ANALYSIS_PROVIDER=ghidra
node "$TASK_REA_ROOT/scripts/rea.mjs" doctor --json
node "$TASK_REA_ROOT/scripts/rea.mjs" providers --json
```

Paths are examples and must exist in the selected realm. Record diagnostics,
source/lock identity and actual versions. Do not invoke interactive `setup`,
install client configuration or let `auto` select a different provider.

For acceptance, use a small owner-created Linux ELF fixture in an approved
Linux-local workspace, never a private/hostile target as the initial probe.
Copy it immutably, hash before and after, and bound execution externally:

```sh
sha256sum /approved-fixtures/sample
timeout 120s node "$TASK_REA_ROOT/scripts/rea.mjs" inspect \
  /approved-fixtures/sample --provider ghidra --format json \
  > /approved-output/inspect.json
sha256sum /approved-fixtures/sample /approved-output/inspect.json
```

Require success, the expected target hash, a real provider/version/profile,
nonempty evidence, explicit limitations, and owned-process cleanup. A timeout,
empty output or successful exit alone is not acceptance. CLI JSON must not be
assumed to be a complete transferable bundle. For MCP, discover tools, open
the explicit target/provider, inspect it, then call `get_evidence_bundle` to
retain the actual upstream bundle. Preserve raw bytes and its SHA-256.

## 4. MCP and WSL2 routing

REA's server command in the Linux realm is:

```sh
node "$TASK_REA_ROOT/scripts/rea.mjs" mcp
```

Use stdio. A connector-neutral launcher stores an argument vector, provider
environment and explicit timeout; it must not construct a shell command from
target input. A Windows client may launch `wsl.exe -d <verified-distro> --exec`
followed by the resolved Linux Node path, entrypoint and `mcp`. Pass Ghidra/JDK
configuration through a reviewed realm-local launcher. Do not assume a Windows
client's environment automatically reaches Linux or open a TCP listener.
No client-specific registration is installed in this PR.

Stage only authorized target bytes inside the Linux filesystem and verify the
hash again there. Return only the selected evidence bundle plus hashes and
receipt. WSL2 does not provide hostile-target containment merely by existing:
host mounts, Windows interop and user credentials can cross its boundary.
Untrusted native parsing needs a separately reviewed disposable VM/container
with no sensitive mounts, least privilege and controlled network access.
Linux analysis of a copied PE is not Windows process execution or browser
observation. macOS-only capabilities also remain unavailable in WSL.

## 5. Alexandria handoff, invalidation and rollback

Validate the candidate envelope against `contract.schema.json`; validate raw
REA evidence against the matching upstream parser and verify bundle SHA-256.
Keep observation, derivation and inference separate. Submit only through the
existing, verified Alexandria writer after its schema is known. This package
does not supply a direct DB write, endpoint, or authority grant. A local bundle
remains `STAGED_LOCAL` until a separate durable ingest receipt is observed.

Store the exact target/provider/source/profile/realm identity with each run.
Any change invalidates affected cache/readiness; preserve the old result as
historical evidence and revalidate. Runtime gate release needs independent
review and owner acceptance, not the producer's metadata check.

Rollback for this PR is a normal revert of the registry commit. A future
installation should remove only its own client registration and versioned
directory after evidence retention is verified; do not remove Ghidra, JDK,
other user projects or shared WSL distributions.
