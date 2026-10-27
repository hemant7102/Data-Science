# Mathematics and Statistics for Machine Learning

A practical, notebook-based learning repository covering the mathematical and statistical concepts required for Machine Learning, Data Science, and Data Analytics.

This repository contains Jupyter notebooks with explanations, calculations, examples, and practice exercises to strengthen my understanding of probability, descriptive statistics, probability distributions, and statistical hypothesis testing.

## 📌 About This Repository

Mathematics and statistics provide the foundation for understanding how Machine Learning algorithms work. This repository documents my learning journey through essential statistical concepts and their practical implementation using Python.

The primary objective is to build a strong foundation in statistics and probability before moving toward more advanced Machine Learning concepts.

## 🎯 Learning Objectives

* Understand descriptive statistics and summarize datasets.
* Learn probability distributions and their characteristics.
* Understand Probability Mass Functions (PMF), Probability Density Functions (PDF), and Cumulative Distribution Functions (CDF).
* Understand the Central Limit Theorem and its importance in statistical inference.
* Explore non-Gaussian probability distributions.
* Learn hypothesis testing and statistical decision-making.
* Understand p-values and their role in interpreting statistical tests.
* Practice implementing statistical concepts using Python and Jupyter Notebook.

## 🛠️ Technologies Used

* **Python** — Statistical calculations and programming.
* **Jupyter Notebook** — Interactive learning and experimentation.
* **NumPy** — Numerical computations.
* **Pandas** — Data manipulation and analysis.
* **Matplotlib** — Data visualization.
* **Seaborn** — Statistical data visualization.
* **SciPy** — Statistical functions and hypothesis testing.

## 📂 Repository Structure

```text
Math-Statistics-for-ML/
│
├── Descriptive-statistics.ipynb
├── Non-Gaussian-Probability-Distribution.ipynb
├── PDF-PMF-CDF.ipynb
├── Central-Limit-Theorem.ipynb
├── Chi-Square-Test.ipynb
├── Hypothesis-Testing-Part-2-(P-Value).ipynb
├── Pratices-Non-Gaussian.ipynb
│
└── README.md
```

## 📚 Topics Covered

### 1. Descriptive Statistics

Learn how to summarize, organize, and understand data using statistical measures.

**Key concepts:**

* Mean, median, and mode
* Measures of dispersion
* Variance and standard deviation
* Quartiles and percentiles
* Interquartile range (IQR)
* Data distribution and outlier analysis

**Notebook:** `Descriptive-statistics.ipynb`

### 2. Probability Distributions

Explore probability distributions and understand how they describe the behavior of random variables.

**Key concepts:**

* Random variables
* Probability distributions
* Gaussian versus non-Gaussian distributions
* Characteristics of non-Gaussian distributions
* Practical probability distribution examples

**Notebooks:**

* `Non-Gaussian-Probability-Distribution.ipynb`
* `Pratices-Non-Gaussian.ipynb`

### 3. PMF, PDF, and CDF

Understand the three important functions used to describe probability distributions.

| Concept | Description                                                                                                  |
| ------- | ------------------------------------------------------------------------------------------------------------ |
| PMF     | Gives the probability of each possible value of a discrete random variable.                                  |
| PDF     | Describes probability density for a continuous random variable; probabilities are calculated over intervals. |
| CDF     | Gives the probability that a random variable is less than or equal to a specified value.                     |

**Notebook:** `PDF-PMF-CDF.ipynb`

### 4. Central Limit Theorem

Study why the sampling distribution of the sample mean approaches a normal distribution under suitable conditions as the sample size increases.

**Key concepts:**

* Population and sample
* Sampling distributions
* Sample means
* Sample size and sampling variability
* Importance of the Central Limit Theorem in statistical inference

**Notebook:** `Central-Limit-Theorem.ipynb`

### 5. Chi-Square Test

Explore the chi-square test as a method for comparing observed categorical counts with expected counts or investigating relationships between categorical variables.

**Key concepts:**

* Observed and expected frequencies
* Null and alternative hypotheses
* Chi-square statistic
* Degrees of freedom
* P-value interpretation
* Goodness-of-fit and independence tests

**Notebook:** `Chi-Square-Test.ipynb`

### 6. Hypothesis Testing and P-Values

Learn how statistical hypothesis testing helps evaluate claims using sample data.

**Key concepts:**

* Null hypothesis and alternative hypothesis
* Significance level
* Test statistics
* P-values
* Statistical significance
* Type I and Type II errors
* Interpreting statistical test results

**Notebook:** `Hypothesis-Testing-Part-2-(P-Value).ipynb`

## ⚙️ Getting Started

Follow these steps to explore the notebooks locally.

### Prerequisites

Install Python and Jupyter Notebook. Familiarity with basic Python programming will be helpful.

### 1. Clone the Repository

Clone the parent Data Science repository and navigate to this project folder.

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Data-Science/Math-Statistics-for-ML
```

Replace `<YOUR-GITHUB-REPOSITORY-URL>` with the actual URL of your GitHub repository. Adjust the folder name if your repository uses a different name.

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

Open any notebook to explore its explanations, code, outputs, and exercises.

## 🚀 Why Statistics Matters in Machine Learning

Statistics plays an important role throughout the Machine Learning workflow.

* **Exploratory Data Analysis:** Understand data patterns, distributions, and outliers.
* **Feature Engineering:** Transform and analyze features.
* **Model Evaluation:** Interpret evaluation results and assess uncertainty.
* **Statistical Inference:** Draw conclusions from sample data.
* **Hypothesis Testing:** Evaluate assumptions and compare outcomes.
* **Probability:** Understand uncertainty and probabilistic predictions.

## 📈 Learning Approach

My approach is to learn each concept, implement it in Python, examine the results, and reinforce my understanding through practical examples and exercises.

This repository will evolve as I explore additional topics in mathematics, probability, and statistics for Machine Learning.

## 🔮 Future Learning Goals

Topics I plan to explore include:

* Correlation and covariance
* Probability rules and Bayes' theorem
* Common probability distributions
* Sampling techniques and confidence intervals
* Z-tests and t-tests
* ANOVA
* Linear algebra for Machine Learning
* Calculus and optimization
* Statistical foundations of Machine Learning algorithms

## 👨‍💻 Author

**Hemant Narute**

Aspiring Data Science and Data Analytics professional interested in Python, statistics, Machine Learning, and data-driven problem-solving.

---

⭐ If you find this repository useful, feel free to explore the notebooks and learn along with me.
