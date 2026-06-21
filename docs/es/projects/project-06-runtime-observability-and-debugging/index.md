[中文版本 →](../../../zh/projects/project-06-runtime-observability-and-debugging/)

> Lecciones relacionadas: [Lección 11. Haz observable el runtime del agente](./../../lectures/lecture-11-why-observability-belongs-inside-the-harness/) · [Lección 12. Handoff limpio al final de cada sesión](./../../lectures/lecture-12-why-every-session-must-leave-a-clean-state/)
> Archivos de plantilla: [templates/](https://amitabhakarmakar.github.io/harness-engineering/es/resources/templates)

# Proyecto 06. Construye un harness completo para agentes (capstone)

## Qué harás

Este es el proyecto final. Ensambla todo lo aprendido en los primeros cinco proyectos, ejecuta un benchmark completo y luego haz una pasada de limpieza para verificar que la calidad sea mantenible.

Usa un conjunto fijo de tareas multi-función que cubra una porción completa del producto: importación de documentos, indexación, Q&A con citas, observabilidad de runtime y estado de repositorio legible y reiniciable. Primero ejecuta con un baseline de harness débil, luego con tu harness más fuerte, después limpia y vuelve a ejecutar. Finalmente, realiza un experimento de ablación del harness: elimina un componente cada vez y observa cuáles importan realmente.

## Usa el proyecto incluido

Ruta en el repositorio: [`projects/project-06/`](https://github.com/amitabhakarmakar/harness-engineering/tree/main/projects/project-06)

| Directorio | Qué contiene | Qué comparar |
|------|------|------|
| [`starter/`](https://github.com/amitabhakarmakar/harness-engineering/tree/main/projects/project-06/starter) | Producto casi completo, pero con superficie de harness debilitada: [`AGENTS.md`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/starter/AGENTS.md) básico, sin `feature_list.json`, `session-handoff.md`, checklist de estado limpio ni scripts de benchmark/cleanup. | Observaciones manuales de la línea base con harness débil. |
| [`solution/`](https://github.com/amitabhakarmakar/harness-engineering/tree/main/projects/project-06/solution) | Harness completo: [`AGENTS.md`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/solution/AGENTS.md), [`CLAUDE.md`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/solution/CLAUDE.md), [`feature_list.json`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/solution/feature_list.json), [`init.sh`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/solution/init.sh), [`session-handoff.md`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/solution/session-handoff.md), [`clean-state-checklist.md`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/solution/clean-state-checklist.md), documentos de calidad/evaluación y scripts. | Ejecutar [`projects/project-06/solution/scripts/benchmark.sh`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/solution/scripts/benchmark.sh) y [`projects/project-06/solution/scripts/cleanup-scanner.sh`](https://github.com/amitabhakarmakar/harness-engineering/blob/main/projects/project-06/solution/scripts/cleanup-scanner.sh), y comparar la evidencia de calidad. |

## Herramientas

- Claude Code o Codex
- Git
- Node.js + Electron
- Plantilla de documento de calidad
- Rúbrica de evaluación
- Todos los componentes de harness acumulados en los primeros cinco proyectos

## Mecanismo de harness

Harness completo: todos los mecanismos + observabilidad + estudio de ablación
