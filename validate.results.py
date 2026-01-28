import pandas as pd
import matplotlib.pyplot as plt

# Load original raw data
df_raw = pd.read_csv("network_anomaly_dataset/network_dataset_labeled.csv")
df_raw["timestamp"] = pd.to_datetime(df_raw["timestamp"])
df_raw = df_raw.sort_values("timestamp").reset_index(drop=True)

# Load scored data
df_scored = pd.read_csv("artifacts/scored_data.csv")

# Merge (index-based,order was preserved)
df = pd.concat([df_raw, df_scored[["anomaly_score", "is_anomaly"]]], axis=1)

print("Model-detected anomalies:", df["is_anomaly"].sum())
print("Provided anomaly labels:", df["anomaly"].sum())

plt.figure(figsize=(12, 5))
plt.plot(df["timestamp"], df["anomaly_score"], label="Anomaly score")
plt.scatter(
    df.loc[df["is_anomaly"] == 1, "timestamp"],
    df.loc[df["is_anomaly"] == 1, "anomaly_score"],
    color="red",
    s=15,
    label="Detected anomaly"
)
plt.xlabel("Time")
plt.ylabel("Anomaly score (lower = more abnormal)")
plt.title("Isolation Forest Anomaly Score Over Time")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(df["timestamp"], df["anomaly_score"], label="Anomaly score")

plt.scatter(
    df.loc[df["anomaly"] == 1, "timestamp"],
    df.loc[df["anomaly"] == 1, "anomaly_score"],
    color="orange",
    s=15,
    label="Provided anomaly label"
)

plt.xlabel("Time")
plt.ylabel("Anomaly score")
plt.title("Model Score vs Provided Anomaly Labels")
plt.legend()
plt.tight_layout()
plt.show()


