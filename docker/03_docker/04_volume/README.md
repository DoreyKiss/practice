# Volumes

```bash
docker run --rm  --entrypoint sh -v /tmp/container:/tmp ubuntu -c "echo 'Hello there,' > tmp/file && cat /tmp/file"
```
Now we can use -v to map files on our computer to files in the container as well. However, there's a small caveat to this. If we try to map a file on our computer that does not exist, it will be mapped as a directory within the container

```bash
touch /tmp/change_this_file
docker run --rm  --entrypoint sh -v /tmp/change_this_file:/tmp/file ubuntu -c "echo 'Hello there,' > tmp/file && cat /tmp/file"
```

### clear the vm running docker.

```bash
    docker rmi 
    or
    # WARNING! This will remove:
    # - all stopped containers
    # - all networks not used by at least one container
    # - all dangling images
    # - unused build cache
    docker system prune
```

###

```bash
    docker stats
    docker top
    docker inspect
```