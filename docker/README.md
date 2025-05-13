
# 📚 Table of Contents

## 🐳 Docker Recap
1. [The Problem Docker Solves](#1-the-problem-docker-solves)  
   - [Traditional Solutions](#traditional-solutions)
2. [What is Docker?](#2-what-is-docker)  
   - [Core Technologies](#core-technologies)  
   - [Key Concepts](#key-concepts)
3. [Why Docker is Better](#3-why-docker-is-better)

## ⚙️ Container Runtimes - Notes
- [Key Concepts](#key-concepts)
- [Manual Steps to Create a Container (Pre-Docker)](#manual-steps-to-create-a-container-pre-docker)
- [Container Runtimes](#container-runtimes)
- [Container Engines vs. Container Runtimes](#container-engines-vs-container-runtimes)

## 📦 OCI and CRI Runtimes - Notes
- [Why Multiple Runtimes Exist](#why-multiple-runtimes-exist)
- [Two Main Categories of Runtimes](#two-main-categories-of-runtimes)
- [1. OCI-Compatible Runtimes](#1-oci-compatible-runtimes)  
   - [What is OCI?](#what-is-oci)  
   - [OCI Runtime Specification ("Runtime Spec")](#oci-runtime-specification-runtime-spec)  
   - [Popular OCI Runtimes](#popular-oci-runtimes)  
   - [Sandboxed OCI Runtimes](#sandboxed-oci-runtimes)
- [2. CRI-Compatible Runtimes](#2-cri-compatible-runtimes)  
   - [What is CRI?](#what-is-cri)  
   - [Popular CRI Runtimes](#popular-cri-runtimes)
- [Summary: OCI vs CRI](#summary-oci-vs-cri)

## ⚙️ The Docker Engine
- [What is a Container Engine?](#what-is-a-container-engine)
- [Popular Container Engines](#popular-container-engines)
  - [Docker Engine](#docker-engine)
  - [Podman](#podman)
- [Summary Table: Docker vs Podman](#summary-table-docker-vs-podman)

## 🗂️ Docker Configuration Files
- [Where are Docker's Configuration Files?](#where-are-dockers-configuration-files)
  - [Key Docker Directories](#key-docker-directories)
  - [Docker API Socket](#docker-api-socket)
  - [Docker Configuration File](#docker-configuration-file)

---

# 🐳 Docker Recap

## 1. 🔧 The Problem Docker Solves

Getting code to run reliably across different machines is difficult due to:

- ❗ **Environment inconsistencies**:
  - OS differences
  - Missing dependencies or incompatible hardware
  - Unavailable files or differing system configurations

### 🧰 Traditional Solutions

- **Configuration Management Tools** (e.g., Chef, Ansible, Puppet):
  - Use "configuration as code" to bring systems to a desired state
  - Require installing tools on target machines
  - Often require learning new languages/frameworks (Ruby, Python, etc.)

- **Vagrant (by HashiCorp)**:
  - Uses **HCL (HashiCorp Configuration Language)** to spin up pre-configured VMs
  - VMs are **resource-heavy** and often require extra post-start configuration
  - Commonly used **alongside configuration management tools**, increasing complexity

---

## 2. 🐳 What is Docker?

Docker uses **containers** and **images** to:
- Package applications and all dependencies
- Ensure consistent app behavior across different environments

### 🧠 Core Technologies

- **Control Groups (cgroups)**: Manage how much system resources (CPU, memory, etc.) containers can consume
- **Namespaces**: Isolate what containers can see or access (files, processes, users, etc.)

### 📦 Key Concepts

- **Images**:
  - Snapshots of file systems
  - Built in **layers**
  - Presented as a single filesystem to containers

- **Containers**:
  - Runtime instances of images
  - Look like regular apps running on the host machine
  - Lightweight, fast, and isolated from each other

---

## 3. ✅ Why Docker is Better

Docker improves developer experience by:
- ✍️ Using a lightweight configuration format: `Dockerfile`
- 📤 Enabling image sharing and reuse via **container registries** (like Docker Hub)
- 🖥️ Offering a user-friendly CLI that wraps complex system APIs


| Feature           | Virtual Machines (VMs)                          | Docker Containers                                 |
|-------------------|------------------------------------------------|---------------------------------------------------|
| **Isolation**      | Full OS isolation via hypervisor               | Process-level isolation via namespaces and cgroups |
| **Resource Usage** | High – each VM runs a full OS                  | Low – shares host OS kernel                        |
| **Startup Time**   | Slow – boots a complete OS                     | Fast – just starts a process                       |
| **Hardware Emulation** | Yes – virtualized hardware                | No – uses host hardware                            |
| **Multiple Apps**  | Can run many apps                              | Typically runs one app per container               |
| **Host Interaction** | Fully isolated from host                    | Can interact with host (configurable)              |


# Container Runtimes - Notes

## Key Concepts

- **Containers** are built on two key Linux kernel features:
  - **Namespaces**: Restrict what resources a container can see and access on the host.
  - **Control Groups (cgroups)**: Limit how much of those resources a container can use.

---

## Manual Steps to Create a Container (Pre-Docker)

1. **Mount a Directory**:
   - Create a file system directory containing everything your app needs.
   - Structure must resemble a standard Linux file system.

2. **Create a Namespace**:
   - Use `unshare` command (invokes the `unshare` syscall).
   - Creates a sandbox environment for the app.

3. **Isolate the File System with `chroot`**:
   - Set the previously created directory as the root of the app’s file system.
   - This prevents the app from affecting the real file system.

4. **Assign to a Control Group**:
   - Limit resource usage (CPU, memory, etc.) for the container.
   - Use `cgroups` to configure these limits.

5. **Set Capabilities**:
   - Further restrict what the app can do using Linux **capabilities**.
   - Limits the system calls the app can perform.
   - Useful for enhancing security within the namespace.

6. **Run the Application**:
   - Only after all the above steps is the containerized app ready to run.

> ⚠️ Networking, storage, and other aspects are still not handled in these manual steps.

---

## Container Runtimes

- **Purpose**: Automate all the above steps.
- **Examples**: Docker, containerd, CRI-O.
- **Function**: Create, manage, and delete containers.

> Instead of running multiple manual commands, you can simply run:  
> `docker run <image-name>`

---

## Container Engines vs. Container Runtimes

| Feature/Responsibility          | Container Runtime               | Container Engine                |
|----------------------------------|----------------------------------|----------------------------------|
| Creates and manages containers   | ✅ Yes                           | ✅ Yes                           |
| Pulls images from registries     | ❌ No                            | ✅ Yes                           |
| Provides user-facing APIs        | ❌ No                            | ✅ Yes                           |
| Handles control groups, namespaces, etc. | ✅ Yes                    | ✅ Via runtime                   |

- **Summary**:  
  - Container runtimes do the heavy lifting of container creation.
  - Container engines provide the full experience including image management, APIs, and user interface.

---

# OCI and CRI Runtimes - Notes

## Why Multiple Runtimes Exist

- Different opinions exist on how containers should be created:
  - Should they run as root?
  - Can the setup be simplified?
- As a result, many **container runtimes** have emerged.

---

## Two Main Categories of Runtimes

1. **OCI-Compatible Runtimes**
2. **CRI-Compatible Runtimes**

---

## 1. OCI-Compatible Runtimes

### What is OCI?
- **OCI = Open Container Initiative**
  - A working group that defines container standards.
  - Provides specs for:
    - **Container images**
    - **Container runtimes**

### OCI Runtime Specification ("Runtime Spec")
- Outlines what a container is.
- Defines what a runtime *should* do (e.g., create/start/stop containers).
- **Does not** enforce *how* those tasks must be done.
- Open source and maintained on GitHub.

### Popular OCI Runtimes

| Runtime | Description |
|--------|-------------|
| **runc** | Docker's original runtime; widely used in the background by many tools. |
| **crun** | Used by Podman (Docker alternative), written in C, maintained by Red Hat. Smaller and faster than runc. |
| **youki** | New runtime written in Rust, offers safety and speed improvements. |

---

## Sandboxed OCI Runtimes

These run containers with **increased isolation** (often with VM-like separation).

| Runtime | Description |
|--------|-------------|
| **gVisor** | Uses a lightweight unikernel between the container and host OS. |
| **Nabla** | Similar to gVisor, fine-tuned control over system interaction. |
| **Kata Containers** | Runs containers inside VMs; ideal for maximum isolation. |

> ✅ All of these still comply with the OCI Runtime Spec.

---

## 2. CRI-Compatible Runtimes

### What is CRI?
- **CRI = Container Runtime Interface**
- Created by **Kubernetes** to:
  - Avoid dependency on any single container runtime.
  - Allow flexible integration with different runtimes.

### Popular CRI Runtimes

| Runtime | Description |
|--------|-------------|
| **containerd** | Default runtime for Docker today. Uses `runc` by default. Supports other runtimes (e.g., gVisor, Kata) via "shims". |
| **CRI-O** | Lightweight Kubernetes-specific runtime. Maintained by Red Hat, Intel, etc. Also supports multiple OCI runtimes. |

---

## Summary: OCI vs CRI

| Feature | OCI Runtimes | CRI Runtimes |
|--------|---------------|---------------|
| Spec Origin | Open Container Initiative | Kubernetes |
| Purpose | Define what a container is and how it behaves | Interface between Kubernetes and container runtimes |
| Example Tools | runc, crun, youki, gVisor, Kata | containerd, CRI-O |
| Compatibility | Follow the OCI Runtime Spec | Integrate with Kubernetes (may use OCI runtimes underneath) |

---

# ⚙️ The Docker Engine

## 🧠 What is a Container Engine?

Container engines operate **above container runtimes**, and their role is to make it easier to manage containers.

They provide:
- Automation tools
- Configuration languages
- Interfaces like CLIs and APIs

> 🔁 They work **with** runtimes (e.g., `runc`, `containerd`), not as replacements.

---

## 🚀 Popular Container Engines

### 1. Docker Engine (Most Popular)
- Includes:
  - `docker` **CLI client**
  - **Dockerfile** syntax for defining how images are built
  - **HTTP REST API** for talking to runtimes
- **Default runtime**: `containerd` (can be changed)
- 🧪 Focus of this course

### 2. Podman (Red Hat’s Alternative)
- Default engine in **Red Hat Enterprise Linux (RHEL)**
- Nearly **functionally equivalent** to Docker
- Key differences:
  - Uses **Buildah** instead of Dockerfile for image creation
  - Uses **crun** as default runtime (instead of containerd)
- Also allows **changing runtimes**

---

## 📝 Summary Table

| Feature             | Docker Engine        | Podman                      |
|---------------------|----------------------|------------------------------|
| **Default Runtime** | `containerd`         | `crun`                       |
| **Image Builder**   | `Dockerfile`         | `Buildah`                    |
| **API Support**     | REST API             | CLI-based (API via Podman v4+) |
| **Platform**        | Cross-platform       | Default on RHEL              |

> ✅ Both engines are flexible, configurable, and support using different runtimes.

---

# 🗂️ Docker Configuration Files & Directories

## 📍 Key Docker Directories (Linux-based Install)

- **`/var/lib/docker`**
  - Main Docker data directory
  - Stores:
    - Containers
    - Container images
    - Metadata used by Docker Engine & runtime

- **`/var/lib/docker/overlay`**
  - Stores **container volumes**
  - These hold persistent or temporary data used by containers during runtime

## 🔌 Docker API Socket

- **`/var/run/docker.sock`**
  - Docker CLI communicates with the Docker Engine through this Unix socket
  - Acts as the "network" bridge between CLI and Engine on the same machine
  - Enables inter-process communication (IPC) locally

## ⚙️ Docker Configuration File

- **`/etc/docker/daemon.json`**
  - Main configuration file for Docker Engine
  - Used to define:
    - Runtime settings
    - HTTP proxy settings
    - Other engine-level configurations
  - 🔹 *Note*: This file might not exist by default. You can create it manually.

---

> 🖥️ This setup assumes Docker is running *natively* on a **Linux VM**.  
> For **Windows users**, it’s recommended to use **Docker Desktop**, which handles much of this setup automatically.