FROM debian:buster-slim

EXPOSE 8080

RUN apt-get update && apt-get install -y --no-install-recommends \
  python3 \
  python3-pip 

RUN mkdir /gitpub

ADD . /gitpub/

WORKDIR /gitpub

RUN pip3 install -r requirements.txt
