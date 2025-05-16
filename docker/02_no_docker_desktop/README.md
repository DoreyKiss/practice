# When docker desktop can't be used for cost efficiency

You can run Docker using a lightweight VM such as Lima, Colima, or OrbStack

1. using brew you can install lima: [lima](https://github.com/lima-vm/lima)
```bash
    brew install lima
```

2. confirm installation using 
```bash
    lima --help
```


### Managing containers

✅ What is Portainer?

- **Portainer** is an open-source **web UI for managing Docker containers**.
- Offers most functionalities of Docker CLI through a **user-friendly interface**.
- It runs **as a Docker container**, making it very easy to install and use.
- Official GitHub repo: [github.com/portainer/portainer](https://github.com/portainer/portainer)

---

## 🚀 Installing Portainer

### Docker Command:
```bash
docker run -d \
  -p 8000:8000 -p 9443:9443 \
  --name portainer \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

- `-p`: Maps host ports to container ports (8000, 9443 for UI).
- `--name`: Names the container `portainer`.
- `--restart=always`: Ensures the container restarts automatically.
- `-v`: Binds Docker socket and data volume.
- `portainer/portainer-ce:latest`: Pulls and runs the latest Portainer Community Edition.

---

## 🌐 Accessing Portainer

- Go to: `https://localhost:9443`
- ⚠️ You'll see a **browser security warning** due to a self-signed certificate.
  - Proceed by accepting the risk (e.g., “This is unsafe” in Chrome).

---

## 👤 Initial Setup

1. **Create Admin User**
   - Use any username.
   - Password must be **at least 12 characters**.
   - Example: `Hello, from Docker Essentials Training`

2. **Telemetry**
   - Optionally allow collection of anonymous stats.

---

## 🔧 Working with Containers in Portainer

### Select Local Environment
- Environments = Docker endpoints (local or remote).
- Click **"Get Started"** to manage your local Docker host.

### Create an NGINX Container

1. Click **"Add Container"**
2. Set name: `nginx`
3. Image: `nginx`
4. Port binding:
   - Host: `8080`
   - Container: `80`
5. Click **"Deploy the container"**

🧪 **Test:** Visit [http://localhost:8080](http://localhost:8080) — should see NGINX test page.

---

## 🗑️ Removing Containers

1. Go to **Containers view**.
2. Check the box next to `nginx`.
3. Click **"Remove"**.
4. Enable **"Delete non-persistent volumes"**.
5. Confirm removal.

---
