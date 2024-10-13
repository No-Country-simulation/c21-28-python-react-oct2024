## Docker 

# Build 
docker compose build --no-cache
docker compose -f compose.yml build --no-cache
docker compose -f compose.yml build nombre --no-cache

# Iniciar

docker compose up -d
docker compose -f compose.yml up -d
docker compose -f compose.yml up -d nombre
 
# Detener

docker compose down
docker compose -f compose.yml down 

# Limpiar

docker compose -f compose.yml down 
docker container prune
docker image prune
docker volume prune 

# Ir a Shell

