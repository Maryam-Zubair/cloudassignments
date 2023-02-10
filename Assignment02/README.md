Setup Docker Network:
docker network create mynetwork (will add containers to the Docker network later while running containers)

Microservice 01:
Created a microservice in Flask, a Python-based web framework that takes the name of a city as input and returns its zip code.
Run the application locally: Testing it on web-broswer -> http://127.0.0.1:3000/zipcode?city=New%20York 
Created Docker File to build a Docker image for a containerized application 
Build Docker Image: docker build -t server1zip
Run container: docker run --net mynetwork -p 3000:3000 --name weather server1zip 

Microservice 02:
Created a microservice in Flask, a Python-based web framework that takes the name of a city as input and returns its zip code.
Run the application locally: Testing it on web-broswer -> http://127.0.0.1:3001/check_weather?zip_code=10001 
Created Docker File to build a Docker image for a containerized application 
Build Docker Image: docker build -t server2wet
Run container: docker run --net mynetwork -p 3001:3001 --name zipcode server2wet 

Created Shared Network:
docker network create mynetwork
