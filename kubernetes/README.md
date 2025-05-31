# Kubernetes

A simple guide to get started with Minikube and basic Kubernetes commands.

---

## 📦 1. Install Minikube

Install Minikube using Homebrew:

```bash
brew install minikube
```

---

## 🚀 2. Start a Kubernetes Cluster

Start a local Kubernetes cluster:

```bash
minikube start
```

---

## 🔧 3. Useful Minikube & kubectl Commands

```bash
kubectl get nodes               # View nodes in the cluster
minikube update-check           # Check for Minikube updates
minikube stop                   # Stop the Minikube cluster
minikube delete                 # Delete the Minikube cluster
minikube start                  # Start (or restart) the cluster
```

---

## 📡 4. View Cluster Info

Display Kubernetes control plane and component info:

```bash
kubectl cluster-info
```

- This will show the IP address and port of the control plane (usually `127.0.0.1:<random-port>`).
- You'll also see info about services like CoreDNS.
- If you see an error like:

  ```
  The connection to the server was refused...
  ```

  It usually means Minikube isn't running. Fix it with:

  ```bash
  minikube start
  ```

---

## 🧪 5. View Pods and Services Across All Namespaces

```bash
kubectl get pods -A             # List all pods in all namespaces
kubectl get services -A         # List all services in all namespaces
```

> The `-A` flag stands for "all namespaces". These commands show both system and user-deployed resources.

---
