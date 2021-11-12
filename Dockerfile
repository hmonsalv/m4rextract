FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get -y install ffmpeg

COPY req .
RUN pip install -r requirements.txt

COPY scripts .

ENTRYPOINT [ "sh" ]
