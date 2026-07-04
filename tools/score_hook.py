from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


AI_CLICHES = [
    "no es solo",
    "descubre",
    "adentrate",
    "una historia que",
    "te hara sentir",
    "en un mundo donde",
    "la magia nos",
    "a veces",
    "el poder de",
    "un viaje",
]

SOFT_METAPHORS = [
    "camino",
    "luz",
    "sombra",
    "distancia",
    "peso",
    "viaje",
    "destino",
    "alma",
]

HUMAN_MARKERS = [
    "cuando",
    "si ",
    "ayer",
    "hoy",
    "me ",
    "te ",
    "leer",
    "libro",
    "personaje",
    "capitulo",
    "villano",
    "final",
    "llorar",
    "guardar",
]

FRICTION_MARKERS = [
    "pero",
    "aunque",
    "nadie",
    "nunca",
    "demasiado",
    "problema",
    "culpa",
    "trampa",
    "miedo",
    "peor",
]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def clamp(value: int) -> int:
    return max(0, min(20, value))


def novelty_score(text: str, index_path: Path | None) -> tuple[int, list[str]]:
    if not index_path or not index_path.exists() or index_path.stat().st_size == 0:
        return 12, ["no content_index available; novelty is estimated"]
    needle = normalize(text)
    words = {w for w in re.findall(r"\w+", needle) if len(w) > 3}
    if not words:
        return 8, ["too few meaningful words"]
    max_overlap = 0.0
    for line in index_path.read_text(encoding="utf-8", errors="replace").splitlines():
        hay = normalize(line)
        hay_words = {w for w in re.findall(r"\w+", hay) if len(w) > 3}
        if not hay_words:
            continue
        overlap = len(words & hay_words) / max(1, len(words))
        max_overlap = max(max_overlap, overlap)
    if max_overlap >= 0.7:
        return 3, [f"high overlap with content_index ({max_overlap:.0%})"]
    if max_overlap >= 0.45:
        return 10, [f"medium overlap with content_index ({max_overlap:.0%})"]
    return 18, []


def score(text: str, index_path: Path | None = None) -> dict:
    raw = text.strip()
    low = normalize(raw)
    words = re.findall(r"\w+", low)
    penalties: list[str] = []

    clarity = 20
    if len(raw) > 95:
        clarity -= 8
        penalties.append("too long for 1s hook")
    if len(words) > 14:
        clarity -= 5
        penalties.append("too many words")
    if not raw or raw[-1] not in ".?!":
        clarity -= 2

    specificity = 8 + min(12, sum(1 for m in HUMAN_MARKERS if m in low) * 3)
    if re.search(r"\b(algo|cosas|gente|mundo|vida)\b", low):
        specificity -= 4
        penalties.append("generic nouns")

    friction = 6 + min(14, sum(1 for m in FRICTION_MARKERS if m in low) * 4)
    if "?" in raw:
        friction += 3

    voice = 16
    found_cliches = [c for c in AI_CLICHES if c in low]
    if found_cliches:
        voice -= min(14, len(found_cliches) * 5)
        penalties.append("AI/copywriting cliche: " + ", ".join(found_cliches))
    found_metaphors = [m for m in SOFT_METAPHORS if re.search(rf"\b{re.escape(m)}\b", low)]
    if found_metaphors:
        voice -= min(8, len(found_metaphors) * 2)
        penalties.append("soft metaphor risk: " + ", ".join(found_metaphors))

    novelty, novelty_notes = novelty_score(raw, index_path)
    penalties.extend(novelty_notes)

    parts = {
        "claridad_1s": clamp(clarity),
        "especificidad_humana": clamp(specificity),
        "friccion_o_contradiccion": clamp(friction),
        "voz_david": clamp(voice),
        "novedad_vs_index": clamp(novelty),
    }
    total = sum(parts.values())
    if total < 60:
        decision = "descartar"
    elif total < 80:
        decision = "reescribir"
    else:
        decision = "producir"
    return {
        "HOOK_SCORE": {
            "hook": raw,
            **parts,
            "penalizaciones": penalties,
            "total": total,
            "decision": decision,
            "motivo": " / ".join(penalties) if penalties else "hook clear enough for review",
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a David Porto social hook")
    parser.add_argument("hook", nargs="+", help="hook text")
    parser.add_argument("--index", default="content_index.jsonl", help="content index JSONL")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = score(" ".join(args.hook), Path(args.index))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        data = result["HOOK_SCORE"]
        print("HOOK_SCORE:")
        for key, value in data.items():
            print(f"  {key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
