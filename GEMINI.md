# Reglas del Proyecto y Flujo de Trabajo (Git Flow & Versionado)

Este archivo contiene las directrices obligatorias que el asistente de IA (Gemini CLI) debe seguir al trabajar en este proyecto.

## 1. Flujo de Trabajo de Git (Git Flow)
*   **Convención de Commits:** Utilizar siempre [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/). Ejemplos: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`.
*   **Commits Atómicos:** Realizar commits pequeños y con un único propósito.
*   **Idioma de los Commits:** Los mensajes de commit pueden estar en inglés (preferido para el prefijo) y el cuerpo en español, o todo en español, pero manteniendo consistencia (ej. `feat: agrega modelo de asistencia`).

## 2. Gestión de Versiones y Changelog (Obligatorio)
Cada vez que se complete una nueva funcionalidad, corrección de errores importante o cambio en la arquitectura, se debe seguir este flujo ESTRICTO antes de hacer commit:

1.  **Determinar el incremento de versión (SemVer):**
    *   **Mayor (X.0.0):** Cambios que rompen la compatibilidad.
    *   **Menor (0.X.0):** Nuevas funcionalidades retrocompatibles.
    *   **Parche (0.0.X):** Correcciones de errores (bugfixes) retrocompatibles.
2.  **Actualizar `CHANGELOG.md`:**
    *   Agregar una nueva sección con la versión, fecha y descripción detallada de los cambios usando el formato [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).
    *   Categorizar los cambios: `### Agregado`, `### Cambiado`, `### Obsoleto`, `### Eliminado`, `### Arreglado`, `### Seguridad`.
3.  **Actualizar `README.md` (si aplica):** Reflejar la nueva versión si hay un indicador visible o actualizar documentación de uso.
4.  **Crear un Commit de Release:**
    *   El commit que engloba estos cambios debe referenciar explícitamente la versión.
    *   Formato: `chore(release): bump version to v[NUEVA_VERSION] - [Breve descripción]` (Ej. `chore(release): bump version to v0.2.0 - agrega módulo de usuarios`).

## 3. Arquitectura y Código
*   **Base de Datos:** El proyecto utiliza PostgreSQL de forma nativa. **Bajo ninguna circunstancia** se debe sugerir o configurar SQLite para el desarrollo local.
*   **Idioma:** Comentarios en el código, docstrings y documentación general deben estar en español. El código (variables, clases, funciones) preferiblemente en inglés o un *spanglish* claro y consistente según el dominio del problema.
*   **Validación:** Todo código nuevo o modificado debe ser validado estructural y lógicamente antes de darse por terminado.
