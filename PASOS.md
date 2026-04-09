# **ETAPA 0: Crearndo la carpeta del Proyecto
```	
mkdir  reloj_control
cd   reloj_contro
```	

# **ETAPA 1: Crear el Entorno Virtual en Python para trabajar con Django
### instalando  paquete para enotrno virtual
```
pip install virtualenvwrapper-win 
```
###  Creando entorno virtual
```
mkvirtualenv reloj_control
```
#### Entrar el entorno

```
workon reloj_control
```

### Problema al entrar entorno"
Permiso de Ejecucion
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
### Persiste el problema forzar ingresar al entorno

```
& "$env:USERPROFILE\Envs\reloj_control\Scripts\Activate.ps1"
```
### Salir del entorno
```
deactivate
```

### Instalando dependencias
```
cd reloj_control
pip install django djangorestframework psycopg2-binary
```
### Tomar Snapshot de libs
```
 pip freeze > requirements.txt
 ```

-----------------------------------------------------------------------------------
### **A. Instalación de Dependencias Core (Paso 2)**
Instalaremos el motor de nuestro backend, el adaptador de base de datos y la extensión para crear la API.

**¿Qué hace cada paquete en nuestra arquitectura?**
* `django`: El framework web principal. Construye la lógica, el ORM y la seguridad.
* `djangorestframework` : La herramienta que transforma los modelos de Django en respuestas JSON (Endpoints) para que React los pueda leer.
* `psycopg2-binary` : Es el conector que permite a Python hablar con PostgreSQL. **Advertencia:** Usar solo `psycopg2` en Windows suele arrojar errores de compilación de C++. La versión `-binary` ya viene precompilada y evitara errores locales.
* `django-crispy-forms` y `crispy-bootstrap5` *(Opcionales aquí)*: Mejoran visualmente los formularios de Django. Las dejaremos instaladas por si quieres que tu panel de administración o tu interfaz auto-generada de la API se vean elegantes.

**Código en terminal:**
`\\$ pip install django djangorestframework psycopg2-binary`

-----------------------------------------------------------------------------------

###**B. Congelamiento de Dependencias (Paso 2.1 - Preparando CI/CD)**
Nunca dejes para el final el registro de tus librerías. Dokploy y GitLab CI/CD necesitan un "manifiesto" exacto de lo que instalaste.

**¿Cómo le decimos al servidor de producción qué debe instalar?**
Utilizamos el comando `freeze` de pip para capturar las versiones exactas y volcarlas en un archivo de texto.

**Código en terminal:**
`\\$ pip freeze > requirements.txt`



###**C. Inicialización del Proyecto Base (Paso 3)**
Con las herramientas instaladas, ahora levantaremos el "esqueleto" maestro del proyecto.

**¿Por qué usar un nombre genérico y un punto al final?**
La mayoría de los tutoriales Junior hacen `django-admin startproject reloj_control`. Esto crea una carpeta `reloj_control` dentro de otra carpeta `reloj_control`, lo cual hace que las rutas de importación y el despliegue en Docker/Dokploy sean un infierno. Nombraremos al núcleo del proyecto `core` (o `backend`) y usaremos un punto (`.`) para decirle a Django que lo instale en la carpeta actual.

**Código en terminal:**
`\\$ django-admin startproject core .`

####***El estándar Mid-Level separa la "Configuración" de la "Lógica". Al llamar a nuestro proyecto maestro `core`, dejamos claro que ahí residen las configuraciones (settings.py, urls.py base), mientras que la lógica de negocio vivirá en una App separada que crearemos después llamada `asistencia`.***

###**A. El Rol de Crispy Forms en una Arquitectura REST**
Es una excelente herramienta, pero debemos separar cómo funciona Django tradicional versus una API moderna.

