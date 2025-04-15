Goal: Run your Flask app from Day 6 on Kubernetes with Minikube


We’ll:

Install and start Minikube

Create Kubernetes Deployment and Service YAMLs

Run Flask + PostgreSQL as pods

Access your app via NodePort

⚙️ Prerequisites
If you don’t have these yet, install:


sudo apt update
sudo apt install -y curl apt-transport-https

# kubectl
curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl && sudo mv kubectl /usr/local/bin/

# minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube-linux-amd64 && sudo mv minikube-linux-amd64 /usr/local/bin/minikube


Folder Structure

day7-k8s/
├── flask-deployment.yaml
├── flask-service.yaml
├── postgres-deployment.yaml
├── postgres-service.yaml

