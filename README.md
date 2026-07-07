# Flask CI/CD Project

A simple Flask application demonstrating a complete CI/CD pipeline using GitHub, Jenkins, Docker, and Python.

## 🚀 Project Overview

This project demonstrates how code changes can automatically trigger a Jenkins pipeline that:

1. Fetches source code from GitHub
2. Installs required dependencies
3. Runs the Flask application build process
4. Builds a Docker image
5. Deploys the application using Docker

## 🛠️ Technologies Used

- Python
- Flask
- Git & GitHub
- Jenkins
- Docker
- Linux

## 📂 Project Structure

```
flaskcicd-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

## 🐍 Application Setup (Local)

### Clone the repository

```bash
git clone https://github.com/<username>/flaskcicd-project.git

cd flaskcicd-project
```

### Create Python virtual environment

```bash
python3 -m venv venv
```

Activate environment:

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Flask application

```bash
python app.py
```

Application will start on:

```
http://localhost:5000
```

---

# 🐳 Running with Docker

## Build Docker image

```bash
docker build -t flask-app .
```

## Run Docker container

```bash
docker run -d -p 5000:5000 flask-app
```

Check running containers:

```bash
docker ps
```

---

# 🔄 Jenkins CI/CD Pipeline

The Jenkins pipeline is defined in the `Jenkinsfile`.

Pipeline stages:

```
GitHub Repository
        |
        ↓
 Jenkins Trigger
        |
        ↓
 Checkout Code
        |
        ↓
 Install Dependencies
        |
        ↓
 Build Application
        |
        ↓
 Build Docker Image
        |
        ↓
 Deploy Container
```

## Jenkins Pipeline Stages

### 1. Checkout

Jenkins downloads the latest source code from GitHub.

### 2. Install Dependencies

Installs Python packages from:

```
requirements.txt
```

### 3. Build

Builds and prepares the Flask application.

### 4. Docker Build

Creates a Docker image:

```bash
docker build -t flask-app .
```

### 5. Deployment

Runs the application inside a Docker container.

---

# 📦 Requirements

Example `requirements.txt`:

```
Flask
```

---

# 🔐 Environment Variables

The Jenkinsfile uses environment variables for configuration.

Example:

```groovy
environment {
    APP_NAME = "flask-app"
}
```

Jenkins also provides built-in variables:

```
BUILD_NUMBER
JOB_NAME
WORKSPACE
GIT_COMMIT
```

---

# 🧪 Testing

Run the application:

```bash
python app.py
```

Verify:

```
http://localhost:5000
```

---

# 📌 Future Improvements

- Add automated unit tests
- Push Docker images to Docker Hub
- Add Kubernetes deployment
- Add monitoring and logging
- Add Jenkins notifications

---

# 👨‍💻 Author

Prithvi Amarnath
