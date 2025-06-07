import pandas as pd
import requests
import os

def load_data(bucket_name):
    population_url = f"https://{bucket_name}.s3.ap-south-1.amazonaws.com/population.json"
    series_url = f"https://{bucket_name}.s3.ap-south-1.amazonaws.com/pr.data.0.Current"

    series = pd.read_csv(series_url, delimiter="\t")
    population_json = requests.get(population_url).json()
    population = pd.json_normalize(population_json, record_path="data")

    return series, population

def analyze_population(population):
    population["Year"] = population["Year"].astype(int)
    population_stats = population[(population["Year"] >= 2013) & (population["Year"] <= 2018)]

    mean = population_stats["Population"].mean()
    std_dev = population_stats["Population"].std()

    print("US Population (2013–2018) — Mean and Std Dev:")
    print(mean, std_dev)

def generate_max_value_series(series):
    # Clean column names
    series.rename(columns={"series_id        ": "series_id"}, inplace=True)
    series.rename(columns={"       value": "value"}, inplace=True)

    # Aggregate and get highest value per series_id
    max_value_series = series.groupby(["series_id", "year"], as_index=False)["value"].agg("sum")
    max_value_series = (
        max_value_series
        .sort_values("value", ascending=False)
        .drop_duplicates("series_id", keep="first")
        .sort_index()
        .reset_index(drop=True)
    )

    print("Top Value per Series ID:")
    print(max_value_series)

def filter_and_merge_series(series, population):
    specific_series = series[
        series["series_id"].str.contains("PRS30006032", case=False) &
        series["period"].str.contains("Q01", case=False)
    ]

    population["Population"] = population["Population"].astype(int)

    result = pd.merge(specific_series, population, left_on="year", right_on="Year", how="left")
    print("Filtered Series for ID 'PRS30006032' and Q01 period:")
    print(result[["series_id", "year", "period", "value", "Population"]])

def lambda_handler(event, context):
    bucket_name = os.environ.get("S3_BUCKET_NAME")

    series, population = load_data(bucket_name)
    print("Series Data:")
    print(series)
    print("Population Data:")
    print(population)

    analyze_population(population)
    generate_max_value_series(series)
    filter_and_merge_series(series, population)

    return "Data processing complete."
