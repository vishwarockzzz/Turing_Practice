# Data Analysis Practice Round

Welcome to the Data Analysis Practice Round! This exercise is designed to assess your data analysis, problem-solving, and coding skills, especially within a test-driven development (TDD) approach. You will be working with the Titanic dataset, focusing on extracting meaningful insights and implementing data transformations to solve specific tasks.

Please read the instructions carefully and complete each task as described. Make sure to follow a test-driven approach by writing functions in the `src` directory and validating your solutions using the `pytest` tests provided in `tests/test_main.py`.

---

## Instructions

1. **Environment Setup**:

   - Ensure you have Python installed on your machine.
   - Install the required packages by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Directory Structure**:

   - You will find the following files and directories in this project:
     ```
     ├── src
     │   ├── dataset.py
     │   ├── task1.py
     │   ├── task2.py
     │   ├── task3.py
     │   ├── task4.py
     │   └── task5.py
     ├── tests
     │   └── test_main.py
     └── README.md
     ```
   - `src/dataset.py`: Contains a function to load and preprocess the Titanic dataset.
   - `src/task1.py` to `src/task5.py`: Each file contains a function for a specific task. You need to complete the implementation of these functions.
   - `tests/test_main.py`: Contains test cases that verify the correctness of your implementations.

3. **Workflow**:

   - Each task has a designated function in the corresponding `src/taskX.py` file.
   - Follow the TDD approach: write or update code in each function, then run the tests in `tests/test_main.py` to validate your solution.
   - If your solution passes the tests, you can move to the next task.

4. **Testing**:
   - Use `pytest` to run all tests:
     ```bash
     pytest tests/test_main.py
     ```
   - Ensure all tests pass for each task before proceeding to the next one.

---

## Tasks

### Task 1: Age and Survival Rate by Class

**File**: `src/task1.py`

**Function**: `get_median_age_difference_by_class(data: pd.DataFrame) -> pd.Series`

Identify the passenger class (`pclass`) that shows the most significant median age difference between survivors and non-survivors.

- **Columns to use**: `pclass`, `survived`, `age`
- **Expected Output**: A `pd.Series` with the class as the index and the median age difference as values, sorted in descending order of difference.

---

### Task 2: Correlation Between Fare and Passenger Demographics

**File**: `src/task2.py`

**Function**: `find_strongest_correlation_with_fare(data: pd.DataFrame) -> tuple[str, float]`

Determine which demographic feature has the strongest correlation with the fare. Correlation strength can be either positive or negative.

- **Columns to use**: `fare`, `age`, `pclass`, `sibsp`, `parch`
- **Expected Output**: A tuple containing the feature name and the correlation value.

---

### Task 3: Family Size and Survival Rate

**File**: `src/task3.py`

**Function**: `calculate_survival_rate_by_family_size(data: pd.DataFrame) -> pd.DataFrame`

Calculate the survival rate by family size. Family size is defined as `sibsp + parch + 1` (including the passenger).

- **Columns to use**: `sibsp`, `parch`, `survived`
- **Expected Output**: A `pd.DataFrame` with two columns, `family_size` and `survived`, sorted in descending order of survival rate.

---

### Task 4: Cabin Fare Premium

**File**: `src/task4.py`

**Function**: `calculate_cabin_fare_premium(data: pd.DataFrame) -> float`

Calculate the fare premium associated with having a cabin. For this dataset, we use the `deck` column as a proxy for cabin presence.

- **Columns to use**: `fare`, `deck`
- **Expected Output**: A float representing the difference in median fare between passengers with a cabin and those without.

---

### Task 5: Best Passenger for Expected Survival

**File**: `src/task5.py`

**Function**: `identify_best_survival_candidate(data: pd.DataFrame) -> pd.Series`

Identify the passenger with the highest likelihood of survival, based on a custom scoring metric:

- Younger age, female gender, and higher class (lower `pclass` number) contribute positively to survival.

Develop a scoring metric based on these factors and use it to identify the passenger with the highest survival score.

- **Columns to use**: `pclass`, `age`, `sex`
- **Expected Output**: A `pd.Series` representing the details of the best candidate.

---

## Example Output and Verification

Each task has corresponding test cases in `tests/test_main.py`, which validate the correctness of your implementation. The test cases include pre-calculated values for each task, so running `pytest` will allow you to verify if your solution matches the expected results.

**Important**: The provided test cases are designed to guide you to the correct solution. However, understanding the problem requirements and implementing a solution is the primary goal.

---

## Additional Tips

- Follow clean coding principles. Ensure your code is well-organized and functions are properly documented.
- Test your functions independently by running each file (e.g., `python src/task1.py`) to confirm the output before relying on the pytest tests.
- Focus on accuracy and efficiency. Aim to complete each task with as few steps as necessary.

Good luck, and happy coding!

---
