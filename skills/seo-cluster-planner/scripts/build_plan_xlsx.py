"""Build the three-tab XLSX content plan from a JSON plan.

Usage:
    python build_plan_xlsx.py plan.json /path/to/output.xlsx

The JSON plan must match the shape documented in SKILL.md. This script
validates the plan shape, enforces quality rules (unique primary keywords,
every cluster has a pillar and at least 3 support pages), and writes the
XLSX. On validation failure it exits non-zero with a readable error so the
calling agent knows to fix the plan and retry.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
except ImportError:
    print(
        "ERROR: openpyxl is required. Install with: "
        "pip install openpyxl --break-system-packages",
        file=sys.stderr,
    )
    sys.exit(2)


VALID_INTENTS = {"informational", "investigational", "transactional", "navigational"}

HEADER_FILL = PatternFill(start_color="1F2937", end_color="1F2937", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF")
PILLAR_FILL = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")


def validate(plan: dict[str, Any]) -> list[str]:
    """Return a list of validation errors. Empty list = valid plan."""
    errors: list[str] = []

    if "clusters" not in plan or not isinstance(plan["clusters"], list):
        errors.append("plan.clusters must be a list")
        return errors

    if not plan["clusters"]:
        errors.append("plan.clusters is empty — nothing to write")
        return errors

    seen_primary: dict[str, str] = {}  # primary_keyword -> location

    for i, cluster in enumerate(plan["clusters"]):
        loc = f"clusters[{i}]"
        name = cluster.get("cluster_name", "").strip()
        if not name:
            errors.append(f"{loc}.cluster_name is missing or empty")

        pillar = cluster.get("pillar")
        if not isinstance(pillar, dict):
            errors.append(f"{loc}.pillar is missing or not an object")
        else:
            pk = pillar.get("primary_keyword", "").strip().lower()
            if not pk:
                errors.append(f"{loc}.pillar.primary_keyword is empty")
            else:
                if pk in seen_primary:
                    errors.append(
                        f"{loc}.pillar.primary_keyword '{pk}' duplicates {seen_primary[pk]}"
                    )
                seen_primary[pk] = f"{loc}.pillar"
            intent = pillar.get("intent", "").strip().lower()
            if intent and intent not in VALID_INTENTS:
                errors.append(
                    f"{loc}.pillar.intent '{intent}' not in {sorted(VALID_INTENTS)}"
                )

        support = cluster.get("support_pages", [])
        if not isinstance(support, list):
            errors.append(f"{loc}.support_pages must be a list")
            support = []
        if len(support) < 3:
            errors.append(
                f"{loc} has only {len(support)} support page(s) — minimum is 3. "
                f"Consider merging this cluster into an adjacent one."
            )
        for j, sp in enumerate(support):
            sloc = f"{loc}.support_pages[{j}]"
            pk = sp.get("primary_keyword", "").strip().lower()
            if not pk:
                errors.append(f"{sloc}.primary_keyword is empty")
            else:
                if pk in seen_primary:
                    errors.append(
                        f"{sloc}.primary_keyword '{pk}' duplicates {seen_primary[pk]}"
                    )
                seen_primary[pk] = sloc
            intent = sp.get("intent", "").strip().lower()
            if intent and intent not in VALID_INTENTS:
                errors.append(
                    f"{sloc}.intent '{intent}' not in {sorted(VALID_INTENTS)}"
                )

        long_tails = cluster.get("long_tails", [])
        if not isinstance(long_tails, list):
            errors.append(f"{loc}.long_tails must be a list")

    return errors


def _style_header(ws, num_cols: int) -> None:
    for col in range(1, num_cols + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 22
    ws.freeze_panes = "A2"


def _autosize(ws, min_w: int = 12, max_w: int = 60) -> None:
    for col_idx, col_cells in enumerate(ws.columns, start=1):
        longest = 0
        for cell in col_cells:
            v = cell.value
            if v is None:
                continue
            longest = max(longest, len(str(v)))
        width = min(max(longest + 2, min_w), max_w)
        ws.column_dimensions[get_column_letter(col_idx)].width = width


def _write_pillars(ws, plan: dict[str, Any]) -> None:
    headers = [
        "cluster_name",
        "primary_keyword",
        "proposed_title",
        "intent",
        "volume",
        "difficulty",
        "support_page_count",
        "notes",
    ]
    ws.append(headers)
    for cluster in plan["clusters"]:
        p = cluster.get("pillar", {})
        ws.append(
            [
                cluster.get("cluster_name", ""),
                p.get("primary_keyword", ""),
                p.get("proposed_title", ""),
                p.get("intent", ""),
                p.get("volume", ""),
                p.get("difficulty", ""),
                len(cluster.get("support_pages", [])),
                p.get("notes", ""),
            ]
        )
    _style_header(ws, len(headers))
    # Color-tint pillar rows so they're visually distinct from Support tab
    for row in range(2, ws.max_row + 1):
        for col in range(1, len(headers) + 1):
            ws.cell(row=row, column=col).fill = PILLAR_FILL
    _autosize(ws)


def _write_support(ws, plan: dict[str, Any]) -> None:
    headers = [
        "parent_cluster",
        "primary_keyword",
        "proposed_title",
        "intent",
        "volume",
        "difficulty",
        "notes",
    ]
    ws.append(headers)
    for cluster in plan["clusters"]:
        for sp in cluster.get("support_pages", []):
            ws.append(
                [
                    cluster.get("cluster_name", ""),
                    sp.get("primary_keyword", ""),
                    sp.get("proposed_title", ""),
                    sp.get("intent", ""),
                    sp.get("volume", ""),
                    sp.get("difficulty", ""),
                    sp.get("notes", ""),
                ]
            )
    _style_header(ws, len(headers))
    _autosize(ws)


def _write_long_tails(ws, plan: dict[str, Any]) -> None:
    headers = ["keyword", "parent_seed", "parent_cluster", "intent_guess"]
    ws.append(headers)
    for cluster in plan["clusters"]:
        for lt in cluster.get("long_tails", []):
            ws.append(
                [
                    lt.get("keyword", ""),
                    lt.get("parent_seed", ""),
                    cluster.get("cluster_name", ""),
                    lt.get("intent_guess", ""),
                ]
            )
    _style_header(ws, len(headers))
    _autosize(ws)


def _write_meta(ws, plan: dict[str, Any]) -> None:
    ws.append(["Field", "Value"])
    ws.append(["ICP context", plan.get("icp_context", "")])
    ws.append(["Generated at", plan.get("generated_at", "")])
    ws.append(["Cluster count", len(plan.get("clusters", []))])
    pillars = len(plan.get("clusters", []))
    support = sum(len(c.get("support_pages", [])) for c in plan.get("clusters", []))
    long_tails = sum(len(c.get("long_tails", [])) for c in plan.get("clusters", []))
    ws.append(["Pillar pages", pillars])
    ws.append(["Support pages", support])
    ws.append(["Long-tail keywords", long_tails])
    dropped = plan.get("dropped_seeds", [])
    if dropped:
        ws.append([])
        ws.append(["Dropped seeds (debrief)"])
        for d in dropped:
            if isinstance(d, dict):
                ws.append([d.get("seed", ""), d.get("reason", "")])
            else:
                ws.append([str(d)])
    _style_header(ws, 2)
    _autosize(ws)


def build(plan: dict[str, Any], output_path: Path) -> None:
    errors = validate(plan)
    if errors:
        msg = "Plan failed validation:\n  - " + "\n  - ".join(errors)
        raise ValueError(msg)

    wb = Workbook()
    # Default sheet becomes Pillars
    pillars_ws = wb.active
    pillars_ws.title = "Pillars"
    _write_pillars(pillars_ws, plan)

    support_ws = wb.create_sheet("Support")
    _write_support(support_ws, plan)

    lt_ws = wb.create_sheet("Long-tails")
    _write_long_tails(lt_ws, plan)

    meta_ws = wb.create_sheet("Meta")
    _write_meta(meta_ws, plan)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(output_path)


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "Usage: python build_plan_xlsx.py <plan.json> <output.xlsx>",
            file=sys.stderr,
        )
        return 2

    plan_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    try:
        with plan_path.open() as f:
            plan = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR reading plan JSON: {e}", file=sys.stderr)
        return 2

    try:
        build(plan, output_path)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    # Brief summary to stdout for the calling agent
    clusters = plan.get("clusters", [])
    print(
        f"OK: wrote {output_path} — "
        f"{len(clusters)} clusters, "
        f"{sum(len(c.get('support_pages', [])) for c in clusters)} support pages, "
        f"{sum(len(c.get('long_tails', [])) for c in clusters)} long-tails."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
