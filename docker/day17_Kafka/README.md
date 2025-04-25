We’re gonna deploy Apache Kafka on Kubernetes and make it talk to Zookeeper like a boss.
Earlier on day 10 we had done kafka with docker

✅ Day 17: Deploy Apache Kafka on Minikube using Bitnami Helm Chart
🧠 What You’ll Learn:

Set up Kafka and Zookeeper in Kubernetes using Helm

Verify services and get ready to produce/consume messages

🛠️ Step-by-Step:
1. Add Bitnami Helm Repo (if not already added)
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

2. Install Kafka + Zookeeper
helm install my-kafka bitnami/kafka
This installs Kafka and its required Zookeeper in your cluster.

3. Verify the Pods
kubectl get pods

You should see:
perl
my-kafka-0
my-kafka-zookeeper-0

4. Verify Services
kubectl get svc

Look for services like:

my-kafka

my-kafka-headless

my-kafka-zookeeper

🧪 Try Connecting to Kafka (inside the pod)
5. Access Kafka Pod
kubectl exec -it my-kafka-0 -- bash

6. List Topics
kafka-topics.sh --bootstrap-server localhost:9092 --list
You’ll probably see nothing yet. Let’s create a topic soon!

💡 Pro Tips:
Bitnami Helm chart simplifies the setup massively.

Kafka uses Zookeeper for managing brokers — it’s mandatory in older versions.

We’ll use the internal hostname to connect: my-kafka.default.svc.cluster.local:9092
