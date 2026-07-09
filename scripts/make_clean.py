#!/usr/bin/env python3
"""
Produce a clean copy of the LaTeX sources with all revision markup removed.

From every .tex file it:
  1. deletes the delimited revision-highlighting preamble block,
  2. removes standalone \\revhl tokens,
  3. unwraps \\revised{...} -> ... (brace-matched, handles nesting).

Usage: python3 make_clean.py SRC_DIR DEST_DIR
The clean sources compile to an identical layout (color/markup do not affect
pagination) and contain no highlighting commands, suitable for submission.
"""
import os
import sys
import shutil
import re

BLOCK_START = "% >>> REVISION HIGHLIGHTING"
BLOCK_END = "% <<< REVISION HIGHLIGHTING <<<"


def strip_revised(text):
    out = []
    i = 0
    tag = r"\revised{"
    while i < len(text):
        j = text.find(tag, i)
        if j == -1:
            out.append(text[i:])
            break
        out.append(text[i:j])
        k = j + len(tag)
        depth = 1
        buf = []
        while k < len(text) and depth > 0:
            c = text[k]
            if c == "{":
                depth += 1
                buf.append(c)
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
                buf.append(c)
            else:
                buf.append(c)
            k += 1
        # recurse in case of nested \revised
        out.append(strip_revised("".join(buf)))
        i = k + 1
    return "".join(out)


def clean_text(text):
    # 1. remove the highlight preamble block
    lines = text.split("\n")
    kept, skipping = [], False
    for ln in lines:
        if ln.strip().startswith(BLOCK_START):
            skipping = True
            continue
        if skipping:
            if BLOCK_END in ln:
                skipping = False
            continue
        kept.append(ln)
    text = "\n".join(kept)
    # 2. remove standalone \revhl tokens
    text = re.sub(r"\\revhl\b\s*", "", text)
    # 3. unwrap \revised{...}
    text = strip_revised(text)
    return text


def main():
    src, dest = sys.argv[1], sys.argv[2]
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    for root, _, files in os.walk(dest):
        for fn in files:
            if fn.endswith(".tex"):
                p = os.path.join(root, fn)
                with open(p, encoding="utf-8") as f:
                    t = f.read()
                with open(p, "w", encoding="utf-8") as f:
                    f.write(clean_text(t))
    print(f"clean sources written to {dest}")


if __name__ == "__main__":
    main()
