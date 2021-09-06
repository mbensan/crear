# Generador de Proyectos Django

> Autor: Matias Bensan Fecha: 2021-06-26

## Para crear proyecto nuevo
- Active el ambiente virtual donde tenga Django 3.2+
- Clone este proyecto
- Ejecute 
    `python crear <nombre_proyecto> <nombre_app>`
- Entre a la carpeta del proyecto y ejecute las migraciones
    `python manage.py makemigrations && python manage.py migrate`
- Ejecute el servidor de desarrollo 
    `python manage.py runserver`

## Para preparar proyecto para el servidor (en DO)
- Crear un archivo 'env.py' en la app con el mismo nombre del proyecto,  con el siguiente contenido
    `env = "local""`
- Agregar a principios del settings.py
    `import os
    from .env import env`
- Modificar la línea 'ALLOWED_HOSTS' con lo siguiente:
    `
    if env == 'cloud':
        ALLOWED_HOSTS = ['ip_del_servidor']
        STATIC_ROOT = os.path.join(BASE_DIR, "static/")
    `
- Modificar la línea: `
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': str(BASE_DIR / 'db.sqlite3'),
        }
    }
`