**¿Por qué Crispy Forms no nos sirve para el Front-End de este proyecto?**
* **El enfoque Tradicional (Monolito):** Normalmente, Django procesa los datos y los envía a un archivo `.html` mezclado con variables (Templates). Aquí es donde `crispy-forms` y Bootstrap brillan, porque Django "dibuja" la interfaz.
* **Nuestro enfoque (API REST + React):** En nuestro Roadmap (Proyecto 1 y 2), Django **no dibujará pantallas**. Nuestro backend será ciego. Solo tomará datos de PostgreSQL y los escupirá como texto puro (JSON). Por ejemplo: `{"empleado": "Luis", "hora": "08:00"}`. 
* La "grilla bonita" de la que hablas la construiremos 100% en **ReactJS** (Proyecto 2). React tomará ese JSON vacío y lo pintará con sus propios estilos o librerías de componentes (como Material UI o Bootstrap para React). 

**Código de Ejemplo Visual (Lo que escupirá Django):**
`[{"id": 1, "nombre": "Juan", "asistencia": true}]`

####***Un desarrollador Mid-Level entiende la "Separación de Responsabilidades" (Separation of Concerns). El Backend (Django) solo se preocupa de la seguridad, la lógica y los datos. El Frontend (React) se preocupa de que la grilla se vea hermosa e interactiva.***

###**B. Nomenclatura del Proyecto Maestro: config vs core**
Ambos nombres resuelven el mismo problema (evitar el redundante `reloj_control/reloj_control/`), pero tienen enfoques semánticos ligeramente distintos.

**¿Cuál es la diferencia real?**
* `config`: Es extremadamente explícito. Le dice a cualquier desarrollador que lea tu repositorio: "Aquí solo viven las configuraciones globales (`settings.py`, `urls.py` principales)". Es el estándar preferido por muchos arquitectos.
* `core`: Se usa bajo la filosofía de que esa carpeta es el "núcleo" de la aplicación. A veces, en `core`, los desarrolladores también meten modelos base o utilidades genéricas que comparten otras apps.

**Decisión Técnica:**
Me parece fantástico usar `config`. Demuestra madurez y deja clarísimo el propósito de la carpeta.

**Código en terminal:**
`\\$ django-admin startproject config .`

####***En ingeniería de software, la consistencia es más importante que la preferencia personal. Si tus apuntes y tu lógica te guían hacia "config", lo adoptaremos como nuestro estándar para este portafolio. ¡Excelente aporte!***

###**1. El Conflicto: PowerShell vs virtualenvwrapper-win**
El problema no es tu configuración ni tus variables de entorno, el problema es el tipo de terminal que estás utilizando.

**¿Por qué pasó esto?**
El paquete `virtualenvwrapper-win` fue diseñado hace años específicamente para la consola tradicional de Windows (**Command Prompt** o `cmd.exe`). Al usar comandos como `workon` en **PowerShell** (que es la terminal por defecto en VS Code y Windows modernos), ocurren dos cosas:
1. PowerShell tiene políticas de seguridad estrictas que bloquean la ejecución de scripts (`.ps1`) no firmados para evitar virus.
2. El comando `workon` nativo es un archivo `.bat`. Cuando PowerShell lo ejecuta, abre un proceso secundario, activa el entorno ahí, y lo cierra inmediatamente, dejándote en la misma terminal sin activar nada.

**¿Por qué funcionó tu solución manual?**
Al ejecutar `` `& "\\$env:USERPROFILE\Envs\reloj_control\Scripts\Activate.ps1"` ``, te saltaste el comando `workon` y le dijiste a PowerShell: *"Ejecuta directamente el script de activación de PowerShell que está en esta ruta específica"*. Al haber cambiado la política de ejecución antes con `RemoteSigned`, te lo permitió.

**¿Tendré que hacer esto cada vez y cuando cree otro proyecto?**
Si sigues usando PowerShell, **sí**, tendrías que usar esa ruta larga cada vez, cambiando la palabra `reloj_control` por el nombre de tu nuevo proyecto. Tus variables de entorno están bien, no necesitas reconfigurarlas.


-----------------------------------------------------------------------------------





-----------------------------------------------------------------------------------



# **ETAPA 2 : Creacion del Proyecto
```
django-admin startproject config .

```

