# Handling Missing Values

This module contains practical Jupyter notebooks exploring how to identify, visualize, analyze, and handle missing data using Python, Pandas, and Scikit-learn.

The exercises cover missing-value patterns, deletion methods, statistical imputation, regression-based imputation, K-Nearest Neighbors (KNN) imputation, missingness indicators, and preprocessing pipelines.

---

## 📂 Repository Contents

```text
Handling Missing Values/
│
├── README.md
├── Handling-Missing-Values.ipynb
├── automatically_select_imputer_parameters.ipynb
├── KNN-Imputer.ipynb
├── Step-By-Step.ipynb
├── 50_Startups.csv
└── train (1).xls
```

| File | Description |
|---|---|
| `Handling-Missing-Values.ipynb` | Explores missing-value detection, visualization, missingness mechanisms, complete-case analysis, missing indicators, and numerical imputation. |
| `automatically_select_imputer_parameters.ipynb` | Builds a preprocessing and classification pipeline, then uses `GridSearchCV` to compare imputation strategies and classifier parameters. |
| `KNN-Imputer.ipynb` | Applies `KNNImputer` to Titanic features and compares its Logistic Regression accuracy with mean imputation using `SimpleImputer`. |
| `Step-By-Step.ipynb` | Demonstrates manual regression-based imputation on a small sample from the 50 Startups dataset, including repeated estimation of missing feature values. |
| `50_Startups.csv` | 50 Startups dataset used by `Step-By-Step.ipynb`. |
| `train (1).xls` | Titanic training data used by `automatically_select_imputer_parameters.ipynb`. The file content is CSV-formatted despite its `.xls` extension; the notebook reads it with `pandas.read_csv()`. |

---

## 📘 Notebook 1: Handling-Missing-Values.ipynb

This notebook covers the following concepts.

### 1. Detecting Missing Values

- Count missing values in each column using `isnull().sum()`.
- Calculate the percentage of missing values per column.
- Calculate the total number of missing values.
- Identify rows containing missing values.

### 2. Visualizing Missing Data

Uses the `missingno` library to visualize missing-value patterns with:

- Bar plot
- Matrix plot
- Heatmap
- Dendrogram

The notebook also loads example datasets from public GitHub raw-data URLs for missing-value exploration.

### 3. Exploring Missingness Patterns

Uses generated sample data to explore missingness and compare observations with and without missing values.

The notebook includes:

- Comparing feature means between groups.
- A two-sample t-test using SciPy.
- Visualizing missingness with a matrix plot.
- A simulated example where the probability of a value being missing depends on another feature.
- A Logistic Regression model to examine whether other variables predict the missingness indicator.
- Comparing feature distributions across groups.

These are practical demonstrations for investigating missingness patterns; they do not, by themselves, prove the true missingness mechanism of an arbitrary real-world dataset.

### 4. Listwise Deletion / Complete Case Analysis (CCA)

- Remove rows containing missing values with `dropna()`.
- Measure how many observations remain after deletion.
- Compare distributions before and after deletion using histograms and density plots.
- Compare categorical proportions before and after deletion.

### 5. Missing Indicators

- Create indicators for missing values using `MissingIndicator`.
- Combine missing indicators and imputation using `ColumnTransformer`.
- Train and evaluate a Logistic Regression model on the transformed data.

### 6. Mean and Median Imputation

- Calculate mean and median values from the training data.
- Fill missing numerical values with mean and median.
- Compare variance before and after imputation.
- Compare distributions using KDE plots.
- Inspect correlations and box plots.

### 7. Imputation with Scikit-learn

- Use `SimpleImputer` with different strategies.
- Apply separate imputers to selected columns through `ColumnTransformer`.
- Fit transformations on training data and apply them to test data.

**Main libraries used:** Pandas, NumPy, Matplotlib, Seaborn, SciPy, Missingno, and Scikit-learn.

---

## 📘 Notebook 2: automatically_select_imputer_parameters.ipynb

This notebook demonstrates how to build a preprocessing pipeline and automatically select imputation and model parameters using cross-validation.

### Workflow

