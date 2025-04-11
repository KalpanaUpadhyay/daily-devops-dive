# Build your image
docker build -t flask-app .

# Run and map port 5000 to your host
docker run -p 5000:5000 flask-app

