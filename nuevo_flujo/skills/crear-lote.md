# SKILL: CREAR LOTE

Usar cuando se pidan varias publicaciones o relleno de calendario.

---

## ENTRADAS OBLIGATORIAS

- Rango de fechas.
- Redes objetivo.
- Cadencia esperada por red.
- Restricciones de David si las hay.

Si faltan, inferir desde `START_HERE.md` y verificar con Metricool antes de programar.

---

## FASE 1 - AUDITORIA DEL CALENDARIO

1. Consultar `getScheduledPosts` mediante `tools/metricool_client.py`.
2. Contar por red y dia.
3. Detectar huecos reales.
4. Detectar saturacion de formato: demasiados videos, demasiadas quote cards, etc.
5. Detectar repeticion de horas.

Salida:

```text
Huecos:
Saturacion:
Horas repetidas:
Redes con regla especial:
```

---

## FASE 2 - MATRIZ DE VARIEDAD

Cada lote debe variar:

- tema;
- formato;
- visual/fondo;
- redaccion del CTA;
- franja horaria;
- red destino;
- fuente de material.

No aceptar un lote donde 4+ piezas compartan la misma estructura narrativa o visual.

---

## FASE 3 - SELECCION DE PIEZAS

Orden de preferencia:

1. Reutilizar/adapter contenido ya producido pero no usado en esa red/dia.
2. Convertir una pieza ganadora a otra red con caption distinto.
3. Crear pieza nueva desde hook humano o contenido real.
4. Usar IA generativa solo si aporta visual/concepto nuevo.

---

## FASE 4 - CONTROL ANTI-REPETICION

Antes de cerrar, responder:

- Que tema se repite y por que se justifica?
- Que formato domina y como se compensa?
- Hay dos captions con la misma plantilla?
- Alguna hora copia patron viejo 11:00/12:30/19:30 sin motivo?
- Algun fondo/clip se parece a una pieza reciente?

Si alguna respuesta es dudosa, variar el lote.
