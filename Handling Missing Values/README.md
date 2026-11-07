# Handling Missing Values

This module contains practical Jupyter notebooks exploring how to identify, visualize, analyze, and handle missing data using Python, Pandas, and Scikit-learn.

The exercises use Titanic and other example datasets to demonstrate missing-value patterns, deletion methods, imputation strategies, missingness indicators, and preprocessing pipelines.

---

## 📂 Repository Contents

```text
Handling Missing Values/
│
├── README.md
├── Handling-Missing-Values.ipynb
├── automatically_select_imputer_parameters.ipynb
└── train (1).xls
```

| File | Description |
|---|---|
| `Handling-Missing-Values.ipynb` | Explores missing-value detection, visualization, missingness mechanisms, complete-case analysis, missing indicators, and numerical imputation. |
| `automatically_select_imputer_parameters.ipynb` | Builds a preprocessing and classification pipeline, then uses `GridSearchCV` to compare imputation strategies and classifier parameters. |
| `train (1).xls` | Titanic training data used by the automatic imputer-selection notebook. The file content is CSV-formatted despite its `.xls` extension; the notebook reads it with `pandas.read_csv()`. |

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

The notebook also loads an example dataset from a public GitHub raw-data URL for missing-value exploration.

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

The notebook searches over:

| Parameter | Values tested |
|---|---|
| Numerical imputation strategy | `mean`, `median` |
| Categorical imputation strategy | `most_frequent`, `constant` |
| Logistic Regression `C` | `0.1`, `1.0`, `10`, `100` |
| Cross-validation | 10 folds |

The notebook displays the best parameter combination, the best internal cross-validation score, and a sorted view of the candidate results.

**Important:** The notebook reports a cross-validation score from the training data. It does not show a final held-out test-set evaluation in the inspected cells, so do not interpret the cross-validation score as test accuracy.

---

## 🗃️ Dataset

### Titanic Training Dataset

The local file `train (1).xls` contains 891 rows and 12 columns. Its content is CSV-formatted and includes:

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

Because the file is CSV-formatted despite the `.xls` extension, keep the filename consistent with the notebook. A cleaner alternative is to rename it to `train.csv` and update the notebook to use:

```python
df = pd.read_csv("train.csv")
```

Do not simply change the extension without confirming the file format.

The first notebook also loads example datasets directly from public GitHub raw-data URLs, including Titanic and data-science-job examples. An internet connection is required for those cells unless the data is downloaded and the code is changed to use local paths.

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

### 4. Open a notebook

Start with `Handling-Missing-Values.ipynb` to learn detection and imputation concepts, then explore `automatically_select_imputer_parameters.ipynb` for a pipeline and GridSearchCV workflow.

Run the notebooks from top to bottom. Some cells download data from external GitHub URLs and therefore require internet access.

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
- Applying different transformations to numerical and categorical columns.
- Building preprocessing pipelines with `Pipeline` and `ColumnTransformer`.
- Searching preprocessing and model hyperparameters with `GridSearchCV`.

---

## ⚠️ Notes and Limitations

- Imputation statistics should be learned from the training set only, then applied to validation or test data. The pipeline notebook follows this pattern by fitting preprocessing through the training workflow.
- Complete-case analysis can reduce the dataset size and may change feature distributions or category proportions; inspect these effects before using it.
- The simulated missingness exercises illustrate analysis techniques. They are not proof of a real dataset's missingness mechanism.
- The automatic selection notebook uses a 10-fold cross-validation score for model selection. A separate final evaluation on held-out test data would make the model assessment more complete.
- The local Titanic file has a `.xls` filename but CSV content. Its filename and the `read_csv()` call must remain consistent, or both should be updated together.

---

## 👨‍💻 Author

**Hemant Narute**  
Aspiring Data Science and Data Analytics Professional

GitHub: [hemant7102](https://github.com/hemant7102)

---

This module is part of my ongoing Data Science and Machine Learning learning journey.
