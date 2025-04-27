📚 Day 19: Writing a Simple Helm Chart
Today we'll build our own Helm Chart instead of using someone else’s.

🏗️ Steps to Create a Basic Helm Chart
1. 📁 Create a Chart Skeleton
helm create my-first-chart
This will generate a folder my-first-chart/ with pre-built structure:

pgsql
my-first-chart/
  Chart.yaml         # Chart metadata (name, version)
  values.yaml        # Default configuration values
  templates/         # Kubernetes YAML templates
    deployment.yaml
    service.yaml
    ingress.yaml
    _helpers.tpl

2. 🛠️ Understand Important Files

File	Purpose
Chart.yaml	Name, description, version of the chart
values.yaml	Configurable values (like image name, port)
templates/	Kubernetes manifest templates with placeholders

3. ✏️ Modify values.yaml
Open values.yaml and define the Docker image you want to use:

image:
  repository: nginx
  pullPolicy: IfNotPresent
  tag: "latest"

service:
  type: ClusterIP
  port: 80

4. ✏️ Modify deployment.yaml Template
In templates/deployment.yaml, replace the image section:

containers:
- name: {{ .Chart.Name }}
  image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
  ports:
    - containerPort: {{ .Values.service.port }}
Here:

{{ .Chart.Name }} -> Injects Chart name dynamically.

{{ .Values.image.repository }} -> Picks image from values.yaml.

5. 🚀 Install Your Chart on Kubernetes
First, make sure your minikube or k8s cluster is running.

Then install:

helm install my-first-release ./my-first-chart
✅ This will deploy Nginx server as a pod and service!

Check:

kubectl get pods
kubectl get services

6. 🔄 Update/Upgrade Helm Release
Modify values.yaml (say, change the image or port), then run:

helm upgrade my-first-release ./my-first-chart

7. 🗑️ Uninstall the Release
helm uninstall my-first-release
This deletes everything Helm created.

✨ Concept Recap
helm create = Generates chart skeleton.

values.yaml = Place your config variables.

templates/ = Write your K8s YAMLs using Helm variables.

helm install/upgrade/uninstall = Manage deployment easily.

🎯 A Very Quick Visual:
mermaid
flowchart LR
A[values.yaml] --> B[deployment.yaml templates]
B --> C[Rendered Kubernetes YAML]
C --> D[Kubernetes Cluster (Pods/Services)]
✅ Today you learned:
How to create a Helm Chart from scratch

How values.yaml connects to templates

How to install/upgrade your own application using Helm


