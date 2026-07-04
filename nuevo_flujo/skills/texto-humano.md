# SKILL: TEXTO HUMANO ANTI-IA

Usar antes de aceptar hooks, captions, texto visual, guiones de reel, hilos o copies multired.

Objetivo: matar texto con olor a IA antes de que llegue a montaje. No optimizar para "viral"; optimizar para claridad, voz de David y lenguaje de lector real.

---

## Fuentes obligatorias

Leer al menos una antes de escribir:

1. `nuevo_flujo/kb/voz-marca.md`
2. `nuevo_flujo/kb/patrones-ganadores-y-fallos.md`
3. `12_Metodo_y_recursos_IA/01_laboratorio_humano/shortlist_alto_impacto_v1.md` si esta disponible
4. `content_index.jsonl` si existe

Si no hay fuente humana o real, el texto queda como `borrador`, no como listo.

---

## Prohibido por defecto

- "No es solo..."
- "La magia nos ensena..."
- "A veces..."
- "En un mundo donde..."
- "Descubre..."
- "Adentrate..."
- "Una historia que..."
- "Te hara sentir..."
- metaforas blandas de camino, peso, luz, sombra, distancia o viaje si no hay imagen concreta
- frases motivacionales genericas
- pregunta final tipo "te leo" repetida sin motivo
- tono de agencia, newsletter o contraportada

---

## Reescritura obligatoria

Para cada hook/caption crear 3 capas:

1. **Version cruda**: directa, casi como comentario de lector.
2. **Version David**: mantiene criterio literario y voz de autor.
3. **Version red**: ajustada a la red sin perder naturalidad.

Elegir la version que suene menos redactada.

---

## Checks de naturalidad

Antes de aprobar:

- se puede decir en voz alta sin verguenza
- contiene una situacion concreta o una friccion
- no parece consejo generico de marketing
- no podria valer igual para cualquier autor
- no explica demasiado
- no repite el texto visual
- no usa mas intensidad emocional de la que merece la pieza

---

## Usar score mecanico

Cuando haya varias opciones, ejecutar o simular:

```powershell
python tools/score_hook.py "texto a evaluar"
```

En este Windows:

```powershell
& "C:\Program Files\LibreOffice\program\python.exe" tools\score_hook.py "texto a evaluar"
```

Regla:

- `<60`: descartar.
- `60-79`: reescribir.
- `80+`: producir si pasa auditoria.

El score no decide solo. Sirve para detectar basura IA, cliche y metafora blanda.

---

## Salida minima

```yaml
HOOK_SCORE:
  hook:
  claridad_1s:
  especificidad_humana:
  friccion_o_contradiccion:
  voz_david:
  novedad_vs_index:
  penalizaciones:
  total:
  decision: producir|reescribir|descartar
  motivo:
```
