# SKILL: CREAR CARRUSEL

Usar para carruseles de Instagram/Facebook/Pinterest adaptado.

---

## FASE 0 - LEER SISTEMA VIGENTE

Leer `04_Assets/sistema_carrusel_instagram.md`.

No usar `generate-design` de Canva como salida final.

---

## FASE 1 - ESTRUCTURA

Un carrusel debe tener:

1. Portada con promesa clara.
2. Slides intermedias que avanzan, no decoran.
3. Cierre con pregunta o accion concreta.

Plantillas utiles:

- "3 señales de..."
- "Elige una..."
- "Mapa de..."
- "Antes/despues..."
- "Lo que parece / lo que es..."
- "Ranking subjetivo..."

---

## FASE 2 - SLIDES

Para cada slide:

```yaml
slide:
  rol: portada|punto|giro|cierre
  texto_principal:
  texto_secundario:
  visual:
  razon_para_guardar:
```

Si una slide no tiene razon para existir, eliminarla.

---

## FASE 3 - QA

- Texto grande legible en movil.
- Nada importante cerca de bordes/cortes.
- Imagen y texto se entienden en 1 segundo.
- No hay lorem/errores/tildes faltantes.
- Export en dimensiones exactas.
- Caption complementa, no repite.
