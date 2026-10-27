# Mathematics and Statistics for Machine Learning

A practical, notebook-based learning repository covering the mathematical and statistical concepts essential for **Machine Learning, Data Science, and Data Analytics**.

This repository documents my learning journey through descriptive statistics, probability distributions, statistical inference, hypothesis testing, and statistical tests using Python and Jupyter Notebook.

It includes practical implementations, datasets, calculations, visualizations, and exercises to strengthen my understanding of statistical concepts and their applications in Machine Learning.

---

## 📌 About This Repository

Mathematics, probability, and statistics are fundamental to understanding data, evaluating assumptions, interpreting results, and developing reliable Machine Learning models.

The purpose of this repository is to build a strong statistical foundation through a combination of theory and hands-on implementation.

Each notebook focuses on a particular concept and provides an opportunity to explore statistical methods using Python.

## 🎯 Learning Objectives

* Understand descriptive statistics and summarize datasets.
* Explore probability distributions and their characteristics.
* Understand Probability Mass Functions (PMF), Probability Density Functions (PDF), and Cumulative Distribution Functions (CDF).
* Understand the Central Limit Theorem and sampling distributions.
* Explore Gaussian and non-Gaussian probability distributions.
* Learn hypothesis testing and statistical decision-making.
* Understand p-values, significance levels, and statistical significance.
* Perform Chi-Square tests and Analysis of Variance (ANOVA).
* Apply statistical concepts to practical datasets.
* Implement statistical calculations and visualizations using Python.

---

## 🛠️ Technologies Used

| Technology       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| Python           | Statistical calculations and programming     |
| Jupyter Notebook | Interactive learning and experimentation     |
| NumPy            | Numerical computations                       |
| Pandas           | Data manipulation and analysis               |
| Matplotlib       | Data visualization                           |
| Seaborn          | Statistical data visualization               |
| SciPy            | Statistical functions and hypothesis testing |

---

## 📂 Repository Structure

```text
Math-Statistics-for-ML/
│
├── README.md
│
├── Descriptive-statistics.ipynb
├── Non-Gaussian-Probability-Distribution.ipynb
├── PDF-PMF-CDF.ipynb
├── Central-Limit-Theorem.ipynb
├── Chi-Square-Test.ipynb
├── Hypothesis-Testing-Part-2-(P-Value).ipynb
├── ANOVA-Test.ipynb
├── Pratices-Non-Gaussian.ipynb
│
├── batsman_runs_ipl.csv
├── bollywood.csv
├── concrete_data.csv
├── ds_salaries.csv
├── movies.csv
├── test.csv
└── train.csv
```

---

## 📚 Topics Covered

### 1. Descriptive Statistics

Learn how to summarize, organize, and understand datasets using statistical measures.

**Key concepts:**

* Mean, median, and mode
* Measures of central tendency
* Measures of dispersion
* Variance and standard deviation
* Quartiles and percentiles
* Interquartile range (IQR)
* Data distribution and outlier analysis

**Notebook:** [`Descriptive-statistics.ipynb`](./Descriptive-statistics.ipynb)

### 2. Probability Distributions

Explore probability distributions and understand how they describe the behavior of random variables.

**Key concepts:**

* Random variables
* Probability distributions
* Gaussian and non-Gaussian distributions
* Distribution shape and characteristics
* Practical probability distribution examples

**Notebooks:**

* [`Non-Gaussian-Probability-Distribution.ipynb`](./Non-Gaussian-Probability-Distribution.ipynb)
* [`Pratices-Non-Gaussian.ipynb`](./Pratices-Non-Gaussian.ipynb)

### 3. PMF, PDF, and CDF

Understand the three fundamental functions used to describe probability distributions.

| Concept | Description                                                                                                     |
| ------- | --------------------------------------------------------------------------------------------------------------- |
| PMF     | Gives the probability of each possible value of a discrete random variable.                                     |
| PDF     | Describes the probability density of a continuous random variable. Probabilities are calculated over intervals. |
| CDF     | Gives the probability that a random variable is less than or equal to a specified value.                        |

**Notebook:** [`PDF-PMF-CDF.ipynb`](./PDF-PMF-CDF.ipynb)

### 4. Central Limit Theorem

Study how the sampling distribution of the sample mean approaches a normal distribution under suitable conditions as the sample size increases.

**Key concepts:**

* Population and sample
* Sampling distributions
* Sample means
* Sample size and sampling variability
* Importance of the Central Limit Theorem in statistical inference

**Notebook:** [`Central-Limit-Theorem.ipynb`](./Central-Limit-Theorem.ipynb)

### 5. Chi-Square Test

Explore the Chi-Square test for analyzing categorical data and comparing observed frequencies with expected frequencies.

**Key concepts:**

* Observed and expected frequencies
* Null and alternative hypotheses
* Chi-Square statistic
* Degrees of freedom
* P-value interpretation
* Goodness-of-fit tests
* Tests of independence

