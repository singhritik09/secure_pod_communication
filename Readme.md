# Wisecow Application
The Wisecow application is a web server that uses fortune and cowsay to display quotes in a browser. This repository includes a Docker setup, GitHub Actions workflow for CI/CD, and Kubernetes deployment for the application.

![Screenshot 2024-07-23 022202](https://github.com/user-attachments/assets/9c11170b-4469-4b8b-bbd5-994e51928e35)

![Uploading Screenshot 2024-07-23 021940.png…]()

## Features
Dockerized Application: Containerized using Docker.
CI/CD Pipeline: Automated build, push, and deployment using GitHub Actions.
Kubernetes Deployment: Deployed as a Kubernetes service with port-forwarding for local testing.
Getting Started
Prerequisites
Docker
Kubernetes (Minikube or other Kubernetes clusters)
GitHub Actions for CI/CD
Secrets configured in GitHub for Docker and Kubernetes
Local Development
Build and Run Locally with Docker


## Deployment
This repository includes a GitHub Actions workflow to automate the build, push, and deployment process to Kubernetes.

GitHub Actions Workflow

The workflow file .github/workflows/build-and-deploy.yml performs the following steps:

Checkout Code: Retrieves the latest code from the repository.

Login to Container Registry: Authenticates with Docker Hub.

Build and Push Docker Image: Builds the Docker image and pushes it to Docker Hub.

Install kubectl: Installs the kubectl command-line tool.
Configure kubectl: Configures kubectl with the Kubernetes cluster credentials.

Start Minikube: Starts a Minikube cluster (or connect to an existing cluster).

Apply Kubernetes Manifests: Applies the deployment and service manifests.

Wait for Pods: Waits for the pods to be running.

## Port-Forward Service: Sets up port forwarding and tests the application.
Kubernetes Manifests

deployment.yaml: Defines the deployment for the Wisecow application.
service.yaml: Defines the service to expose the Wisecow application.
Testing
After deploying to Kubernetes, the workflow will set up port-forwarding to access the application locally.
The port-forwarding command maps the Kubernetes service port to a local port, 
allowing you to test the application by accessing http://localhost:4499.
