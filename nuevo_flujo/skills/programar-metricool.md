# SKILL: PROGRAMAR EN METRICOOL

Usar solo cuando el contenido ya este aprobado/listo.

---

## FASE 0 - LEER DOCUMENTACION

Leer:

- `00_Contexto/START_HERE.md` seccion Metricool.
- `05_Integraciones/metricool-mcp.md`.

---

## FASE 1 - COMPROBAR CALENDARIO

Antes de crear nada:

1. Consultar `getScheduledPosts`.
2. Verificar hueco real.
3. Verificar que no hay dos posts de la misma red demasiado pegados salvo decision consciente.
4. Verificar si la red tiene regla especial.

---

## FASE 2 - CREAR/ACTUALIZAR

Recordatorios tecnicos vivos:

- `date` debe existir arriba y dentro de `info.publicationDate`.
- `info.descendants` debe existir como lista.
- Para carrusel Instagram, NO enviar `instagramData.type: "CAROUSEL"`.
- Para Pinterest, usar `boardId` real confirmado.
- Para YouTube, incluir `youtubeData.title`, `youtubeData.audience` y `youtubeData.type: "SHORT"`.
- Para GBP, red interna `gmb`.
- Tras error, consultar `getScheduledPosts` antes de reintentar.

---

## FASE 3 - VERIFICACION

Despues de crear o actualizar:

```text
Red:
Fecha/hora:
ID:
Estado:
AutoPublish:
Media:
```

Si algo queda en draft o con error, no cerrar.

---

## FASE 4 - REGISTRO

Actualizar:

- `06_Seguimiento/tracking_formatos_tecnicas_temas.md`
- `06_Seguimiento/seguimiento_activo.md`
- `nuevo_flujo/kb/estado-sesion.md`
