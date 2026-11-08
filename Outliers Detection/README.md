# Outliers Detection

This module contains practical Jupyter notebooks focused on **detecting
and handling outliers** in numerical data using Python, Pandas, NumPy,
Matplotlib, and Seaborn.

The notebooks use a student placement dataset to explore distribution
analysis, box plots, the Interquartile Range (IQR), standard-deviation
boundaries, Z-scores, trimming, and capping (winsorization-style
boundary replacement).

------------------------------------------------------------------------

## 📂 Folder Structure

``` text
Outliers Detection/
│
├── Finding-outliers.ipynb
├── Trimming-Capping.ipynb
└── placement.csv
```

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `Finding-outliers.ipynb`            Detects outliers in
                                      `placement_exam_marks` using the
                                      IQR method, then demonstrates
                                      trimming and capping.

  `Trimming-Capping.ipynb`            Examines `cgpa` distributions and
                                      outliers using the
                                      three-standard-deviation rule and
                                      Z-scores, followed by trimming and
                                      capping.

  `placement.csv`                     Student placement dataset used by
                                      both notebooks.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 📘 Notebook Details

### 1. `Finding-outliers.ipynb`

This notebook demonstrates how to identify outliers in
`placement_exam_marks` using the **Interquartile Range (IQR) method**.

**Workflow and concepts:**

1.  Import NumPy, Pandas, Matplotlib, and Seaborn.

2.  Load `placement.csv`.

3.  Visualize the distributions of `cgpa` and `placement_exam_marks`.

4.  Inspect descriptive statistics for `placement_exam_marks`.

5.  Use a box plot to inspect potential outliers.

6.  Calculate the 25th percentile (Q1) and 75th percentile (Q3).

7.  Calculate the IQR:

    `IQR = Q3 - Q1`

8.  Calculate the lower and upper boundaries:

    `Lower boundary = Q1 - 1.5 × IQR`

    `Upper boundary = Q3 + 1.5 × IQR`

9.  Identify observations above the upper boundary and below the lower
    boundary.

10. Apply trimming and compare the original and modified distributions.

11. Apply capping by replacing values outside the IQR boundaries with
    the corresponding boundary values.

12. Compare distributions and box plots before and after capping.

**Important implementation detail:** The trimming cell in this notebook
filters with `placement_exam_marks < upper_limit`. It removes values
above the upper boundary but does not explicitly filter values below the
lower boundary. The capping cell, in contrast, handles both lower- and
upper-bound violations. If you intend symmetric IQR trimming, use both
conditions:

``` python
new_df = df[
    (df["placement_exam_marks"] >= lower_limit) &
    (df["placement_exam_marks"] <= upper_limit)
]
```

### 2. `Trimming-Capping.ipynb`

This notebook focuses on detecting and handling outliers in the `cgpa`
column.

**Part A --- Distribution and three-standard-deviation rule**

-   Inspect the dataset shape and sample records.

-   Visualize the distributions of `cgpa` and `placement_exam_marks`.

-   Calculate the skewness of `placement_exam_marks`.

-   Calculate the mean, standard deviation, minimum, and maximum of
    `cgpa`.

-   Calculate lower and upper boundaries using the
    three-standard-deviation rule:

    `Lower boundary = Mean - 3 × Standard Deviation`

    `Upper boundary = Mean + 3 × Standard Deviation`

-   Identify values outside the boundaries.

-   Trim observations that fall outside the selected CGPA limits.

The notebook uses the values `5.11` and `8.80` in its first trimming
example.

**Part B --- Z-score method**

The notebook calculates a Z-score for each CGPA value:

`Z-score = (Value - Mean) / Standard Deviation`

It then:

-   Identifies observations with Z-scores greater than `+3`.
-   Identifies observations with Z-scores less than `-3`.
-   Identifies observations outside the interval `[-3, +3]`.
-   Creates a trimmed dataset containing observations inside that
    interval.

**Part C --- Capping**

-   Recalculates the three-standard-deviation lower and upper
    boundaries.
-   Uses `np.where()` to replace CGPA values below the lower boundary or
    above the upper boundary with the nearest boundary.
-   Inspects the resulting dataset shape and descriptive statistics.

**Concepts practiced:**

-   Distribution analysis and skewness.
-   Mean and standard deviation.
-   Three-standard-deviation rule.
-   Z-score-based outlier detection.
-   Trimming observations.
-   Capping extreme values.

------------------------------------------------------------------------

## 🗃️ Dataset: `placement.csv`

The dataset contains **1,000 rows and 3 columns**.

  ------------------------------------------------------------------------
  Column                   Data type               Description
  ------------------------ ----------------------- -----------------------
  `cgpa`                   `float64`               Student CGPA values.

  `placement_exam_marks`   `float64`               Student placement
                                                   examination marks.

  `placed`                 `int64`                 Placement outcome
                                                   represented
                                                   numerically.
  ------------------------------------------------------------------------

