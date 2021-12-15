#FROM python:2.7-alpine
FROM python:2.7
MAINTAINER Milos Acimovac

ENV PYTHONUNBUFFERED 1

RUN apt-get update
# && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y python2.7-dev
RUN apt-get install -y graphviz
RUN apt-get install -y libgraphviz-dev
RUN apt-get install -y pkg-config


COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app

#RUN chmod -R 777 /app
#RUN chmod -R 777 /app/logs
