# ESTADO DE SESION

Este archivo acumula cierres de sesion del agente. No borrar entradas antiguas salvo que se migren a `00_Contexto/START_HERE.md` o `06_Seguimiento/`.

---

## Pendientes explicitos

- Consolidar el flujo en el uso real de las proximas sesiones y mover a `START_HERE.md` cualquier regla que demuestre ser critica.
- Pedir a David/GPT una lista de 20-50 publicaciones propias con mejor rendimiento, con URL/ID, red, fecha, formato, texto visual, caption y metricas.
- Pedir a David/GPT competidores o referencias humanas reales que quiera imitar estructuralmente, no copiar.

---

[SESSION_UPDATE]
Fecha: 2026-07-04
Tarea: creacion del agente nuevo_flujo para RRSS
Fuentes leidas: `00_Contexto/START_HERE.md`, `06_Seguimiento/tracking_formatos_tecnicas_temas.md`, `06_Seguimiento/seguimiento_activo.md`, `12_Metodo_y_recursos_IA/README.md`, `manual escritura/novela fantasia/nuevo_flujo`
Piezas tocadas: ninguna
Decisiones nuevas: se crea arquitectura con PASO 0, skills por tarea, KB compacta, auditoria adversarial y contrato de cierre
Fallos evitados/detectados: crear desde cero, repetir templates, no revisar metricas antes de producir, no dejar memoria
Pendiente siguiente sesion: alimentar `kb/patrones-ganadores-y-fallos.md` con metricas reales detalladas de las mejores y peores publicaciones
[/SESSION_UPDATE]

[SESSION_UPDATE]
Fecha: 2026-07-04
Tarea: especializacion del flujo por proveedor/red y primer healthcheck
Fuentes leidas: feedback GPT adjunto, `nuevo_flujo/AGENTS.md`, `skills/crear-reel.md`, carpetas `09_Usados_video/flow`, `09_Usados_video/meta`, `09_Usados_video/pixverse`
Piezas tocadas: ninguna
Decisiones nuevas: se anaden skills para `video-router`, `video-flow`, `video-pixverse`, `video-meta`, `redes-plataformas`, `reciclar-pieza` y `postmortem-semanal`; se anaden contratos `QA_RESULT` y temas saturados; se crea `tools/rrss_healthcheck.py`
Fallos evitados/detectados: evitar que todo video pase por una skill generica; detectar memoria falsa antes de producir; healthcheck PASS con avisos por falta de `content_index.jsonl` y `assets_registry.csv`
Pendiente siguiente sesion: crear `content_index.jsonl` y `assets_registry.csv`, despues `audit_lote.py`
[/SESSION_UPDATE]

[SESSION_UPDATE]
Fecha: 2026-07-04
Tarea: conectar fuentes locales existentes y endurecer contratos
Fuentes leidas: feedback GPT adjunto, `12_Metodo_y_recursos_IA/00_metodo/pipeline_referencia_real_a_contenido.md`, `reverse_engineering_json.md`, `shortlist_alto_impacto_v1.md`, `07_factory/operacion_semanal.md`, listados de `TRACKING.md`
Piezas tocadas: ninguna
Decisiones nuevas: `pipeline-contenido.md` usa contratos `PIEZA`/`QA_RESULT`; `video-router.md` exige scoring y proveedores descartados; las skills de video incluyen fallos tipicos; `reciclar-pieza.md` tiene anti-calco; `postmortem-semanal.md` exige `POSTMORTEM_RESULT`; se crea `buscar-patrones-humanos.md` y `kb/fuentes-locales-utiles.md`
Fallos evitados/detectados: habia una fabrica semanal y schemas de reverse engineering ya creados pero no conectados al agente; ahora son fuentes prioritarias antes de inventar
Pendiente siguiente sesion: materializar datos estructurados (`content_index.jsonl`, `assets_registry.csv`) y luego auditor mecanico de lote
[/SESSION_UPDATE]

[SESSION_UPDATE]
Fecha: 2026-07-04
Tarea: especializacion por imagen, subtitulos y clipping
Fuentes leidas: feedback GPT adjunto sobre imagen/video/subtitulos/scheduling, `08_Usados_foto/gpt/protocolo.md`, `08_Usados_foto/perplexity/piezas/01-samuel-bookstagram/TRACKING.md`, `tools/reel_template`, `tools/quote_card_template`
Piezas tocadas: ninguna
Decisiones nuevas: se anaden skills `imagen-assets.md`, `subtitulos-captions.md` y `video-clipping-largo.md`; se crea `kb/tool-registry.md`; se anaden contratos `ASSET_RECORD`, `SUBTITLE_PLAN` y `CLIP_PLAN`; el healthcheck comprueba estas rutas
Fallos evitados/detectados: evitar captions finales sacados de captioning visual, subtitulos demasiado agresivos por defecto, tratar clips de video largo como reels inventados desde cero y adoptar herramientas de publicacion con scraping/anti-detection
Pendiente siguiente sesion: crear `assets_registry.csv` y `content_index.jsonl` con datos reales para que el agente pueda detectar repeticion y reutilizar ganadores
[/SESSION_UPDATE]
