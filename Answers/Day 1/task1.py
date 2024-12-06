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
    # Calculate median ages by class and survival status
    median_ages = data.groupby(["pclass", "survived"])["age"].median().unstack()

    # Calculate the absolute difference between median ages of survivors and non-survivors
    median_age_diff = (median_ages[1] - median_ages[0]).abs()

    # Remove the name of the index to match the test expectation
    median_age_diff.index.name = None

    return median_age_diff.sort_values(ascending=False)


if __name__ == "__main__":
    from dataset import load_titanic_data

    data = load_titanic_data()
    print(get_median_age_difference_by_class(data))
