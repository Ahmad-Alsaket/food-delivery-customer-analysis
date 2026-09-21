# Food Delivery Customer Analysis

Exploratory analysis of an online food delivery customer survey: who the customers are and whether they say they will order again.

## Dataset

`data/online_food_delivery_dataset.csv` holds one row per customer, with demographics (age, gender, marital status, occupation, income, education, family size), location (latitude, longitude, pin code), customer type, feedback, and an `Output` column recording whether the customer will order again.

## Usage

Requires Python 3 and pandas.

```
pip install pandas
py main.py
```

`main.py` loads the CSV and prints the row and column counts, the first rows, column types, missing values per column, and the `Output` and `Feedback` distributions.

## Status

Work in progress. Data cleaning, summary statistics and correlation analysis will be added.
