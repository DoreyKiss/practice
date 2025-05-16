# The cli.

## Docker desktop is very convenient and easy to use.

1. you can install it using homebrew or from this link [link](https://www.docker.com/products/docker-desktop/)
```bash
    # The --cask option tells Homebrew that this package is maintained by the open-source community instead of Homebrew developers. 
    brew install docker --cask
```

2. confirm docker is working
```bash
    docker run --rm hello-world
```

## The Docker cli
### Long way of creating containers

```bash
    --help
```

1. Create a docker container the long way

Containers are created from **container images**.

A **container image** is a compressed and pre-packaged file system that contains:

- Your application
- Its environment
- Configuration files
- Instructions on how to start the app

> 💡 The instruction to start the application is called the **entry point**.

2. First need to create a container from an image.

- If the image is not available on your local machine, Docker will automatically **pull it from a container image registry**.
- By default, Docker pulls images from **[Docker Hub](https://hub.docker.com/)**.

```bash
    docker container create hello-world:linux
```

docker `create` creates the containers but does not start them

3. will only show us containers that are actively running
```bash
    docker ps
```

4.
```bash
    docker ps --all
    docker container start <id>
    # state is now exited
    docker ps --all
    # no need to provide the whole id, first few chars is enough
    docker logs <id>
```

5.
```bash
    docker container start --attach
```

### short

1. Docker run automatically created a container from the hello world image, started it, and attached to the container to show us its output immediately.  docker run = docker container create + docker container start + docker container attach.You need to use docker ps to get IDs for containers started with docker run.
```bash
    docker run hello-world:linux
```

- So far, we’ve used **public images** from [Docker Hub](https://hub.docker.com).
- To containerize your **own applications**, you need to:
  - Create a custom **Dockerfile**
  - Build an image from it
  - Start containers based on your image
  - Optionally, push the image to Docker Hub to share

---

#### 📁 Example Files

- `Dockerfile`: Instructions to build the image
- `entrypoint.bash`: Example app that displays the current time

---

## 📝 Dockerfile Overview

A **Dockerfile** is a script with step-by-step instructions to build a Docker image.

#### 🔑 Common Dockerfile Keywords

| Keyword     | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| `FROM`      | Sets the **base image** (local or remote). If missing locally, pulled from Docker Hub. |
| `LABEL`     | Adds metadata (e.g., `maintainer`) to the image.                            |
| `USER`      | Specifies the **user** to run commands as (default is `root`).              |
| `COPY`      | Copies files from the **build context** (usually your working directory).   |
| `RUN`       | Executes commands to **customize the image** (install packages, etc.).      |
| `ENTRYPOINT`| Sets the command that will run when a container is started.                |
| `CMD`       | Provides default arguments to the `ENTRYPOINT` (optional).                  |

---

#### 👤 User and Security Considerations

- Running as **root** inside a container is common but not recommended for security reasons.
- Use the `USER` keyword to switch to a less privileged user like `nobody`.

```Dockerfile```
USER nobody

#### first image

1. tags associate a convenient name with the docker id, so we don't have to remember the image ID
```bash
     docker build -t our-first-image .
```



### image scanners:

1. use verified images or inspect using:
- Calir
- Trivy
- Dagda

## 🧩 Single vs. Multi-Component Apps

- Docker is great for **single application containers**.
- Real-world applications often include **multiple components**:
  - Example: Web app → API/Backend → Database.

## ⚠️ Why Not Just One Container?

- While you *can* put everything into one container, it's **not recommended**:
  - Docker containers are designed to run **one main process**.
  - Running multiple apps in one container can cause:
    - ❌ Data loss
    - ❌ Unpredictable behavior
    - ❌ Difficult maintenance and debugging

---

## 🔗 Connecting Multiple Containers

- The better approach is to run **multiple containers**:
  - 🧠 One for the web app
  - 🔄 One for the backend/API
  - 💾 One for the database
- Connect them using:
  - **Docker virtual networks**
  - **Named volumes** for shared and persistent data

---

## 🚀 Enter Docker Compose

- Writing many `docker run` commands is **tedious and error-prone**.
- **Docker Compose** simplifies managing multiple containers:
  - Uses a single file: `docker-compose.yml`
  - Defines:
    - Containers
    - Networks
    - Volumes
    - Relationships between services
- Start everything with **one simple command**:
  ```bash
  docker-compose up