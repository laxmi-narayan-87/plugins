#!/usr/bin/env python3
"""Run Not Ai's deterministic genre-aware editorial gate."""
import argparse, json, sys
from pathlib import Path
from not_ai_core.gate import evaluate, render, POLICIES
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input_file",nargs="?")
    p.add_argument("--stdin",action="store_true")
    p.add_argument("--genre",default="linkedin",choices=sorted(POLICIES))
    p.add_argument("--json",action="store_true")
    p.add_argument("--ascii-punctuation",action="store_true")
    p.add_argument("--protect",action="append",default=[])
    p.add_argument("--explain",nargs="?",const=True,default=False)
    a=p.parse_args()
    if isinstance(a.explain,str):
        print(f"{a.explain}: Findings are review prompts, not authorship, truth, or quality verdicts.")
        return 0
    if a.stdin or not a.input_file: text=sys.stdin.read()
    else:
        f=Path(a.input_file)
        if not f.is_file(): print(f"Error: file not found: {f}",file=sys.stderr); return 2
        text=f.read_text(encoding="utf-8")
    r=evaluate(text,a.genre,a.protect,a.ascii_punctuation)
    print(render(r,a.json))
    return 0 if r.passed else 1
if __name__=="__main__": raise SystemExit(main())