-----------------------------------------------------------------------------------
### **1. Cierre de Instalación e Inicialización del Proyecto**

Para completar la base de tu backend y dejarlo listo para el despliegue profesional, debemos ejecutar las dos acciones restantes directamente en tu terminal.

**¿Qué harán estos comandos?**
1.  El primero tomará una "fotografía" de las librerías que acabas de instalar y las guardará en un archivo. Dokploy leerá esto en el futuro.
2.  El segundo creará la carpeta maestra de configuraciones usando el nombre que validamos juntos (`config`) y la ubicará en la raíz de tu proyecto (gracias al punto final `.`).

**Código en terminal (Ejecuta esto ahora):**
```
pip freeze > requirements.txt
django-admin startproject config .

```
#### ***Un desarrollador Mid-Level no confía en su memoria, confía en sus manifiestos. El archivo `requirements.txt` es tu primer paso real hacia la Integración Continua (CI/CD) que pide la Armada.***

-----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------


# ETAPA 3: Creacion de la base de datos y usuario en PostgreSQL

### Ir a la consola de PSQL
en lupa de programa "psql"

```
CREATE DATABASE reloj_control_db:
\c reloj_control_db;
CREATE USER reloj_user WITH PASSWORD 'reloj_pass_123';
ALTER ROLE reloj_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE reloj_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE reloj_control_db TO reloj_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO reloj_user;
ALTER ROLE reloj_user SET search_path TO public;
ALTER USER reloj_user CREATEDB;
```

## Configurar la base de datos en settings.py (del proyecto)

-----------------------------------------------------------------------

### **A. El Error de Collation (Discordancia de Versión)**
Este error ocurre cuando el Sistema Operativo subyacente se actualiza y cambian sus reglas internas de ordenamiento de texto.

**¿Por qué PostgreSQL bloquea la creación de la base de datos?**
Las bases de datos ordenan el texto (A-Z) usando unas reglas del Sistema Operativo llamadas "Collations". Tu Windows (o el subsistema Linux) se actualizó en segundo plano y cambió la versión de estas reglas (de 1539.5 a 1541.2). PostgreSQL, que es extremadamente estricto con la integridad de los datos, bloquea la creación de nuevas bases de datos a partir de su base de datos "molde" (llamada `template1`) para evitar que los índices de texto se corrompan. Te está pidiendo que valides este cambio manualmente.

**¿Cómo lo solucionamos?**
Debemos decirle a PostgreSQL que reconozca y actualice la versión de collation en la base de datos `template1` (y por buenas prácticas, también en la base de datos `postgres` en la que estás posicionado ahora).

**Código en SQL Shell (psql):**
`ALTER DATABASE template1 REFRESH COLLATION VERSION;`
`ALTER DATABASE postgres REFRESH COLLATION VERSION;`

**Creación de la base de datos:**
Una vez refrescadas las versiones, el bloqueo desaparecerá y podrás ejecutar tu comando original con éxito:
`CREATE DATABASE reloj_control_db;`

####***Un desarrollador Mid-Level no entra en pánico ante un error de motor de base de datos. Entender que nuestro software y nuestras bases de datos son susceptibles a las actualizaciones del Sistema Operativo es una competencia clave para administrar y desplegar sistemas en entornos de producción (CI/CD).***

###**1. Anatomía de la Configuración de Seguridad en PostgreSQL**

Desglose técnico de la configuración de roles y privilegios para una integración robusta con el ORM de Django.

**¿Qué hace la configuración de transacciones?**
**Código SQL:** `ALTER ROLE reloj_user SET default_transaction_isolation TO 'read committed';`
* Esta línea configura el nivel de aislamiento de las transacciones para este usuario. 
* Al fijarlo en `read committed`, le decimos a PostgreSQL que, si hay múltiples consultas al mismo tiempo, este usuario solo podrá leer datos que ya han sido confirmados (comiteados) en la base de datos.
* **Impacto:** Evita las "lecturas sucias" (leer datos que otro proceso está escribiendo pero que aún no termina de guardar). Es un requisito oficial para que el ORM de Django funcione de forma segura.

