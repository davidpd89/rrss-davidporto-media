from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


def load_index(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    rows: list[dict] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            rows.append({"_error": f"invalid json line {line_no}", "raw": line})
    return rows


def field_values(text: str, field: str) -> list[str]:
    pattern = re.compile(rf"^\s*{re.escape(field)}\s*:\s*(.+?)\s*$", re.MULTILINE)
    return [m.group(1).strip().strip("'\"") for m in pattern.finditer(text) if m.group(1).strip()]


def repeated(values: list[str]) -> dict[str, int]:
    return {k: v for k, v in Counter(values).items() if v > 1 and k.lower() not in {"null", "none", "[]"}}


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a RRSS batch/lote")
    parser.add_argument("lote", help="markdown/yaml/json file with proposed batch")
    parser.add_argument("--index", default="content_index.jsonl")
    parser.add_argument("--assets", default="assets_registry.csv")
    args = parser.parse_args()

    lote_path = Path(args.lote)
    text = lote_path.read_text(encoding="utf-8", errors="replace")
    index = load_index(Path(args.index))
    warnings: list[str] = []
    blockers: list[str] = []

    if not index:
        warnings.append("content_index missing or empty; 7d/30d repetition cannot be trusted")
    if not Path(args.assets).exists() or Path(args.assets).stat().st_size == 0:
        warnings.append("assets_registry missing or empty; asset repetition cannot be trusted")

    temas = field_values(text, "tema")
    formatos = field_values(text, "formato")
    ctas = field_values(text, "cta")
    captions = field_values(text, "caption_base") + field_values(text, "caption")
    hooks = field_values(text, "gancho_1") + field_values(text, "hook")

    repeated_topics = repeated(temas)
    repeated_formats = repeated(formatos)
    repeated_ctas = repeated(ctas)
    if repeated_topics:
        warnings.append(f"repeated topics: {repeated_topics}")
    if len(formatos) >= 4 and repeated_formats:
        warnings.append(f"repeated formats: {repeated_formats}")
    if repeated_ctas:
        blockers.append(f"repeated CTA: {repeated_ctas}")
    if any("QA_RESULT:" in block and "status: pass" not in block for block in text.split("PIEZA:")[1:]):
        blockers.append("piece with QA_RESULT not pass")
    if any(cliche in text.lower() for cliche in ["no es solo", "descubre", "adentrate", "una historia que"]):
        blockers.append("AI/copywriting cliche detected")
    if "reel" in text.lower() and "MONTAGE_PRESET:" not in text:
        blockers.append("reel/video without MONTAGE_PRESET")

    status = "fail" if blockers else "pass"
    print("LOTE_AUDIT_RESULT:")
    print(f"  status: {status}")
    print(f"  rango_fechas: null")
    print(f"  piezas_revisadas: {text.count('PIEZA:')}")
    print(f"  equilibrio_70_20_10: {dict(Counter(field_values(text, 'categoria_70_20_10')))}")
    print(f"  repeticion_tema: {repeated_topics}")
    print(f"  repeticion_formato: {repeated_formats}")
    print("  repeticion_visual: {}")
    print(f"  repeticion_cta: {repeated_ctas}")
    print(f"  captions_similares: {len(captions) != len(set(captions))}")
    print(f"  saturacion_detectada: {warnings}")
    print("  metricool_ok: null")
    print(f"  bloqueantes: {blockers}")
    print(f"  avisos: {warnings}")
    print("  correcciones_requeridas: []")
    print(f"  hooks_revisados: {len(hooks)}")
    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
