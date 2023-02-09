Microservice 01:
Created a microservice in Flask, a Python-based web framework that takes the name of a city as input and returns its zip code.
Run the application locally: Testing it on web-broswer -> http://127.0.0.1:3000/zipcode?city=New%20York
Created Docker File to build a Docker image for a containerized application
Build Docker Image: docker build -t server1
Run container: docker run -dp 3000:3000 microservice1

Microservice 02:
Created another microservice in Flask, a Python-based web framework that takes the zip_code of a city as input and returns it's weather description and temperature
Run the application locally: Testing it on web-broswer -> http://127.0.0.1:3001/check_weather?zip_code=10001
Created Docker File to build a Docker image for a containerized application
Build Docker Image: docker build -t server2
Run container: docker run -dp 3001:3001 microservice2
