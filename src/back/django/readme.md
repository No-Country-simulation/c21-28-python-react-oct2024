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


