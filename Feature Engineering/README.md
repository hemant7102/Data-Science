# Feature Engineering with Scikit-learn

This folder contains hands-on Jupyter notebooks covering feature
engineering and preprocessing with **Python and Scikit-learn**. The
material explores numerical transformations, categorical encoding,
numerical binning (discretization), custom estimators and transformers,
and reusable preprocessing workflows built with `ColumnTransformer` and
`Pipeline`.

The examples use car, customer, and Titanic data, along with generated
datasets and datasets loaded within the notebooks.

------------------------------------------------------------------------

## 📂 Folder Structure

``` text
Feature Engineering/
│
├── README.md
├── cars.csv
├── customer.csv
├── train.csv
├── pipe.pkl
│
├── SKlearn-Deep-Dive.ipynb
├── SKlearn-Columntransformer-Pipeline.ipynb
├── Encoding-Categoricl-Variables.ipynb
├── Binning.ipynb
├── Num-To-Cateorical-Using-Binning.ipynb
├── Basic-Transformation.ipynb
└── Feature-Transformer.ipynb
```

> Keep notebook filenames exactly as they exist in the repository,
> including the current spelling of
> `Encoding-Categoricl-Variables.ipynb` and
> `Num-To-Cateorical-Using-Binning.ipynb`.

------------------------------------------------------------------------

# 📘 Notebooks

## 1. `SKlearn-Deep-Dive.ipynb`

Explores Scikit-learn’s estimator and transformer APIs, including:

- **Custom Estimators** — creating a classifier by extending
  `BaseEstimator` and `ClassifierMixin`.
- **Scoring** — implementing a custom `score()` method and evaluating
  with cross-validation.
- **Transformers and Pipelines** — combining preprocessing and model
  steps.
- **FunctionTransformer** — wrapping a Python function as a transformer.
- **Custom Transformers** — building transformers with `BaseEstimator`
  and `TransformerMixin`; the notebook demonstrates a median/IQR-based
  scaler.
- **ColumnTransformer** — applying different transformations to selected
  columns.
- **FeatureUnion** — combining outputs from multiple feature
  transformations.
- **Combined preprocessing workflow** — joining imputation, encoding,
  text processing, feature extraction/selection, and a model in a
  pipeline.

## 2. `SKlearn-Columntransformer-Pipeline.ipynb`

Demonstrates manual preprocessing and then a more maintainable
Scikit-learn workflow.

Topics include:

1.  Train-test splitting
2.  Ordinal encoding
3.  One-hot encoding
4.  `ColumnTransformer` for column-specific transformations
5.  Inspecting transformer metadata and output feature names
6.  Missing-value imputation with `SimpleImputer`
7.  Feature scaling with `MinMaxScaler`
8.  Feature selection with `SelectKBest` and chi-squared scoring
9.  Model training with tree-based regressors
10. Building a sequential `Pipeline`
11. Cross-validation
12. Hyperparameter tuning
13. Exporting the fitted pipeline

## 3. `Encoding-Categoricl-Variables.ipynb`

Covers techniques for converting categorical variables into numerical
representations.

Topics include:

- **Ordinal Encoding** — encoding categories with an explicit order;
  also explores unknown and infrequent categories and missing-value
  handling.
- **Label Encoding** — encoding target labels.
- **One-Hot Encoding** — creating binary indicator columns for input
  categories.
- **One-Hot Encoder options** — dropping a category, handling unknown
  categories, and controlling infrequent or maximum categories.
- **Label Binarizer** — converting labels into binary representations.
- **MultiLabelBinarizer** — representing multiple labels.
- **Count / Frequency Encoding** — representing categories using their
  counts or frequencies.
- **ColumnTransformer integration** — applying encoding and imputation
  to selected columns.

The notebook uses `customer.csv` and `cars.csv`, and also creates
example data for some encoding demonstrations.

## 4. `Binning.ipynb`

Explores **binning**, also known as discretization: converting
continuous numerical values into intervals or groups.

Methods covered:

- **Custom Binning** — defining bin boundaries and labels with
  `pandas.cut()`.
- **Uniform Binning** — dividing a numerical range into bins of equal
  width using `KBinsDiscretizer`.
- **Quantile Binning** — creating bins based on quantiles.
- **K-Means Binning** — using clustering to determine bin boundaries.
- **Binarization** — converting numerical values into binary values
  based on a threshold.
- **Decision Tree Binning** — using a decision tree to identify useful
  splits.

The notebook also investigates bin edges, visualizes distributions, and
explores how outliers and the number of bins can affect discretization.

## 5. `Num-To-Cateorical-Using-Binning.ipynb`

Explores why and how numerical features can be converted into
categorical or discrete features through binning.

The notebook investigates these use cases:

1.  **Reducing Overfitting** — testing discretization as a way to
    simplify a model’s representation of numerical inputs.
2.  **Handling Non-Linear Relationships** — using binned features in
    regression and classification examples.
3.  **Handling Outliers** — examining discretization in the presence of
    extreme values.
4.  **Better Interpretability** — grouping numerical values into
    understandable intervals.