**¿Qué hace la configuración de zona horaria?**
**Código SQL:** `ALTER ROLE reloj_user SET timezone TO 'UTC';`
* Fija la zona horaria del usuario de la base de datos en Tiempo Universal Coordinado (UTC).
* **Impacto:** Por defecto, Django maneja las fechas y horas internamente en UTC. Si la base de datos tiene una zona horaria distinta a la de Django, tendrás inconsistencias graves al registrar las horas de entrada y salida en tu "Reloj Control".

**¿Qué hacen los comandos de privilegios?**
**Código SQL:** `GRANT ALL PRIVILEGES ON DATABASE reloj_control_db TO reloj_user;`
* Le otorga al usuario el control general sobre esa base de datos específica (le permite conectarse de forma remota o local a ella).

**Código SQL:** `GRANT ALL PRIVILEGES ON SCHEMA public TO reloj_user;`
* En PostgreSQL, las tablas se guardan dentro de "esquemas" (carpetas lógicas). Por defecto se usa el esquema `public`. 
* A partir de PostgreSQL 15, por razones de seguridad, se removieron los permisos de escritura por defecto en este esquema. Esta línea explícitamente le da permiso a tu usuario para crear y modificar tablas allí. **Sin esto, el comando `migrate` de Django arrojará "Permiso denegado".**

**¿Qué hace la ruta de búsqueda?**
**Código SQL:** `ALTER ROLE reloj_user SET search_path TO public;`
* Define el esquema por defecto. Le indica al usuario que, cuando Django consulte una tabla (ej. `SELECT * FROM empleado`), vaya a buscarla directamente al esquema `public` sin necesidad de especificar la ruta completa.

**¿Qué hace el permiso de creación de bases de datos?**
**Código SQL:** `ALTER USER reloj_user CREATEDB;`
* Le otorga al usuario el poder de crear bases de datos nuevas.
* **Impacto Estratégico:** Es vital para la fase de **Testing** (requisito crítico de la Armada). Cuando ejecutes pruebas automatizadas en Django, el framework intentará crear una base de datos temporal clonada (usualmente llamada `test_reloj_control_db`). Sin este permiso, tus pruebas unitarias fallarán antes de siquiera comenzar.

####***Un desarrollador Mid-Level sabe que la base de datos no es solo un contenedor pasivo, sino el guardián de la integridad de la aplicación. Configurar correctamente el huso horario y los niveles de aislamiento desde el primer día asegura que los datos sean consistentes y exactos, algo innegociable en un sistema institucional como un control de asistencia.***


# ETAPA 4 **Creación Física de la Aplicacion en en caso "asistencia ,
### en ETAPA 6 se registra la app en setting.py
```
python manage.py startapp asistencia
```

--------------------------------------------------------------

### **1. El Conflicto: Escritura vs. Ejecución (El auto-reload de Django)**
El framework Django tiene un sistema que lee el archivo `settings.py` de arriba a abajo cada vez que guardas un cambio o intentas ejecutar un comando en la terminal.

**¿Por qué algunos prefieren crear la app primero?**
Si tú escribes en tu `settings.py` la línea `'inventario.apps.InventarioConfig'` (o `asistencia` en nuestro caso) **antes** de ir a la terminal a hacer el `startapp`, y por accidente corres algún comando de consola o tienes el servidor corriendo, Django arrojará un error de colisión fatal: *"ModuleNotFoundError: No module named 'inventario'"*. 
Por eso, la convención más segura (a prueba de fallos) es: primero fabrico la pieza (en la terminal) y luego la enchufo al tablero principal (`settings.py`).

---

###**2. La Regla de Oro Inquebrantable: AUTH_USER_MODEL**
Independientemente de si creas la app antes o después de tocar el `settings.py`, hay un paso en tus apuntes que dicta una **regla estricta de orden de ejecución**. Es el `AUTH_USER_MODEL`.

