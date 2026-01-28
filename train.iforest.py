import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib
import os

RAW_PATH = "network_anomaly_dataset/network_dataset_labeled.csv"
ART_DIR = "artifacts"

feature_columns = [
    "bandwidth",
    "throughput",
    "congestion",
    "packet_loss",
    "latency",
    "jitter",
]

# 1) Load raw data
df = pd.read_csv(RAW_PATH)

# 2) Select only features (ignore non-numeric columns)
X_raw = df[feature_columns].copy()

# 3) Scale using a scaler that we will SAVE
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)

# 4) Train Isolation Forest
model = IsolationForest(
    n_estimators=300,
    contamination=0.05,
    random_state=42
)
model.fit(X_scaled)

# 5) Predict flags and scores
pred = model.predict(X_scaled)               # 1 normal, -1 anomaly
is_anomaly = (pred == -1).astype(int)        # 1 anomaly, 0 normal
score = model.decision_function(X_scaled)    # lower = more abnormal

# 6) Save artifacts
os.makedirs(ART_DIR, exist_ok=True)

joblib.dump(model, f"{ART_DIR}/isolation_forest.joblib")
joblib.dump(scaler, f"{ART_DIR}/scaler.joblib")
joblib.dump(feature_columns, f"{ART_DIR}/feature_columns.joblib")

# 7) Save scored dataset (for analysis)
out = df.copy()
out["anomaly_score"] = score
out["is_anomaly"] = is_anomaly
out.to_csv(f"{ART_DIR}/scored_data.csv", index=False)

print("Saved:")
print(f"- {ART_DIR}/isolation_forest.joblib")
print(f"- {ART_DIR}/scaler.joblib")
print(f"- {ART_DIR}/feature_columns.joblib")
print(f"- {ART_DIR}/scored_data.csv")
print("\nDetected anomalies:", int(is_anomaly.sum()), "out of", len(is_anomaly))
