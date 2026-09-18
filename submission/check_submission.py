"""Validate current submission membership and integrity using only the standard library."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROLES = {'paper': 'publications/pnp-mathic/editions/20260918T220300Z/Problem_No_Problem_Paginated.pdf', 'paper_source': 'publications/pnp-mathic/editions/20260918T220300Z/Problem_No_Problem_Layout_Source.docx', 'paper_lock': 'publications/pnp-mathic/editions/20260918T220300Z/LOCK.json', 'paper_checksums': 'publications/pnp-mathic/editions/20260918T220300Z/SHA256SUMS.json', 'guide': 'review/reader-guide/v1_0/Problem_No_Problem_READERS_GUIDE_v1_0.LOCKED.pdf', 'score': 'charts/pnp/TRYX.PNP.LOCAL.CLOSURE.MATHIC.SCORE.LYRIC.SUCCESSOR.260905.LOCKED.html', 'governing_source': 'publications/pnp-mathic/sources/TRYX.PNP.CONTINUITY.CLOSURE.REINTRODUCTION.BENCHMARK.260831.235122Z.md', 'lean_core': 'verification/tryx-lean/TryxProof.lean', 'lean_bridge': 'verification/tryx-lean/TryxMathic.lean', 'lean_challenge': 'verification/tryx-lean/TryxChallenge.lean', 'independent_targets': 'verification/tryx-lean/comparator.json', 'dependency_pins': 'verification/tryx-lean/lake-manifest.json', 'toolchain': 'verification/tryx-lean/lean-toolchain', 'instrument': 'charts/pnp/PNP_CODEBREAKER_TRI_E6B_XMAS_FORMULA_PAGE_v65.LOCKED.html', 'replay': 'publications/pnp-mathic/replay.py', 'oracle': 'publications/pnp-mathic/independent_check.py', 'authority': 'submission/AUTHORITY.md', 'verification': 'submission/VERIFICATION.md', 'citation': 'CITATION.cff'}

def main():
    manifest = json.loads((ROOT / "submission/MANIFEST.json").read_text())
    if manifest.get("schema") != "PNP.SUBMISSION.v1":
        raise SystemExit("Unsupported submission schema")
    if manifest.get("roles") != REQUIRED_ROLES:
        raise SystemExit("Missing or changed required submission role")
    files = manifest["files_sha256"]
    for role, name in REQUIRED_ROLES.items():
        if name not in files:
            raise SystemExit(f"Unhashed required artifact: {role}: {name}")
    for name, expected in files.items():
        path = Path(name)
        if path.is_absolute() or ".." in path.parts:
            raise SystemExit(f"Invalid manifest path: {name}")
        if "BETA" in name or "LIVE_CANDIDATE" in name or name.startswith("archive/"):
            raise SystemExit(f"Historical/candidate artifact in current submission: {name}")
        actual = ROOT / path
        if not actual.is_file() or hashlib.sha256(actual.read_bytes()).hexdigest() != expected:
            raise SystemExit(f"Submission missing or altered: {name}")
    for directory in ["publications/pnp-mathic/editions/20260918T220300Z", "review/reader-guide/v1_0"]:
        for name, expected in json.loads((ROOT / directory / "SHA256SUMS.json").read_text()).items():
            path = ROOT / directory / name
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                raise SystemExit(f"Locked edition mismatch: {directory}/{name}")
    print(f"PASS: current submission roles, {len(files)} artifact hashes, and locked editions")

if __name__ == "__main__":
    main()
