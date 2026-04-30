# 🚀 Django CI/CD Pipeline with Docker & AWS EC2
---

## 📌 Project Overview

This project demonstrates a complete **DevOps CI/CD pipeline** by deploying a Django web application using:

* Docker (containerization)
* GitHub Actions (automation)
* DockerHub (image registry)
* AWS EC2 (deployment)
* Docker Volumes (persistent storage)

---

## 🧱 Tech Stack

* 🐍 Python (Django)
* 🐳 Docker
* 🔄 GitHub Actions
* 📦 DockerHub
* ☁️ AWS EC2
* 💾 SQLite (Persistent via Docker Volume)

---

## 🏗️ Architecture Diagram

```
          ┌──────────────┐
          │  Developer   │
          └──────┬───────┘
                 │ git push
                 ▼
        ┌──────────────────┐
        │     GitHub       │
        └────────┬─────────┘
                 │ triggers
                 ▼
        ┌──────────────────┐
        │ GitHub Actions   │
        │ (CI/CD Pipeline) │
        └────────┬─────────┘
                 │
     ┌───────────┴────────────┐
     ▼                        ▼
Build Docker Image     Push to DockerHub
     │                        │
     └───────────┬────────────┘
                 ▼
        ┌──────────────────┐
        │      EC2         │
        │  (Docker Host)   │
        └────────┬─────────┘
                 │
         Pull latest image
                 │
         Restart container
                 │
                 ▼
        🌐 Live Django App
```

---

## ⚙️ Step-by-Step Setup

---

### 🟢 1. Launch EC2 Instance

* OS: Ubuntu
* Instance: t2.micro
* Open Ports:

  * 22 (SSH)
  * 8000 (App)

---

### 🔐 2. Connect to EC2

```bash
ssh -i MyKeyPair.pem ubuntu@<EC2-IP>
```

---

### 🐍 3. Install Python & Django

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install django
```

---

### 🐳 4. Install Docker

```bash
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

Reconnect:

```bash
exit
ssh -i ssh-Key.pem ubuntu@<EC2-IP>
```

---

### 📦 5. Clone Repository

```bash
git clone https://github.com/<your-username>/django-cicd-app.git
cd django-cicd-app
```

---

### 🐳 6. Build Docker Image

```bash
docker build -t django-app .
```

---

### ▶️ 7. Run Container

```bash
docker volume create django_data

docker run -d \
  --name django-container \
  -p 8000:8000 \
  -v django_data:/data \
  django-app
```

---

### 🌐 8. Access Application

```
http://<EC2-IP>:8000
```

---

### 🌍 9. Elastic IP Setup

* Allocate Elastic IP
* Associate with EC2

Update Django:

```python
ALLOWED_HOSTS = ['<Elastic-IP>']
```

---

## 🔄 CI/CD Pipeline

---

### 🔐 GitHub Secrets

Add:

```
DOCKER_USERNAME
DOCKER_PASSWORD
EC2_HOST
EC2_USER
EC2_SSH_KEY
```

---

### ⚙️ Workflow File

`.github/workflows/cicd.yml`

Pipeline:

1. Build Docker image
2. Push to DockerHub
3. SSH into EC2
4. Pull latest image
5. Restart container

---

## 🔁 Deployment Flow

```
Git Push →
GitHub Actions →
Docker Build →
DockerHub →
EC2 Deployment →
Live App
```

---

## 💾 Data Persistence

```
-v django_data:/data
```

Ensures:

* No data loss
* Persistent DB across restarts

---

## 🧪 Verify Stored Data

```bash
docker exec -it django-container bash
cd project
python manage.py shell
```

```python
from app.models import Insurance
Insurance.objects.all()
```

---

## 🚀 Features

* 📄 Insurance Form UI
* 💾 Persistent storage
* 🔄 Auto deployment
* 🐳 Dockerized app
* ☁️ Cloud hosted (AWS)

---

## ⚠️ Notes

* `ALLOWED_HOSTS = ['*']` used for demo
* SQLite used for simplicity

---

## 📈 Future Improvements

* 🔁 Nginx reverse proxy
* 🛢 PostgreSQL database
* 🌍 Custom domain + HTTPS
* 🏗 Terraform infrastructure

---

## 🧑‍💻 Author

**Musthaq Ahamed**
---

## ⭐ If you like this project, give it a star!
