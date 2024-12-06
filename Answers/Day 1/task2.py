# src/task2.py
import pandas as pd


def find_strongest_correlation_with_fare(data: pd.DataFrame) -> tuple[str, float]:
    """
    Find the demographic feature with the strongest correlation with fare.

    Args:
        data (pd.DataFrame): The Titanic dataset.

    Returns:
        tuple[str, float]: The feature name and correlation value.
    """
    # TODO: Implement the function to calculate correlation with fare
    correlations = (
        data[["age", "pclass", "sibsp", "parch", "fare"]].corr()["fare"].drop("fare")
    )
    strongest_feature = correlations.abs().idxmax()
    return strongest_feature, correlations[strongest_feature]


if __name__ == "__main__":
    from dataset import load_titanic_data

    data = load_titanic_data()
    print(find_strongest_correlation_with_fare(data))
