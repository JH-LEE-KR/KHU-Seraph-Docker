# Dockerfile
# Set base image 
FROM python:3.8
ENV PYTHONUNBUFFERED 1
# Set maintainer
MAINTAINER "Jaeho Lee <dlwogh9344@khu.ac.kr>"

# Get some package
RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    apt-utils \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /docker-server/seraph-web
ADD . /docker-server/seraph-web

WORKDIR /docker-server/seraph-web

# Install packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run django application on the port 8080
# EXPOSE 8080

# Modify the django hasher code for our custom hasher
RUN sed -i '163s/.*/        algorithm = encoded.split("$")[1 if encoded.startswith("$") else 0]/' /usr/local/lib/python3.8/site-packages/django/contrib/auth/hashers.py
