# SKILL: MONTAJE ESTABLE

Usar cuando una pieza implique render, montaje, video local, Ken Burns, quote card animada, subtitulos o plantilla visual.

Objetivo: que el mismo brief produzca el mismo tipo de pieza. El montaje no debe reinventarse en cada sesion.

---

## Regla principal

Primero elegir preset. Despues renderizar.

No cambiar simultaneamente:

- fuente visual
- timing
- tipografia
- posicion de texto
- musica
- transicion
- color grade
- proveedor

Si se cambia mas de una variable, registrar prueba A/B o mantener la pieza en `borrador`.

---

## Presets gratuitos/locales prioritarios

1. `reel_texto_2s_local`
   - Herramientas: `tools/reel_template/render_reel_v6_paced.py`, `render_text_pngs.py`
   - Uso: reels con texto cada 2s y fondo/banco visual.

2. `karaoke_ass_local`
   - Herramienta: `tools/reel_template/generar_ass_karaoke.py`
   - Uso: voz o ritmo alto con subtitulo sincronizado.

3. `quote_card_static_local`
   - Herramienta: `tools/quote_card_template/render_quote.py`
   - Uso: frases, reseñas, citas o piezas estaticas.

4. `ken_burns_asset_real`
   - Uso: portada, foto o imagen real que no debe deformarse con IA.

No usar herramienta de pago si hay preset local suficiente.

---

## Contrato MONTAGE_PRESET

```yaml
MONTAGE_PRESET:
  pieza_id:
  preset:
  script_o_template:
  formato:
  duracion_objetivo:
  fps:
  resolucion:
  safe_area:
  fuente_visual:
  fuente_audio:
  subtitulos:
  color_grade:
  transiciones:
  variables_bloqueadas:
  variable_en_prueba:
  export_path:
  reproducible: si|no
  notas:
```

---

## QA de estabilidad

Antes de entregar:

- mismo preset que piezas equivalentes salvo motivo escrito
- texto no salta de posicion entre escenas
- duracion por pantalla consistente
- safe area respetada
- audio no cambia sin razon
- color/contraste no cambia de una pieza a otra por accidente
- ruta de script/template documentada
- salida reproducible con los mismos parametros
