# src/dataset.py
import pandas as pd
import seaborn as sns


def load_titanic_data() -> pd.DataFrame:
    """
    Load the Titanic dataset from seaborn and perform basic preprocessing.
    Returns:
        pd.DataFrame: The Titanic dataset with necessary columns for analysis.
    """
    data = sns.load_dataset("titanic")
    # Drop rows with missing values in critical columns
    data = data.dropna(
        subset=["pclass", "survived", "age", "fare", "sibsp", "parch", "sex"]
    )
    # Add column for cabin presence based on 'deck' as a proxy
    data["has_cabin"] = data["deck"].notna()
    return data


if __name__ == "__main__":
    print(load_titanic_data().head())
