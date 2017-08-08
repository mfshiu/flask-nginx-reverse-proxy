FROM ubuntu:latest

RUN apt-get update -y && \
apt-get install -y python python-pip python-dev build-essential && \
easy_install -U pip

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT 	["python"]

CMD ["app.py"]