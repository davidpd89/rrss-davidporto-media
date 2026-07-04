# SKILL: VIDEO LARGO A SHORTS

Usar esta skill cuando haya que convertir una entrevista, presentacion, directo, lectura, charla, evento o video horizontal/largo en reels, shorts o clips verticales.

Objetivo: no tratar un clip derivado como si fuera un reel inventado desde cero. Primero encontrar el momento humano, despues adaptar formato.

---

## Entradas necesarias

- Ruta o enlace del video largo.
- Objetivo de la pieza.
- Red principal.
- Timestamps si existen.
- Transcripcion si existe.
- Persona/tema/libro/evento implicado.
- Restricciones: duracion, tono, CTA, fecha de publicacion.

Si faltan timestamps o transcripcion, proponer un primer pase de deteccion de momentos antes de escribir captions.

---

## Flujo

1. Localizar 3-10 momentos candidatos.
2. Elegir momentos con una tension concreta: pregunta, frase rara, revelacion, contradiccion, imagen potente o cierre emocional.
3. Definir hook visual y verbal para los primeros 1-2 segundos.
4. Decidir encuadre: 9:16, reframing, cortes, b-roll, portada o texto.
5. Pasar subtitulos por `nuevo_flujo/skills/subtitulos-captions.md`.
6. Adaptar caption por `nuevo_flujo/skills/caption-multired.md`.
7. Auditar con `nuevo_flujo/skills/auditoria-calidad.md`.
8. Registrar resultado y aprendizaje.

---

## Reglas de seleccion

Preferir:

- frases con especificidad de autor/lector/libro
- momentos donde David suene humano y no promocional
- ideas que se entienden sin todo el contexto
- cortes que no dependan de una explicacion larga

Evitar:

- intros largas
- saludos de directo
- frases demasiado internas
- cortes que parecen sacados de contexto de forma injusta
- clips donde el caption tenga que explicar todo el sentido

---

## Contrato CLIP_PLAN

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

## Herramientas a evaluar

Para clipping automatizado o semiautomatizado, evaluar herramientas solo como apoyo. No delegar el juicio editorial.

- `mcp-video`: referencia para pipelines de video programables.
- `reelstack`: referencia API-first para reels/subtitulos/render.
- `short-video-maker`: util para faceless, menos control creativo.
- `OpenMontage`: referencia para montaje y cortes.

Evitar soluciones que publiquen o interactuen con redes mediante scraping, anti-detection o navegador no oficial.
