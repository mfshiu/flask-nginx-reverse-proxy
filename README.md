# Flask, Docker and Ngnix Reverse Proxy

This repository contains a basic configuration using reverse proxy:

* [Nginx Server](https://nginx.org/en/) (HTTP and reverse proxy server)
* [Docker Machine](https://www.docker.com/) (Ubuntu 16.04 version)
* [Pip](https://pip.pypa.io/en/stable/installing) (Package manager for Python)
* [Flask](http://flask.pocoo.org/) (Python Microframework)

#### How it works
* In docker-compose file is specified two containers to each application. Each application has a build dir and port configuration 
* Still in this file there is an nginx section specifying the machine version and volume config
* Basically the config files add two virtual hosts (appwww1.localhost and appwww2.localhost) to nginx host

#### How to run
* Run `docker-compose build` to start docker machine
* Run `docker-compose up` to start applications on server

#### Test and results
* To access in a web-browser www1.localhost or localhost:5001 (change www2 and 5001 to app2)
* To access in terminal:
```sh
$ curl www1.localhost
Flask Dockerized App1 
$ curl www2.localhost
Flask Dockerized App2
```	