# Exploratory Data Analysis (EDA)

This folder contains my **Exploratory Data Analysis (EDA)** work using Python, Pandas, Matplotlib, and Seaborn.

The notebooks focus on understanding datasets before machine learning or further analysis by performing data inspection, cleaning, visualization, missing-value analysis, outlier detection, bivariate analysis, and feature engineering.

---

## 📂 Folder Contents

```text
EDA/
│
├── README.md
│
├── car_data.xlsx
├── car_EDA.ipynb
│
├── EDA-Titanic-dataset.ipynb
├── titanic_dataset.ipynb
├── train.csv
└── test.csv
```

> **Note:** The Titanic notebooks cover similar EDA concepts. They are kept separately because they represent different working versions/practice notebooks.

---

# 📊 Projects

## 1. Car Dataset EDA

### Notebook
`car_EDA.ipynb`

### Dataset
`car_data.xlsx`

The car dataset contains **1,610 records and 17 columns** covering vehicle information such as:

- Make
- Model
- Year
- Trim
- MSRP
- Invoice Price
- Used/New Price
- Body Size
- Body Style
- Cylinders
- Engine Aspiration
- Drivetrain
- Transmission
- Horsepower
- Torque
- Highway Fuel Economy

### Work Performed

#### Data Loading & Inspection

- Loaded Excel data using Pandas
- Checked dataset shape
- Inspected columns and data types
- Used `head()`, `info()`, and `describe()`
- Checked missing values

#### Data Cleaning

- Standardized column names
- Removed spaces and special characters from column names
- Converted price-related columns from string/object values to numeric values
- Removed duplicate records

#### Missing Value Handling

Missing values were analyzed and handled using approaches based on the available vehicle attributes.

Examples include:

- Invoice price estimation using the relationship between MSRP and invoice price
- Cylinder imputation using grouped mode
- Horsepower and torque imputation using grouped medians
- Highway fuel economy imputation using grouped medians

#### Outlier Analysis

The notebook uses:

- Box plots
- Histograms
- IQR-based outlier detection

The IQR method is applied to numerical columns such as:

- Invoice Price
- Horsepower
- Torque
- Highway Fuel Economy

---

# 🚢 2. Titanic Dataset EDA

### Notebooks

- `EDA-Titanic-dataset.ipynb`
- `titanic_dataset.ipynb`

### Dataset

- `train.csv`
- `test.csv`

The Titanic analysis explores passenger information and survival patterns.

The training dataset contains **891 records and 12 columns**, while the test dataset contains **418 records and 11 columns**.

### Main Columns

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

---

## 🔎 Titanic EDA Workflow

### 1. Numerical Analysis

The notebooks analyze numerical variables such as:

- `Age`
- `Fare`

Techniques include:

- Descriptive statistics
- Histograms
- KDE plots
- Box plots
- Skewness analysis
- Outlier investigation
- Missing-value analysis

---

### 2. Categorical Analysis

Categorical variables analyzed include:

- `Survived`
- `Pclass`
- `Sex`
- `SibSp`
- `Parch`
- `Embarked`

Visualizations include:

- Bar charts
- Pie charts
- Frequency analysis

---

### 3. Bivariate Analysis

Relationships between variables are explored using cross-tabulation and heatmaps.

Examples:

- Survival vs Pclass
- Survival vs Sex
- Survival vs Embarked
- Sex vs Embarked
- Pclass vs Embarked
- Survival vs Age

Percentage-based cross-tabulations are also used to compare groups.

---

# 🛠️ Feature Engineering

The Titanic analysis also demonstrates feature engineering techniques.

### Individual Fare

A passenger-level fare feature is created using:

```python
individual_fare = Fare / (SibSp + Parch + 1)
```

This attempts to estimate the fare paid by an individual passenger rather than using only the shared ticket fare.

---

### Family Size

A `family_size` feature is created:

```python
family_size = SibSp + Parch + 1
```

The `+1` represents the passenger themselves.

---

### Family Type

Passengers are grouped into:

- `alone`
- `small`
- `large`

based on family size.

---

### Surname Extraction

The surname is extracted from the passenger's name to investigate family-level patterns.

---

### Title Extraction

Passenger titles are extracted from the `Name` column.

Examples include:

- Mr.
- Miss.
- Mrs.
- Master
- Other titles

Several less-common titles are grouped into an `other` category.

---

### Cabin / Deck Analysis

Missing cabin information is examined and a deck feature is created from the first character of the cabin value.

This allows analysis of:

- Deck distribution
- Passenger class vs deck
- Survival rate vs deck

---

# 📈 Visualization Techniques

The notebooks use multiple visualization techniques:

| Visualization | Purpose |
|---|---|
| Histogram | Understand numerical distributions |
| KDE Plot | Analyze distribution shape |
| Box Plot | Detect outliers and spread |
| Bar Chart | Compare categorical frequencies |
| Pie Chart | Show category proportions |
| Heatmap | Visualize relationships between categories |
| Stacked Bar Chart | Compare survival proportions |
| Cross-tabulation | Analyze categorical relationships |

---

# 🧰 Technologies & Libraries

### Programming Language

- Python

### Libraries

```text
Pandas
NumPy
Matplotlib
Seaborn
OpenPyXL
Jupyter Notebook
```

---

# 🔄 General EDA Workflow

The approach followed in these projects is:

```text
Load Dataset
     ↓
Understand Dataset
     ↓
Inspect Shape & Columns
     ↓
Check Data Types
     ↓
Check Missing Values
     ↓
Descriptive Statistics
     ↓
Univariate Analysis
     ↓
Bivariate Analysis
     ↓
Outlier Detection
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Visualization
     ↓
Extract Patterns & Insights
```

---

# 🎯 What I Practiced

Through these notebooks, I practiced:

- Loading CSV and Excel datasets
- Data inspection with Pandas
- Data cleaning
- Column name standardization
- Data type conversion
- Missing-value analysis
- Missing-value imputation
- Duplicate removal
- Descriptive statistics
- Univariate analysis
- Bivariate analysis
- Categorical analysis
- Numerical analysis
- Distribution analysis
- Skewness analysis
- Outlier detection using IQR
- Data visualization
- Cross-tabulation
- Feature engineering
- Group-based transformations
- Basic statistical reasoning

---

# 🚀 How to Run

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

## 2. Navigate to the EDA Directory

```bash
cd "Data Science/EDA"
```

## 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

## 4. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn openpyxl jupyter
```

## 5. Start Jupyter Notebook

```bash
jupyter notebook
```

Open any notebook from the EDA folder.

---

# 📌 Important Notes

The notebooks are primarily **learning and practice projects focused on EDA**.

They are not intended to represent production-ready machine learning pipelines.

The main objective is to demonstrate the process of:

> **Understanding → Cleaning → Exploring → Visualizing → Transforming → Extracting Insights**

---

# 👨‍💻 Author

### Hemant Narute

Aspiring **Data Analyst | Data Scientist**

Interested in:

- Data Analytics
- Data Science
- Machine Learning
- Generative AI
- MLOps

---

## ⭐ If You Find This Repository Useful

Feel free to explore the notebooks and datasets to understand the complete EDA workflow.
