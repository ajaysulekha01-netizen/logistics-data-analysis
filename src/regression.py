import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


def train_regression_model(file_path):
    """
    Train a linear regression model to predict route duration.
    """

    df = pd.read_csv(file_path)

    required_columns = [
        "route_duration",
        "distance",
        "stops",
        "package_count"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        print("Missing columns:", missing_columns)
        return

    df = df[required_columns].dropna()

    X = df[["distance", "stops", "package_count"]]
    y = df["route_duration"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("Regression Model Results")
    print("------------------------")
    print("Mean Absolute Error:", mae)
    print("R2 Score:", r2)

    return model


if __name__ == "__main__":

    file_path = "data/raw/logistics_routes.csv"

    try:
        train_regression_model(file_path)

    except FileNotFoundError:
        print("Dataset not found.")
        print("Please add the dataset to data/raw/")
