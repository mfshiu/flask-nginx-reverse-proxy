# Flask, Docker and Ngnix Reverse Proxy

This repository contains a basic configuration using reverse proxy
Contains: 
	- [Nginx Server](https://nginx.org/en/) (HTTP and reverse proxy server)
	- [Docker](https://www.docker.com/) (Machine - Ubuntu 16.04)
	- [Pip](https://pip.pypa.io/en/stable/installing) (Package manager - Python)
	- [Flask](http://flask.pocoo.org/) (Microframework Python)

#### How to run
* Add appwww1.localhost and appwww2.localhost to ngix hosts
* Run `docker-compose build` to start the docker machine
* Run `docker-compose up` to start applications in server

#### Test and results
```sh
$ google-chrome appwww1.localhost or $ curl appwww1.localhost
Flask Dockerized App1 
$ google-chrome appwww2.localhost or $ curl appwww2.localhost
$ curl app2.localhost
Flask Dockerized App2
```