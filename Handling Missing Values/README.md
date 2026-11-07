# Handling Missing Values

This module contains hands-on Jupyter notebooks focused on identifying,
analyzing, visualizing, and handling missing data using **Python,
Pandas, and Scikit-learn**.

The notebooks explore missingness patterns, deletion methods,
statistical imputation, missing-value indicators, regression-based
estimation, K-Nearest Neighbors (KNN) imputation, Scikit-learn's
`IterativeImputer`, and end-to-end preprocessing pipelines.

------------------------------------------------------------------------

## 📂 Repository Contents

``` text
Handling Missing Values/
│
├── README.md
├── 50_Startups.csv
├── train (1).xls
│
├── Handling-Missing-Values.ipynb
├── automatically_select_imputer_parameters.ipynb
├── Step-By-Step.ipynb
├── KNN-Imputer.ipynb
└── Iterative-Imputer.ipynb
```

  -------------------------------------------------------------------------------------
  File                                              Description
  ------------------------------------------------- -----------------------------------
  `Handling-Missing-Values.ipynb`                   Covers missing-value detection,
                                                    visualization, missingness
                                                    exploration, complete-case
                                                    analysis, missing indicators, and
                                                    numerical imputation.

  `automatically_select_imputer_parameters.ipynb`   Builds a preprocessing and
                                                    classification pipeline and uses
                                                    `GridSearchCV` to compare
                                                    imputation strategies and model
                                                    parameters.

  `Step-By-Step.ipynb`                              Demonstrates manual, repeated
                                                    regression-based estimation of
                                                    missing numerical values using a
                                                    small sample from the 50 Startups
                                                    dataset.

  `KNN-Imputer.ipynb`                               Applies `KNNImputer` to Titanic
                                                    features and compares Logistic
                                                    Regression performance with mean
                                                    imputation.

  `Iterative-Imputer.ipynb`                         Explores `IterativeImputer`,
                                                    including a Random Forest-based
                                                    imputation example, preprocessing
                                                    with `ColumnTransformer`, and
                                                    cross-validated comparison of
                                                    Simple, KNN, and Iterative
                                                    imputation approaches.

  `50_Startups.csv`                                 Dataset used in the manual
                                                    regression-based imputation
                                                    notebook.

  `train (1).xls`                                   Titanic training data used by the
                                                    automatic imputer-parameter
                                                    selection notebook. The file is
                                                    CSV-formatted despite its `.xls`
                                                    extension and is read with
                                                    `pandas.read_csv()`.
  -------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 📘 Notebooks

### 1. `Handling-Missing-Values.ipynb`

Introduces missing-data analysis and foundational imputation techniques.

**Topics covered:**

-   Counting missing values with `isnull()` and `isna()`.
-   Calculating missing-value percentages by column.
-   Identifying rows containing missing values.
-   Visualizing missingness with the `missingno` library:
    -   Bar plot
    -   Matrix plot
    -   Heatmap
    -   Dendrogram
-   Exploring relationships between missingness indicators and other
    variables.
-   Comparing feature distributions for observations with and without
    missing values.
-   Using a two-sample t-test in a missingness exploration example.
-   Applying complete-case analysis (listwise deletion) with `dropna()`.
-   Comparing distributions before and after row deletion.
-   Creating missingness indicators with `MissingIndicator`.
-   Applying mean and median imputation.
-   Comparing variance, distributions, correlations, and box plots
    before and after imputation.
-   Using `SimpleImputer` and `ColumnTransformer`.

**Libraries used:** Pandas, NumPy, Matplotlib, Seaborn, SciPy,
Missingno, and Scikit-learn.

### 2. `automatically_select_imputer_parameters.ipynb`

Demonstrates how imputation strategies can be selected as part of a
machine-learning workflow.

**Workflow:**

1.  Load the Titanic training dataset.
2.  Remove columns excluded from the model.
3.  Separate input features and the `Survived` target.
4.  Split the data into training and testing sets.
5.  Define numerical and categorical preprocessing steps.
6.  Combine transformations with `ColumnTransformer`.
7.  Build a Scikit-learn pipeline with Logistic Regression.
8.  Use `GridSearchCV` to compare preprocessing and classifier
    parameters.
9.  Inspect the best parameter combination and cross-validation results.

**Preprocessing design:**

  -----------------------------------------------------------------------
  Feature type            Example columns         Processing
  ----------------------- ----------------------- -----------------------
  Numerical               `Age`, `Fare`           Imputation followed by
                                                  scaling

  Categorical             `Embarked`, `Sex`       Imputation followed by
                                                  one-hot encoding
  -----------------------------------------------------------------------

The search explores mean/median numerical imputation,
most-frequent/constant categorical imputation, and Logistic Regression
regularization values. The notebook uses 10-fold cross-validation.

**Evaluation note:** The inspected workflow reports cross-validation
results from the training data. Do not describe that score as final
held-out test accuracy unless a separate test evaluation is added.

### 3. `Step-By-Step.ipynb`

Demonstrates a manual regression-based method for estimating missing
numerical values.

**Dataset:** `50_Startups.csv`

**Selected columns:**

