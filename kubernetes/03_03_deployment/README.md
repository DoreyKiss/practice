### deployment in kubernetes

1. Before running our deployment lets make sure we have our namespaces

```bash
 kubectl gt ns
```

2. run

```bash
kubectl apply -f deployment.yaml
```

3. confirm by listing all the available deployments in the development namespace

```bash
kubectl get deployments -n development
```

4.  the pods that the deployment created.

```bash
kubectl get pods -n deployments
```


5. delete or check health of a pod.

```bash
kubectl delete pod pod-info-deployment-123 -n development
kubectl describe pod pod-info-deployment-123 -n development
```
