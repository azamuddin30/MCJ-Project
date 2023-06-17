# To run source code, there are two ways


## using Django Built-In WebServer

- go to folder containing manage.py

- Modify .env file --> comment out 'DATABASE_URL=postgres://postgres:postgres@db/postgres', add # infront the string

- Modify .env file --> uncomment 'DATABASE_URL=sqlite:///db.sqlite3'

- in shell or bash or cmd --> type 'pip install -r requirements.txt'

- in shell or bash or cmd --> type 'python3 manage.py migrate'

- in shell or bash or cmd --> type 'python3 manage.py collectstatic'

- in shell or bash or cmd --> type 'python3 manage.py createsuperuser'

- in shell or bash or cmd --> type 'python3 manage.py runserver'

- copy 'http://127.0.0.1:8000'

- login with superuser username and password create before.

- in shell or bash or cmd --> press ctrl-c to quit the server.




## using docker-compose.yml

- go to folder containing manage.py

- Modify .env file --> uncomment 'DATABASE_URL=postgres://postgres:postgres@db/postgres'

- Modify .env file --> comment out 'DATABASE_URL=sqlite:///db.sqlite3' add # infront the string

- in shell or bash or cmd --> type 'docker compose up -d --build'

- in shell or bash or cmd --> type 'docker compose up exec web python3 manage.py migrate'

- in shell or bash or cmd --> type 'docker compose up exec web python3 manage.py collectstatic'

- in shell or bash or cmd --> type 'docker compose up exec web python3 manage.py createsuperuser'

- then just go to http://127.0.0.1

- login with superuser username and password create before.

- in shell or bash or cmd --> type 'docker compose down' to stop the containers

