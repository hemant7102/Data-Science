# 📊 Data Science & Machine Learning



A hands-on repository documenting my learning journey in **Data Science, Data Analytics, Statistics, Python, Data Visualization, Feature Engineering, and Machine Learning**.



This repository contains practical Jupyter notebooks, datasets, statistical exercises, exploratory data analysis, feature preprocessing techniques, visualization methods, and data analysis projects. Each module focuses on building practical skills through coding, experimentation, and working with datasets.



My goal is to develop a strong foundation in data analysis and statistics, progress toward Machine Learning and Deep Learning, and eventually build reproducible, production-ready data science applications.



---



## 📚 Table of Contents



- [About the Repository](#-about-the-repository)

- [Learning Roadmap](#-learning-roadmap)

- [Repository Structure](#-repository-structure)

- [Learning Modules](#-learning-modules)

  - [1. NumPy](#1-numpy)

  - [2. Pandas](#2-pandas)

  - [3. Matplotlib](#3-matplotlib)

  - [4. Seaborn](#4-seaborn)

  - [5. Plotly](#5-plotly)

  - [6. Mathematics and Statistics for ML](#6-mathematics-and-statistics-for-machine-learning)

  - [7. Exploratory Data Analysis](#7-exploratory-data-analysis-eda)

  - [8. Feature Engineering](#8-feature-engineering)

  - [9. Feature Scaling](#9-feature-scaling)

  - [10. Web Scraping Using Python](#10-web-scraping-using-python)
  - [11. Data Analysis Projects](#11-data-analysis-projects)

- [Technologies Used](#-technologies-used)

- [Getting Started](#-getting-started)

- [Learning Objectives](#-learning-objectives)

- [Current Progress](#-current-progress)

- [Future Improvements](#-future-improvements)

- [Connect With Me](#-connect-with-me)



---



## 🎯 About the Repository



This repository serves as a practical learning portfolio covering the essential concepts and tools used in Data Science and Data Analytics.



The content is organized into topic-specific directories so that individual subjects can be explored independently. Most topics include a dedicated `README.md` describing the notebooks, concepts, datasets, and instructions for getting started.



### What you will find here



- Python-based numerical computing

- Data manipulation and analysis using Pandas

- Data cleaning and preprocessing exercises

- Exploratory Data Analysis (EDA)

- Statistical concepts and probability distributions

- Data visualization using Matplotlib, Seaborn, and Plotly

- Feature engineering and categorical-variable encoding

- Feature transformation and scaling techniques

- Analysis of datasets related to IPL, movies, salaries, cars, COVID-19, and other subjects

- Jupyter notebooks containing practical exercises and case studies

- Data analysis applications and dashboards
- Web scraping and HTML parsing with BeautifulSoup
- Smartphone product-data extraction, cleaning, feature engineering, and EDA



The repository is continuously evolving as I learn new concepts and implement additional projects.



---



## 🗺️ Learning Roadmap



My learning roadmap is organized into the following areas.



| Stage | Area | Focus |

|---|---|---|

| 1 | Foundations | Python, mathematics, probability, and statistics |

| 2 | Numerical Computing | NumPy arrays, indexing, vectorization, and mathematical operations |

| 3 | Data Manipulation | Pandas, filtering, grouping, merging, and data cleaning |

| 4 | Exploratory Data Analysis | Univariate, bivariate, and multivariate analysis |

| 5 | Data Visualization | Matplotlib, Seaborn, Plotly, and dashboard development |

| 6 | Statistical Analysis | Probability distributions, hypothesis testing, and statistical inference |

| 7 | Feature Engineering | Encoding, binning, transformations, and Scikit-learn preprocessing tools |

| 8 | Feature Scaling | Standardization, normalization, robust scaling, and other scaling methods |

| 9 | Web Scraping | HTML parsing, data extraction, and preparing scraped data for analysis |
| 10 | Machine Learning | Regression, classification, clustering, and model evaluation |

| 11 | Deep Learning | Neural networks and deep learning frameworks |

| 12 | MLOps | Experiment tracking, data versioning, Docker, APIs, and deployment |

| 13 | End-to-End Projects | Applying data science techniques to practical problems |



**Note:** This roadmap describes my broader learning goals. The modules listed below represent the learning materials and projects currently documented in this repository.



---



## 📂 Repository Structure



The following is a high-level view of the repository. Some supporting datasets are grouped or described rather than listed individually to keep the structure readable. Refer to each directory for its complete contents.



```text

Data-Science/

│

├── README.md

├── .gitignore

│

├── Numpy/

│   ├── README.md

│   ├── numpy.ipynb

│   ├── numpy2.ipynb

│   ├── Advanced numpy.ipynb

│   ├── Numpy-3D-Graphs-Revision.ipynb

│   ├── numpy-Graph-plot.ipynb

│   ├── Numpy_tricks.ipynb

│   └── quize_numpy.ipynb

│

├── Pandas/

│   ├── README.md

│   ├── Series and DataFrame notebooks

│   ├── GroupBy and filtering exercises

│   ├── Merging, joining, and concatenation

│   ├── Date and time operations

│   ├── Time series analysis

│   ├── Text dataset case studies

│   └── Supporting CSV datasets

│

├── Matplotlib/

│   ├── README.md

│   ├── Basic-Matplotlib-Plotting-Graph.ipynb

│   ├── Advanced-Matplotlib.ipynb

│   └── Supporting CSV datasets

│

├── Seaborn/

│   ├── README.md

│   ├── Plotting-using-seaborn-session-25.ipynb

│   ├── seaborn-graph-ploting.ipynb

│   └── session-26-seaborn.ipynb

│

├── Plotly/

│   ├── README.md

│   ├── Plotly.ipynb

│   └── Plotly-express.ipynb

│

├── Math-Statistics-for-ML/

│   ├── README.md

│   ├── Descriptive-statistics.ipynb

│   ├── Normal-Distribution.ipynb

│   ├── Non-Gaussian-Probability-Distribution.ipynb

│   ├── PDF-PMF-CDF.ipynb

│   ├── Central-Limit-Theorem.ipynb

│   ├── Chi-Square-Test.ipynb

│   ├── Hypothesis-Testing-Part-2-(P-Value).ipynb

│   ├── ANOVA-Test.ipynb

│   ├── Linear-Algebra-Tensor-Vectors.ipynb

│   ├── Transformations.ipynb

│   ├── Pratices-Non-Gaussian.ipynb

│   ├── Case-Study-IPL-runs.ipynb

│   ├── Case-Study-using-CLT-titanic.ipynb

│   ├── case-study-on-salary-dataset.ipynb

│   └── Supporting CSV datasets

│

├── EDA/

│   ├── README.md

│   ├── car_EDA.ipynb

│   ├── EDA-Titanic-dataset.ipynb

│   ├── titanic_dataset.ipynb

│   ├── car_data.xlsx

│   ├── train.csv

│   └── test.csv

│

├── Feature Engineering/

│   ├── README.md

│   ├── SKlearn-Deep-Dive.ipynb

│   ├── SKlearn-Columntransformer-Pipeline.ipynb

│   ├── Encoding-Categoricl-Variables.ipynb

│   ├── Binning.ipynb

│   ├── Num-To-Cateorical-Using-Binning.ipynb

│   ├── Basic-Transformation.ipynb

│   ├── Feature-Transformer.ipynb

│   └── Supporting CSV / serialized pipeline files

│

├── Feature Scaling/

│   ├── README.md

│   ├── Scaling-Techin.ipynb

│   └── Standardization.ipynb

│

├── Web Scraping Using Python/
│   └── Smartprix Mobile/ (scraping, cleaning, EDA notebooks and datasets)
│
├── Imbalanced Data Handling/
│   ├── Imbalanced-Data.ipynb
│   ├── Over-Sampling.ipynb
│   └── Under-Sampling.ipynb
│
│   ├── README.md
│   └── Smartprix Mobile/
│       ├── 91mobiles.html
│       ├── 91Mobiles.ipynb
│       ├── Web-Scraping-using-selenium.ipynb
│       ├── smartprix.html
│       ├── Web-Scraping.ipynb
│       ├── Dataset-Cleaning-Round1-part1.ipynb
│       ├── Data-Cleaning-Round1-Part2.ipynb
│       ├── Data-Cleaning-Round2.ipynb
│       ├── EDA-on-Cleaned-DataSet.ipynb
│       └── Smartphone CSV datasets
│
└── Data Analysis Project/

    └── covid-19-Dashboard/

        ├── app.py

        ├── sample-code.ipynb

        ├── covid_19_india.csv

        ├── AgeGroupDetails.csv

        └── IndividualDetails.csv

```



**Repository structure note:** This is a documentation-oriented overview, not a guarantee that every file is present in every checkout. Notebook names and supporting files may change as the repository evolves. Check the relevant directory for its latest contents.



---



## 📖 Learning Modules



### 1. NumPy



📁 Directory: [`Numpy/`](./Numpy/)



NumPy provides the foundation for numerical computing in Python.



Topics explored include:



- NumPy arrays and multidimensional arrays

- Array indexing and slicing

- Array operations and mathematical computations

- Vectorized operations

- Advanced NumPy techniques

- Three-dimensional arrays and graph-related exercises

- NumPy tricks and practice exercises



**Documentation:** [`Numpy/README.md`](./Numpy/README.md)



### 2. Pandas



📁 Directory: [`Pandas/`](./Pandas/)



Pandas is used for data manipulation, cleaning, transformation, and analysis.



Topics explored include:



- Series and DataFrames

- Data selection and filtering

- GroupBy operations and aggregation

- Merging, joining, and concatenation

- MultiIndex

- Date and time operations

- Time series analysis

- IPL data analysis

- Text dataset case studies

- Working with CSV datasets



**Documentation:** [`Pandas/README.md`](./Pandas/README.md)



### 3. Matplotlib



📁 Directory: [`Matplotlib/`](./Matplotlib/)



Matplotlib is used to create static visualizations and communicate insights from data.



Topics explored include:



- Basic plotting

- Advanced plotting techniques

- Chart customization

- Labels, titles, legends, and axes

- Graph interpretation

- Visualization using supporting datasets



**Documentation:** [`Matplotlib/README.md`](./Matplotlib/README.md)



### 4. Seaborn



📁 Directory: [`Seaborn/`](./Seaborn/)



Seaborn provides statistical visualization tools built on top of Matplotlib.



Topics explored include:



- Statistical plots

- Distribution visualization

- Relationship analysis

- Categorical visualization

- Correlation analysis

- Visual exploration of datasets



**Documentation:** [`Seaborn/README.md`](./Seaborn/README.md)



### 5. Plotly



📁 Directory: [`Plotly/`](./Plotly/)



Plotly is used to create interactive visualizations for exploring and presenting data.



Topics explored include:



- Plotly fundamentals

- Plotly Express

- Interactive charts

- Data visualization and exploration



**Documentation:** [`Plotly/README.md`](./Plotly/README.md)



### 6. Mathematics and Statistics for Machine Learning



📁 Directory: [`Math-Statistics-for-ML/`](./Math-Statistics-for-ML/)



This module covers mathematical and statistical foundations that support data analysis and Machine Learning.



Topics include:



- Descriptive statistics

- Normal and non-Gaussian probability distributions

- Probability Mass Function (PMF)

- Probability Density Function (PDF)

- Cumulative Distribution Function (CDF)

- Central Limit Theorem (CLT)

- Hypothesis testing and P-values

- Chi-Square tests

- Analysis of Variance (ANOVA)

- Linear algebra, tensors, and vectors

- Data transformations

- Practical statistical case studies



The module also contains datasets used for exercises and case studies involving IPL runs, salaries, Titanic data, and other subjects.



**Documentation:** [`Math-Statistics-for-ML/README.md`](./Math-Statistics-for-ML/README.md)



### 7. Exploratory Data Analysis (EDA)



📁 Directory: [`EDA/`](./EDA/)



This module contains practical exploratory analysis notebooks.



Current materials include:



- Car dataset analysis

- Titanic dataset exploration

- Supporting CSV and Excel datasets



The focus is on understanding dataset structure, examining variables, identifying patterns, exploring distributions, detecting potential data-quality issues, and visualizing relationships.



**Documentation:** [`EDA/README.md`](./EDA/README.md)



### 8. Feature Engineering



📁 Directory: [`Feature Engineering/`](./Feature%20Engineering/)



This module focuses on preparing raw data and transforming input variables into features that can be used effectively by Machine Learning algorithms.



Topics explored include:



- Scikit-learn preprocessing tools

- Encoding categorical variables

- Binning numerical variables

- Converting numerical variables into categorical features using binning

- Basic feature transformations

- Custom feature transformers

- ColumnTransformer

- Scikit-learn pipelines

- Building and understanding reusable preprocessing workflows



The notebooks include practical exercises and supporting datasets such as car and customer data. A serialized pipeline file may also be included for experimentation.



**Documentation:** [`Feature Engineering/README.md`](./Feature%20Engineering/README.md)



### 9. Feature Scaling



📁 Directory: [`Feature Scaling/`](./Feature%20Scaling/)



This module explores feature-scaling techniques used to bring numerical features onto comparable scales. Scaling can be important for algorithms that are sensitive to feature magnitude.



The current notebooks cover:



- Standardization using `StandardScaler`

- Min-Max scaling using `MinMaxScaler`

- Robust scaling using `RobustScaler`

- Maximum absolute scaling using `MaxAbsScaler`

- L1 and L2 normalization

- Comparing feature distributions before and after scaling

- Exploring the effect of outliers on scaling methods

- Comparing model performance with and without scaling

- Applying scaling within a train-test workflow



The notebooks use practical datasets, including Social Network Ads and Wine data, and demonstrate additional scaling experiments with other datasets.



**Documentation:** [`Feature Scaling/README.md`](./Feature%20Scaling/README.md)



### 10. Web Scraping Using Python

📁 Directory: [`Web Scraping Using Python/`](./Web%20Scraping%20Using%20Python/)

This module covers collecting structured information from HTML pages and preparing scraped data for analysis. The practical work includes two separate exercises: an introductory 91Mobiles exercise and a larger Smartprix smartphone-data workflow.

**Topics and practical work include:**

- Loading saved HTML pages and parsing them with BeautifulSoup and `lxml`
- Finding product-card elements and extracting smartphone attributes
- Extracting model, price, rating, SIM, processor, RAM, battery, display, camera, storage-card, and operating-system information
- Cleaning inconsistent values and converting text fields into structured features
- Feature extraction for brand, connectivity, processor, memory, battery, camera, display, and operating-system attributes
- Handling missing values and preparing data for analysis
- Exploratory Data Analysis of the cleaned smartphone dataset

**Smartprix workflow:**

1. `Web-Scraping.ipynb` — parses the saved `smartprix.html` snapshot and extracts smartphone product information.
2. `Dataset-Cleaning-Round1-part1.ipynb` — performs the first cleaning pass.
3. `Data-Cleaning-Round1-Part2.ipynb` — extracts structured features from text columns.
4. `Data-Cleaning-Round2.ipynb` — performs further cleaning, transformations, and missing-value handling.
5. `EDA-on-Cleaned-DataSet.ipynb` — explores the cleaned smartphone data and produces the final analysis dataset.

The folder also contains intermediate and final CSV files, including `smartphone_cleaned.csv`, the versioned cleaning outputs, and `smartphone_final_cleaned.csv`.

**Important notes:**

- The notebooks use saved HTML snapshots (`91mobiles.html` and `smartprix.html`); these files are not live websites and do not represent a live, continuously refreshed scrape.
- The cleaning workflow expects `smartprix_smartphone.csv`, which is generated by running `Web-Scraping.ipynb` first.
- `Web-Scraping-using-selenium.ipynb` is retained as a separate exercise; its current implementation uses BeautifulSoup rather than Selenium, despite the notebook filename.
- Run the notebooks from the `Smartprix Mobile/` directory, or update their relative file paths accordingly.

### 11. Imbalanced Data Handling

📁 Directory: [`Imbalanced Data Handling/`](./Imbalanced%20Data%20Handling/)

This module explores techniques for handling imbalanced classification datasets, where one target class has substantially fewer observations than another. The notebooks use synthetic datasets and classification models to demonstrate how resampling and class-weighting approaches affect class distributions and model evaluation.

**Topics and techniques covered:**

- Understanding class imbalance and inspecting class distributions
- Random undersampling and random oversampling
- Resampling with the `imbalanced-learn` library
- SMOTE (Synthetic Minority Over-sampling Technique)
- Borderline-SMOTE, including its second variant
- ADASYN and SVM-SMOTE
- Tomek Links
- Edited Nearest Neighbours (ENN)
- Neighbourhood Cleaning Rule
- Cluster Centroids
- Class weighting in Logistic Regression
- Balanced Random Forest
- Evaluating classifiers with confusion matrices, classification reports, ROC curves, and ROC-AUC scores

**Notebooks:**

1. `Imbalanced-Data.ipynb` — introduces class imbalance and demonstrates random and library-based over/undersampling, SMOTE, class weighting, and Balanced Random Forest.
2. `Over-Sampling.ipynb` — compares Random OverSampling, SMOTE, Borderline-SMOTE, ADASYN, and SVM-SMOTE with classifier evaluation and visualizations.
3. `Under-Sampling.ipynb` — explores Tomek Links, Edited Nearest Neighbours, Neighbourhood Cleaning Rule, and Cluster Centroids.

**Important practice:** Split the data into training and test sets before applying resampling. Resample only the training data; keep the test set at its original class distribution to avoid data leakage and to evaluate performance on a realistic distribution.

### 12. Data Analysis Projects



📁 Directory: [`Data Analysis Project/`](./Data%20Analysis%20Project/)



This directory contains practical data analysis project work.



#### COVID-19 Dashboard



📁 Project: [`covid-19-Dashboard/`](./Data%20Analysis%20Project/covid-19-Dashboard/)



The project contains a Python application, a Jupyter notebook, and supporting COVID-19 datasets.



Files include:



- `app.py` — dashboard application

- `sample-code.ipynb` — notebook-based exploration

- `covid_19_india.csv` — COVID-19 dataset

- `AgeGroupDetails.csv` — age-group data

- `IndividualDetails.csv` — individual-level dataset



Open the project directory to inspect the implementation and its data requirements.



---



## 🛠️ Technologies Used



| Technology | Purpose |

|---|---|

| Python | Core programming language |

| NumPy | Numerical computing |

| Pandas | Data manipulation and analysis |

| Matplotlib | Static data visualization |

| Seaborn | Statistical visualization |

| Plotly | Interactive data visualization |

| SciPy | Scientific and statistical computing |

| Scikit-learn | Data preprocessing and Machine Learning tools |
| imbalanced-learn | Resampling methods for imbalanced classification datasets |
| BeautifulSoup | HTML parsing and web data extraction |
| lxml | HTML parsing backend |

| Jupyter Notebook | Interactive coding and experimentation |

| CSV / Excel | Dataset storage and analysis |

| Git | Version control |

| GitHub | Repository hosting and project documentation |



Additional libraries may be required for individual notebooks or applications.



---



## 🚀 Getting Started



Follow these steps to explore the repository locally.



### Prerequisites



Install the following tools:



- Python

- Git

- Jupyter Notebook

- Visual Studio Code or another Python-compatible editor



### 1. Clone the Repository



```bash

git clone https\://github.com/hemant7102/Data-Science.git

cd Data-Science

```



### 2. Create a Virtual Environment



On Windows PowerShell:



```powershell

python -m venv .venv

```



### 3. Activate the Environment



```powershell

.\.venv\Scripts\Activate.ps1

```



If PowerShell blocks script execution, consult your Python environment setup instructions before changing execution policies.



### 4. Install Common Libraries



```bash

python -m pip install --upgrade pip

python -m pip install numpy pandas matplotlib seaborn plotly scipy scikit-learn imbalanced-learn beautifulsoup4 lxml jupyter openpyxl

```



Individual projects may require additional dependencies. Install those separately according to the relevant notebook or project documentation.



### 5. Launch Jupyter Notebook



```bash

jupyter notebook

```



Alternatively, open the repository in Visual Studio Code and select a notebook kernel that uses the virtual environment.



### 6. Start Exploring



A suggested learning order:



1. Start with `Numpy/` for numerical computing.

2. Continue with `Pandas/` for data manipulation.

3. Explore `Matplotlib/`, `Seaborn/`, and `Plotly/` for visualization.

4. Study `Math-Statistics-for-ML/` for statistical foundations.

5. Explore `EDA/` to practice understanding datasets.

6. Study `Feature Engineering/` and `Feature Scaling/` to learn preprocessing workflows.

7. Explore `Web Scraping Using Python/` to practice HTML parsing and data extraction.
8. Study `Imbalanced Data Handling/` to understand resampling and class-imbalance strategies.
9. Explore `Data Analysis Project/` for practical application work.



---



## 🎓 Learning Objectives



Through this repository, I aim to:



1. Strengthen my Python programming skills.

2. Understand numerical computing with NumPy.

3. Perform data manipulation and cleaning using Pandas.

4. Develop effective data visualization skills.

5. Understand probability, statistics, and statistical inference.

6. Conduct structured Exploratory Data Analysis.

7. Apply feature engineering and preprocessing techniques.

8. Understand when and how to scale numerical features.

9. Analyze real-world datasets and identify meaningful patterns.

10. Build practical data analysis projects.

11. Progress toward Machine Learning and Deep Learning.

12. Develop reproducible workflows and deploy data-driven applications.
13. Collect, parse, clean, and analyze structured data extracted from HTML pages.
14. Understand class imbalance and apply suitable resampling and class-weighting techniques.



---



## 📈 Current Progress



The repository contains practical learning materials in the following areas.



| Area | Repository status |

|---|---|

| NumPy | Learning materials and practice notebooks available |

| Pandas | Learning materials and datasets available |

| Matplotlib | Basic and advanced plotting notebooks available |

| Seaborn | Visualization notebooks available |

| Plotly | Plotly and Plotly Express notebooks available |

| Mathematics and Statistics | Statistical notebooks and case studies available |

| Exploratory Data Analysis | Car and Titanic analysis materials available |

| Feature Engineering | Encoding, binning, transformations, and pipeline notebooks available |

| Feature Scaling | Standardization, normalization, and alternative scaling notebooks available |

| Web Scraping Using Python | 91Mobiles exercise and Smartprix scraping, cleaning, and EDA workflow available |
| Imbalanced Data Handling | Over-sampling, under-sampling, SMOTE variants, cleaning methods, and class-weighting notebooks available |
| Data Analysis Projects | COVID-19 dashboard project available |

| Machine Learning | Part of the broader learning roadmap |

| Deep Learning | Part of the broader learning roadmap |

| MLOps | Part of the broader learning roadmap |



The status of each area reflects the presence of learning materials, not necessarily mastery or completion of every topic. Some notebooks may require dataset paths, package versions, or external data sources to be configured before they run successfully.



---



## 🔮 Future Improvements



Planned improvements include:



- Add more practical exercises and real-world datasets.

- Improve notebook explanations and documentation.

- Expand SQL and database analysis exercises.
- Improve web-scraping workflows with robust request handling, pagination, retries, and responsible scraping practices.
- Add comparative experiments for imbalanced-data techniques using consistent train/test splits and evaluation metrics.

- Add more comprehensive EDA case studies.

- Expand feature engineering and preprocessing examples.

- Add practical feature selection techniques.

- Develop dedicated Machine Learning modules.

- Implement regression, classification, clustering, and ensemble methods.

- Explore model evaluation, validation, and hyperparameter tuning.

- Explore Deep Learning frameworks and neural networks.

- Expand experiment tracking and data versioning with MLOps tools.

- Build more end-to-end data science projects.

- Improve project documentation and reproducibility.

- Keep the repository structure and learning progress updated.



---



## 👨‍💻 Connect With Me



**Hemant Narute**



Aspiring Data Science and Data Analytics Professional



Interested in:



- Python and data analysis

- Statistics and Machine Learning

- Feature engineering and data preprocessing

- Data visualization and dashboards

- Practical data science projects

- Building data-driven applications



GitHub: [hemant7102](https\://github.com/hemant7102)



---



⭐ If you find this repository useful, consider giving it a star.



This repository represents an ongoing learning journey. I will continue adding notebooks, datasets, projects, and documentation as I develop my skills in Data Science and Machine Learning.
