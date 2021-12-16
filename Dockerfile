#FROM python:2.7-alpine
FROM python:2.7
MAINTAINER Milos Acimovac

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y python2.7-dev
RUN apt-get install -y graphviz
RUN apt-get install -y libsndfile1-dev
RUN apt-get install -y libgraphviz-dev
RUN apt-get install -y pkg-config
RUN apt-get install -y ffmpeg

COPY ./requirements.txt /requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app

EXPOSE 8000