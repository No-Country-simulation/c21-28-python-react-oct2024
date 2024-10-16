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

# 
python3 manage.py migrate 
python3 manage.py makemigrate 
python3 manage.py runserver 0.0.0.0:8000

#
https://www.okteto.com/blog/how-to-develop-django-and-postgres-applications-with-docker-and-okteto-cli-2-0/

https://www.freecodecamp.org/espanol/news/como-configurar-tu-terminal-de-macos-con-zsh/
 