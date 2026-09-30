import pandas as pd


def load_data(file_path):
    """Load logistics data from a CSV file."""
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """Perform basic data cleaning."""
    
    # Remove duplicate records
    df = df.drop_duplicates()

    # Display missing values
    print("Missing values:")
    print(df.isnull().sum())

    # Remove completely empty rows
    df = df.dropna(how="all")

    return df


if __name__ == "__main__":
    file_path = "data/raw/logistics_routes.csv"

    try:
        df = load_data(file_path)
        df = clean_data(df)

        print("\nDataset shape:", df.shape)
        print("\nFirst five rows:")
        print(df.head())

    except FileNotFoundError:
        print("Dataset file not found.")
        print("Please place the logistics dataset inside data/raw/")
