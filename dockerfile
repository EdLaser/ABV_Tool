FROM python:3.9.6-alpine

WORKDIR /usr/src/Antragsverwaltungstool
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add mysql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requierements.txt .
RUN pip install -r requierements.txt

COPY . .