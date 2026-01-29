# Network Anomaly Detection – ML + AWS Deployment

End-to-end project for detecting network anomalies using machine learning and deploying the model as a production-ready API on AWS.

This project demonstrates a **full AI engineering pipeline**:
data preparation → model training → validation → API serving → containerization → cloud deployment.

---

## Project Overview

The goal of this project is to detect anomalous behavior in network telemetry data
(e.g. throughput, latency, packet loss, jitter) using an **unsupervised machine learning approach**.

An **Isolation Forest** model is trained and then deployed as a **REST API** using **FastAPI**, **Docker**, and **AWS ECS (Fargate)** behind an **Application Load Balancer**.

---

## Machine Learning Approach

- **Problem type:** Unsupervised anomaly detection  
- **Model:** Isolation Forest  
- **Why Isolation Forest:**  
  - Works well when anomalies are rare  
  - No labeled data required  
  - Efficient and interpretable  


### Key steps
1. Data cleaning & feature selection  
2. Feature scaling (StandardScaler)  
3. Model training with contamination tuning  
4. Anomaly scoring and thresholding  
5. Validation against provided anomaly labels  

---

## 📊 Results & Validation

- Model-detected anomalies vs provided anomaly labels
- Visual inspection of anomaly scores over time
- Tuned contamination rate for realistic anomaly detection

Example outputs:
- Anomaly score timeline
- Comparison between detected anomalies and labeled anomalies

---

## System Architecture

![Architecture](docs/architecture.png)

**Architecture summary:**


---

## Cloud Deployment (AWS)

The API is deployed on AWS using:

- **Docker** – containerized application
- **Amazon ECR** – container image registry
- **Amazon ECS (Fargate)** – serverless container runtime
- **Application Load Balancer** – public HTTP access
- **FastAPI + Uvicorn** – API framework and ASGI server

### Deployment proof

| | |
|---|---|
| Swagger UI running on AWS | ECS service running |
| ![Swagger](docs/aws-swagger.png) | ![ECS](docs/ecs-cluster-running.png) |