-   `R&D Spend`
-   `Administration`
-   `Marketing Spend`
-   `Profit`

**Workflow:**

1.  Load the 50 Startups dataset.
2.  Select the numerical columns and prepare a small sample.
3.  Introduce missing values for demonstration.
4.  Use column means as initial estimates.
5.  Fit `LinearRegression` models using available features and rows.
6.  Predict selected missing values.
7.  Repeat the estimation process and inspect the updated values.

**Concepts practiced:**

-   Initial mean imputation.
-   Regression-based estimation of missing values.
-   Using other features to estimate a missing feature.
-   Repeated or iterative estimation.

**Important:** This notebook manually demonstrates regression-based
imputation on a five-row sample. It is not an implementation of
Scikit-learn's `IterativeImputer`, and the tiny sample is for
understanding the procedure rather than reliable model evaluation.

### 4. `KNN-Imputer.ipynb`

Applies K-Nearest Neighbors imputation to selected Titanic dataset
features.

**Features used:**

-   `Age`
-   `Pclass`
-   `Fare`

**Target:** `Survived`

**Workflow:**

1.  Load Titanic data from a public GitHub raw-data URL.
2.  Separate the features and target.
3.  Split the data into training and testing sets (`test_size=0.2`,
    `random_state=2`).
4.  Apply `KNNImputer` with `n_neighbors=3`.
5.  Fit the imputer on training features and transform both training and
    testing features.
6.  Train a Logistic Regression classifier and calculate test accuracy.
7.  Repeat the workflow with the default mean strategy of
    `SimpleImputer`.
8.  Compare the resulting accuracy scores.

**Concepts practiced:**

-   Distance-based imputation.
-   Choosing the number of neighbors.
-   Fitting preprocessing only on training data.
-   Comparing imputation approaches through downstream model evaluation.

**Evaluation note:** The comparison is specific to the selected
features, split, and model. One train/test split does not establish that
KNN or mean imputation is universally better.

### 5. `Iterative-Imputer.ipynb`

Explores Scikit-learn's `IterativeImputer` and compares multiple
missing-value handling approaches in classification pipelines.

**Part A --- Random Forest-based Iterative Imputation**

-   Loads Titanic data and selects `Survived`, `Pclass`, `Age`, and
    `Fare`.
-   Separates features and target.
-   Uses an 80/20 train/test split with `random_state=0`.
-   Applies `IterativeImputer` with a `RandomForestRegressor` estimator
    (`n_estimators=10`, `max_iter=10`).
-   Fits the imputer on training features and transforms the test
    features.
-   Trains a `RandomForestClassifier` and evaluates accuracy.

**Part B --- Preprocessing pipeline and parameter search**

-   Removes selected identifier/text columns from the Titanic data.
-   Uses `ColumnTransformer` to apply different transformations to
    selected columns.
-   Applies `SimpleImputer` to `Age`.
-   Applies `OneHotEncoder` to `Sex` and an imputation-plus-encoding
    pipeline to `Embarked`.
-   Creates a missingness indicator for `Cabin`.
-   Combines preprocessing and a `RandomForestClassifier` in a
    `Pipeline`.
-   Uses `GridSearchCV` to compare imputation choices and evaluate the
    selected pipeline.

**Part C --- Comparing Simple, KNN, and Iterative Imputation**

The notebook defines three preprocessing alternatives:

  Approach     Method used for `Age`
  ------------ -----------------------
  Approach 1   `SimpleImputer`
  Approach 2   `KNNImputer`
  Approach 3   `IterativeImputer`

The alternatives are evaluated in a pipeline with a
`RandomForestClassifier` using 10-fold `GridSearchCV`.

The parameter search explores:

-   Simple imputation strategies.
-   KNN neighbor counts and weighting options.
-   Iterative imputation iteration limits and imputation order.
-   `BayesianRidge`, `ExtraTreesRegressor`, and `RandomForestRegressor`
    as candidate estimators for `IterativeImputer`.

**Important implementation detail:** In the initial Random Forest
example, `IterativeImputer` receives multiple numerical features
(`Pclass`, `Age`, and `Fare`). In the later three-way comparison, the
`IterativeImputer` transformer is configured on the `Age` column alone.
That later setup does not exploit relationships among multiple
incomplete columns in the way a multivariate imputation setup would.
Consider expanding the selected columns if the goal is to demonstrate
multivariate imputation.

The notebook includes a comparison table of imputation methods. Treat
broad statements about missingness mechanisms (MCAR, MAR, and MNAR) as
simplified study notes, not as universal rules that identify the
mechanism from the imputation method alone.

------------------------------------------------------------------------

## 🗃️ Datasets

### `train (1).xls` --- Titanic training data

The local file is used by
`automatically_select_imputer_parameters.ipynb`.

**File-format note:** Although the filename ends in `.xls`, the file
content is CSV-formatted and the notebook reads it with:

``` python
df = pd.read_csv("train (1).xls")
```

Keep the filename consistent with the code. A cleaner alternative is to
rename the file to `train.csv` and update the notebook accordingly. Do
not simply change the extension without checking the actual file format.

