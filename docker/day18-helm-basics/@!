📚 Day 18: Introduction to Helm

What is Helm?
Helm is a package manager for Kubernetes.

It helps you define, install, and upgrade complex Kubernetes applications.

Think of it like "apt" for Ubuntu or "yum" for CentOS, but for Kubernetes!

🛠️ Key Concepts:
1. Helm Charts 📦
A Chart is a package of Kubernetes resources (YAML files) bundled together.

A Helm Chart defines:

Deployments

Services

ConfigMaps

Secrets

Ingress

and other k8s objects

2. Helm Repositories 📚
A Helm repository is a place where charts are stored and shared.

Example: https://artifacthub.io/ (official repository of public charts)

3. Helm Release 🚀
When you install a chart, it becomes a Release in your Kubernetes cluster.

You can install multiple releases of the same chart with different names or configurations.

🧩 How Helm Works?
Chart → Customized using values.yaml → Installed into Kubernetes as a Release

🏗️ Basic Helm Commands:

Action	Command
Install Helm	`curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
Check Helm version	helm version
Add a repo	helm repo add bitnami https://charts.bitnami.com/bitnami
Update repo	helm repo update
Search a chart	helm search repo mysql
Install a chart	helm install my-mysql bitnami/mysql
List installed releases	helm list
Upgrade a release	helm upgrade my-mysql bitnami/mysql
Uninstall a release	helm uninstall my-mysql

🧪 Example: Install MySQL using Helm
helm repo add bitnami https://charts.bitnami.com/bitnami (one time thing)
helm install my-mysql bitnami/mysql

This command will:

Pull MySQL Chart from Bitnami repo

Install it in your Kubernetes cluster

Create Kubernetes objects like Deployment, Service, PVC, etc.

📄 Structure of a Helm Chart:
my-chart/
  Chart.yaml        # Metadata about the chart
  values.yaml       # Default values for the templates
  templates/        # Folder containing Kubernetes YAML templates
    deployment.yaml
    service.yaml
    configmap.yaml

🌟 Why Helm is Powerful?
Reuse: Same chart can be used for dev, staging, and prod by just changing values.yaml.

Versioning: Rollbacks to previous version are easy.

Customization: Override only what you need.

Simplifies Deployment: Single command deploys multiple Kubernetes objects.

⚡ Summary
Helm = Kubernetes Package Manager

Chart = Package of k8s resources

Release = A deployed chart instance

values.yaml = Place to customize your deployments easily


Happy Helming ;)