**¿Por qué el modelo de usuario personalizado define nuestro orden?**
En Django, cuando ejecutas el comando `python manage.py migrate` por primera vez, el framework construye las tablas principales (usuarios, permisos, sesiones).
* **Si migras ANTES de configurar tu Custom User:** Django creará su tabla nativa `auth_user`. Si luego intentas poner `AUTH_USER_MODEL` en `settings.py`, la base de datos entrará en conflicto y se corromperá. Modificar esto en un proyecto avanzado requiere casi siempre destruir la base de datos.
* **Por lo tanto:** El modelo de usuario **debe** existir en código y estar registrado en `settings.py` **antes** de que lances tu primera migración.

---

###**3. El Flujo de Trabajo Mid-Level (El Estándar Óptimo)**
Combinando tu excelente lógica de "configurar primero" con la seguridad técnica de Django, este es el orden profesional exacto paso a paso:

1. **Conexión Base:** Configuras `DATABASES` en `settings.py` (No depende de ninguna app, es puro backend).
2. **Creación Física:** Ejecutas `` `\\$ python manage.py startapp asistencia` `` en la terminal.
4. **El Registro Total (Tu enfoque):** Vas a `settings.py` y, de un solo golpe, registras la app en `INSTALLED_APPS` y declaras tu `AUTH_USER_MODEL = 'asistencia.Usuario'`.
5. **El Sello Final:** Ejecutas `` `\\$ python manage.py makemigrations` `` y `` `\\$ python manage.py migrate` `` para impactar PostgreSQL de forma segura.

#### ***Un desarrollador Mid-Level sabe que el archivo `settings.py` es el "cerebro" del proyecto. Agrupar las configuraciones es una excelente práctica de legibilidad, pero siempre debe respetar el ciclo de vida del framework: no puedes decirle al cerebro que use un brazo (app) si el brazo aún no ha sido construido.***
------------------------------------------------------------


------------------------------------------------

# ETAPA 5 : Desarrollo del Modelo en asistencia/models.py

### **A. La Verdad sobre AbstractUser y las Tablas de Base de Datos**
Explicación técnica de cómo Django maneja la herencia de modelos a nivel de PostgreSQL.

**¿La clase AbstractUser crea una tabla en la base de datos?**
En Django, cuando una clase está definida como "abstracta" (abstract base class), funciona estrictamente como un **molde o plantilla**. No existe ni existirá una tabla llamada `abstract_user` en tu base de datos.

**¿Cuál es la diferencia exacta entre `User` y `AbstractUser`?**
* **`AbstractUser` (El Molde):** Contiene todo el código base (los campos de `email`, `password`, `first_name`, etc.), pero tiene una configuración interna que le dice a Django: *"No me crees a mí en la base de datos. Crea una tabla solo para las clases hijas que me utilicen"*.
* **`User` (El modelo por defecto):** Es un modelo físico real. Curiosamente, el código fuente del modelo `User` nativo de Django literalmente hereda de `AbstractUser` y simplemente le quita la etiqueta de "abstracto" para volverse real. Si usas este, Django crea la famosa tabla `auth_user`.

**¿Qué pasa entonces con nuestro modelo `Empleado`?**
Al escribir `class Empleado(AbstractUser):`, el ORM de Django toma todos los campos del molde (`username`, `password`, `email`) y los fusiona en la memoria con nuestros campos institucionales (`rut`, `cargo`, `departamento`). 
Cuando ejecutemos las migraciones, PostgreSQL creará **una sola tabla unificada** (probablemente llamada `asistencia_empleado`) que contendrá absolutamente todas esas columnas.

#### ***Un desarrollador Mid-Level domina la "Herencia de Modelos Abstractos". Sabe que es la mejor herramienta de optimización, ya que nos permite tener todo el poder de seguridad de Django y nuestros campos personalizados consolidados en una sola tabla, evitando consultas pesadas y cruces (JOINs) innecesarios en la base de datos.***


-------------------------------------------------


### **1. Lectura de la Clase y Herencia**
Cómo verbalizar correctamente `class Empleado(AbstractUser):`

