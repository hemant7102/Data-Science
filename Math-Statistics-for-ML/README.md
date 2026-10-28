# Mathematics and Statistics for Machine Learning

A practical, notebook-based learning repository covering the mathematical and statistical concepts essential for **Machine Learning, Data Science, and Data Analytics**.

This repository documents my learning journey through descriptive statistics, probability distributions, statistical inference, hypothesis testing, linear algebra, mathematical transformations, and real-world statistical case studies using Python and Jupyter Notebook.

It includes practical implementations, datasets, calculations, visualizations, and exercises to strengthen my understanding of mathematical and statistical concepts and their applications in Machine Learning.

---

## 📌 About This Repository

Mathematics, probability, and statistics are fundamental to understanding data, evaluating assumptions, interpreting results, and developing reliable Machine Learning models.

The objective of this repository is to build a strong foundation in mathematics and statistics through theoretical understanding and hands-on implementation.

Each notebook focuses on specific concepts and provides opportunities to explore statistical methods, perform calculations, analyze datasets, and visualize results using Python.

## 🎯 Learning Objectives

* Understand descriptive statistics and summarize datasets.
* Explore probability distributions and their characteristics.
* Understand Probability Mass Functions (PMF), Probability Density Functions (PDF), and Cumulative Distribution Functions (CDF).
* Understand the Central Limit Theorem and sampling distributions.
* Explore Gaussian and non-Gaussian probability distributions.
* Learn hypothesis testing and statistical decision-making.
* Understand p-values, significance levels, and statistical significance.
* Perform Chi-Square tests and Analysis of Variance (ANOVA).
* Understand normal distributions and their properties.
* Learn linear algebra fundamentals, including vectors and tensors.
* Explore mathematical and statistical transformations.
* Apply statistical concepts to real-world datasets.
* Conduct practical statistical case studies.
* Implement mathematical and statistical concepts using Python.

---

## 🛠️ Technologies Used

| Technology       | Purpose                                        |
| ---------------- | ---------------------------------------------- |
| Python           | Mathematical and statistical programming       |
| Jupyter Notebook | Interactive learning and experimentation       |
| NumPy            | Numerical computing and array operations       |
| Pandas           | Data manipulation and analysis                 |
| Matplotlib       | Data visualization                             |
| Seaborn          | Statistical data visualization                 |
| SciPy            | Scientific computing and statistical functions |

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
├── Linear-Algebra-Tensor-Vectors.ipynb
├── Normal-Distribution.ipynb
├── Transformations.ipynb
│
├── Case-Study-IPL-runs.ipynb
├── Case-Study-using-CLT-titanic.ipynb
├── case-study-on-salary-dataset.ipynb
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
* Distribution shapes and characteristics
* Practical probability distribution examples

**Notebooks:**

* [`Non-Gaussian-Probability-Distribution.ipynb`](./Non-Gaussian-Probability-Distribution.ipynb)
* [`Pratices-Non-Gaussian.ipynb`](./Pratices-Non-Gaussian.ipynb)

### 3. Normal Distribution

Study the normal distribution and its importance in probability, statistics, and Machine Learning.

**Key concepts:**

* Characteristics of a normal distribution
* Mean and standard deviation
* Symmetry and distribution shape
* Probability calculations
* Applications in statistical inference

**Notebook:** [`Normal-Distribution.ipynb`](./Normal-Distribution.ipynb)

### 4. PMF, PDF, and CDF

Understand three fundamental functions used to describe probability distributions.

| Concept | Description                                                                                                     |
| ------- | --------------------------------------------------------------------------------------------------------------- |
| PMF     | Gives the probability of each possible value of a discrete random variable.                                     |
| PDF     | Describes the probability density of a continuous random variable. Probabilities are calculated over intervals. |
| CDF     | Gives the probability that a random variable is less than or equal to a specified value.                        |

**Notebook:** [`PDF-PMF-CDF.ipynb`](./PDF-PMF-CDF.ipynb)

### 5. Central Limit Theorem

Study how the sampling distribution of the sample mean approaches a normal distribution under suitable conditions as the sample size increases.

**Key concepts:**

* Population and sample
* Sampling distributions
* Sample means
* Sample size and sampling variability
* Applications in statistical inference

**Notebook:** [`Central-Limit-Theorem.ipynb`](./Central-Limit-Theorem.ipynb)

### 6. Chi-Square Test

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

### 7. Hypothesis Testing and P-Values

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

### 8. Analysis of Variance (ANOVA)

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

*Note: A significant one-way ANOVA result indicates that at least one group mean differs. Additional statistical comparisons may be needed to identify which groups differ.*

### 9. Linear Algebra: Tensors and Vectors

Explore linear algebra concepts that provide a mathematical foundation for numerical computing and Machine Learning.

**Topics:**

* Vectors
* Tensors
* Numerical representations of data
* Mathematical operations on vectors and arrays
* Applications in Machine Learning

**Notebook:** [`Linear-Algebra-Tensor-Vectors.ipynb`](./Linear-Algebra-Tensor-Vectors.ipynb)

### 10. Mathematical and Statistical Transformations

Explore transformations that modify data representations and help prepare numerical data for analysis.

**Potential applications:**

* Transforming numerical variables
* Understanding changes in data distributions
* Preparing data for statistical analysis
* Exploring transformations relevant to Machine Learning

**Notebook:** [`Transformations.ipynb`](./Transformations.ipynb)

