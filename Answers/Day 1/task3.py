# src/task3.py
import pandas as pd


def calculate_survival_rate_by_family_size(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the survival rate by family size.

    Args:
        data (pd.DataFrame): The Titanic dataset.

    Returns:
        pd.DataFrame: Family size and survival rate.
    """
    # TODO: Implement the function to calculate survival rate by family size
    data["family_size"] = data["sibsp"] + data["parch"] + 1
    survival_rates = data.groupby("family_size")["survived"].mean().reset_index()
    return survival_rates.sort_values(by="survived", ascending=False)


if __name__ == "__main__":
    from dataset import load_titanic_data

    data = load_titanic_data()
    print(calculate_survival_rate_by_family_size(data))
