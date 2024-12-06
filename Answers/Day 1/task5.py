# src/task5.py
import pandas as pd


def identify_best_survival_candidate(data: pd.DataFrame) -> pd.Series:
    """
    Identify the passenger most likely to survive.

    Args:
        data (pd.DataFrame): The Titanic dataset.

    Returns:
        pd.Series: The passenger details for the one with the highest survival score.
    """
    # TODO: Implement the function to identify the best survival candidate
    data["survival_score"] = (
        (3 - data["pclass"]) * 0.5
        + (data["sex"] == "female") * 1
        + (1 / (data["age"] + 1))
    )
    best_candidate = data.loc[data["survival_score"].idxmax()]
    return best_candidate


if __name__ == "__main__":
    from dataset import load_titanic_data

    data = load_titanic_data()
    print(identify_best_survival_candidate(data))
