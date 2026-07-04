# SKILL: CAPTION MULTIRED

Usar para adaptar una misma idea a Instagram, TikTok, Threads, Facebook, YouTube Shorts, Pinterest, LinkedIn, GBP o Bluesky.

---

## PRINCIPIO

La idea puede ser la misma. El caption no.

Antes de adaptar por red, pasar el texto por `texto-humano.md`. Si suena a agencia o a IA generica, reescribir antes de multiplicarlo.

Cada red optimiza una senal distinta:

- Instagram Reel: compartir/guardar, primera frase visible.
- Instagram carrusel: guardado y comentario.
- TikTok: completion, comentario rapido, lenguaje directo.
- Threads: respuestas.
- Bluesky: comunidad y opinion.
- Facebook: claridad sin trigger words.
- YouTube Shorts: titulo SEO y descripcion exacta.
- Pinterest: titulo/descripcion buscables.
- LinkedIn: aprendizaje/proceso.
- GBP: actualizacion real.

---

## SALIDA CANONICA

```yaml
captions:
  instagram:
    texto:
    hashtags:
    senal_objetivo:
  facebook:
    texto:
    senal_objetivo:
  tiktok:
    texto:
    hashtags:
    senal_objetivo:
  threads:
    texto:
    topic_tag:
    senal_objetivo:
  bluesky:
    texto:
    hashtags:
    senal_objetivo:
  youtube:
    title:
    description:
    hashtags:
  pinterest:
    title:
    description:
    boardId:
    url:
  linkedin:
    texto:
    hashtags:
  gbp:
    texto:
    cta_url:
```

Incluir solo redes necesarias.

---

## CHECKS

- No repetir texto visual.
- No usar "descubre", "adentrate", "no es solo", "una historia que" ni tono de contraportada.
- No usar la misma pregunta en todas las redes.
- No mas de 3-5 hashtags salvo regla local distinta.
- X maximo 2 hashtags si se usa.
- Threads maximo 1 topic tag.
- Bluesky maximo 300 caracteres.
- Pinterest con keyword y tablero.
- Facebook sin palabras de venta agresiva.
