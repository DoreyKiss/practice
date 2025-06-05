### debugging kubernetes

1. use -o wido for extra info like ip adrdresses
```bash
kubectl get pods -n development -o wide
```


2. 
```bash
kubectl get pods # copy the pod name of busybox pod.
kubectl exec -it <podname> -- /bin/sh # gets us inside the container
#wget
```
