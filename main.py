"""Entry point for exploring the online food delivery dataset."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent / "data" / "online_food_delivery_dataset.csv"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def summarize(df: pd.DataFrame) -> None:
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}\n")

    print("First 5 rows:")
    print(df.head(), "\n")

    print("Column dtypes:")
    print(df.dtypes, "\n")

    print("Missing values per column:")
    print(df.isna().sum(), "\n")

    if "Output" in df.columns:
        print("Output distribution (will the customer order again):")
        print(df["Output"].value_counts(), "\n")

    if "Feedback" in df.columns:
        print("Feedback distribution:")
        print(df["Feedback"].value_counts(), "\n")


def main() -> None:
    df = load_data()
    summarize(df)


if __name__ == "__main__":
    main()
