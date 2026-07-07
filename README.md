# Flask CI/CD Pipeline using Jenkins and Docker

## Project Overview

This project demonstrates a basic CI/CD pipeline for a Python Flask application using Jenkins, Docker, GitHub, and Docker Hub.

The pipeline automatically:

* Pulls the latest code from GitHub
* Installs Python dependencies from `requirements.txt`
* Builds a Docker image
* Pushes the Docker image to Docker Hub

---

## Project Structure

```
flaskcicd-project/
│
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image instructions
├── Jenkinsfile            # Jenkins CI pipeline
├── deployment.yaml        # Kubernetes deployment file
├── service.yaml           # Kubernetes service file
└── README.md              # Project documentation
```

---

## Technologies Used

* Python
* Flask
* Docker
* Jenkins
* GitHub
* Docker Hub

---

## Application Setup

### Clone Repository

```bash
git clone https://github.com/prithvi-A24/flaskcicd-project.git
```

Move into the project directory:

```bash
cd flaskcicd-project
```

---

## Run Flask Application Locally

Install dependencies:

```bash
pip3 install --break-system-packages -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

The application will start on:

```
http://localhost:5000
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t prithvia24/flask-app .
```

## Run Docker Container

```bash
docker run -d -p 5000:5000 prithvia24/flask-app
```

The application will be available at:

```
http://localhost:5000
```

---

# Jenkins CI Pipeline

## Pipeline Flow

```
Developer
    |
    |
    v
GitHub Repository
    |
    |
    v
Jenkins Pipeline
    |
    ├── Checkout Code
    |
    ├── Install Requirements
    |
    ├── Build Docker Image
    |
    └── Push Image to Docker Hub
```

---

## Jenkins Stages

### 1. Checkout

Jenkins downloads the latest source code from GitHub.

### 2. Install Requirements

Jenkins installs Python dependencies using:

```bash
pip3 install --break-system-packages -r requirements.txt
```

### 3. Docker Build

Jenkins creates a Docker image:

```bash
docker build -t prithvia24/flask-app:${BUILD_NUMBER} .
```

The build number is automatically provided by Jenkins.

Example:

```
prithvia24/flask-app:1
prithvia24/flask-app:2
prithvia24/flask-app:3
```

### 4. Docker Push

Jenkins authenticates with Docker Hub using stored credentials and pushes the image:

```bash
docker push prithvia24/flask-app:${BUILD_NUMBER}
```

---

# Docker Image Repository

Docker Hub Repository:

```
prithvia24/flask-app
```

Images are stored using Jenkins build numbers as tags.

Example:

```
prithvia24/flask-app:5
```

---

# CI/CD Workflow

Whenever code changes are pushed:

```
Code Change
     |
     v
Git Push
     |
     v
Jenkins Build Trigger
     |
     v
Checkout Latest Code
     |
     v
Install Dependencies
     |
     v
Build Docker Image
     |
     v
Push Image to Docker Hub
```

---

## Future Improvements

Possible next steps:

* Add automated testing stage
* Add deployment stage
* Deploy Docker image to Cloud Run or Kubernetes
* Add monitoring and logging
