import pandas as pd
import matplotlib.pyplot as plt


def explore_data(file_path):
    """Perform basic exploratory data analysis."""

    df = pd.read_csv(file_path)

    print("Dataset Shape:")
    print(df.shape)

    print("\nDataset Information:")
    print(df.info())

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    return df


def plot_route_duration(df):
    """Plot route duration distribution."""

    if "route_duration" in df.columns:
        plt.figure(figsize=(8, 5))
        plt.hist(df["route_duration"].dropna(), bins=30)
        plt.title("Route Duration Distribution")
        plt.xlabel("Route Duration")
        plt.ylabel("Number of Routes")
        plt.tight_layout()
        plt.show()
    else:
        print("route_duration column not found.")


if __name__ == "__main__":

    file_path = "data/raw/logistics_routes.csv"

    try:
        df = explore_data(file_path)
        plot_route_duration(df)

    except FileNotFoundError:
        print("Dataset not found.")
        print("Please add the dataset to data/raw/")
