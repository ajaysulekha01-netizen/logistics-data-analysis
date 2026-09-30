# clustering.py
# Logistics Data Analysis - Route Clustering

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def perform_clustering(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Select available numerical features
    possible_features = [
        "distance",
        "route_distance",
        "stops",
        "number_of_stops",
        "package_count",
        "packages",
        "route_duration",
        "duration"
    ]

    features = [col for col in possible_features if col in df.columns]

    if len(features) < 2:
        print("At least two suitable numerical features are required.")
        print("Available columns:", list(df.columns))
        return

    # Prepare data
    X = df[features].copy()

    # Convert values to numeric
    for column in features:
        X[column] = pd.to_numeric(X[column], errors="coerce")

    # Remove missing values
    X = X.dropna()

    if len(X) < 3:
        print("Not enough valid records for clustering.")
        return

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply K-Means clustering
    n_clusters = min(3, len(X))

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(X_scaled)

    # Add cluster labels
    X["Cluster"] = clusters

    # Display cluster summary
    print("\nSelected Features:")
    print(features)

    print("\nCluster Summary:")
    print(X.groupby("Cluster")[features].mean())

    # Visualization using first two features
    plt.figure(figsize=(8, 6))

    plt.scatter(
        X[features[0]],
        X[features[1]],
        c=X["Cluster"],
        alpha=0.7
    )

    plt.xlabel(features[0])
    plt.ylabel(features[1])
    plt.title("Logistics Route Clustering")
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    # Replace this with your actual dataset path
    file_path = "../data/logistics_data.csv"

    perform_clustering(file_path)
