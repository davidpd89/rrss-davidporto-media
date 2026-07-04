# SKILL: PIPELINE DE CONTENIDO COMPLETO

Punto de entrada principal para crear una pieza o lote publicable.

---

## FASE 0 - ORIENTACION

1. Ejecutar PASO 0 de `nuevo_flujo/AGENTS.md`.
2. Definir objetivo: publicar, dejar en revision, crear borrador, adaptar, analizar o programar.
3. Definir redes destino y formato.
4. Revisar `tracking_formatos_tecnicas_temas.md` para evitar repeticion de tema/formato.
5. Revisar `seguimiento_activo.md` para aplicar metricas recientes.

Salida de fase:

```text
Objetivo:
Redes:
Formato:
Fuente humana/real:
Riesgo principal:
Skill secundaria:
```

---

## FASE 1 - MATERIAL BASE

Elegir al menos una fuente, en este orden:

1. Metricas propias o pieza propia que funciono.
2. Hook/patron de `01_laboratorio_humano`.
3. Referencia humana estructurada con `12_Metodo_y_recursos_IA/00_metodo/reverse_engineering_json.md`.
4. Contenido real de David: premio, feria, web, libro, proceso, foto propia.
5. Backlog/ideas ya investigadas: `07_fuentes_externas/ideas y hashtags/`, `01_Estrategia/banco_ideas_creativas.md`, `03_Publicaciones/Banco de ideas.md`.
6. Stock/API solo como soporte visual, no como idea principal.

Prohibido: "idea generica de fantasia/libros" sin ancla.

Si se usa una referencia humana externa, invocar `buscar-patrones-humanos.md` antes de producir.

---

## FASE 2 - CONCEPTO

Crear un brief de pieza:

```yaml
id_propuesto:
objetivo:
redes:
formato:
idea_unica:
gancho_1:
fuente_real:
visual:
texto_en_pantalla:
caption_base:
cta:
hashtags_o_keywords:
riesgos:
```

Reglas:

- `gancho_1` debe poder parar scroll sin contexto.
- `idea_unica` no puede contener dos tesis.
- Si hay video, el texto debe avanzar cada ~2s.
- Si hay carrusel, cada slide debe aportar informacion nueva.

---

## FASE 3 - PRODUCCION POR FORMATO

Derivar a la skill correspondiente:

- Reel -> `crear-reel.md`
- Carrusel -> `crear-carrusel.md`
- Caption multired -> `caption-multired.md`
- Lote -> `crear-lote.md`

---

## FASE 4 - AUDITORIA

Invocar `auditoria-calidad.md`.

No entregar a David ni programar si falla algun P0:

- gancho inicial debil;
- texto con faltas;
- visual generico/repetido;
- ratio incorrecto;
- fuente/licencia ausente;
- caption repite texto visual;
- red mal adaptada;
- posible dato inventado.

Salida obligatoria de esta fase:

```yaml
QA_RESULT:
  status: pass|fail
  fecha:
  pieza_id:
  p0_bloqueantes:
  p1_correcciones:
  texto_ok:
  visual_ok:
  fuente_ok:
  red_ok:
  repeticion_ok:
  metricool_ok:
  correcciones_aplicadas:
```

Si `QA_RESULT.status` no es `pass`, el estado maximo permitido es `revision_david`.

---

## FASE 5 - ENTREGA

Entregar usando el contrato `PIEZA` de `nuevo_flujo/kb/contratos-salida.md`:

```yaml
PIEZA:
  id:
  estado: borrador|revision_david|lista_para_programar|programada
  objetivo:
  red_principal:
  redes_secundarias:
  formato:
  tema:
  categoria_70_20_10: interes|autor_proceso|libro_cta
  fuente_real:
  asset_origen:
  texto_visual:
  caption_base:
  captions_por_red:
  hashtags_keywords:
  archivos:
  riesgos:
```

Si el formato es video/reel, anadir tambien:

```yaml
video_provider_decision:
  proveedor:
  motivo:
  proveedores_descartados:
  skill_siguiente:
  riesgos:
  creditos_o_limites:
  que_no_animar:
  plan_b:

provider_QA_RESULT:
  provider:
  status: pass|fail
  bloqueantes:
```

Reglas de estado:

- Si falta `QA_RESULT: pass`, maximo `revision_david`.
- Si falta `fuente_real` o `asset_origen`, maximo `borrador`.
- Si es video y falta `video_provider_decision`, maximo `borrador`.
- Si es video y falta `provider_QA_RESULT: pass`, maximo `revision_david`.

---

## FASE 6 - CIERRE

1. Si se programa: usar `programar-metricool.md`.
2. Actualizar tracking y seguimiento.
3. Escribir `SESSION_UPDATE`.
