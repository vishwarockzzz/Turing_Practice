# src/task4.py
import pandas as pd


def calculate_cabin_fare_premium(data: pd.DataFrame) -> float:
    """
    Calculate the median fare premium for passengers with a cabin.

    Args:
        data (pd.DataFrame): The Titanic dataset.

    Returns:
        float: The difference in median fare between passengers with and without a cabin.
    """
    # TODO: Implement the function to calculate cabin fare premium
    pass


if __name__ == "__main__":
    from dataset import load_titanic_data

    data = load_titanic_data()
    print(calculate_cabin_fare_premium(data))
