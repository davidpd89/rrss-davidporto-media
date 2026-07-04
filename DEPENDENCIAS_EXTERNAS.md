# DEPENDENCIAS EXTERNAS

Este repo puede publicarse para revision, pero algunas fuentes maestras viven en el repo operativo local.

---

## Fuentes maestras locales

- `00_Contexto/START_HERE.md`
  - Ruta local: `C:\GIT\RRSS_DavidPorto\00_Contexto\START_HERE.md`
  - Uso: estado real, redes, reglas tecnicas y decisiones vivas.
  - Fallback publico: `nuevo_flujo/kb/contexto-activo.md`

- `06_Seguimiento/seguimiento_activo.md`
  - Ruta local: `C:\GIT\RRSS_DavidPorto\06_Seguimiento\seguimiento_activo.md`
  - Uso: metricas, aprendizajes y pendientes por pieza.
  - Fallback publico: no crear lotes listos; solo borradores.

- `06_Seguimiento/tracking_formatos_tecnicas_temas.md`
  - Ruta local: `C:\GIT\RRSS_DavidPorto\06_Seguimiento\tracking_formatos_tecnicas_temas.md`
  - Uso: anti-repeticion de temas, formatos, tecnicas y horarios.
  - Fallback publico: consultar `content_index.jsonl`; si esta vacio, no aprobar lote.

---

## Reglas si faltan

- No programar.
- No tocar Metricool.
- No marcar piezas como `lista_para_programar`.
- No crear lote final.
- Si se genera algo, dejarlo como `borrador` con bloqueantes claros.
