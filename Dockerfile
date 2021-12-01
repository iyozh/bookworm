FROM python:3.8.3-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile* /code
RUN cd /code && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /code/requirements.txt
COPY . /code/