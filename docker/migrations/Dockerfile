FROM python:3.11-alpine

WORKDIR /migration
COPY requirements.txt .
COPY migrations .
RUN pip install --upgrade pip
RUN pip install yoyo-migrations psycopg2-binary
