## Docker 

# Build 

docker compose -f compose.yml build --no-cache

# Iniciar

docker compose -f compose.yml up -d

 
# Detener

docker compose -f compose.yml down 

# Ir a Shell

cd folderX
docker exec -it nombre_servicio sh

python3 manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000

# Limpiar

docker compose -f compose.yml down 
docker container prune
docker image prune
docker volume prune 

