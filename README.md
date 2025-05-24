# 📖 ParroquiaWeb - Sistema de Gestión de Catequesis

¡Bienvenido a ParroquiaWeb! Este es un sistema web diseñado para gestionar catequistas, catequizandos y todo el proceso de catequesis en una parroquia, desarrollado por **Grupo 7**.

---

## 🚀 Funcionalidades Principales

✅ Registro, modificación y eliminación de **catequistas**
✅ Registro, modificación y eliminación de **catequizandos**
✅ Validación de relaciones con la base de datos SQL Server
✅ Login y logout de usuarios
✅ Eliminación en cascada con confirmación de catequistas
✅ Mensajes visuales de éxito y error

---

## 🛠️ Tecnologías Usadas

* **Django 4.2.2**
* **SQL Server Express 2019**
* **Python 3.9.x**
* **ODBC Driver 17 for SQL Server**

---

## 📂 Estructura del Proyecto

```
parroquiaweb/
├── catequesis/           # App principal
│   ├── templates/        # Plantillas HTML
│   │   ├── login.html
│   │   ├── home.html
│   │   ├── registrar_catequizando.html
│   │   ├── registrar_catequista.html
│   │   ├── ...
│   ├── views.py          # Vistas
│   ├── urls.py           # Rutas
│   └── ...
├── parroquiaweb/         # Configuración global de Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py             # Script de Django
├── .gitignore            # Archivos y carpetas ignorados en GitHub
└── requirements.txt      # (Opcional) Lista de dependencias
```

---

## 🏃‍♂️ ¿Cómo Ejecutar el Proyecto? (Paso a Paso)

1️⃣ **Clonar el repositorio**

```bash
git clone https://github.com/JustinGomezcoello/ParroquiaWeb.git
```

2️⃣ **Crear y activar el entorno virtual**

```bash
python -m venv env
source env/Scripts/activate   # En Windows
```

3️⃣ **Instalar dependencias necesarias**

```bash
pip install django pyodbc django-mssql-backend
```

4️⃣ **Configurar la Base de Datos**

* Asegúrate de tener SQL Server instalado y corriendo.
* Crea la base de datos **ParroquiaDB**.
* Ejecuta los scripts SQL (tablas y stored procedures) previamente preparados.
* Revisa el archivo `settings.py` para confirmar la conexión:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'ParroquiaDB',
        'HOST': '.\\SQLEXPRESS',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}
```

5️⃣ **Crear el superusuario para login (usuario: grupo7, contraseña: grupo7)**

```bash
python manage.py createsuperuser
```

(Usa las credenciales que desees, pero para pruebas puedes usar `grupo7` / `grupo7`)

6️⃣ **Ejecutar el servidor de desarrollo**

```bash
python manage.py runserver
```

7️⃣ **Acceder al sistema**

* Abre el navegador en `http://127.0.0.1:8000/login/`
* Ingresa las credenciales de login: `grupo7` / `grupo7`.
* Una vez dentro, navega por el sistema usando las opciones de la interfaz.

---

## 💡 Funcionalidades Especiales
```
🔸 **Validaciones Lógicas**: Al registrar un catequista, se valida la existencia del nivel de catequesis.
🔸 **Eliminación en Cascada**: Si intentas eliminar un catequista con asignaciones, el sistema te pide confirmación para eliminar las asignaciones relacionadas.
🔸 **Interfaz Bonita y Minimalista**: La interfaz de login y páginas están estilizadas para una mejor experiencia.
```


---

## ❌ Archivos que NO deben subirse a GitHub

Asegúrate de tener un archivo `.gitignore` con:

```
env/
*.env
*.pyc
__pycache__/
*.sqlite3
*.log
.DS_Store
```

Así no subirás tu entorno virtual ni archivos temporales.

---

## 💙 Créditos

Desarro
