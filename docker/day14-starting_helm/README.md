✅ Day 14: Use Helm to Deploy Cassandra on Kubernetes
🧠 What You'll Learn:
How to use Helm (a package manager for Kubernetes)

Deploying Cassandra using an official Helm chart

Verifying the deployment

🪛 Prerequisites:
Kubernetes cluster running (like Minikube or Docker Desktop with Kubernetes enabled)

Helm installed (helm version)  [curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 |
This script:Downloads the latest Helm binary  ,  Installs it to /usr/local/bin/helm]

kubectl installed and working

STEPS:
1. Add the Bitnami Helm Repo

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

2. Install Cassandra via Helm

helm install cassandra bitnami/cassandra
This will deploy Cassandra using default values. You can explore values.yaml later for customization.

3. Check Cassandra Pods

kubectl get pods
Make sure all Cassandra pods are in Running or Ready state.

4. Port-forward the Cassandra service (optional)
If you want to access it from your host:

kubectl port-forward svc/cassandra 9042:9042

5. Test Cassandra (Optional)
If you have cqlsh installed:

cqlsh localhost 9042
Or you can exec into the pod:
kubectl exec -it $(kubectl get pod -l app.kubernetes.io/name=cassandra -o jsonpath="{.items[0].metadata.name}") -- bash
cqlsh


📌 Notes:
Bitnami Helm charts are widely used and well-maintained.

This is a real-world skill, especially if you want to manage stateful services like databases in Kubernetes.

Tomorrow, we can explore how to scale the Cassandra stateful set or connect an app to it.
