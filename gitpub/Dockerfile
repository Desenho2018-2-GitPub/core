FROM debian:stretch-slim

EXPOSE 8080

RUN apt-get update && apt-get install -y --no-install-recommends \
  python3 \
  python3-pip \
  pylint

RUN mkdir /gitpub

COPY . /gitpub/

WORKDIR /gitpub

RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
