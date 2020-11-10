# Para correr el proyecto


1. Instalar pipenv en el computador:

    `pip install pipenv`

2. Instalar pipenv para correr el proyecto:

    `pipenv --python 3.8`

3. Activar pipenv:

    `pipenv shell`

4. Sincronizar todos las librerías:

    `pipenv sync`

    Si estás corriendo el proyecto en local:

    `pipenv sync --sync`

5. crear superuser:

    `python manage.py createsuperuser`

6. Correr el proyecto:

    `python manage.py runserver 0.0.0.0:8000`

7. Entrar a `localhost:8000/admin` o a `localhost:8000`
