# SKILL: RECICLAR PIEZA

Usar para convertir una pieza que funciono en otro formato o red sin parecer copia.

---

## ENTRADA

```yaml
pieza_origen:
  id:
  red:
  formato:
  metrica_que_justifica:
  hook:
  tema:
  que_funciono:
  que_no_repetir:
red_destino:
formato_destino:
```

---

## TRANSFORMACIONES VALIDAS

- Reel ganador -> carrusel de criterio.
- Reel ganador -> Threads/Bluesky como pregunta conversacional.
- Carrusel -> reel con una sola tension.
- Threads/Bluesky -> reel si la respuesta/comentario revela patron humano.
- TikTok -> YouTube Shorts con titulo SEO.
- Foto real -> LinkedIn si hay aprendizaje/proceso.

---

## REGLAS

1. Conservar patron, no texto literal.
2. Cambiar gancho.
3. Cambiar CTA.
4. Cambiar visual si vuelve a publicarse en una red visual.
5. Declarar por que merece reciclarse.
6. Leer `kb/temas-saturados.md`.
7. Leer `content_index.jsonl` cuando exista.

---

## BLOQUE ANTI-CALCO

```yaml
anti_calco:
  conserva:
  cambia:
  frase_prohibida:
  visual_prohibido:
  cta_prohibida:
  estructura_demasiado_parecida:
```

Si `red_destino` es visual, `nuevo_visual` debe ser distinto. No basta con otra version del mismo fondo.

Si `riesgo_saturacion` es alto, estado maximo = `idea`, no `listo_para_qa`.

---

## SALIDA

```yaml
reciclaje:
  conserva:
  cambia:
  anti_calco:
  nuevo_gancho:
  nuevo_formato:
  nuevo_visual:
  caption:
  riesgo_saturacion:
  listo_para_qa:
```
