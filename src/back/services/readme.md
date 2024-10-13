## Docker 

# Build 
docker compose build --no-cache
docker compose -f compose.yml build --no-cache
docker compose -f compose.yml build c-21-28.shell_django --no-cache

# Iniciar

docker compose up -d
docker compose -f compose.yml up -d
docker compose -f compose.yml up -d c-21-28.shell_django
c-21-28.django
# Detener

docker compose down
docker compose -f compose.yml down 

# Limpiar

docker compose -f compose.yml down 
docker container prune
docker image prune
docker volume prune 

# Ir a Shell

