# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-04-09
### Agregado
- **Modelo de Empleado:** Creación del modelo `Empleado` que hereda de `AbstractUser` conservando la seguridad nativa de Django y extendiendo con campos personalizados: RUT (identificador único chileno), cargo y departamento.
- **Configuración de Usuario Personalizado:** Integración del modelo `Empleado` en Django mediante `AUTH_USER_MODEL = 'asistencia.Empleado'` en `settings.py`.
- **Integración de Aplicaciones:** Inclusión de la aplicación `asistencia.apps.AsistenciaConfig` y `rest_framework` en `INSTALLED_APPS`.
- **Vistas Base:** Scaffolding inicial de `views.py` para la aplicación de asistencia.

### Seguridad
- Se mantiene el uso de PostgreSQL como base de datos nativa, evitando el uso de SQLite en desarrollo local.

## [0.1.0] - 2026-04-09
### Agregado
- **Documentación:** Creación y estructuración profesional del archivo `README.md` detallando la arquitectura base, uso de PostgreSQL sobre SQLite, y pasos para configurar el entorno de desarrollo local.
- **Registro de Cambios:** Inclusión del archivo `CHANGELOG.md` para mantener un historial de versiones ordenado bajo la norma SemVer.
- **Ignorados de Git:** Creación del archivo `.gitignore` configurado para excluir entornos virtuales (`.venv/`, `env/`), archivos compilados de Python (`__pycache__/`, `*.pyc`), bases de datos locales y archivos temporales/propios como `PASOS.md`.
- **Entorno de Desarrollo:** Creación del entorno virtual de Python (`.venv`) en el directorio raíz.
- **Backend Core:** Scaffolding inicial del proyecto Django (`reloj_control`) con su respectivo `manage.py` y carpeta de configuración (`config/`).
- **Dependencias:** Archivo `requirements.txt` base para las librerías del proyecto.

### Seguridad
- Seizó mediante el `.gitignore` que archivos con información sensible, privada del desarrollador (`PASOS.md`), o generados automáticamente, no sean subidos al repositorio público.
