# SKILL: IMAGEN Y ASSETS

Usar esta skill cuando la tarea implique una imagen, portada, foto, captura, quote card, fondo, thumbnail, limpieza de fondo, seleccion de assets o indexacion visual.

Objetivo: convertir imagenes y assets en material reutilizable sin confundir "descripcion de imagen" con caption final.

---

## Fuentes que leer antes de decidir

1. `04_Assets/`
2. `08_Usados_foto/*/piezas/**/TRACKING.md`
3. `08_Usados_foto/gpt/protocolo.md`
4. `tools/quote_card_template/`
5. `rrss-davidporto-media/` si existe en el entorno
6. `assets_registry.csv` si existe

Si la pieza lleva libro, portada, autor, feria o prensa, priorizar asset real antes que imagen IA.

---

## Regla principal

Los generadores de caption desde imagen sirven para diagnosticar e indexar:

- que aparece en la imagen
- que tono visual tiene
- que riesgos de licencia o repeticion hay
- que uso podria tener

No sirven como caption final de David Porto. Todo caption final debe pasar por:

1. `nuevo_flujo/kb/voz-marca.md`
2. `nuevo_flujo/skills/caption-multired.md`
3. `nuevo_flujo/skills/auditoria-calidad.md`

---

## Decision de uso

Para cada imagen, clasificar:

- **asset principal**: puede sostener una pieza por si solo.
- **asset de apoyo**: sirve como fondo, textura, slide secundaria o b-roll.
- **asset tecnico**: logo, portada, mockup, plantilla, badge, elemento recortado.
- **descartar**: mala licencia, mala calidad, aspecto generico, repetido o incoherente con David.

No usar foto anonima tipo catalogo como primera solucion si existe una foto humana real, portada real o material propio.

---

## Lecciones locales ya detectadas

- Foto humana real + portada real puede funcionar mejor que flat lay generico.
- La composicion local con Pillow/plantilla puede ganar a una imagen IA si preserva portada, manos, luz y proporciones.
- Vigilar dedos, oclusiones, texto deformado, portadas inventadas y luces que no casan.
- Hacer match de luz, grano, contraste y perspectiva antes de considerar una imagen "lista".
- Para quote cards y thumbnails, preferir sistemas locales reproducibles antes que prompts visuales irrepetibles.

---

## Limpieza y edicion

Usar limpieza de fondo solo si aporta claridad:

- recortar portada/persona/producto
- crear thumbnail limpio
- aislar elemento para carrusel
- eliminar ruido de captura

No limpiar fondos si elimina contexto humano o vuelve la pieza demasiado plastica.

---

## Contrato ASSET_RECORD

Registrar o proponer este bloque cuando se incorpore un asset:

```yaml
ASSET_RECORD:
  id:
  path:
  tipo: principal|apoyo|tecnico|descartar
  fuente:
  licencia_uso:
  descripcion_visual:
  objetos_detectados:
  personas_detectadas:
  texto_visible:
  uso_recomendado:
  redes_formatos:
  piezas_usadas:
  riesgo_repeticion: bajo|medio|alto
  requiere_limpieza_fondo: si|no
  caption_sugerido_no_final:
  notas_qa:
```

Si no existe `assets_registry.csv`, dejar el `ASSET_RECORD` en la respuesta o en la pieza para migrarlo despues.

---

## QA visual minimo

Antes de dar por buena una imagen:

- portada o texto legible
- rostro/manos sin artefactos raros
- formato correcto para la red
- no parece stock generico si la pieza necesita presencia humana
- no repite asset usado cerca en calendario
- licencia/fuente documentada
- no inventa premios, resenas, logos ni datos
