FROM python:2.7-alpine
MAINTAINER Milos Acimovac

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app

#RUN chmod -R 777 /app
#RUN chmod -R 777 /app/logs
