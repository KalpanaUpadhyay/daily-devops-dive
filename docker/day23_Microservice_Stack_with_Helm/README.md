🎯 Deploy a Full Microservice Stack with Helm (App + PostgreSQL)

This day is about combining everything you’ve learned — deploying a real microservice + PostgreSQL DB via Helm, with configs, PVCs, services, and all.

🏗️ 1. Project Structure
We'll build a Helm chart like:

my-microservice/
├── charts/
│   └── postgresql/          # Dependency chart
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── values.yaml
└── Chart.yaml

🧩 2. PostgreSQL as a Dependency
You can add PostgreSQL as a subchart:

In Chart.yaml:
dependencies:
  - name: postgresql
    version: 12.1.5
    repository: https://charts.bitnami.com/bitnami
Then run:

helm dependency update

📝 3. values.yaml Configuration
postgresql:
  auth:
    username: kalpana
    password: mysecret
    database: appdb

app:
  image:
    repository: myapp/image
    tag: latest
  env:
    DB_HOST: postgresql.default.svc.cluster.local
    DB_USER: kalpana
    DB_PASS: mysecret
    DB_NAME: appdb

📦 4. Deployment Template (templates/deployment.yaml)

apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-microservice.fullname" . }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ include "my-microservice.name" . }}
  template:
    metadata:
      labels:
        app: {{ include "my-microservice.name" . }}
    spec:
      containers:
        - name: app
          image: "{{ .Values.app.image.repository }}:{{ .Values.app.image.tag }}"
          env:
            - name: DB_HOST
              value: {{ .Values.app.env.DB_HOST | quote }}
            - name: DB_USER
              value: {{ .Values.app.env.DB_USER | quote }}
            - name: DB_PASS
              value: {{ .Values.app.env.DB_PASS | quote }}
            - name: DB_NAME
              value: {{ .Values.app.env.DB_NAME | quote }}
🚀 5. Install the Chart
helm install my-microservice ./my-microservice

🔍 6. Verify Deployment
kubectl get pods
kubectl logs <app-pod>
kubectl get svc
Check that:

PostgreSQL is up (postgresql-*)

Your app is connecting and running

Logs show no DB connection errors

🧪 Optional: Use helm lint + helm template before deploying!
🔁 Recap:

Component	Purpose
PostgreSQL Subchart	Manages DB for your app
values.yaml	Pass DB creds + image configs
templates/	YAML templates for your app’s resources
helm install	One-click deploys your stack
