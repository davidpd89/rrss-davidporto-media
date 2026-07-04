# REGISTRO DE HERRAMIENTAS Y RIESGOS

Este archivo orienta que tipo de herramienta mirar segun la tarea. No es una lista de dependencias instaladas.

Politica actual: priorizar gratuito, local, reproducible y auditable. No incorporar pagos, creditos, trials, MuAPI, Stripe, SaaS ni autoposting como base del sistema sin permiso explicito.

---

## Imagen y assets

Usar como referencia:

- Captioning de imagen: util para indexar assets y detectar contenido visual; no para caption final.
- Background removal: util para portadas, personas, thumbnails y quote cards.
- Editores de thumbnail: utiles si mantienen control sobre texto, portada y marca.

Regla: la imagen final debe pasar por `imagen-assets.md` y la copia final por `caption-multired.md`.

---

## Video vertical

Usar como referencia:

- `mcp-video`: pipelines programables de video.
- `reelstack`: base tecnica API-first.
- `short-video-maker`: faceless desde texto, valido solo para pruebas controladas.
- `OpenMontage`: montaje/cortes.
- `clip-factory`: referencia para long-form a clips con Whisper/FFmpeg; copiar patron de highlights, no tono.
- `videocut-cli`: referencia para comando `doctor`, checks FFmpeg y subcomandos.
- `tools/reel_template/`: primera opcion local cuando ya resuelve la pieza.

Regla: el proveedor se decide en `video-router.md`; no elegir Flow/PixVerse/Meta por costumbre. Si un preset local resuelve el caso, usar local.

---

## Subtitulos

Usar como referencia:

- SRT/ASS/pycaps/captions-cli: formatos y render reproducible.
- Herramientas one-word: solo cuando el ritmo lo justifique.
- `tools/reel_template/generar_ass_karaoke.py`: opcion local prioritaria para ASS/karaoke.

Regla: estilo sobrio por defecto; no usar subtitulos agresivos salvo decision explicita.

---

## Scheduling y publicacion

Benchmark:

- TryPost
- Postiz
- calendarios open-source

Produccion actual:

- Metricool y flujos oficiales documentados.

Regla: no sustituir Metricool sin decision explicita. No usar publicacion por navegador, scraping, anti-detection, MuAPI ni wrappers no oficiales de pago.

---

## Herramientas con cuidado

No usar en produccion sin auditoria previa:

- cualquier herramienta que pida pago/creditos/trial para el camino basico
- herramientas que prometen publicar en Instagram/TikTok via Puppeteer, Selenium o anti-detection
- agentes que automatizan likes, follows, DMs o comentarios
- UGC/AI actors si no hay consentimiento, licencia y encaje de marca
- generadores visuales que inventan portadas, premios, resenas o logos

---

## Criterio de adopcion

Antes de incorporar una herramienta:

```yaml
TOOL_DECISION:
  nombre:
  categoria:
  uso_propuesto:
  sustituye_a:
  datos_que_necesita:
  riesgo_cuenta:
  riesgo_legal:
  coste:
  control_creativo:
  reproducibilidad:
  decision: usar|probar|referencia|rechazar
  razon:
```
