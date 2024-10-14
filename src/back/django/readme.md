tuve que modificar el archivo de las credenciales de la base de datos asi que si no les funca es muy problable que sea por eso 🙌

>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3307', ---> antes estaba en el 3306
        'USER': 'root',
        'PASSWORD': '123456789', ---> y la password es la que tengo en mi base de datos
        'NAME': 'reservapp',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}



## Docker 

13-10-2024

# Build 
docker compose build c-21-28.django --no-cache
docker compose -f compose.yml build c-21-28.django --no-cache
docker compose -f compose.yml build --no-cache

# Iniciar

docker compose up -d c-21-28.django
docker compose -f compose.yml up -d c-21-28.django
docker compose -f compose.yml up -d

 
# Detener

docker compose down c-21-28.django
docker compose -f compose.yml down 

# Ir a Shell

docker exec -it c-21-28.django sh
cd yair
cd nehuen
hacer xxxxxxxx
python3 manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000

# Limpiar

docker compose -f compose.yml down 
docker container prune
docker image prune
docker volume prune 

# Virtual Env

https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

https://medium.com/@akshatgadodia/dockerizing-your-django-project-environment-wise-8939400d5ab8


