# Bookworm

Bookworm is a web-platform for creating book shops

## Installation

Bookworm requires [docker-compose](https://docs.docker.com/compose/gettingstarted/) to run.

Move to project directory, create file `.env.dev`

MacOS example:
```sh
cd bookworm
nano .env.dev
```
Configure `.env.dev` with the following settings

```sh
DEBUG=1
SECRET_KEY=your_secret_key
DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'
ENGINE=django.db.backends.postgresql
DATABASE=postgres
USER=postgres
PASSWORD=postgres
HOST=db
PORT=5432
```
## Docker-compose

Build image and run the docker-container
```sh
docker-compose up --build
```
#### Migrations

Apply all migrations
```sh
docker-compose exec web python3 manage.py migrate
```

Verify the deployment by navigating to your server address in
your preferred browser.

127.0.0.1:8000
