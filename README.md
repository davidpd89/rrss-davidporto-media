# RRSS David Porto Media + Flujo

Repositorio publico para alojar media de redes de David Porto y exponer el flujo operativo de contenido a GPT/Codex.

## Contenido

- `images/` y `videos/`: media publicada o preparada.
- `nuevo_flujo/`: agente de produccion, correccion y auditoria de contenido.
- `tools/`: scripts gratuitos/locales para validar hooks, contratos, lotes y salud del flujo.
- `content_index.jsonl`: indice de piezas. Ahora existe sin datos inventados; hay que alimentarlo con publicaciones reales.
- `assets_registry.csv`: registro de assets. Ahora contiene cabecera; hay que alimentarlo con assets reales.
- `DEPENDENCIAS_EXTERNAS.md`: rutas maestras que pueden vivir fuera de este repo.
- `NO_PUBLICAR.md`: frenos de calidad para texto, visual y montaje.

## Punto de entrada

Leer primero:

```text
nuevo_flujo/AGENTS.md
```

Antes de producir o auditar un lote:

```bash
python tools/rrss_healthcheck.py
```

Si faltan las fuentes maestras externas, no programar ni marcar piezas como listas.
