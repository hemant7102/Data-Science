# Feature Engineering with Scikit-learn

This folder contains hands-on notebooks exploring **feature engineering and preprocessing with Scikit-learn**. The work covers individual preprocessing techniques as well as combining them into reusable machine-learning workflows using `ColumnTransformer` and `Pipeline`.

The examples use car and customer/review data, along with Scikit-learn's built-in and synthetic datasets.

---

## 📂 Folder Structure

```text
Feature Engineering/
│
├── README.md
├── cars.csv
├── customer.csv
├── pipe.pkl
├── SKlearn-Deep-Dive.ipynb
└── SKlearn-Columntransformer-Pipeline.ipynb
```

## 📘 Notebooks

### 1. `SKlearn-Deep-Dive.ipynb`

Explores Scikit-learn's estimator and transformer APIs, including:

- **Custom Estimators** — creating a classifier by extending `BaseEstimator` and `ClassifierMixin`.
- **Scoring** — implementing a custom `score()` method and evaluating with cross-validation.
- **Transformers and Pipelines** — combining preprocessing and model steps.
- **FunctionTransformer** — wrapping a Python function as a transformer.
- **Custom Transformers** — building a transformer with `BaseEstimator` and `TransformerMixin`; the notebook demonstrates a median/IQR-based scaler.
- **ColumnTransformer** — applying different transformations to selected columns.
- **FeatureUnion** — combining outputs from multiple feature transformations.
- **Combined preprocessing workflow** — joining imputation, encoding, text processing, feature extraction/selection, and a model in a pipeline.

### 2. `SKlearn-Columntransformer-Pipeline.ipynb`

Demonstrates manual preprocessing first, then a more maintainable Scikit-learn approach.

Topics include:

1. Train-test splitting
2. Ordinal encoding
3. One-hot encoding
4. `ColumnTransformer` for column-specific transformations
5. Inspecting transformer metadata and output feature names
6. Missing-value imputation with `SimpleImputer`
7. Feature scaling with `MinMaxScaler`
8. Feature selection with `SelectKBest` and chi-squared scoring
9. Model training with tree-based regressors
10. Building a sequential `Pipeline`
11. Cross-validation
12. Hyperparameter tuning
13. Exporting the fitted pipeline

---

## 🧰 Tools & Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

Key Scikit-learn components used:

```python
BaseEstimator
ClassifierMixin
TransformerMixin
FunctionTransformer
ColumnTransformer
FeatureUnion
Pipeline
SimpleImputer
OrdinalEncoder
OneHotEncoder
StandardScaler
MinMaxScaler
SelectKBest
cross_val_score
```

---

## 📊 Datasets and Model Artifact

| File | Purpose |
|---|---|
| `cars.csv` | Car data used in the ColumnTransformer and pipeline notebook |
| `customer.csv` | Customer/review data used for transformation examples |
| `pipe.pkl` | Serialized Scikit-learn pipeline exported from the notebook |

`pipe.pkl` is a Python pickle artifact. Load it only from a trusted source. Pickled Scikit-learn objects can also depend on the library versions used when they were created; use a compatible environment when loading the file.

---

## 🔄 Typical Preprocessing Pipeline

The ColumnTransformer/Pipeline notebook follows this general sequence:

```text
Raw Dataset
    ↓
Train-Test Split
    ↓
Missing Value Imputation
    ↓
Categorical Encoding
    ↓
Feature Scaling
    ↓
Feature Selection
    ↓
Model Training
    ↓
Cross-Validation
    ↓
Hyperparameter Tuning
    ↓
Export Fitted Pipeline
```

A key benefit of using a Scikit-learn `Pipeline` is that preprocessing steps and the estimator can be kept together, helping apply the same transformations consistently during training and prediction.

---

## ⚙️ Setup & Run

Run these commands from the repository root.

### 1. Create and activate a virtual environment (optional)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install numpy pandas scikit-learn jupyter
```

### 3. Open Jupyter Notebook

```powershell
jupyter notebook
```

Open either notebook from the `Feature Engineering` folder.

> If you load `pipe.pkl`, use a compatible Scikit-learn version. The notebooks do not specify a pinned dependency version, so the environment may need to be adjusted to match the version used to create the artifact.

---

## 🎯 Learning Outcomes

Through these notebooks, I practiced:

- Understanding Scikit-learn's estimator and transformer interfaces
- Creating custom estimators and transformers
- Applying function-based transformations
- Encoding categorical features
- Imputing missing values
- Scaling numerical features
- Selecting useful features
- Applying different transformations to different columns
- Combining transformations with `FeatureUnion`
- Building end-to-end preprocessing and modeling pipelines
- Using cross-validation and hyperparameter tuning
- Saving a fitted pipeline for reuse

---

## 👨‍💻 Author

**Hemant Narute**  
Aspiring Data Analyst | Data Scientist

Interests: Data Analytics, Data Science, Machine Learning, and MLOps.

---

*This folder is a learning resource documenting practical feature-engineering and Scikit-learn preprocessing workflows.*
