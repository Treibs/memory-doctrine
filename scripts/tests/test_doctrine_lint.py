import subprocess, sys, textwrap
from pathlib import Path

LINT = Path(__file__).resolve().parents[1] / "doctrine_lint.py"

def _pkg(tmp_path, axioms=None, evidence=None):
    (tmp_path / "axioms").mkdir(); (tmp_path / "evidence").mkdir()
    for name, body in (axioms or {}).items():
        (tmp_path / "axioms" / f"{name}.md").write_text(textwrap.dedent(body))
    for name, body in (evidence or {}).items():
        (tmp_path / "evidence" / f"{name}.md").write_text(textwrap.dedent(body))
    return tmp_path

GOOD_AX = """\
    ---
    id: B1-x
    type: axiom
    cluster: B-retrieval
    title: t
    statement: s
    domain: d
    generativity: 5
    confidence: 0.9
    status: locked
    relations: {derives-from: [], supports: [], generalizes: [], contradicts: [], applies-to-kpm: []}
    evidence: [src-1]
    provenance: p
    verification: {challenged: true, citations_checked: true, gate: g}
    ---
    Body cites [[src-1]].
    """
GOOD_EV = """\
    ---
    id: src-1
    type: evidence
    ref: r
    url: https://example.com
    verified: 2026-06-03
    supports: [B1-x]
    proves: p
    limits: l
    ---
    Note.
    """

def run(pkg):
    return subprocess.run([sys.executable, str(LINT), str(pkg)],
                          capture_output=True, text=True)

def test_clean_package_passes(tmp_path):
    pkg = _pkg(tmp_path, {"B1-x": GOOD_AX}, {"src-1": GOOD_EV})
    r = run(pkg)
    assert r.returncode == 0, r.stdout + r.stderr

def test_confidence_out_of_range_fails(tmp_path):
    bad = GOOD_AX.replace("confidence: 0.9", "confidence: 1.7")
    pkg = _pkg(tmp_path, {"B1-x": bad}, {"src-1": GOOD_EV})
    r = run(pkg)
    assert r.returncode == 1 and "confidence" in r.stdout

def test_missing_evidence_fails(tmp_path):
    bad = GOOD_AX.replace("evidence: [src-1]", "evidence: []")
    pkg = _pkg(tmp_path, {"B1-x": bad}, {"src-1": GOOD_EV})
    r = run(pkg)
    assert r.returncode == 1 and "evidence" in r.stdout

def test_dangling_relation_fails(tmp_path):
    bad = GOOD_AX.replace("supports: []", "supports: [does-not-exist]")
    pkg = _pkg(tmp_path, {"B1-x": bad}, {"src-1": GOOD_EV})
    r = run(pkg)
    assert r.returncode == 1 and "does-not-exist" in r.stdout

def test_relation_not_wikilinked_fails(tmp_path):
    other = GOOD_AX.replace("id: B1-x", "id: B-other")
    bad = GOOD_AX.replace("supports: []", "supports: [B-other]")
    pkg = _pkg(tmp_path, {"B1-x": bad, "B-other": other}, {"src-1": GOOD_EV})
    r = run(pkg)
    assert r.returncode == 1 and "wikilink" in r.stdout.lower()

def test_contradicts_among_locked_fails_F2(tmp_path):
    other = GOOD_AX.replace("id: B1-x", "id: B-other")
    bad = GOOD_AX.replace("contradicts: []", "contradicts: [B-other]") \
                 .replace("Body cites [[src-1]].", "Body cites [[src-1]] vs [[B-other]].")
    pkg = _pkg(tmp_path, {"B1-x": bad, "B-other": other}, {"src-1": GOOD_EV})
    r = run(pkg)
    assert r.returncode == 1 and "F2" in r.stdout

def test_evidence_missing_url_fails(tmp_path):
    bad_ev = GOOD_EV.replace("url: https://example.com\n", "")
    pkg = _pkg(tmp_path, {"B1-x": GOOD_AX}, {"src-1": bad_ev})
    r = run(pkg)
    assert r.returncode == 1 and "url" in r.stdout