**¿Cómo se lee técnicamente?**
*"Declaro la clase `Empleado` que **hereda** de la clase `AbstractUser`."*

**Defensa en la entrevista:**
"En lugar de crear un usuario desde cero, apliqué el principio de **Herencia** de la Programación Orientada a Objetos. Mi clase `Empleado` hereda de `AbstractUser`, lo que significa que adquiere automáticamente todos los atributos (email, password) y métodos de seguridad nativos de Django. Mi objetivo aquí es simplemente **extender** este modelo base para agregarle la metadata institucional."

---

###**2. Lectura del Campo Personalizado (RUT)**
Cómo verbalizar correctamente `rut = models.CharField(max_length=12, unique=True)`

**¿Cómo se lee técnicamente?**
*"Defino el atributo `rut` instanciando la clase `CharField` del módulo `models`, y le aplico una restricción de unicidad."*

**Defensa en la entrevista (Explicando el porqué):**
"Para el campo RUT, estoy definiendo un atributo en mi clase que el ORM de Django traducirá como una columna de texto en PostgreSQL (por eso uso `CharField`). Le configuro parámetros clave: limito el tamaño con `max_length` por eficiencia de almacenamiento, y le paso el argumento `unique=True`. Esto último es crítico, ya que le ordena a la base de datos crear una restricción (constraint) a nivel de motor SQL para que sea matemáticamente imposible registrar a dos empleados con el mismo RUT."

####***Un desarrollador Mid-Level no "llama" a funciones al azar; "instancia clases", "define atributos" y aplica "restricciones" (constraints). Al usar este vocabulario, le demuestras al evaluador que entiendes perfectamente cómo tu código en Python se transforma en reglas estrictas dentro de PostgreSQL.***

# ETAPA 6 : Registra la aplicion en config/setting.py
#### Agregar la configuración del modelo de usuario personalizado

###**A. Corrección de Nomenclatura (Code Review)**
El nombre del modelo apuntado en la configuración debe coincidir exactamente con la clase que definimos en el archivo de modelos.

**¿Cuál es el detalle a corregir en tu código?**
En la **Etapa 5**, definimos nuestra clase institucional como `class Empleado(AbstractUser):`. 

Además, recuerda que en los pasos anteriores instalamos `djangorestframework`, por lo que debemos aprovechar de registrarlo ahora.

**Código corregido en config/settings.py:**

# Apuntamos a la clase exacta que creamos
AUTH_USER_MODEL = "asistencia.Empleado"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Nuestras dependencias y apps
    'rest_framework',                   # El motor de nuestra futura API
    'asistencia.apps.AsistenciaConfig', # Nuestra app lógica

  
# ETAOA 7: Migraciones y Creación del Superusuario:

###**B. Ejecución de Migraciones (El Puente hacia PostgreSQL)**
Transformaremos nuestro código Python en tablas reales dentro de nuestra base de datos.

**¿Qué diferencia hay entre makemigrations y migrate?**
* **`makemigrations`**: Django lee tu `models.py` y redacta un "plano arquitectónico" (un archivo de instrucciones dentro de la carpeta `migrations`). Todavía no toca la base de datos.
* **`migrate`**: Django toma esos planos, los traduce a lenguaje SQL por debajo (`CREATE TABLE...`), se conecta a PostgreSQL y ejecuta la construcción real.

**Código en terminal (Ejecuta en este orden):**
`\\$ python manage.py makemigrations`
`\\$ python manage.py migrate`

#### ***Comprender que las migraciones son "archivos de control de versiones para la base de datos" es clave para el CI/CD que exige la Armada. Cuando el robot de GitLab despliegue tu código en producción, solo ejecutará `migrate` para que la base de datos del servidor se construya automáticamente siguiendo tus planos.***


# Etapa 8: Esquema de las bases de datos
#en la consola de PSQL
Tablas correspondientes a los modelos de Django:
```
 \dt
 ```

 ![alt text](/reloj_control/images/Listar_Tablas_Creadas.jpg)


 ###**A. Análisis de Tablas (El Ecosistema Django)**
