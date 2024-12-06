# src/task1.py
import pandas as pd


def get_median_age_difference_by_class(data: pd.DataFrame) -> pd.Series:
    """
    Identify the passenger class with the biggest median age difference between
    survivors and non-survivors.

    Args:
        data (pd.DataFrame): The Titanic dataset.

    Returns:
        pd.Series: Median age difference by class.
    """
    # TODO: Implement the function to calculate median age difference
    pass


if __name__ == "__main__":
    from dataset import load_titanic_data

    data = load_titanic_data()
    print(get_median_age_difference_by_class(data))
