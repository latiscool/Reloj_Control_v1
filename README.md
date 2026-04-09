# Reloj Control (Backend Django)

## Descripción
Sistema de control de asistencia (Reloj Control) construido con Django y Django REST Framework, utilizando PostgreSQL como base de datos principal. Diseñado con una arquitectura orientada a producción desde el inicio, preparado para ser desplegado mediante Dokploy en un VPS.

## Tecnologías Principales
* **Framework:** Django & Django REST Framework
* **Lenguaje:** Python 3
* **Base de Datos:** PostgreSQL (adaptador `psycopg2-binary`)
* **Despliegue planeado:** Dokploy / VPS

## Requisitos Previos (Desarrollo Local)
* Python 3.10 o superior.
* PostgreSQL instalado y en ejecución en tu máquina.
* Git.

## Configuración del Entorno de Desarrollo

> **Nota Arquitectónica:** El estándar de este proyecto dicta que el entorno de desarrollo local debe imitar lo mejor posible al entorno de producción. Por ello, se descarta SQLite desde el primer momento y se fuerza el uso de PostgreSQL localmente. Esto evitará problemas de "Data Type Mismatch" o "en mi máquina sí funciona" al momento de subir a Dokploy.

### 1. Clonar el repositorio
```bash
git clone https://github.com/latiscool/Reloj_Control_v1.git
cd RelojControl-DJANGO
```

### 2. Crear y activar el entorno virtual exclusivo
```bash
python -m venv .venv

# En Windows:
.venv\Scripts\activate

# En Linux/Mac:
# source .venv/bin/activate
```

### 3. Instalar dependencias core
Asegúrate de tener tu entorno virtual activado antes de ejecutar:
```bash
pip install -r requirements.txt
```

### 4. Configuración de Base de Datos Local
1. Accede a tu PostgreSQL local (pgAdmin o psql) y crea una base de datos para el proyecto (ej. `reloj_control_db`).
2. Configura las variables de entorno en tu archivo `.env` para que Django pueda conectarse (Próximamente se agregará un `.env.example`).

### 5. Migraciones y ejecución del servidor
Levanta el scaffolding y aplica las migraciones a tu base de datos local:
```bash
cd reloj_control
python manage.py migrate
python manage.py runserver
```

## Versionado
Este proyecto sigue [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Todo el registro de cambios detallado se encuentra en el archivo [CHANGELOG.md](./CHANGELOG.md).

---
*Desarrollado por Luis Torres Gomez.*
