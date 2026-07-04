# SKILL: VIDEO PIXVERSE

Usar para movimiento dramatico, multi-toma, escenas fantasticas con energia visual o variaciones rapidas cuando PixVerse tenga creditos disponibles.

---

## LEER ANTES

- `00_Contexto/START_HERE.md` secciones PixVerse.
- `09_Usados_video/pixverse/piezas/*/TRACKING.md` similares.
- Scripts disponibles: `tools/pv_*.py`, `tools/pixverse_*.py` si existen.

---

## CUANDO USAR

- Escenas con energia: duelo, transformacion, resaca visual, gestos fuertes.
- Multi-toma.
- Cuando el resultado necesita impacto rapido mas que continuidad perfecta.

## CUANDO NO USAR

- Si aparece el modal/upsell y no se puede cerrar.
- Si los creditos no alcanzan.
- Si hay texto legible en el plano.
- Si el objetivo es continuidad milimetrica entre clips.

---

## FALLOS TIPICOS YA CONOCIDOS

- Manos/caras raras cuando el movimiento es demasiado agresivo.
- Miniatura prometedora pero video flojo: revisar el clip completo.
- Movimiento fuerte que tapa la lectura del texto.
- Prompt demasiado fantastico que produce ruido visual.
- Creditos/modal impiden crear aunque parezca que el boton funciona.

---

## PROTOCOLO

1. Comprobar saldo real y cerrar modal si aparece.
2. Definir duracion y coste antes de generar.
3. Evitar prompts con texto escrito dentro del video.
4. Descargar variaciones y elegir por movimiento, no solo por miniatura.
5. Montar localmente con texto propio, logo/vignette si hace falta.
6. Revisar que no haya artefactos raros en manos/caras/texto.

---

## QA_RESULT ESPECIFICO

```yaml
QA_RESULT:
  provider: pixverse
  status: pass|fail
  creditos_comprobados:
  modal_cerrado:
  duracion_real:
  multi_toma:
  artefactos:
  texto_generado_por_ia: false
  texto_local_ok:
  ratio_9_16:
  bloqueantes:
```
