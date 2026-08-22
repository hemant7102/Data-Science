# Pandas Learning

A practical collection of Pandas learning, revision, data manipulation, analysis, visualization, and practice notebooks.

This section is part of my broader Data Science & Machine Learning roadmap, focusing on building strong practical skills with Pandas.

---

## Notebooks

| Notebook | Description |
|---|---|
| `series-method.ipynb` | Pandas Series methods and operations |
| `Pandas-DataFrame2.ipynb` | DataFrame operations, sorting, ranking, indexing, missing values, duplicates, and `apply()` |
| `Pandas-Graph-ploting.ipynb` | Data visualization using Pandas plotting |
| `GroupBy-object.ipynb` | GroupBy operations and grouped data analysis |
| `Exercise-on-groupby.ipynb` | Practical exercises for understanding and applying GroupBy operations |
| `merging-joining-concatenating.ipynb` | Combining DataFrames using merge, join, and concatenation |
| `MultiIndex-series.ipynb` | MultiIndex Series and hierarchical indexing |

---

## Topics Covered

### 1. Pandas Series

- Creating Series
- Series indexing
- Series data types
- `astype()`
- `between()`
- `clip()`
- `drop_duplicates()`
- Filtering Series
- Series methods

### 2. DataFrames

- Creating DataFrames
- Reading CSV files
- Inspecting datasets
- Selecting rows and columns
- Boolean filtering
- Sorting values
- Sorting by multiple columns
- Ranking
- Setting an index
- Resetting an index
- Renaming columns and indexes
- Dropping rows and columns
- Removing duplicates

### 3. Missing Data

- `isnull()`
- `notnull()`
- `hasnans`
- `dropna()`
- `fillna()`
- Forward filling
- Handling missing values by column

### 4. Data Transformation

- `value_counts()`
- `unique()`
- `nunique()`
- Boolean conditions
- Applying custom functions
- `apply()`
- Data filtering
- Data transformation

### 5. GroupBy

The GroupBy notebooks focus on grouping and analyzing data using Pandas.

Topics include:

- Creating GroupBy objects
- Grouping data by columns
- Selecting groups
- Aggregating grouped data
- Applying functions to groups
- Analyzing grouped results
- Practical GroupBy exercises

### 6. Merging, Joining & Concatenating

The `merging-joining-concatenating.ipynb` notebook covers techniques for combining multiple DataFrames.

Topics include:

- `pd.merge()`
- Inner join
- Left join
- Right join
- Outer join
- DataFrame `join()`
- `pd.concat()`
- Combining rows
- Combining columns
- Working with multiple datasets

### 7. MultiIndex

The `MultiIndex-series.ipynb` notebook explores hierarchical indexing in Pandas.

Topics include:

- MultiIndex Series
- Creating hierarchical indexes
- Selecting MultiIndex data
- Working with multiple index levels
- Index-based data organization
- Accessing hierarchical data

### 8. Data Visualization

The Pandas visualization notebook covers:

- Line plots
- Bar plots
- Histograms
- Box plots
- Scatter plots
- Area plots
- Pie charts

Pandas plotting is used for quick exploratory visualization of DataFrame and Series data.

---

## Datasets

The Pandas section contains datasets used for practical exercises and notebook examples.

| Dataset | Purpose |
|---|---|
| `batsman_runs_ipl.csv` | IPL batsman analysis |
| `bollywood.csv` | Bollywood/movie data analysis |
| `deliveries.csv` | IPL delivery-level analysis and GroupBy exercises |
| `imdb-top-1000.csv` | Movie data analysis |
| `ipl-matches.csv` | IPL match analysis |
| `kohli_ipl.csv` | Virat Kohli IPL analysis |
| `movies.csv` | Movie data analysis |

These datasets support practical learning through filtering, grouping, aggregation, sorting, visualization, and other Pandas operations.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Learning Objectives

The goal of this section is to develop practical skills in:

1. Loading datasets
2. Understanding Series and DataFrames
3. Manipulating structured data
4. Handling missing values
5. Sorting and ranking
6. Filtering and transforming data
7. Grouping and aggregating data
8. Combining multiple datasets
9. Working with hierarchical indexes
10. Creating data visualizations
11. Solving practical data analysis exercises

---

## Folder Structure

```text
Pandas/
│
├── README.md
│
├── series-method.ipynb
├── Pandas-DataFrame2.ipynb
├── Pandas-Graph-ploting.ipynb
├── GroupBy-object.ipynb
├── Exercise-on-groupby.ipynb
├── merging-joining-concatenating.ipynb
├── MultiIndex-series.ipynb
│
├── batsman_runs_ipl.csv
├── bollywood.csv
├── deliveries.csv
├── imdb-top-1000.csv
├── ipl-matches.csv
├── kohli_ipl.csv
└── movies.csv