5.  **Model Compatibility** — comparing model behavior with discretized
    features, including experiments using the Wine Quality dataset.

The notebook uses generated regression/classification data and loads the
Wine Quality dataset in one experiment.

## 6. `Basic-Transformation.ipynb`

Covers basic numerical feature transformations and their use in
preprocessing workflows.

Topics include:

- Handling missing values.
- Applying log transformation.
- Using `FunctionTransformer` to apply custom transformations.
- Applying column-specific preprocessing with `ColumnTransformer`.
- Inspecting feature distributions with histograms and Q-Q plots.
- Comparing Logistic Regression and Decision Tree models.
- Evaluating model performance with cross-validation.

## 7. `Feature-Transformer.ipynb`

Explores common mathematical transformations and Scikit-learn tools for
transforming numerical features.

Topics include:

- Polynomial feature generation.
- Logarithmic, square-root, reciprocal, and square transformations.
- Using `FunctionTransformer` for custom transformations.
- Box-Cox and Yeo-Johnson power transformations.
- Evaluating regression performance using R² and mean squared error
  (MSE).

------------------------------------------------------------------------

# 🧰 Tools & Libraries

### Programming and analysis

- Python
- Pandas
- NumPy
- Jupyter Notebook

### Machine learning and preprocessing

- Scikit-learn
- SciPy
- `category_encoders` (used for count/frequency encoding examples)

### Visualization

- Matplotlib
- Seaborn

Key Scikit-learn components used across the notebooks include:

``` python
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
LabelEncoder
LabelBinarizer
MultiLabelBinarizer
KBinsDiscretizer
Binarizer
StandardScaler
MinMaxScaler
SelectKBest
cross_val_score
```

------------------------------------------------------------------------

# 📊 Datasets and Model Artifact

| File           | Purpose                                                                        |
|----------------|--------------------------------------------------------------------------------|
| `cars.csv`     | Car data used in categorical encoding and preprocessing examples               |
| `customer.csv` | Customer data used in encoding and transformation examples                     |
| `train.csv`    | Titanic training dataset used for numerical-to-categorical/binning experiments |
| `pipe.pkl`     | Serialized Scikit-learn pipeline exported from the pipeline notebook           |

Some notebooks also generate sample datasets or load datasets directly
from external URLs.

**About `pipe.pkl`:** This is a Python pickle artifact. Load it only
from a trusted source. Pickled Scikit-learn objects may depend on the
Scikit-learn and Python versions used when they were created, so a
compatible environment may be required.

------------------------------------------------------------------------

# 🔄 Typical Feature Engineering Workflow

The preprocessing and modeling notebooks demonstrate workflows such as:

``` text
Raw Dataset
    ↓
Train-Test Split
    ↓
Missing Value Imputation
    ↓
Categorical Encoding
    ↓
Numerical Transformation / Binning
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

Not every notebook uses every step. The sequence above summarizes the
techniques explored across this folder.

A key benefit of a Scikit-learn `Pipeline` is that preprocessing steps
and the estimator can be kept together, helping apply transformations
consistently during training and prediction. Fit data-dependent
preprocessing steps on the training data, then use the fitted
transformations on validation or test data to avoid data leakage.

------------------------------------------------------------------------

# ⚙️ Setup & Run

Run these commands from the repository root.

## 1. Create and activate a virtual environment (optional)

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2. Install dependencies

``` powershell
pip install numpy pandas scikit-learn scipy matplotlib seaborn jupyter category-encoders
```

## 3. Start Jupyter Notebook

``` powershell
jupyter notebook
```

Open a notebook from the `Feature Engineering` folder.

> If you load `pipe.pkl`, use versions compatible with the environment
> in which the artifact was created. The notebooks do not provide a
> pinned dependency file.

------------------------------------------------------------------------

# 🎯 Learning Outcomes

Through these notebooks, I practiced:

- Understanding Scikit-learn’s estimator and transformer interfaces.
- Creating custom estimators and transformers.
- Applying function-based and mathematical transformations.
- Generating polynomial features.
- Exploring Box-Cox and Yeo-Johnson transformations.
- Encoding categorical features with ordinal, label, one-hot, and
  binarization techniques.
- Exploring count/frequency encoding.
- Handling unknown, infrequent, and missing categories.
- Converting continuous numerical features into bins.
- Comparing custom, uniform, quantile, K-Means, and decision-tree
  binning approaches.
- Investigating the effect of outliers and bin counts.
- Imputing missing values and scaling numerical features.
- Selecting useful features.
- Applying different transformations to different columns.
- Combining transformations with `FeatureUnion`.
- Building end-to-end preprocessing and modeling pipelines.
- Using cross-validation and hyperparameter tuning.
- Saving a fitted pipeline for reuse.

------------------------------------------------------------------------

# 👨‍💻 Author

**Hemant Narute**  
Aspiring Data Analyst \| Data Scientist

Interests: Data Analytics, Data Science, Machine Learning, and MLOps.

------------------------------------------------------------------------

*This folder is a learning resource documenting practical feature
engineering and Scikit-learn preprocessing workflows.*
