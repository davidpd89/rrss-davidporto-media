# SKILL: CREAR REEL

Usar para Reels, TikTok y YouTube Shorts.

---

## FASE 0 - DECIDIR TIPO DE REEL

Antes de elegir herramienta, invocar `video-router.md`.

| Tipo | Cuando usar |
|---|---|
| Texto + video real | Situacion lectora simple, humor, pregunta rapida. |
| Multi-escena IA | Transformacion visual, historia breve, concepto novedoso. |
| Ken Burns sobre imagen | Objeto/texto delicado, evitar deformacion de IA. |
| Voz/subtitulos | Cuando el guion necesita ritmo narrativo, no solo frase visual. |

---

## FASE 1 - GUION

Reglas:

1. Linea 1 = gancho. No contexto.
2. Texto nuevo cada ~2s.
3. Cada linea avanza: no cadenas de negaciones ni sinonimos.
4. Ultima linea no repite la primera.
5. Si el usuario puede entenderlo sin audio, mejor.

Plantilla:

```text
1. [gancho que funciona solo]
2. [situacion concreta]
3. [contradiccion/giro]
4. [detalle visual o emocional]
5. [pregunta/participacion/remate]
```

---

## FASE 2 - VISUAL

Antes de generar:

- buscar asset propio o referencia real;
- revisar ultimas 3-4 piezas para no repetir fondo;
- documentar fuente/licencia si es stock;
- decidir que planos NO debe animar IA por riesgo de deformar texto/cara/objeto.

---

## FASE 3 - MONTAJE

Usar los sistemas vigentes del repo:

- `04_Assets/sistema_reel_instagram.md`
- `tools/reel_template/`
- `09_Usados_video/meta/protocolo.md` si aplica Meta.
- `09_Usados_video/flow/` + scripts `tools/flow_*.py` si aplica Flow.
- `09_Usados_video/pixverse/` + scripts `tools/pv_*.py` si aplica PixVerse.

QA minimo:

- ratio 9:16 real;
- duracion de clips suficiente;
- texto legible;
- tildes/eñes/¿/¡ revisadas visualmente;
- watermark tapado o ausente;
- primer frame con gancho o imagen fuerte;
- audio no repetido si hay piezas vecinas.

Salida obligatoria:

```text
QA_RESULT:
  status: pass|fail
  proveedor:
  ratio_ok:
  texto_ok:
  tildes_ok:
  watermark_ok:
  continuidad_ok:
  fuente_documentada:
  bloqueantes:
  correcciones:
```

---

## FASE 4 - CAPTION

Pasar por `caption-multired.md`.

Regla: el caption no repite literalmente el texto del reel. Debe abrir otra puerta: pregunta, comentario, contexto breve o invitacion.
