# Expose Your Application to the Internet with a LoadBalancer

- Up until this point, we've deployed an application, but we've only been able to access it by using a busybox container inside the cluster.

How do you expose your application to the internet?

The answer is a Kubernetes **Service**. A Kubernetes service is a **load balancer** that directs traffic from the internet to Kubernetes pods.

Key points about a LoadBalancer service:

- It has a **public** and **static** IP address.
- The **public IP** means anyone can access it from the internet.
- The **static** IP is important because pods and their IPs change frequently, but the service IP needs to remain the same.

### Service YAML Manifest Overview

We're going to create a service called `demo-service` in the `development` namespace.

Important part:

- The **selector map** tells the service which pods to route traffic to.
- In this case: `app: pod-info`

Check your **deployment spec** to ensure:

- Pods created have the label `app: pod-info`
- If labels don’t match, the service won’t direct traffic properly.

### Port Configuration

- The service port is set to **80** (default HTTP port, so it doesn’t need to be typed in the URL).
- Internally, traffic is sent to port **3000** in the container.

### Service Type

- The type is set to **LoadBalancer**
- Kubernetes supports 3 types of services:
  1. ClusterIP
  2. NodePort
  3. LoadBalancer (used here)

### Deploying the Service

1. **Open a new terminal tab** and run:

```

minikube tunnel

```

2. **In your original tab**, apply the service manifest:

```

kubectl apply -f service.yaml

```

3. **Check the external IP** with:

```

kubectl get services -n development

```

You'll see two IP addresses:

- Internal cluster IP
- External IP (Note: in Minikube, this is typically `127.0.0.1`, your localhost)

**Important Note**:

- Minikube only works locally, so it won’t provide a real public IP.
- On cloud providers like GCP, AWS, or Azure, you will get an actual public IP.

### Testing the Application

1. Copy the external IP (usually `127.0.0.1`) into your browser.
2. If it doesn't work:

- Check the terminal running `minikube tunnel`
- You might need to enter your system password to allow the tunnel.

3. Try accessing the app again — you should see the JSON object from the pod info app.

### Wrap Up

- Stop the tunnel process with `Ctrl + C`
- Congratulations! You've successfully used a Kubernetes LoadBalancer service to expose your app to the internet 🎉

**Reminder**:
Minikube tunnel can be finicky. If it didn’t work perfectly — don’t worry. You’ve learned the concept.

Next up: Adding resource requests and limits to a container — a Kubernetes best practice.

Add resource requests and limits to your pod
Selecting transcript lines in this section will navigate to timestamp in the video

# Add Resource Requests and Limits to Your Pod


Well-configured containers let Kubernetes know how much memory and CPU to reserve on a worker node.

In this guide, you'll learn how to set **CPU** and **memory** requests and limits on the containers in your pods.

### Why Set Resource Requests and Limits?

- **Resources** refer to the available CPU and memory on a node running your pods.
- Without **resource requests**:
  - Pods might be scheduled on nodes without enough capacity.
  - This can lead to **node failure**.
- Without **resource limits**:
  - A container may consume all the node’s resources.
  - This can also cause the **node to crash** and lead to **outages**.

### Setting Resources in Deployment YAML

We’ll add resource requests and limits to our `pod-info` container.

1. Go to the official Kubernetes documentation page on **Resource Management for Pods and Containers**.
2. Find the YAML snippet that shows how to set `resources` with `requests` and `limits`.
3. Copy the relevant section and paste it into your `deployment.yaml` file **under the `image:` key**.

Make sure the indentation is correct:
```yaml
containers:
- name: pod-info
  image: <your-image>
  resources:
    requests:
      memory: "64Mi"
      cpu: "250m"
    limits:
      memory: "128Mi"
      cpu: "500m"
````

### Understanding the Values

- **requests**:
  - Do not schedule the pod unless the node has at least:
    - `64Mi` memory
    - `250m` (0.25 cores) CPU
- **limits**:
  - The container will be throttled or terminated if it tries to use more than:
    - `128Mi` memory
    - `500m` (0.5 cores) CPU

These values are based on the needs of the `pod-info` container, which is lightweight.

### Deploy the Updated Configuration

Run the following command:

```
kubectl apply -f deployment.yaml
```

You should see confirmation that your deployment was configured.

Check pod status:

```
kubectl get pods -n development
```

You’ll notice:

- The old pods are **terminating**
- New pods with the updated resource settings are **running**

This is expected. When you update pod specs, Kubernetes replaces the old pods with new ones.

### Recap

Setting resource **requests and limits** helps:

- Prevent node failures
- Improve cluster stability
- Avoid outages

Now you know how to define and apply these settings in Kubernetes!
