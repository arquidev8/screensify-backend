# Screensify Backend

Backend para la plataforma Screensify, una herramienta para desarrollo de aplicaciones móviles con enfoque MCP (Model-Controller-Presenter).

## Arquitectura

- **Framework**: FastAPI
- **Base de datos**: PostgreSQL
- **Autenticación**: JWT
- **Estructura**: Organizada por módulos siguiendo principios de Clean Architecture

## Estructura de Carpetas

```
screensify-backend/
├── app/
│   ├── api/routers/mcp.py  # Endpoint /mcp/execute
│   ├── services/mcp/
│   │   ├── __init__.py
│   │   ├── orchestrator.py # Lógica principal del endpoint /mcp/execute
│   │   ├── tools/          # Implementación de cada Tool interna
│   │   │   ├── __init__.py
│   │   │   ├── base_tool.py
│   │   │   ├── component_generator.py # Llama a LLM, devuelve code+JSON
│   │   │   └── code_exporter.py       # Genera zip Expo/CLI
│   │   └── context_builder.py # Ayuda a reunir contexto para las tools
│   ├── core/, crud/, models/, schemas/, db/ # (Similares a antes)
│   └── main.py
```

## Sprints Planificados

- **Sprint 0**: Fundación y Autenticación
- **Sprint 1**: Gestión Proyectos y Pantallas + Shell Editor
- **Sprint 2**: Estado Editor Visual y Renderizado Básico
- **Sprint 3**: Edición Visual - D&D y Propiedades
- **Sprint 4**: Editor de Código Integrado y Vista Previa Inicial
- **Sprint 5**: Framework MCP y 1ª Tool Interna (AI Component Gen)
- **Sprint 6**: Navegación Visual y Tool de Exportación Completa#   s c r e e n s i f y - b a c k e n d  
 