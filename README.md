# MyCyberJebat CTF Platform

## Requirements : docker, create .env file on your production machine

File : .env

```python


# create  .env file in project directory, same directory as manage.py, eg: touch .env 

# The format of the connection string is postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...] # or use sqlite DATABASE_URL=sqlite:///db.sqlite3 for development
# db is the name of our database in docker-compose.yml, replace database_user, user_password, and database_name accoridng to your own preference.
DATABASE_URL=postgres://:database_username:user_password@db/database_name #

# fill with same value in DATABASE_URL above
POSTGRES_DB="" #database_name
POSTGRES_USER="" 
POSTGRES_PASSWORD="" # set database password here, mandatory to get postgres running in docker

# ---------------------------------------------------------------------
# generate your own secret key using 
# SECURITY WARNING: keep the secret key used in production secret! :
# from django.core.management.utils import get_random_secret_key
# get_random_secret_key()
# or docker-compose exec web python -c "import secrets; print(secrets.token_urlsafe(38))"
# With Base64 encoding on average each byte has 1.3 characters. So using 38 results in 51 characters
# in this case
#----------------------------------------------------------------------
DJANGO_SECRET_KEY="" 

# set False in production  server
DJANGO_DEBUG=True 


DEF_EMAIL=""
EMAIL_HOST=""
EMAIL_HOST_PASSWORD=""
EMAIL_HOST_USER="
EMAIL_PORT=587
EMAIL_USE_TLS=True

# for SSL need to get certificate first, search Let's Encrypt for free SSL Certificate, then edit nginx config in "config/nginx/conf.d/local.conf" to use SSL
# SSL and HSTS options can only be used after getting SSL Certificate

DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_SECURE_HSTS_SECONDS = 0 
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS = False
DJANGO_SECURE_HSTS_PRELOAD = False
DJANGO_SESSION_COOKIE_SECURE = True
DJANGO_CSRF_COOKIE_SECURE = True




```




## Quick Start

To start docker container, change directory to project directory, where manage.py reside.
then run this. if use latest docker compose, just replace "docker-compose" to "docker compose"


### 1. cd /path/to/your/fav/directory

### 2. Run git clone https://github.com/azamuddin30/MCJ-Project.git

### 3. To run source code, there are two ways 

> using Django Built-In WebServer for development 

>> - go to folder containing manage.py

>> - Modify .env file --> comment out 'DATABASE_URL=postgres://postgres:postgres@db/postgres', add # infront the string

>> - Modify .env file --> uncomment 'DATABASE_URL=sqlite:///db.sqlite3'

>> - in shell or bash or cmd --> type 'pip install -r requirements.txt'

>> - in shell or bash or cmd --> type 'python3 manage.py migrate'

>> - in shell or bash or cmd --> type 'python3 manage.py collectstatic'

>> - in shell or bash or cmd --> type 'python3 manage.py createsuperuser'

>> - in shell or bash or cmd --> type 'python3 manage.py runserver'

>> - copy 'http://127.0.0.1:8000'

>> - login with superuser username and password create before.

>> - in shell or bash or cmd --> press ctrl-c to quit the server.



> using docker-compose.yml

>> - go to folder containing manage.py

>> - Modify .env file --> uncomment 'DATABASE_URL=postgres://postgres:postgres@db/postgres'

>> - Modify .env file --> comment out 'DATABASE_URL=sqlite:///db.sqlite3' add # infront the string

>> - in shell or bash or cmd --> type 'docker compose up -d --build'

>> - in shell or bash or cmd --> type 'docker compose up exec web python3 manage.py migrate'

>> - in shell or bash or cmd --> type 'docker compose up exec web python3 manage.py collectstatic'

>> - in shell or bash or cmd --> type 'docker compose up exec web python3 manage.py createsuperuser'

>> - then just go to http://127.0.0.1

>> - login with superuser username and password create before.

>> - in shell or bash or cmd --> type 'docker compose down' to stop the containers




## License
MIT License

## Project status
Active
