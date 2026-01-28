import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load raw dataset
df = pd.read_csv("network_anomaly_dataset/network_dataset_labeled.csv")

# Sort by time to preserve temporal order
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

# Features used for anomaly detection
feature_columns = [
    "bandwidth",
    "throughput",
    "congestion",
    "packet_loss",
    "latency",
    "jitter",
]

# Select numeric features only
X = df[feature_columns].copy()

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame
X_scaled_df = pd.DataFrame(
    X_scaled,
    columns=feature_columns
)

# Save prepared dataset
X_scaled_df.to_csv(
    "network_anomaly_scaled.csv",
    index=False
)

# Sanity checks
print("Prepared dataset saved.")
print("Shape:", X_scaled_df.shape)
print("\nFirst 5 rows:")
print(X_scaled_df.head())


