# SKILL: POSTMORTEM SEMANAL

Usar una vez por semana o al cerrar un lote grande.

---

## FASE 1 - IMPORTAR DATOS

- Consultar Metricool.
- Leer `06_Seguimiento/seguimiento_activo.md`.
- Leer `06_Seguimiento/tracking_formatos_tecnicas_temas.md`.

Rangos minimos: 7 dias y 30 dias si hay datos.

---

## FASE 2 - TOP/BOTTOM

Separar por red y formato:

```yaml
top:
  - id:
    red:
    formato:
    metrica:
    patron:
bottom:
  - id:
    red:
    formato:
    metrica:
    fallo:
```

---

## FASE 3 - DECISION EDITORIAL

Cada postmortem debe producir decisiones:

- repetir;
- pausar;
- reciclar;
- test A/B;
- cambiar horario;
- cambiar proveedor;
- cambiar duracion;
- actualizar tema saturado.

---

## FASE 4 - ACTUALIZAR MEMORIA

Actualizar:

- `kb/patrones-ganadores-y-fallos.md`
- `kb/temas-saturados.md`
- `06_Seguimiento/seguimiento_activo.md`

No cerrar con resumen pasivo.

---

## SALIDA OBLIGATORIA

```yaml
POSTMORTEM_RESULT:
  rango_7d:
  rango_30d:
  top_por_red:
    - red:
      piezas:
      patron:
  bottom_por_red:
    - red:
      piezas:
      fallo:
  patrones_a_repetir:
  temas_a_pausar:
  piezas_a_reciclar:
  tests_ab_propuestos:
  cambios_de_horario:
  cambios_de_proveedor_video:
  archivos_actualizados:
  pendientes_siguiente_semana:
```

Regla: no cerrar si no produce al menos 3 decisiones accionables.
