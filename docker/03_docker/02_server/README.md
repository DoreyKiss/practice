#

1. build
```bash
    docker build --file server.Dockerfile --tag our-first-server .
```

2. if we use run the terminal will hang. but will not accept keystrokes.
```bash
    docker kill <id>
```

3. use -d
```bash
    docker run -d our-first-server 
    docker exec our-first-server date
    docker exec --interactive --tty e1 bash 
```

4. stopping container

```bash
    # graceful stop
    docker stop <id>

    # immediate stop that can lead to data loss
    docker stop -t 0 
```

5. removing containers
```bash
    # remove container image
    docker rm <id>
    # stop and remove container image
    docker rm -f <if>
```

6. we're listing all containers with the docker PS dash A command, using the dash Q option to only list IDs, then using xargs to take each ID from the left and feed it into Docker RM on the right.
```bash
    docker ps -aq | xargs docker rm
```

7. list and delete images

```bash
    docker images
    docker rmi our-first-server
    # force..
    docker rmi -f our-first-server
```