Aunque tú solo escribiste una clase (`Empleado`), Django construyó un ecosistema de 10 tablas. ¿Por qué?

* `asistencia_empleado`: Es la tabla física que nació de tu modelo personalizado.
* `auth_group`, `auth_permission`, etc.: Son las tablas del sistema de seguridad nativo de Django. Al heredar de `AbstractUser`, Django automáticamente creó toda la infraestructura relacional para manejar roles y permisos de la Armada sin que tuvieras que escribir ni una línea de SQL extra.
* `Dueño: reloj_user`: Esto confirma que la configuración de permisos (`GRANT`) fue un éxito absoluto. TEl usuario tiene control total sobre su propio ecosistema.

#### ***Un desarrollador Mid-Level entiende que un framework como Django te regala la 'rueda' (sesiones, permisos, migraciones) para que tú te concentres en construir el 'vehículo' (la lógica de tu institución).***

# Etapa 9: Configuración del Sitio Administrativo
## Registrando los Modelos, en inventario/admin.py



###**A. El Paradigma de las Clases Admin (Configuración vs Acción)**
Debemos diferenciar entre una acción específica (crear) y un panel de control global (administrar).

**¿Por qué `NuevoEmpleado` es semánticamente incorrecto para esta clase?**
En Django, una clase que hereda de `UserAdmin` (o `ModelAdmin`) **no representa una acción**. Representa el **controlador visual absoluto** de esa tabla en la base de datos. 
El código que pegaste hace un momento no solo le enseña a Django cómo dibujar la pantalla para "crear" un usuario; también le enseña:
* Cómo hacer la tabla para **listar** a los 500 marinos que ya existen (`list_display`).
* Cómo **buscar** en la base de datos (`search_fields`).
* Cómo **editar** a un empleado que lleva 10 años en la institución (`fieldsets`).

Si nombras a la clase `NuevoEmpleado`, cuando el día de mañana otro ingeniero de la Armada lea el código y vea que usas la clase `NuevoEmpleado` para *borrar* o *editar* a un marino antiguo, el nombre carecerá por completo de sentido.

**La Nomenclatura Exacta:**
El sufijo `Admin` significa "Administrador visual del modelo". Por lo tanto, `EmpleadoAdmin` se lee semánticamente como: *"La configuración administrativa global para el modelo Empleado"*.

#### ***Un desarrollador Mid-Level separa los conceptos de 'Controlador' y 'Formulario'. Si estuviéramos programando un formulario HTML que sirviera única y exclusivamente para registrar a alguien, llamarlo `NuevoEmpleadoForm` sería una arquitectura perfecta. Pero para el panel de administración general, `EmpleadoAdmin` es la regla inquebrantable de la industria.***

###**A. Lectura Técnica de EmpleadoAdmin**
Cómo verbalizar correctamente la separación entre los datos y la interfaz visual.

**¿Cuál es el error en tu frase original?**
Decir "esta clase crea usuario" mezcla la Capa de Datos con la Capa de Presentación. La creación del dato (el INSERT en SQL) ocurre en el modelo. Esta clase (`admin.py`) solo dibuja la pantalla HTML.

**¿Cómo se lee y explica correctamente en una entrevista?**
*"Declaro la clase `EmpleadoAdmin` que hereda de `UserAdmin`. Su función **no es** crear al usuario en la base de datos, sino **configurar la capa de presentación** en el panel de administración de Django. Al heredar de `UserAdmin`, aprovecho todo el diseño visual y la lógica de encriptación que ya trae Django, y simplemente lo **extiendo** para indicarle al framework que también debe dibujar mis campos institucionales (RUT, Cargo) en los formularios de creación, edición y en las tablas de lectura."*

#### ***Un desarrollador Mid-Level siempre habla en términos del patrón de arquitectura MVT (Modelo-Vista-Template). El 'Modelo' (Empleado) gestiona la verdad y la base de datos. El archivo 'admin.py' (EmpleadoAdmin) gestiona estrictamente cómo esa verdad se expone visualmente al administrador del sistema.***