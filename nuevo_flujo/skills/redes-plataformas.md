# SKILL: REDES Y PLATAFORMAS

Usar cuando una pieza se adapte a una o varias redes. Esta skill evita el copy-paste multired.

---

## MAPA RAPIDO

| Red | Objetivo | Formato fuerte | Cuidado |
|---|---|---|---|
| Instagram | Guardados, compartidos, retencion | Reels, carruseles, quote cards | Caption no repite texto visual |
| Facebook | Alcance sobrio y comunidad ligera | Foto, reel, texto corto | Evitar trigger words y venta dura |
| TikTok | Retencion y comentario rapido | Reel directo | Gancho en 1s, lenguaje menos literario |
| Threads | Respuestas | Texto conversacional | No sonar a caption reciclado |
| Bluesky | Comunidad/nicho | Opinion breve | Max 300 caracteres |
| Pinterest | Busqueda visual | Pin/carrusel reutilizado | Titulo SEO, descripcion, boardId real |
| LinkedIn | Cultura/proceso/oficio | Texto largo + foto | No vender como booktok |
| GBP | Presencia verificable | Update real | Baja frecuencia, nada generico |
| YouTube Shorts | Retencion + SEO | Shorts | Titulo exacto, no clickbait |
| X | Conversacion/manual | Texto breve | Max 2 hashtags, programacion nativa |

---

## SALIDA POR RED

Cada adaptacion debe declarar:

```yaml
platform_adaptation:
  red:
  senal_objetivo:
  formato:
  texto:
  hashtags_o_keywords:
  cambio_vs_origen:
  riesgo:
```

Si `cambio_vs_origen` es "ninguno", no esta adaptado.