1. Load the Titanic training dataset.
2. Remove columns that are not used in the model: `PassengerId`, `Name`, `Ticket`, and `Cabin`.
3. Separate the input features and target (`Survived`).
4. Split the data into training and testing sets.
5. Define separate numerical and categorical preprocessing pipelines.
6. Combine the transformations with `ColumnTransformer`.
7. Build a complete Scikit-learn pipeline with Logistic Regression.
8. Use `GridSearchCV` to search over preprocessing and classifier parameters.
9. Review the best parameters, cross-validation score, and candidate results.

### Preprocessing Design

| Feature type | Columns | Pipeline steps |
|---|---|---|
| Numerical | `Age`, `Fare` | `SimpleImputer` followed by `StandardScaler` |
| Categorical | `Embarked`, `Sex` | `SimpleImputer` followed by `OneHotEncoder(handle_unknown='ignore')` |

### Grid Search Parameters

| Parameter | Values tested |
|---|---|
| Numerical imputation strategy | `mean`, `median` |
| Categorical imputation strategy | `most_frequent`, `constant` |
| Logistic Regression `C` | `0.1`, `1.0`, `10`, `100` |
| Cross-validation | 10 folds |

The notebook displays the best parameter combination, the best internal cross-validation score, and a sorted view of the candidate results.

**Important:** The notebook reports a cross-validation score from the training data. It does not show a final held-out test-set evaluation in the inspected cells, so do not interpret the cross-validation score as test accuracy.

---

## 📘 Notebook 3: KNN-Imputer.ipynb

This notebook applies K-Nearest Neighbors imputation to missing values in selected Titanic dataset features and compares it with mean imputation.

### Dataset and Features

The notebook loads the Titanic dataset from a public GitHub raw-data URL and selects:

- `Age`
- `Pclass`
- `Fare`
- `Survived`

The target variable is `Survived`. The input features are `Age`, `Pclass`, and `Fare`.

### Workflow

1. Load the Titanic data and inspect missing values.
2. Separate input features (`X`) and target (`y`).
3. Split the data into training and testing sets using `test_size=0.2` and `random_state=2`.
4. Create a `KNNImputer` with `n_neighbors=3`.
5. Fit the imputer on training features and transform both training and testing features.
6. Train a Logistic Regression model using the KNN-imputed features.
7. Predict on the test set and calculate accuracy.
8. Repeat the preprocessing and model evaluation using the default `SimpleImputer` strategy (mean imputation).
9. Compare the two accuracy scores.

### Key Concepts

- KNN-based imputation
- Distance-based estimation of missing values
- Train/test split
- Fitting an imputer on training data only
- Transforming test data without refitting
- Comparing KNN imputation with mean imputation
- Evaluating a classification model with `accuracy_score`

**Important:** The notebook compares model accuracy for two imputation approaches. The result is specific to this dataset, feature selection, split, and model; it does not establish that one imputation method is always better.

---

## 📘 Notebook 4: Step-By-Step.ipynb

This notebook demonstrates a step-by-step, regression-based approach to estimating missing numerical values using the 50 Startups dataset.

### Dataset and Features

The notebook reads `50_Startups.csv` and selects the following numerical columns:

- `R&D Spend`
- `Administration`
- `Marketing Spend`
- `Profit`

It scales the selected values by dividing by `10,000`, rounds them, and samples five rows using a fixed random seed.

### Workflow

1. Load and prepare a five-row sample from the 50 Startups dataset.
2. Select the three spending features and introduce missing values for demonstration.
3. Initially fill missing values with each column's mean.
4. Reintroduce a missing value in one feature.
5. Train a `LinearRegression` model using the other available features and rows.
6. Predict the missing value and insert the estimate.
7. Repeat the process for other features.
8. Compare successive imputation estimates and iterations.

### Key Concepts

- Mean imputation as an initial estimate
- Predicting missing numerical values with Linear Regression
- Using other features to estimate a missing feature
- Repeated or iterative regression-based imputation
- Comparing imputed values across iterations

**Important:** This notebook manually demonstrates regression-based iterative estimation on a small sample. It is not an implementation of Scikit-learn's `IterativeImputer` class. The small sample is intended for learning the process, not for drawing conclusions about model performance.

---

