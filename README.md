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
Configure `.env.dev` file. Example of the settings is presented in `.env.dev.example`

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
