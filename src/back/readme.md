## Docker 

# Build 

docker compose -f compose.yml build --no-cache

# Iniciar

docker compose -f compose.yml up -d

 
# Detener

docker compose -f compose.yml down 

# Ir a Shell
 
docker exec -it nombre_servicio sh

docker exec -it django_api sh
  
python3 manage.py migrate --noinput
python manage.py runserver localhost:8000

# Limpiar

docker compose -f compose.yml down 
docker container prune
docker image prune
docker volume prune 