*Refer to the notebook for the exact transformations and methods implemented.*

---

## 🔬 Practical Statistical Case Studies

This section contains practical case studies that connect statistical concepts with real-world datasets.

### 1. IPL Runs Analysis

Explore cricket batting performance using IPL runs data.

**Notebook:** [`Case-Study-IPL-runs.ipynb`](./Case-Study-IPL-runs.ipynb)

**Learning objectives:**

* Explore and understand cricket performance data.
* Apply descriptive statistical techniques.
* Analyze runs and batting performance.
* Identify patterns in the dataset.
* Interpret statistical findings.

### 2. Central Limit Theorem — Titanic Dataset

Explore the Central Limit Theorem using the Titanic dataset.

**Notebook:** [`Case-Study-using-CLT-titanic.ipynb`](./Case-Study-using-CLT-titanic.ipynb)

**Learning objectives:**

* Explore the Titanic dataset.
* Understand population and sample concepts.
* Investigate sampling distributions.
* Explore sample means and sample size.
* Demonstrate the Central Limit Theorem through practical analysis.

### 3. Salary Dataset Analysis

Explore salary data through practical statistical analysis.

**Notebook:** [`case-study-on-salary-dataset.ipynb`](./case-study-on-salary-dataset.ipynb)

**Learning objectives:**

* Explore salary-related variables.
* Calculate descriptive statistics.
* Understand distributions and variability.
* Identify patterns in numerical data.
* Visualize and interpret statistical results.

*Note: These learning objectives describe the intended analytical scope based on the notebook names. Refer to the actual notebooks for the specific analyses, methods, and conclusions implemented.*

---

## 🗃️ Datasets

This repository includes datasets for practical statistical analysis, experimentation, and data exploration.

| Dataset               | File                                             | Potential Applications                                  |
| --------------------- | ------------------------------------------------ | ------------------------------------------------------- |
| IPL Batsman Runs      | [`batsman_runs_ipl.csv`](./batsman_runs_ipl.csv) | Cricket performance analysis and descriptive statistics |
| Bollywood             | [`bollywood.csv`](./bollywood.csv)               | Analysis of movie-related variables                     |
| Concrete Data         | [`concrete_data.csv`](./concrete_data.csv)       | Statistical analysis of concrete properties             |
| Data Science Salaries | [`ds_salaries.csv`](./ds_salaries.csv)           | Salary distributions and employment data analysis       |
| Movies                | [`movies.csv`](./movies.csv)                     | Movie dataset exploration and statistical analysis      |
| Test Dataset          | [`test.csv`](./test.csv)                         | Dataset-specific analysis and practice                  |
| Training Dataset      | [`train.csv`](./train.csv)                       | Dataset-specific analysis and practice                  |

The exact applications of each dataset depend on its columns and the analyses performed in the notebooks.

**Dataset note:** Not every notebook necessarily uses these datasets. Check the relevant notebook to identify its required input files.

---

## ⚙️ Getting Started

Follow these steps to explore the notebooks locally.

### Prerequisites

* Python
* Jupyter Notebook
* Basic knowledge of Python programming

### 1. Clone the Repository

Clone the parent Data Science repository and navigate to this project folder.

```bash
git clone https://github.com/hemant7102/Data-Science.git
cd Data-Science/Math-Statistics-for-ML
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

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

*Note: Individual notebooks may require additional dependencies or datasets. Install any additional dependencies required by the notebook you intend to run.*

---

## 🚀 Why Mathematics and Statistics Matter in Machine Learning

Mathematics and statistics support several stages of the Machine Learning workflow.

* **Exploratory Data Analysis:** Understand data patterns, distributions, and outliers.
* **Feature Engineering:** Analyze and transform input features.
* **Model Development:** Understand the mathematical foundations of algorithms.
* **Model Evaluation:** Interpret evaluation results and assess uncertainty.
* **Statistical Inference:** Draw conclusions from sample data.
* **Hypothesis Testing:** Evaluate assumptions and compare outcomes.
* **Probability:** Understand uncertainty and probabilistic predictions.
* **Optimization:** Understand the mathematical principles behind model training.

---

## 📈 Learning Approach

My learning approach focuses on understanding concepts, implementing calculations in Python, analyzing results, and reinforcing understanding through practical exercises.

The process involves:

1. Understanding the theoretical foundation.
2. Implementing calculations using Python.
3. Exploring datasets and visualizing results.
4. Interpreting the outcomes.
5. Practicing with additional examples.
6. Connecting mathematical and statistical concepts to Machine Learning applications.

This repository will continue to evolve as I explore more advanced topics in mathematics, probability, statistics, and Machine Learning.

---

## 🔮 Future Learning Goals

Topics I plan to explore include:

* Correlation and covariance
* Probability rules and Bayes' theorem
* Additional probability distributions
* Sampling techniques
* Confidence intervals
* Z-tests and t-tests
* One-way and two-way ANOVA
* Post-hoc statistical tests
* Regression analysis
* Advanced linear algebra
* Matrix operations and eigenvalues
* Calculus and optimization
* Statistical foundations of Machine Learning algorithms

---

## 👨‍💻 Author

### Hemant Narute

**Data Science | Data Analytics | Machine Learning**

Aspiring Data Science and Data Analytics professional interested in Python, mathematics, statistics, Machine Learning, and data-driven problem-solving.

---

⭐ If you find this repository useful, explore the notebooks and learn along with me.
