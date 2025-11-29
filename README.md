# Gestor de Tareas (Django In-Memory)

Este proyecto es una aplicación web desarrollada con Django como parte de una evaluación técnica. Su objetivo es gestionar tareas (crear, leer y eliminar) utilizando almacenamiento en memoria para los datos de las tareas, mientras se aprovecha el sistema de autenticación robusto de Django (SQLite) para la gestión de usuarios.

## 📋 Funcionalidades Principales

1.  **Autenticación de Usuarios:**
    * Inicio de sesión (Login) y Cierre de sesión (Logout).
    * Protección de rutas: Solo usuarios autenticados pueden acceder al sistema.
2.  **Gestión de Tareas (CRUD Parcial):**
    * **Crear:** Los usuarios pueden agregar nuevas tareas mediante un formulario.
    * **Leer:** Visualización de lista de tareas y vista de detalles individuales.
    * **Eliminar:** Opción para borrar tareas específicas.
3.  **Almacenamiento en Memoria:**
    * Las tareas no persisten en una base de datos SQL; se almacenan en una estructura de datos global (`lista` de `diccionarios`) dentro de la aplicación mientras el servidor está activo.
4.  **Privacidad de Datos:**
    * Aislamiento lógico: Cada usuario solo puede ver, editar y eliminar sus propias tareas.

## 📂 Estructura del Proyecto

El proyecto sigue la arquitectura MVT (Modelo-Vista-Template) de Django, adaptada para el almacenamiento en memoria:

* **`gestor_tareas/`**: Directorio principal de configuración (settings, urls globales).
* **`tareas/`**: Aplicación principal.
    * `views.py`: Contiene la lógica de negocio y la variable global `TAREAS_DB` que actúa como base de datos en memoria.
    * `forms.py`: Definición de `forms.Form` para la validación de datos de entrada.
    * `urls.py`: Rutas específicas de la aplicación.
* **`templates/`**: Archivos HTML estilizados con Bootstrap 5.

## 🚀 Guía de Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1. Clonar el repositorio
Descarga el código fuente a tu máquina:
```bash
git clone https://github.com/Wimpy122/EvaluacionModulo6
cd gestor_tareas
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
