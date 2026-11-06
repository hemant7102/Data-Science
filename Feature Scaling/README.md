# Feature Scaling

This folder contains hands-on Jupyter Notebook exercises covering
feature scaling and normalization techniques using **Python, Pandas,
NumPy, and Scikit-learn**.

The notebooks explore how scaling changes the range and distribution of
numerical features, how different scalers respond to outliers, and why
scaling can affect some machine-learning algorithms more than others.

------------------------------------------------------------------------

## 📂 Folder Structure

``` text
Feature Scaling/
│
├── README.md
├── Scaling-Techin.ipynb
└── Standardization.ipynb
```

> Keep the notebook filename `Scaling-Techin.ipynb` exactly as it exists
> in the repository.

------------------------------------------------------------------------

# 📘 Notebooks

## 1. `Standardization.ipynb`

Explores standardization using Scikit-learn’s `StandardScaler`.

Topics include:

- **Train-Test Split** — splitting the dataset into training and testing
  sets before scaling.
- **Standard Scaling** — fitting `StandardScaler` on the training data
  and transforming both training and test data.
- **Scaler Statistics** — inspecting the mean learned by the scaler and
  comparing feature summaries before and after scaling.
- **Visual Comparison** — comparing scatter plots and feature
  distributions before and after standardization.
- **Effect on Models** — comparing Logistic Regression and Decision Tree
  performance on original and scaled features using accuracy.
- **Outlier Exploration** — examining the dataset after adding extreme
  values.

The notebook uses the Social Network Ads dataset loaded from a GitHub
raw CSV URL. It works with the `Age` and `EstimatedSalary` features and
predicts `Purchased`.

## 2. `Scaling-Techin.ipynb`

Explores several feature scaling and normalization techniques.

Topics include:

- **Min-Max Scaling / Min-Max Normalization** — using `MinMaxScaler` to
  rescale features to a fixed range.
- **Train-Test Split** — fitting the scaler on training data and
  transforming the test data.
- **Distribution Comparison** — inspecting feature summaries, scatter
  plots, and distributions before and after scaling.
- **Robust Scaling** — using `RobustScaler` and comparing its behavior
  with standard and min-max scaling on data containing an outlier.
- **Max-Abs Scaling** — using `MaxAbsScaler` and examining its behavior
  with generated data and an added outlier.
- **L1 and L2 Normalization** — applying row-wise normalization with
  Scikit-learn’s `normalize` function and visualizing the results.
- **Dataset Experiments** — applying scaling techniques to examples
  using the Wine dataset, California Housing dataset, and Boston Housing
  data source.

------------------------------------------------------------------------

# 🧰 Tools & Libraries

### Programming and analysis

- Python
- NumPy
- Pandas
- Jupyter Notebook

### Feature scaling and machine learning

- Scikit-learn

### Visualization

- Matplotlib
- Seaborn

Key Scikit-learn components used in the notebooks include:

``` python
StandardScaler
MinMaxScaler
RobustScaler
MaxAbsScaler
normalize
train_test_split
LogisticRegression
DecisionTreeClassifier
accuracy_score
fetch_california_housing
```

------------------------------------------------------------------------

# 📊 Datasets and Data Sources

The notebooks load or generate their data within the notebook code; no
separate local CSV file is listed as a required companion file.

| Dataset / Data Source      | Use                                                                     |
|----------------------------|-------------------------------------------------------------------------|
| Social Network Ads         | Standardization example using `Age`, `EstimatedSalary`, and `Purchased` |
| Wine dataset               | Min-Max scaling and distribution comparison                             |
| Generated numerical arrays | Demonstrations of RobustScaler, MaxAbsScaler, and L1/L2 normalization   |
| California Housing         | Scaling experiment using Scikit-learn’s dataset loader                  |
| Boston Housing CSV source  | Robust scaling example loaded from a CSV URL                            |

Some notebook cells retrieve datasets from external URLs or Scikit-learn
dataset loaders. An internet connection may therefore be required when
running those cells for the first time.

------------------------------------------------------------------------

# 🔄 Feature Scaling Workflow

The notebooks demonstrate a workflow similar to:

``` text
Raw Numerical Features
        ↓
Train-Test Split
        ↓
Fit Scaler on Training Data
        ↓
Transform Training Data
        ↓
Transform Test Data Using the Same Scaler
        ↓
Compare Feature Distributions
        ↓
Train and Evaluate Model
```

**Important:** Fit the scaler using only the training data. Do not fit
it separately on the test data, because that can cause data leakage.
Reuse the scaler fitted on the training data to transform validation and
test data.

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
pip install numpy pandas scikit-learn matplotlib seaborn jupyter
```

## 3. Start Jupyter Notebook

``` powershell
jupyter notebook
```

Open either notebook from the `Feature Scaling` folder and run its cells
in order.

------------------------------------------------------------------------

# 🎯 Learning Outcomes

Through these notebooks, I practiced:

- Understanding why numerical features may need scaling.
- Applying standardization with `StandardScaler`.
- Applying min-max scaling with `MinMaxScaler`.
- Understanding robust scaling and its use with outliers.
- Applying maximum-absolute scaling with `MaxAbsScaler`.
- Performing L1 and L2 normalization.
- Comparing feature distributions before and after scaling.
- Fitting scalers on training data and reusing them on test data.
- Observing how scaling can affect Logistic Regression.
- Comparing model results before and after scaling.
- Exploring scaling behavior with real and generated datasets.

------------------------------------------------------------------------

# 👨‍💻 Author

**Hemant Narute**  
Aspiring Data Analyst \| Data Scientist

Interests: Data Analytics, Data Science, Machine Learning, and MLOps.

------------------------------------------------------------------------

*This folder is a learning resource documenting practical feature
scaling and normalization techniques.*
