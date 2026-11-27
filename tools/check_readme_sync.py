#!/usr/bin/env python3
"""Check the translated READMEs against the English one.

The translations drift: a row gets added to README.md, a status flips from
planned to completed, a specification is corrected — and the other four files
keep the old version until a reader notices. This checks the things that must
not differ between translations and deliberately ignores the things that must:

  * how many roadmap tables there are,
  * how many rows each of those tables has,
  * the status glyph (OK / in progress / planned) on each row,
  * the numbers in the hardware specification table,
  * the set of language-neutral GitHub links (repositories, profiles, assets).

Prose is never compared, so translators stay free to phrase things their own
way. Run it from the repository root:

    python tools/check_readme_sync.py

Exits 0 when the files agree, 1 when they do not.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

SOURCE = "README.md"
TRANSLATIONS = ["README_zh.md", "README_JP.md", "README_Fr.md", "README_es.md"]

STATUS_GLYPHS = "\u2705\U0001F6A7\u23F3"  # done / in progress / planned
STATUS_RE = re.compile(f"[{STATUS_GLYPHS}]")

# A measurement in the specification table: "767 mm", "1.5kg", "DC 24V", "< 0.2 mm".
# Decimal separators differ by locale (1.5 kg vs 1,5 kg), so they are normalised.
NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)?")

# GitHub repository, profile, and raw asset links are language-neutral and
# should stay aligned across all translations (unlike regional store links).
GITHUB_URL_RE = re.compile(
    r"https?://(?:raw\.)?github(?:usercontent)?\.com/[^\s)\"'>]+"
)


def read_lines(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read().splitlines()


def split_tables(lines):
    """Group consecutive pipe-table lines, keeping only tables with statuses."""
    tables, current = [], []
    for line in lines:
        if line.strip().startswith("|"):
            current.append(line)
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    return [t for t in tables if any(STATUS_RE.search(line) for line in t)]


def status_rows(table):
    """The status glyphs of each row, in order."""
    rows = []
    for line in table:
        if not STATUS_RE.search(line):
            continue
        rows.append("".join(STATUS_RE.findall(line)))
    return rows


def spec_numbers(lines):
    """Numbers from the hardware specification table, row by row.

    Identified by the row label mentioning a parameter the table always
    carries; matching on position instead would break the moment a translation
    reorders a row, which is allowed.
    """
    out = {}
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        label = cells[0]
        key = None
        for marker, name in (
            (r"Reach|臂展|リーチ|Portée|Alcance", "reach"),
            (r"Payload|负载|負荷|Charge utile|Carga", "payload"),
            (r"Weight|自重|Poids|Peso", "weight"),
            (r"Voltage|电压|電圧|Tension|Tensión", "voltage"),
            (r"Repeatability|重复定位|繰り返し|Répétabilité|Repetibilidad", "repeatability"),
        ):
            if re.search(marker, label, re.I):
                key = name
                break
        if key is None or key in out:
            continue
        values = []
        for cell in cells[1:3]:
            values.append([n.replace(",", ".") for n in NUMBER_RE.findall(cell)])
        out[key] = values
    return out


def github_links(lines):
    """Language-neutral GitHub URLs referenced in the document."""
    urls = set()
    for line in lines:
        for url in GITHUB_URL_RE.findall(line):
            urls.add(url.rstrip(".,;:"))
    return urls


def check(root):
    source_lines = read_lines(os.path.join(root, SOURCE))
    source_tables = split_tables(source_lines)
    source_specs = spec_numbers(source_lines)
    source_github = github_links(source_lines)
    problems = []

    for name in TRANSLATIONS:
        path = os.path.join(root, name)
        if not os.path.exists(path):
            problems.append(f"{name}: file is missing")
            continue
        lines = read_lines(path)
        tables = split_tables(lines)

        if len(tables) != len(source_tables):
            problems.append(
                f"{name}: has {len(tables)} roadmap tables, {SOURCE} has "
                f"{len(source_tables)}"
            )

        for index, (src, dst) in enumerate(zip(source_tables, tables), start=1):
            src_rows, dst_rows = status_rows(src), status_rows(dst)
            if len(src_rows) != len(dst_rows):
                problems.append(
                    f"{name}: roadmap table {index} has {len(dst_rows)} rows, "
                    f"{SOURCE} has {len(src_rows)} — a row was added or removed "
                    f"in one and not the other"
                )
                continue
            for row, (a, b) in enumerate(zip(src_rows, dst_rows), start=1):
                if a != b:
                    problems.append(
                        f"{name}: roadmap table {index} row {row} is marked "
                        f"{b!r}, {SOURCE} marks it {a!r}"
                    )

        specs = spec_numbers(lines)
        for key, expected in source_specs.items():
            if key not in specs:
                problems.append(f"{name}: specification table has no {key} row")
                continue
            if specs[key] != expected:
                problems.append(
                    f"{name}: specification {key} is {specs[key]}, "
                    f"{SOURCE} says {expected}"
                )

        dst_github = github_links(lines)
        for url in sorted(source_github - dst_github):
            problems.append(f"{name}: missing GitHub link from {SOURCE}: {url}")
        for url in sorted(dst_github - source_github):
            problems.append(f"{name}: extra GitHub link not in {SOURCE}: {url}")

    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="repository root (default: current directory)",
    )
    args = parser.parse_args()

    problems = check(args.root)
    if not problems:
        print(f"{len(TRANSLATIONS)} translations agree with {SOURCE}.")
        return 0

    print(f"{len(problems)} disagreement(s) with {SOURCE}:\n")
    for problem in problems:
        print(f"  {problem}")
    print(
        "\nUpdate the translation to match README.md, or update README.md if it "
        "is the one that is wrong."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
