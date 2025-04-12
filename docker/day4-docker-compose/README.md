We have built a Flask web app storing data in Redis, both running in separate containers but managed together using docker-compose.


Docker Compose makes multi-container setups simple.

We defined a Flask app + Redis as services.

Used Dockerfile for the web service and a prebuilt Redis image.

depends_on ensures Redis starts before Flask.