The notebooks use `cgpa` and `placement_exam_marks` for outlier
exploration and treatment. The `placed` column is present in the dataset
but is not used in the outlier-handling steps described above.

------------------------------------------------------------------------

## 🧰 Tools and Libraries

  -----------------------------------------------------------------------
  Library                             Purpose
  ----------------------------------- -----------------------------------
  Python                              Programming language

  Pandas                              Loading, filtering, and
                                      manipulating tabular data

  NumPy                               Numerical calculations and
                                      conditional replacement with
                                      `np.where()`

  Matplotlib                          Plot creation and layout

  Seaborn                             Distribution plots and box plots

  Jupyter Notebook                    Interactive analysis
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🚀 Setup and Run

Run the following commands from the repository root.

### 1. Create a virtual environment (if needed)

``` powershell
python -m venv .venv
```

### 2. Activate the environment

``` powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

``` powershell
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib seaborn jupyter
```

### 4. Launch Jupyter Notebook

``` powershell
jupyter notebook
```

Open the `Outliers Detection` folder and run either notebook from top to
bottom.

Keep `placement.csv` in the same directory as the notebooks, or update
the file path in the loading cell if you move it.

------------------------------------------------------------------------

## 🧠 Key Concepts

### Outlier

An outlier is an observation that lies unusually far from the majority
of values in a dataset. An unusual value is not automatically an error;
it may represent a valid observation that deserves investigation.

### Interquartile Range (IQR)

The IQR measures the spread of the middle 50% of observations:

`IQR = Q3 - Q1`

The common IQR fences are:

-   Lower fence: `Q1 - 1.5 × IQR`
-   Upper fence: `Q3 + 1.5 × IQR`

### Z-score

A Z-score expresses how many standard deviations an observation is from
the mean:

`Z = (X - Mean) / Standard Deviation`

The notebooks use `-3` and `+3` as boundaries for identifying extreme
values.

### Trimming

Trimming removes observations outside selected outlier boundaries. This
reduces the number of rows and can also remove valid but extreme
observations.

### Capping

Capping retains the rows but replaces values outside selected boundaries
with the corresponding lower or upper boundary. It changes the values in
the affected feature rather than deleting those observations.

------------------------------------------------------------------------

## ⚠️ Practical Notes and Limitations

-   **Investigate before removing:** Outliers can be valid observations,
    data-entry errors, or evidence of an unusual population. Understand
    their source before changing them.
-   **Choose the method based on the data:** The IQR method and
    standard-deviation/Z-score methods make different distribution
    assumptions and may identify different observations.
-   **Check skewness:** Mean-and-standard-deviation boundaries can be
    sensitive to skewed distributions and extreme values.
-   **Preserve the original data:** Keep an unchanged copy before
    trimming or capping so that the effect of treatment can be compared.
-   **Avoid data leakage in predictive modeling:** If outlier boundaries
    are used as part of a predictive workflow, estimate those boundaries
    from the training data only and apply the same fitted boundaries to
    validation and test data.
-   **Review the trimming condition:** The IQR trimming example in
    `Finding-outliers.ipynb` removes only values above the upper fence.
    Use both lower and upper conditions if symmetric trimming is
    intended.
-   **Notebook compatibility:** Both notebooks use `sns.distplot()`,
    which is deprecated in newer Seaborn versions. If it raises an
    error, replace it with `sns.histplot(..., kde=True)` or
    `sns.kdeplot()` as appropriate.
-   **Results are not claimed here:** This README documents the notebook
    code and workflow; it does not claim that the notebooks have been
    executed end-to-end or that a particular model-performance
    improvement was achieved.

------------------------------------------------------------------------

## 🎯 Learning Outcomes

Through these notebooks, I practiced:

-   Exploring numerical feature distributions.
-   Using descriptive statistics and skewness to understand data.
-   Detecting outliers visually with box plots and distribution plots.
-   Calculating IQR-based lower and upper fences.
-   Detecting extreme observations with standard-deviation boundaries.
-   Calculating and interpreting Z-scores.
-   Applying trimming to remove selected outlier observations.
-   Applying capping to limit extreme values.
-   Comparing feature distributions before and after outlier treatment.
-   Understanding the trade-offs between deleting observations and
    modifying extreme values.

------------------------------------------------------------------------

## 👨‍💻 Author

**Hemant Narute**\
Aspiring Data Analyst \| Data Science and Machine Learning Enthusiast

GitHub: [hemant7102](https://github.com/hemant7102)

------------------------------------------------------------------------

This folder is part of my Data Science learning repository and documents
practical experiments in outlier detection and treatment.