## 🗃️ Datasets

### 1. Titanic Training Dataset — `train (1).xls`

The local file contains 891 rows and 12 columns, including:

- `PassengerId`
- `Survived`
- `Pclass`
- `Name`
- `Sex`
- `Age`
- `SibSp`
- `Parch`
- `Ticket`
- `Fare`
- `Cabin`
- `Embarked`

The automatic imputer-selection notebook loads it using:

```python
df = pd.read_csv("train (1).xls")
```

The file is CSV-formatted despite its `.xls` extension. Keep the filename consistent with the notebook. A cleaner alternative is to rename it to `train.csv` and update the notebook to use:

```python
df = pd.read_csv("train.csv")
```

Do not simply change the extension without confirming the file format.

The KNN notebook downloads a Titanic dataset from a public GitHub raw-data URL rather than reading this local file. An internet connection is required for that cell.

### 2. 50 Startups Dataset — `50_Startups.csv`

This dataset contains 50 rows and five columns:

- `R&D Spend`
- `Administration`
- `Marketing Spend`
- `State`
- `Profit`

The `Step-By-Step.ipynb` notebook uses the three spending columns and demonstrates regression-based imputation. The `Profit` and `State` columns are not used in the notebook's selected sample.

---

## 🛠️ Technologies and Libraries

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- Missingno
- Scikit-learn

Install the main dependencies with:

```bash
python -m pip install numpy pandas matplotlib seaborn scipy missingno scikit-learn jupyter openpyxl
```

---

## 🚀 Getting Started

Run these commands from the root of the repository.

### 1. Activate your virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install numpy pandas matplotlib seaborn scipy missingno scikit-learn jupyter openpyxl
```

### 3. Launch Jupyter Notebook

```powershell
jupyter notebook
```

### 4. Recommended learning order

1. Start with `Handling-Missing-Values.ipynb` for missing-value detection, analysis, and basic imputation.
2. Continue with `Step-By-Step.ipynb` to understand manual regression-based estimation.
3. Explore `KNN-Imputer.ipynb` to compare KNN and mean imputation.
4. Finish with `automatically_select_imputer_parameters.ipynb` to study preprocessing pipelines and hyperparameter search.

Run notebooks from top to bottom. Some notebooks download data from external GitHub URLs and therefore require internet access.

---

## 🎯 Learning Outcomes

After working through these notebooks, the topics practiced include:

- Detecting and quantifying missing values.
- Visualizing missing-data patterns.
- Investigating relationships between missingness and other variables.
- Applying complete-case analysis.
- Creating missingness indicators.
- Comparing mean and median imputation.
- Using Scikit-learn imputers.
- Estimating missing numerical values with Linear Regression.
- Applying KNN-based imputation.
- Comparing imputation approaches through model evaluation.
- Applying different transformations to numerical and categorical columns.
- Building preprocessing pipelines with `Pipeline` and `ColumnTransformer`.
- Searching preprocessing and model hyperparameters with `GridSearchCV`.

---

## ⚠️ Notes and Limitations

- Imputation statistics should be learned from the training set only, then applied to validation or test data. The KNN and pipeline examples demonstrate this separation.
- Complete-case analysis can reduce dataset size and change feature distributions or category proportions; inspect these effects before using it.
- The simulated missingness exercises illustrate analysis techniques. They are not proof of a real dataset's missingness mechanism.
- The automatic selection notebook uses a 10-fold cross-validation score for model selection. A separate final evaluation on held-out test data would make the model assessment more complete.
- The KNN notebook compares two imputation strategies under one train/test split. For a robust comparison, consider repeated cross-validation and appropriate preprocessing.
- The regression-based notebook uses only five sampled rows to illustrate the mechanics of iterative estimation. It is a teaching example, not a robust imputation strategy for production data.
- The local Titanic file has a `.xls` filename but CSV content. Its filename and the `read_csv()` call must remain consistent, or both should be updated together.

---

## 👨‍💻 Author

**Hemant Narute**  
Aspiring Data Science and Data Analytics Professional

GitHub: [hemant7102](https://github.com/hemant7102)

---

This module is part of my ongoing Data Science and Machine Learning learning journey.
