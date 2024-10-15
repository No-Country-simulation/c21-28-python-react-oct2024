## Docker 

# Build 
docker compose build c-21-28.mysql c-21-28.django_api --no-cache
docker compose -f compose.yml build c-21-28.mysql c-21-28.django_api --no-cache
docker compose -f compose.yml build --no-cache

# Iniciar

docker compose up -d c-21-28.mysql c-21-28.django_api
docker compose -f compose.yml up -d c-21-28.django_api
docker compose -f compose.yml up -d

 
# Detener

docker compose down c-21-28.django_api c-21-28.mysql
docker compose -f compose.yml down 

# Ir a Shell

docker exec -it c-21-28.django_api sh
 
python3 manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000

# Limpiar

docker compose -f compose.yml down 
docker container prune
docker image prune
docker volume prune 

 