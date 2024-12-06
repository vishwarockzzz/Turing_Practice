# tests/test_main.py
import pytest
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.dataset import load_titanic_data
from src.task1 import get_median_age_difference_by_class
from src.task2 import find_strongest_correlation_with_fare
from src.task3 import calculate_survival_rate_by_family_size
from src.task4 import calculate_cabin_fare_premium
from src.task5 import identify_best_survival_candidate


@pytest.fixture(scope="module")
def titanic_data():
    # Load Titanic data
    data = load_titanic_data()
    # Add necessary columns
    data["has_cabin"] = data["deck"].notna()
    return data


def test_task1_median_age_difference_by_class(titanic_data):
    result = get_median_age_difference_by_class(titanic_data)
    # Expected values for each class based on analysis
    expected_result = pd.Series({1: 10.25, 3: 3.00, 2: 2.50})
    pd.testing.assert_series_equal(result, expected_result, atol=0.01)


def test_task2_strongest_correlation_with_fare(titanic_data):
    result = find_strongest_correlation_with_fare(titanic_data)
    # Expected result for correlation with fare
    expected_feature = "pclass"
    expected_correlation = -0.554
    assert result[0] == expected_feature
    assert abs(result[1] - expected_correlation) < 0.01


def test_task3_survival_rate_by_family_size(titanic_data):
    result = calculate_survival_rate_by_family_size(titanic_data)
    # Expected top survival rates by family size based on analysis
    expected_result = pd.DataFrame(
        {"family_size": [4, 3, 2], "survived": [0.7778, 0.5699, 0.5468]}
    )
    pd.testing.assert_frame_equal(
        result.head(3).reset_index(drop=True), expected_result, atol=0.01
    )


def test_task4_cabin_fare_premium(titanic_data):
    result = calculate_cabin_fare_premium(titanic_data)
    # Expected cabin fare premium
    expected_premium = 45.08
    assert abs(result - expected_premium) < 0.01


def test_task5_best_survival_candidate(titanic_data):
    result = identify_best_survival_candidate(titanic_data)
    # Expected attributes for best survival candidate
    assert result["pclass"] == 1
    assert result["age"] == 2.0
    assert result["sex"] == "female"
    assert abs(result["survival_score"] - 2.333) < 0.01
