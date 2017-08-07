# NGINX Docker Reverse Proxy

This repository contains a basic configuration using reverse proxy
Contains: 
	- Ngix Server
	- Docker Machine (Ubuntu 16.04)
	- Pip (Manager packages)
	- Flask (Microframework Python)

* Add app1.localhost and app2.localhost in your /etc/hosts
* Run ´
* Run `docker-compose up`

The results

```bash
$ curl app1.localhost
hello APP1
$ curl app2.localhost
hello APP2
```
