from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load artifacts
model = joblib.load("artifacts/isolation_forest.joblib")
scaler = joblib.load("artifacts/scaler.joblib")
feature_columns = joblib.load("artifacts/feature_columns.joblib")

app = FastAPI(title="Network Anomaly Detection API")


class NetworkMetrics(BaseModel):
    bandwidth: float
    throughput: float
    congestion: float
    packet_loss: float
    latency: float
    jitter: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/detect")
def detect(metrics: NetworkMetrics):
    x = np.array([[getattr(metrics, col) for col in feature_columns]])
    x_scaled = scaler.transform(x)

    pred = model.predict(x_scaled)[0]      # 1 normal, -1 anomaly
    score = model.decision_function(x_scaled)[0]

    return {
        "is_anomaly": 1 if pred == -1 else 0,
        "anomaly_score": float(score)
    }
