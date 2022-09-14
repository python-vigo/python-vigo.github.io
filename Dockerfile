FROM python:3.5.10

COPY . /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG es_ES.UTF-8
ENV LC_ALL es_ES.UTF-8

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN nikola build
CMD nikola serve --browser