**Notebook:** [`Chi-Square-Test.ipynb`](./Chi-Square-Test.ipynb)

### 6. Hypothesis Testing and P-Values

Learn how hypothesis testing uses sample data to evaluate statistical claims.

**Key concepts:**

* Null hypothesis and alternative hypothesis
* Significance level
* Test statistics
* P-values
* Statistical significance
* Type I and Type II errors
* Interpretation of statistical test results

**Notebook:** [`Hypothesis-Testing-Part-2-(P-Value).ipynb`](./Hypothesis-Testing-Part-2-%28P-Value%29.ipynb)

### 7. Analysis of Variance (ANOVA)

Explore Analysis of Variance (ANOVA), a statistical method used to test whether the means of multiple groups differ significantly.

**Key concepts:**

* Purpose of ANOVA
* Null and alternative hypotheses
* Between-group and within-group variation
* F-statistic
* P-value interpretation
* Significance level
* Interpretation of ANOVA results

**Notebook:** [`ANOVA-Test.ipynb`](./ANOVA-Test.ipynb)

*Note: A significant one-way ANOVA result indicates that at least one group mean differs; additional comparisons may be needed to identify which groups differ.*

---

## 🗃️ Datasets

This repository includes datasets for practical statistical analysis and experimentation.

| Dataset               | File                                             | Potential Applications                                      |
| --------------------- | ------------------------------------------------ | ----------------------------------------------------------- |
| IPL Batsman Runs      | [`batsman_runs_ipl.csv`](./batsman_runs_ipl.csv) | Cricket performance analysis and descriptive statistics     |
| Bollywood             | [`bollywood.csv`](./bollywood.csv)               | Analysis of movie-related variables                         |
| Concrete Data         | [`concrete_data.csv`](./concrete_data.csv)       | Descriptive analysis and exploration of concrete properties |
| Data Science Salaries | [`ds_salaries.csv`](./ds_salaries.csv)           | Salary distribution and employment data analysis            |
| Movies                | [`movies.csv`](./movies.csv)                     | Movie dataset exploration and statistical analysis          |
| Test Dataset          | [`test.csv`](./test.csv)                         | Dataset-specific analysis and practice                      |
| Training Dataset      | [`train.csv`](./train.csv)                       | Dataset-specific analysis and practice                      |

The exact applications of each dataset depend on its columns, data quality, and the questions explored in the notebooks.

**Dataset note:** The notebooks may use only a subset of these files. Check the corresponding notebook to determine which dataset it requires.

---

## ⚙️ Getting Started

Follow these steps to explore the notebooks locally.

### Prerequisites

* Python
* Jupyter Notebook
* Basic knowledge of Python programming

### 1. Clone the Parent Repository

Clone the parent Data Science repository and navigate to this folder.

```bash
git clone <https://github.com/hemant7102/Data-Science.git>
cd "Data Science/Math-Statistics-for-ML"
```


### 2. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Required Libraries

```bash
python -m pip install numpy pandas matplotlib seaborn scipy jupyter
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open a notebook to explore its explanations, code, outputs, and exercises.

---

## 🚀 Why Statistics Matters in Machine Learning

Statistics plays an important role throughout the Machine Learning workflow.

* **Exploratory Data Analysis:** Understand data patterns, distributions, and outliers.
* **Feature Engineering:** Analyze and transform features.
* **Model Evaluation:** Interpret results and assess uncertainty.
* **Statistical Inference:** Draw conclusions from sample data.
* **Hypothesis Testing:** Evaluate assumptions and compare outcomes.
* **Probability:** Understand uncertainty and probabilistic predictions.
* **Experimental Analysis:** Determine whether observed differences may reflect meaningful effects.

---

## 📈 Learning Approach

My learning approach focuses on understanding the theory, implementing statistical methods in Python, analyzing the results, and reinforcing the concepts through practical exercises.

The process involves:

1. Understanding the statistical concept.
2. Implementing the calculations using Python.
3. Exploring datasets and visualizing results.
4. Interpreting the outcomes.
5. Practicing with additional examples.

This repository will continue to evolve as I explore more advanced topics in probability, statistics, and Machine Learning.

---

## 🔮 Future Learning Goals

Topics I plan to explore include:

* Correlation and covariance
* Probability rules and Bayes' theorem
* Common probability distributions
* Sampling techniques
* Confidence intervals
* Z-tests and t-tests
* One-way and two-way ANOVA
* Post-hoc statistical tests
* Regression analysis
* Linear algebra for Machine Learning
* Calculus and optimization
* Statistical foundations of Machine Learning algorithms

---

## 👨‍💻 Author

**Hemant Narute**

Aspiring Data Science and Data Analytics professional interested in Python, statistics, Machine Learning, and data-driven problem-solving.

---

⭐ If you find this repository useful, explore the notebooks and learn along with me.
