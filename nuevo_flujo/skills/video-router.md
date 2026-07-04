# SKILL: VIDEO ROUTER

Usar antes de crear cualquier reel/video con IA. Decide proveedor y evita usar la herramienta comoda por defecto.

---

## MATRIZ DE DECISION

| Necesidad | Proveedor recomendado | Skill |
|---|---|---|
| Continuidad narrativa, clips extensibles, cambios de escena controlados | Flow/Veo | `video-flow.md` |
| Movimiento dramatico, multi-toma, energia visual, escenas fantasticas potentes | PixVerse | `video-pixverse.md` |
| Transformar imagen/foto en video corto, pruebas rapidas, planos sencillos | Meta AI | `video-meta.md` |
| Texto/objeto delicado que no debe deformarse | Ken Burns local | `crear-reel.md` + `tools/reel_template/` |
| Clips realistas sin IA generativa | Banco video/API | `04_Assets/sistema_reel_instagram.md` |

---

## SCORING COMPARATIVO

Puntuar de 1 a 5 cada proveedor antes de decidir. 5 = mejor para esa dimension.

```yaml
provider_score:
  flow:
    control_continuidad:
    impacto_visual:
    riesgo_deformacion:
    coste_creditos:
    velocidad_produccion:
    adecuacion_david_porto:
  pixverse:
    control_continuidad:
    impacto_visual:
    riesgo_deformacion:
    coste_creditos:
    velocidad_produccion:
    adecuacion_david_porto:
  meta:
    control_continuidad:
    impacto_visual:
    riesgo_deformacion:
    coste_creditos:
    velocidad_produccion:
    adecuacion_david_porto:
  ken_burns_local:
    control_continuidad:
    impacto_visual:
    riesgo_deformacion:
    coste_creditos:
    velocidad_produccion:
    adecuacion_david_porto:
  banco_video_api:
    control_continuidad:
    impacto_visual:
    riesgo_deformacion:
    coste_creditos:
    velocidad_produccion:
    adecuacion_david_porto:
```

Interpretacion:

- `riesgo_deformacion`: 5 significa poco riesgo.
- `coste_creditos`: 5 significa barato o gratis.
- Si hay texto/portada/logo/manuscrito legible, proveedor por defecto = `ken_burns_local` salvo justificacion explicita.

---

## PREGUNTAS OBLIGATORIAS

1. Hay persona real reconocible? Si si, evitar cambios dramaticos de identidad.
2. Hay texto, portada, logo, reloj, marcapaginas o manuscrito legible? Si si, no animarlo con IA.
3. Necesita continuidad entre escenas? Si si, priorizar Flow/Ampliar o tecnica documentada.
4. Hay creditos suficientes hoy? Comprobar antes.
5. El proveedor elegido ya fallo en este tipo de tarea?
6. La pieza puede resolverse mejor con montaje local que con mas generacion?

---

## SALIDA

```yaml
video_provider_decision:
  proveedor:
  motivo:
  provider_score:
  proveedores_descartados:
    - proveedor:
      motivo:
  skill_siguiente:
  riesgos:
  creditos_o_limites:
  que_no_animar:
  plan_b:
```

Si no hay al menos dos proveedores descartados con motivo, la decision no esta suficientemente pensada.
