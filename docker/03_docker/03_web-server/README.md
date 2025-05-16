1. build

```bash
    docker build -t our-web-server -f web-server.Dockerfile .
    docker run -d --name web-server our-web-server 
    docker logs web-server  
```

2. add port

```bash 
    docker run -d --name web-server -p 5001:5000 our-web-server 
```

3. 

```bash
    docker run --rm  --entrypoint sh ubuntu -c "echo 'Hello there,' > tmp/file && cat /tmp/file"
```