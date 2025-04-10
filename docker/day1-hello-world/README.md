# Day 1: Hello Docker 🐳

## ✅ Goals
- Install Docker
- Run your first container
- Understand image vs container

## Installed
## 🔧 Commands
```bash
# Check Docker version
docker --version

##checked the version is Docker version 28.0.4, build b8034c0
# Run hello-world
docker run hello-world
## This is a pre built docker, This pulls the hello-world image from Docker Hub and runs it.

# List running containers
docker ps

# List all containers
docker ps -a


docker container prune  # Removes stopped containers


🧱 Docker Image vs Docker Container
🔹	Docker Image                     	Docker Container
📦	A blueprint or template	                A running instance of that blueprint
📁	Like a class in programming     	Like an object created from the class
🛠	Contains everything needed to run an app: 
        code, libraries, dependencies	        Is the actual execution of the app
🧊	Read-only	                        Writable (in its own layer)
📤	You can build, pull, or push images	You can start, stop, or destroy containers
📍	Static – doesn’t change when running	Dynamic – changes based on what the app does


Image = recipe

Container = dish prepared using the recipe



