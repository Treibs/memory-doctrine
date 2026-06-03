#!/usr/bin/env python3
"""Validate the doctrine KPM. Exit 0 = clean, 1 = violations (printed)."""
from __future__ import annotations
import re, sys
from pathlib import Path
import yaml

WIKILINK = re.compile(r"\[\[([^\]|#]+)")
REL_KEYS = ["derives-from", "supports", "generalizes", "contradicts", "applies-to-kpm"]

def _parse(p: Path):
    text = p.read_text()
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    try:
        return (yaml.safe_load(fm) or {}), body
    except yaml.YAMLError:
        return {}, text

def load(pkg: Path):
    notes = {}
    for sub in ("axioms", "evidence", "operators", "clusters"):
        d = pkg / sub
        if not d.is_dir():
            continue
        for f in d.glob("*.md"):
            fm, body = _parse(f)
            nid = fm.get("id", f.stem)
            notes[nid] = {"fm": fm, "body": body, "kind": sub, "path": f}
    return notes

def check(pkg: Path):
    notes = load(pkg)
    ids = set(notes)
    errs = []
    for nid, n in notes.items():
        fm, body, kind = n["fm"], n["body"], n["kind"]
        if kind == "axioms":
            c = fm.get("confidence")
            if not isinstance(c, (int, float)) or not (0.0 <= c <= 1.0):
                errs.append(f"{nid}: confidence {c!r} not in [0,1]")
            g = fm.get("generativity")
            if g not in (1, 2, 3, 4, 5):
                errs.append(f"{nid}: generativity {g!r} not in 1..5")
            ev = fm.get("evidence") or []
            if not ev:
                errs.append(f"{nid}: no evidence (every axiom needs >=1)")
            for e in ev:
                if e not in ids:
                    errs.append(f"{nid}: evidence '{e}' does not resolve")
            rel = fm.get("relations") or {}
            wikilinks = set(WIKILINK.findall(body))
            for k in REL_KEYS:
                for tgt in (rel.get(k) or []):
                    if k != "applies-to-kpm" and tgt not in ids:
                        errs.append(f"{nid}: relation {k} -> '{tgt}' does not resolve")
                    if k != "applies-to-kpm" and tgt in ids and tgt not in wikilinks:
                        errs.append(f"{nid}: relation {k} -> '{tgt}' missing matching [[wikilink]] in body")
                if k == "contradicts":
                    for tgt in (rel.get("contradicts") or []):
                        if fm.get("status") == "locked" and notes.get(tgt, {}).get("fm", {}).get("status") == "locked":
                            errs.append(f"{nid}: F2 invariant — 'contradicts' edge to locked axiom '{tgt}'")
        if kind == "evidence":
            if not fm.get("url"):
                errs.append(f"{nid}: evidence note missing url")
            if not fm.get("verified"):
                errs.append(f"{nid}: evidence note missing verified date")
    if errs:
        print(f"doctrine_lint: {len(errs)} violation(s):")
        for e in errs:
            print("  - " + e)
        return 1
    print(f"doctrine_lint: OK ({len(notes)} notes, 0 violations)")
    return 0

if __name__ == "__main__":
    pkg = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    sys.exit(check(pkg))
