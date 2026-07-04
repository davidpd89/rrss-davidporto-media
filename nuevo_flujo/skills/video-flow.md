# SKILL: VIDEO FLOW / VEO

Usar cuando la pieza necesita continuidad narrativa, clips extensibles o escenas encadenadas con mas control que Meta/PixVerse.

---

## LEER ANTES

- `00_Contexto/START_HERE.md` secciones Flow/Veo.
- `09_Usados_video/flow/` y `TRACKING.md` de piezas similares.
- Scripts disponibles: `tools/flow_*.py`, `tools/generate_flow_video.py`, `tools/check_flow_credits.py`.

---

## CUANDO USAR

- Transformaciones por etapas.
- Mundos/escenas que cambian.
- Mini-historia de 2-5 beats.
- Extensiones donde la continuidad importa.
- Videos con ritmo mas cinematografico.

## CUANDO NO USAR

- Una sola frase sobre fondo bonito.
- Objeto con texto importante que debe permanecer exacto.
- Si no hay creditos suficientes para completar la secuencia.
- Si el concepto cabe en quote card/carrusel.

---

## FALLOS TIPICOS YA CONOCIDOS

- Continuidad falsa si se usa un ultimo fotograma como simple referencia y no como extension real.
- "Ampliar" puede reemplazar el clip anterior: descargar antes de ampliar.
- Coste de creditos mayor del previsto por extender o audio.
- Secuencia visualmente bonita pero sin mensaje legible.
- Duracion real distinta a la asumida por el montaje.

---

## PROTOCOLO

1. Comprobar creditos reales.
2. Escribir `script.json` o brief con beats.
3. Definir que clip se descarga antes de ampliar.
4. Descargar cada clip inmediatamente antes de cualquier extension que pueda reemplazarlo.
5. Guardar clips, ultimo frame si aplica, prompts y `TRACKING.md`.
6. Montar localmente con texto propio y marca.
7. Auditar continuidad y duracion.

---

## QA_RESULT ESPECIFICO

```yaml
QA_RESULT:
  provider: flow
  status: pass|fail
  creditos_comprobados:
  clips_descargados_antes_de_extender:
  continuidad_entre_beats:
  duracion_real:
  texto_cada_2s:
  audio:
  watermark:
  ratio_9_16:
  fuente_documentada:
  bloqueantes:
```
