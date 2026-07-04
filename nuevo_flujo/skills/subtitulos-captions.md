# SKILL: SUBTITULOS Y CAPTIONS DE VIDEO

Usar esta skill cuando la tarea implique subtitulos, texto quemado, karaoke, SRT/ASS, captions sincronizados, transcripcion o legibilidad de un reel/short.

Objetivo: que el texto en pantalla ayude a retener sin convertir el contenido de David en una pieza chillona o generica.

---

## Fuentes y herramientas locales

Leer segun el caso:

- `04_Assets/sistema_reel_instagram.md`
- `tools/reel_template/generar_ass_karaoke.py`
- `tools/reel_template/render_text_pngs.py`
- `tools/reel_template/render_reel_v6_paced.py`
- `09_Usados_video/*/piezas/**/TRACKING.md`

---

## Estilo por defecto

- Subtitulos discretos, claros y editoriales.
- No usar estilo MrBeast/Hormozi amarillo gigante salvo que David lo pida para una pieza concreta.
- Frases cortas; una idea por pantalla.
- Si hay voz, no tapar boca, manos, portada ni elemento narrativo.
- Si no hay voz, el texto debe poder leerse sin pausar.
- Revisar tildes, signos, saltos de linea y viudas visuales.

---

## Eleccion de modo

- `texto_2s`: reel visual sin voz; frases breves por escena.
- `karaoke_ass`: voz clara y ritmo alto; destacar palabras clave sin saturar.
- `srt`: version interoperable o pieza que ira a edicion externa.
- `one_word`: solo si el ritmo lo exige; no usar por defecto.
- `sin_subtitulos`: si el visual y caption hacen el trabajo y el texto estorba.

---

## Contrato SUBTITLE_PLAN

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

## QA de subtitulos

Antes de entregar:

- se entiende en silencio
- se entiende con audio
- no duplica exactamente el caption
- no tapa el elemento principal
- no usa demasiadas palabras por segundo
- no rompe la voz de marca
- export o ruta propuesta es reproducible
