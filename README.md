# Flask, Docker and Ngnix Reverse Proxy

This repository contains a basic configuration using reverse proxy:

* [Nginx Server](https://nginx.org/en/) (HTTP server for reverse proxy server)
* [Docker Machine](https://www.docker.com/) (Ubuntu 16.04 version)
* [Pipenv](https://github.com/pypa/pipenv) (Package manager for Python)
* [Flask](http://flask.pocoo.org/) (Python Microframework)

#### How it works
* In docker-compose file are specified two containers to each application. Each application has a build dir and port configuration
* Still in this file there is a nginx section specifying the machine version and volume config
* Basically the nginx config file default add two virtual hosts (www1.localhost to app1 and www2.localhost to app2)

#### How to run
* Run `docker-compose build` to start docker machine
* Run `docker-compose up` to start applications on server

### Configure local host 
* Add www1.localhost and www2.localhost as local dns hosts (it will be dependent of your distribution)

* For linux you can follow this link: https://www.geeksforgeeks.org/creating-custom-domain-name-instead-of-localhost-in-ubuntu/
* For mac you can follow this link: https://osxdaily.com/2009/10/28/set-a-local-domain-to-ease-local-development/

#### Test and results
* To access in a web-browser www1.localhost or localhost:5001 (change www2 and 5001 to app2)
* To access in terminal:
```sh
$ curl www1.localhost
Flask Dockerized App1
$ curl www2.localhost
Flask Dockerized App2
```