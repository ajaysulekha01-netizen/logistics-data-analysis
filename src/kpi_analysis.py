import pandas as pd


def calculate_kpis(df):
    """Calculate key logistics performance indicators."""

    kpis = {}

    if "route_duration" in df.columns:
        kpis["Average Route Duration"] = df["route_duration"].mean()

    if "stops" in df.columns:
        kpis["Average Stops per Route"] = df["stops"].mean()

    if "distance" in df.columns:
        kpis["Average Distance per Route"] = df["distance"].mean()

    if "on_time" in df.columns:
        kpis["On-Time Delivery Rate"] = (
            df["on_time"].mean() * 100
        )

    return kpis


def display_kpis(kpis):
    """Display calculated KPIs."""

    print("\nLogistics KPIs")
    print("-" * 30)

    for name, value in kpis.items():
        print(f"{name}: {value:.2f}")


if __name__ == "__main__":

    file_path = "data/raw/logistics_routes.csv"

    try:
        df = pd.read_csv(file_path)

        kpis = calculate_kpis(df)
        display_kpis(kpis)

    except FileNotFoundError:
        print("Dataset not found.")
        print("Please add the dataset to data/raw/")
