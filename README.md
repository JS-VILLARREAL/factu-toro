# Proyecto Django REST Framework

Este proyecto es una API RESTful construida con Django y Django REST Framework. Proporciona endpoints para gestionar [indicar la funcionalidad principal de la API, por ejemplo, usuarios, productos, etc.].

## Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.x
- pip (o tu gestor de paquetes preferido)
- Un entorno virtual (recomendado)

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/JS-VILLARREAL/factu-toro.git
   cd factu-toro

   ```

2. Crea y activa un entorno virtual

   ```bash
   python -m venv .venv
   # En Windows
   .venv\Scripts\activate
   # En MacOS/Linux
   source .venv/bin/activate

   ```

3. Instala las dependencias

   ```bash
   pip install -r requirements.txt

   ```

## Configuración las variables de entorno

4. Renombra el archivo .env.example a .env y edítalo con tus configuraciones locales.

   ```env
   DEBUG=True
   SECRET_KEY=tu_secret_key
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3

   ```

## Migraciones de Base de Datos

5. Aplica las migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate

   ```

## Ejecuta el servidor

6. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver

   ```

## Documentación de la API

Si estás usando Django Rest Framework con drf-spectacular o Swagger, puedes acceder a la documentación de la API en:

- http://127.0.0.1:8000/api/schema/swagger-ui/
- http://127.0.0.1:8000/api/schema/redoc/
