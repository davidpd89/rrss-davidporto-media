# CONTRATOS DE SALIDA

Este archivo define bloques que el agente debe producir. Sirve para que "revisado" signifique algo verificable.

---

## PIEZA

```yaml
PIEZA:
  id:
  estado: idea|borrador|revision_david|lista_para_programar|programada
  objetivo:
  red_principal:
  redes_secundarias:
  formato:
  tema:
  categoria_70_20_10: interes|autor_proceso|libro_cta
  fuente_real:
  asset_origen:
  texto_visual:
  caption_base:
  captions_por_red:
  hashtags_keywords:
  archivos:
  riesgos:
```

---

## QA_RESULT

```yaml
QA_RESULT:
  status: pass|fail
  fecha:
  pieza_id:
  p0_bloqueantes:
  p1_correcciones:
  texto_ok:
  visual_ok:
  fuente_ok:
  red_ok:
  repeticion_ok:
  metricool_ok:
  correcciones_aplicadas:
```

---

## HOOK_SCORE

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

---

## CONTENT_RECORD

```yaml
CONTENT_RECORD:
  id:
  fecha_creacion:
  fecha_publicacion:
  red:
  formato:
  estado:
  categoria_70_20_10: interes|autor_proceso|libro_cta
  tema:
  hook:
  texto_visual:
  caption:
  cta:
  asset_ids:
  fuente_real:
  proveedor_video:
  montaje_preset:
  url_publicada:
  metricas:
  diagnostico:
  repetir:
  evitar:
```

---

## LOTE_AUDIT_RESULT

```yaml
LOTE_AUDIT_RESULT:
  status: pass|fail
  rango_fechas:
  piezas_revisadas:
  equilibrio_70_20_10:
  repeticion_tema:
  repeticion_formato:
  repeticion_visual:
  repeticion_cta:
  captions_similares:
  saturacion_detectada:
  metricool_ok:
  bloqueantes:
  avisos:
  correcciones_requeridas:
```

---

## POSTMORTEM_RESULT

```yaml
POSTMORTEM_RESULT:
  rango_7d:
  rango_30d:
  top_por_red:
  bottom_por_red:
  patrones_a_repetir:
  temas_a_pausar:
  piezas_a_reciclar:
  tests_ab:
  cambios_horario:
  cambios_proveedor:
  archivos_actualizados:
```

---

## ASSET_RECORD

```yaml
ASSET_RECORD:
  id:
  path:
  tipo: principal|apoyo|tecnico|descartar
  fuente:
  licencia_uso:
  descripcion_visual:
  objetos_detectados:
  personas_detectadas:
  texto_visible:
  uso_recomendado:
  redes_formatos:
  piezas_usadas:
  riesgo_repeticion: bajo|medio|alto
  requiere_limpieza_fondo: si|no
  caption_sugerido_no_final:
  notas_qa:
```

---

## SUBTITLE_PLAN

```yaml
SUBTITLE_PLAN:
  pieza_id:
  modo: texto_2s|karaoke_ass|srt|one_word|sin_subtitulos
  fuente_audio:
  texto_base:
  timing:
  estilo:
  safe_area:
  palabras_destacadas:
  export:
  riesgos_legibilidad:
  qa:
```

---

## CLIP_PLAN

```yaml
CLIP_PLAN:
  pieza_id:
  video_origen:
  red_principal:
  objetivo:
  momentos_candidatos:
    - timestamp_inicio:
      timestamp_fin:
      frase_hook:
      razon:
      riesgo:
  clip_elegido:
  formato_visual:
  subtitulos:
  caption_base:
  assets_apoyo:
  qa:
  pendiente_edicion:
```

---

## MONTAGE_PRESET

```yaml
MONTAGE_PRESET:
  pieza_id:
  preset:
  script_o_template:
  formato:
  duracion_objetivo:
  fps:
  resolucion:
  safe_area:
  fuente_visual:
  fuente_audio:
  subtitulos:
  color_grade:
  transiciones:
  variables_bloqueadas:
  variable_en_prueba:
  export_path:
  reproducible: si|no
  notas:
```

---

## TOOL_DECISION

Ver `nuevo_flujo/kb/tool-registry.md`.

---

## SESSION_UPDATE

Usar el contrato de `nuevo_flujo/AGENTS.md`.
