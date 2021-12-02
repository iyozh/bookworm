FROM python:3.8.3-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
