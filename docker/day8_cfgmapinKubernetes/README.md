🎯 Goal: Externalize your config using ConfigMap + Secret for Flask + Postgres
We'll:

Create ConfigMap for DB name + user

Create Secret for password

Use them in your Flask and Postgres pods via environment variables




Apply everything!

kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f flask-deployment.yaml


Check everything!

kubectl get configmap
kubectl get secret
kubectl describe pod <flask-pod-name>