The KNN and Iterative Imputer notebooks load Titanic data from a public
GitHub raw-data URL in their code, so those cells require an internet
connection.

### `50_Startups.csv`

Contains 50 records and five columns:

-   `R&D Spend`
-   `Administration`
-   `Marketing Spend`
-   `State`
-   `Profit`

Used by `Step-By-Step.ipynb` for a small regression-based imputation
demonstration.

------------------------------------------------------------------------

## 🧰 Tools and Libraries

  -----------------------------------------------------------------------
  Tool / Library                      Purpose
  ----------------------------------- -----------------------------------
  Python                              Programming language

  Jupyter Notebook                    Interactive experimentation

  Pandas                              Data loading and manipulation

  NumPy                               Numerical operations

  Matplotlib                          Data visualization

  Seaborn                             Statistical visualization

  SciPy                               Statistical tests

  Missingno                           Missing-data visualization

  Scikit-learn                        Imputation, preprocessing,
                                      pipelines, and model evaluation
  -----------------------------------------------------------------------

Scikit-learn components used across the notebooks include:

-   `SimpleImputer`
-   `KNNImputer`
-   `IterativeImputer`
-   `MissingIndicator`
-   `ColumnTransformer`
-   `Pipeline`
-   `OneHotEncoder`
-   `StandardScaler`
-   `GridSearchCV`
-   `LinearRegression`
-   `BayesianRidge`
-   `RandomForestRegressor`
-   `ExtraTreesRegressor`
-   `RandomForestClassifier`
-   `LogisticRegression`

`IterativeImputer` is experimental in Scikit-learn and requires enabling
its experimental API before importing it:

``` python
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
```

------------------------------------------------------------------------

## 🚀 Setup and Run

Run the commands below from the repository root.

### 1. Activate the virtual environment

Windows PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

If you do not already have an environment, create one first:

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

``` powershell
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib seaborn scipy missingno scikit-learn jupyter openpyxl
```

### 3. Launch Jupyter Notebook

``` powershell
jupyter notebook
```

Open the `Handling Missing Values` directory and run the notebooks from
top to bottom.

Some notebooks retrieve Titanic data from GitHub URLs and therefore
require internet access. The local `train (1).xls` and `50_Startups.csv`
files should remain in the same folder as the notebooks unless their
paths are updated in the code.

### Recommended learning order

1.  `Handling-Missing-Values.ipynb` --- understand missingness and
    foundational techniques.
2.  `Step-By-Step.ipynb` --- understand manual regression-based
    estimation.
3.  `KNN-Imputer.ipynb` --- explore neighbor-based imputation.
4.  `Iterative-Imputer.ipynb` --- explore model-based iterative
    imputation and compare methods.
5.  `automatically_select_imputer_parameters.ipynb` --- study automated
    preprocessing and parameter selection.

------------------------------------------------------------------------

## 🎯 Learning Outcomes

Through these notebooks, I practiced:

-   Detecting and quantifying missing values.
-   Visualizing missing-data patterns.
-   Exploring possible relationships between missingness and other
    variables.
-   Applying complete-case analysis and understanding its limitations.
-   Creating missingness indicators.
-   Applying mean, median, most-frequent, and constant-value imputation.
-   Estimating missing values with Linear Regression.
-   Applying KNN-based imputation.
-   Using Scikit-learn's `IterativeImputer` with different estimators.
-   Comparing imputation strategies using downstream classification
    models.
-   Building preprocessing workflows with `ColumnTransformer` and
    `Pipeline`.
-   Using cross-validation and `GridSearchCV` to compare preprocessing
    configurations.
-   Understanding why preprocessing must be fitted on training data and
    then applied to test data.

------------------------------------------------------------------------

## ⚠️ Practical Notes

-   **Avoid data leakage:** Fit imputers, scalers, encoders, and other
    data-dependent transformations on training data only. Apply the
    fitted transformations to validation and test data.
-   **Do not choose an imputer by habit:** Consider feature
    distributions, relationships among variables, missingness patterns,
    computational cost, and downstream model performance.
-   **Deletion has a cost:** Complete-case analysis can reduce the
    sample size and change the distributions of the retained data.
-   **Missingness mechanisms require investigation:** A method such as
    mean, KNN, or iterative imputation does not by itself prove whether
    data are MCAR, MAR, or MNAR.
-   **Evaluate fairly:** Compare methods using the same splits or
    cross-validation strategy. A single accuracy score is not enough to
    establish general superiority.
-   **Inspect notebook execution:** The README describes the code and
    workflow; it does not claim that every notebook has been executed
    successfully in the current environment.
-   **Check dependency compatibility:** Scikit-learn APIs and serialized
    objects can behave differently across versions. Use a consistent
    environment when reproducing notebook results.

------------------------------------------------------------------------

## 👨‍💻 Author

**Hemant Narute**\
Aspiring Data Analyst \| Data Science and Machine Learning Enthusiast

GitHub: [hemant7102](https://github.com/hemant7102)

------------------------------------------------------------------------

This module is part of my ongoing Data Science learning journey,
documenting practical work with data preprocessing, missing-value
analysis, and machine-learning workflows.
