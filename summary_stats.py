"""Summary statistics for the online food delivery dataset."""

import pandas as pd

from main import load_data

CATEGORICAL_COLUMNS = [
    "Gender",
    "Marital Status",
    "Occupation",
    "Monthly Income",
    "Educational Qualifications",
    "Customer Type",
    "Output",
    "Feedback",
]

OCCUPATION_FIXES = {"Self Employeed": "Self Employed"}


def load_clean_data() -> pd.DataFrame:
    df = load_data()

    df = df.drop(columns=["Unnamed: 13"], errors="ignore")

    object_columns = df.select_dtypes(include=["object", "str"]).columns
    for column in object_columns:
        df[column] = df[column].str.strip()

    if "Occupation" in df.columns:
        df["Occupation"] = df["Occupation"].replace(OCCUPATION_FIXES)

    df = df.drop_duplicates().reset_index(drop=True)

    return df


def main() -> None:
    df = load_clean_data()

    print("Summary statistics (numeric columns):")
    print(df.describe(), "\n")

    for column in CATEGORICAL_COLUMNS:
        if column in df.columns:
            print(f"Value counts - {column}:")
            print(df[column].value_counts(), "\n")


if __name__ == "__main__":
    main()
