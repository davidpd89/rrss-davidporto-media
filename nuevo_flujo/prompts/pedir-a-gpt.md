# PROMPT PARA PEDIR A GPT LO QUE FALTA

Copia este bloque cuando quieras alimentar el nuevo flujo con datos externos o analisis de publicaciones.

```text
Estoy construyendo un agente para crear contenido de redes de David Porto Diaz, escritor de fantasia juvenil y ficcion especulativa. No quiero ideas genericas: quiero datos estructurados para alimentar un flujo que aprende de metricas, piezas que funcionaron y fallos reales.

Necesito que hagas 7 entregables:

1. MIS MEJORES PUBLICACIONES
Si te paso URLs, capturas o metricas, crea una tabla con:
- red
- fecha
- formato
- texto visual
- caption
- metricas disponibles
- patron de gancho
- CTA
- por que funciono
- como repetir la estructura sin copiar el contenido

2. MIS PEORES PUBLICACIONES
Tabla igual, pero añade:
- que fallo
- si suena a IA generica
- que antipatron aparece
- como la reescribirias
- si merece reciclarse o descartarse

3. REFERENCIAS HUMANAS REALES
Busca ejemplos reales en español de autores, bookstagram/booktok, lectores comentando libros, reseñas o conversaciones publicas. No copies contenido largo. Extrae patrones:
- primera frase
- situacion concreta
- tension/contradiccion
- remate
- CTA o motivo para comentar
- que señal busca: guardar, compartir, responder, retener

4. BANCO DE HOOKS HUMANOS PARA DAVID PORTO
Crea 60 hooks divididos en:
- humor lector
- libros que duelen
- fantasia con criterio
- villanos/secundarios
- bloqueo lector
- proceso de escritor
- Samuel entre mundos / magia con coste / portales, sin sonar promocional
- preguntas participativas

Reglas:
- Nada de "no es solo..." ni "la magia nos enseña..." ni frases motivacionales genericas.
- Gancho primero, 1-2 segundos.
- Lenguaje de lector real, no de agencia.
- Cada hook debe venir con formato recomendado: reel, carrusel, quote card, Threads/Bluesky, TikTok o LinkedIn.
- Indica cuales son mas adecuados para comentario, guardado, compartido o retencion.

5. CONTENT_INDEX PARA NO REPETIR
Con las publicaciones que te pase, crea lineas compatibles con JSONL, una por pieza, con estos campos:
- id
- red
- fecha
- formato
- tema
- angulo
- hook
- texto_visual_resumen
- caption_resumen
- CTA
- asset_usado
- metrica_principal
- rendimiento: alto|medio|bajo|desconocido
- patron_reutilizable
- riesgo_repeticion
- reciclable: si|no

6. ASSETS_REGISTRY
Si te paso imagenes, carpetas, capturas o descripciones de assets, crea una tabla CSV con:
- id
- path_o_fuente
- tipo: principal|apoyo|tecnico|descartar
- licencia_uso
- descripcion_visual
- objetos_detectados
- personas_detectadas
- texto_visible
- uso_recomendado
- redes_formatos
- piezas_usadas
- riesgo_repeticion
- requiere_limpieza_fondo
- caption_sugerido_no_final
- notas_qa

Importante: el caption sugerido desde imagen NO es caption final. Solo sirve para indexar.

7. VIDEO LARGO, CLIPS Y SUBTITULOS
Si te paso video largo, transcripcion o timestamps, devuelve:
- 10 momentos candidatos con timestamp, frase hook, razon y riesgo
- 3 clips prioritarios en formato CLIP_PLAN
- tipo de subtitulo recomendado: texto_2s, karaoke_ass, srt, one_word o sin_subtitulos
- palabras clave a destacar
- caption base por red principal
- riesgos de contexto, corte injusto o texto ilegible
```
