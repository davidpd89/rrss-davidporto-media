# SKILL: VIDEO META AI

Usar para transformar imagenes o fotos en clips cortos, especialmente planos sencillos, gestos pequenos y pruebas rapidas.

---

## LEER ANTES

- `09_Usados_video/meta/protocolo.md`
- `09_Usados_video/meta/capacidades_meta.md`
- `00_Contexto/START_HERE.md` secciones Meta AI.

---

## CUANDO USAR

- Imagen base real que necesita movimiento sutil.
- Plano de persona de espaldas/perfil sin riesgo alto de identidad.
- Objeto/ambiente sin texto delicado.
- Pruebas rapidas de concepto.

## CUANDO NO USAR

- Texto/portada/logo que debe conservarse exacto.
- Cara frontal con dramatismo fuerte.
- Secuencia larga donde la continuidad dura sea imprescindible.
- Si el clip sale en ratio no valido y no hay plan de recorte.

---

## FALLOS TIPICOS YA CONOCIDOS

- Ratio original no valido para Instagram si se toma como pieza final.
- Deformacion de portadas, letras, manos o caras.
- Movimiento bonito pero plano, sin mensaje.
- Subida de imagen que falla en silencio.
- Continuidad debil entre clips si no se usa tecnica documentada.

---

## PROTOCOLO

1. Documentar imagen base y fuente.
2. Generar imagen/video como materia prima, nunca como pieza final.
3. Si hay varios beats, usar tecnica documentada de continuidad o aceptar que es montaje.
4. Recortar a 9:16 si hace falta.
5. Quemar texto propio localmente.
6. Guardar `SOURCE.json` o `TRACKING.md`.

---

## QA_RESULT ESPECIFICO

```yaml
QA_RESULT:
  provider: meta
  status: pass|fail
  source_json:
  ratio_original:
  ratio_final_9_16:
  texto_local:
  deformaciones:
  watermark:
  fuente_documentada:
  bloqueantes:
```
