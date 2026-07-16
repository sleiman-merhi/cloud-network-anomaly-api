# 🚀Network Anomaly Detection – ML + AWS Deployment

Designed and deployed a cloud-native REST API on AWS for real-time network anomaly detection. The application uses an Isolation Forest model exposed through FastAPI, containerized with Docker, and deployed on Amazon ECS Fargate behind an Application Load Balancer.

---
## ❓What problem are we solving?

Reliable network connectivity is essential, and early issue detection helps prevent failures, minimize downtime, and maintain service quality.

---
## 📌Project Overview

The goal of this project is to detect anomalous behavior in network telemetry data
(e.g. throughput, latency, packet loss, jitter) using an **unsupervised machine learning approach**.

An **Isolation Forest** model is trained and then deployed as a **REST API** using **FastAPI**, **Docker**, and **AWS ECS (Fargate)** behind an **Application Load Balancer**.

---
## 📦 Tech Stack

Python, Scikit-learn, Pandas, Uvicorn, FastAPI, Docker, AWS (ECR, ECS, ALB), Matplotlib  

---
## 🤖Why Isolation Forest?

- Designed for anomaly detection when abnormal events are rare  
- Does not require labeled downtime data  
- Fast and scalable for large telemetry datasets  
- Produces an anomaly score to measure how unusual each data point is

---
## 🔧Pipeline Steps

1. Data cleaning & feature selection  
2. Feature scaling (StandardScaler)  
3. Model training with contamination tuning  
4. Anomaly scoring and thresholding  
5. Validation against provided anomaly labels  

---

## ☁️ Cloud Deployment (AWS)

The API is deployed on AWS using:

- **Docker** – containerized application
- **Amazon ECR** – container image registry
- **Amazon ECS (Fargate)** – serverless container runtime
- **Application Load Balancer** – public HTTP access
- **FastAPI + Uvicorn** – API framework and ASGI server

---

## 🏗️ System Architecture

![Architecture](docs/architecture.png)

---

## 📊Results & Validation

### Anomaly Score 
![Score](isolation_anomaly_score.png)
### Comparison between detected anomalies and labeled anomalies 
![Comparison](model_score_vs_provided_lables.png)

---

## Deployment Proof

| | |
|---|---|
| Swagger UI running on AWS | ECS service running |
| ![Swagger](docs/aws-swagger.png) | ![ECS](docs/ecs-cluster-running.png) |
