FROM python:3.9.6

WORKDIR /usr/src/Antragsverwaltungstool
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requierements.txt .
RUN pip install -r requierements.txt

COPY . .