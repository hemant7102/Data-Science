# Web Scraping Using Python – Smartprix Mobile Data Project

## Overview

This project demonstrates an end-to-end data workflow using smartphone listings from Smartprix:

1. Scrape smartphone listing information from saved HTML pages.
2. Inspect and clean the raw scraped dataset.
3. Extract structured features from text columns.
4. Handle inconsistent values and missing data.
5. Perform exploratory data analysis (EDA).
6. Export cleaned and model-ready datasets.

The project uses **BeautifulSoup, Pandas, NumPy, Matplotlib, and Seaborn**. The notebooks work with locally saved HTML files and CSV files.

> **Important:** The HTML files are saved snapshots, not live data. Product availability, prices, and specifications in them reflect the snapshot captured at the time of scraping.

---

## Project Structure

```text
Web Scraping Using Python/
│
├── README.md
│
└── Smartprix Mobile/
    ├── 91mobiles.html
    ├── 91Mobiles.ipynb
    ├── Web-Scraping-using-selenium.ipynb
    │
    ├── smartprix.html
    ├── Web-Scraping.ipynb
    │
    ├── Dataset-Cleaning-Round1-part1.ipynb
    ├── Data-Cleaning-Round1-Part2.ipynb
    ├── Data-Cleaning-Round2.ipynb
    ├── EDA-on-Cleaned-DataSet.ipynb
    │
    ├── smartphone_cleaned.csv
    ├── smartphone_cleaned_v1.csv
    ├── smartphone_cleaned_v2.csv
    ├── smartphone_cleaned_v3.csv
    ├── smartphone_cleaned_v4.csv
    ├── smartphone_final_cleaned.csv
    └── smartphones_cleaned_v5.csv
```

The list above groups the main files by role. Keep the actual filenames unchanged unless you also update the corresponding notebook paths.

---

## Notebooks

### 1. Initial 91Mobiles exercises

| File | Purpose |
|---|---|
| `91Mobiles.ipynb` | A starter exercise that loads `91mobiles.html` and explores HTML elements with BeautifulSoup. |
| `Web-Scraping-using-selenium.ipynb` | Contains a smartphone-card extraction exercise. Despite its filename, the inspected implementation uses BeautifulSoup rather than Selenium browser automation. |

These are separate exercises from the Smartprix pipeline below. Check the input filename and selectors before rerunning them; the saved HTML snapshots have different structures.

### 2. Smartprix scraping

**`Web-Scraping.ipynb`**

- Loads the local `smartprix.html` snapshot.
- Parses the page using BeautifulSoup and `lxml`.
- Finds smartphone product cards.
- Extracts fields such as model, price, rating, SIM, processor, RAM, battery, display, camera, memory-card support, and operating system.
- Builds a Pandas DataFrame.
- Exports the raw scraped data to CSV.

The saved `smartprix.html` snapshot contains 1,016 matching smartphone product cards.

The notebook writes:
- `smartprix_smartphone.csv` — the raw scraped table used by the first cleaning notebook.
- `smartphone_cleaned.csv` — another export of the scraped table.

### 3. Dataset cleaning – Round 1, Part 1

**`Dataset-Cleaning-Round1-part1.ipynb`**

- Loads `smartprix_smartphone.csv`.
- Inspects data quality and tidiness issues.
- Cleans the price field and removes records below the notebook's selected price threshold.
- Corrects misplaced or inconsistent values across processor, RAM, battery, display, camera, memory-card, and OS fields.
- Exports `smartphone_cleaned_v1.csv`.

### 4. Dataset cleaning – Round 1, Part 2

**`Data-Cleaning-Round1-Part2.ipynb`**

- Loads `smartphone_cleaned_v1.csv`.
- Extracts brand names and structured features from text fields.
- Derives features such as 5G, NFC, IR blaster, processor brand, core count, processor speed, RAM capacity, internal memory, battery capacity, fast charging, screen size, resolution, refresh rate, camera counts, and extended-memory information.
- Exports `smartphone_cleaned_v2.csv`.

### 5. Dataset cleaning – Round 2

**`Data-Cleaning-Round2.ipynb`**

- Loads `smartphone_cleaned_v2.csv`.
- Inspects distributions, outliers, missing values, and inconsistent categories.
- Cleans processor-brand and other categorical values.
- Transforms selected features, including core count, charging information, OS, and extended-memory fields.
- Applies a KNN imputation workflow in the later part of the notebook.
- Exports `smartphone_cleaned_v3.csv` and `smartphones_cleaned_v5.csv`.

### 6. Exploratory data analysis

**`EDA-on-Cleaned-DataSet.ipynb`**

- Loads `smartphone_cleaned_v3.csv`.
- Examines brand, model, price, rating, connectivity, processor, battery, memory, display, camera, and operating-system features.
- Uses descriptive statistics and visualizations to explore distributions and relationships.
- Includes correlation analysis and missing-value inspection.
- Exports `smartphone_final_cleaned.csv`.

---

## Dataset Files

The CSV files represent different stages of the workflow. Their shapes were checked from the supplied files.

| Dataset | Rows | Columns | Description |
|---|---:|---:|---|
| `smartphone_cleaned.csv` | 1,016 | 11 | Initial scraped smartphone table. |
| `smartphone_cleaned_v1.csv` | 984 | 12 | First cleaning stage. |
| `smartphone_cleaned_v2.csv` | 982 | 23 | Structured feature extraction stage. |
| `smartphone_cleaned_v3.csv` | 982 | 24 | Further cleaned and transformed dataset. |
| `smartphone_cleaned_v4.csv` | 982 | 88 | Wide, encoded dataset with many indicator columns. |
| `smartphone_final_cleaned.csv` | 982 | 24 | Dataset exported by the EDA notebook. |
| `smartphones_cleaned_v5.csv` | 982 | 88 | Wide, encoded dataset exported by the Round 2 notebook. |

**Pipeline note:** `smartphone_cleaned_v4.csv` is present in the supplied folder, but the supplied notebooks do not show an export step that creates this exact filename. Do not assume it can be regenerated from the documented notebook sequence without checking its origin.

The two 88-column datasets (`smartphone_cleaned_v4.csv` and `smartphones_cleaned_v5.csv`) contain many one-hot encoded indicator columns. The 24-column files retain the more interpretable feature representation.

---

## Execution Order

Run the Smartprix pipeline in this order:

1. `Web-Scraping.ipynb`
2. `Dataset-Cleaning-Round1-part1.ipynb`
3. `Data-Cleaning-Round1-Part2.ipynb`
4. `Data-Cleaning-Round2.ipynb`
5. `EDA-on-Cleaned-DataSet.ipynb`

The sequence matters because each cleaning notebook reads the CSV produced by the preceding stage.

### Input/output dependencies

```text
smartprix.html
    │
    ▼
Web-Scraping.ipynb
    ├── smartprix_smartphone.csv
    └── smartphone_cleaned.csv
             │
             ▼
Dataset-Cleaning-Round1-part1.ipynb
    └── smartphone_cleaned_v1.csv
             │
             ▼
Data-Cleaning-Round1-Part2.ipynb
    └── smartphone_cleaned_v2.csv
             │
             ▼
Data-Cleaning-Round2.ipynb
    ├── smartphone_cleaned_v3.csv
    └── smartphones_cleaned_v5.csv
             │
             ▼
EDA-on-Cleaned-DataSet.ipynb
    └── smartphone_final_cleaned.csv
```

`smartphone_cleaned_v4.csv` is an additional supplied dataset; its generating step is not established by the notebooks listed above.

---

## Requirements

Install the main libraries in your Python environment:

```bash
pip install pandas numpy beautifulsoup4 lxml matplotlib seaborn jupyter scikit-learn
```

If using Anaconda, activate the intended environment before launching Jupyter:

```bash
conda activate <your-environment>
jupyter notebook
```

---

## Running the Project

1. Clone or download the repository.
2. Open the `Web Scraping Using Python/Smartprix Mobile/` directory.
3. Install the dependencies.
4. Open the notebooks in Jupyter.
5. Run the Smartprix notebooks in the execution order above.
6. Confirm that the expected intermediate CSV files are generated before running the next notebook.

The notebooks use relative paths such as `smartprix.html` and `smartphone_cleaned_v1.csv`. Run them with the `Smartprix Mobile` folder as the working directory, or update the paths to match your environment.

---

## Important Checks and Limitations

- **HTML snapshot:** `smartprix.html` is a local snapshot. It does not automatically fetch current Smartprix listings.
- **Scraping selectors:** Website HTML can change. If product cards or fields are not extracted, inspect the saved page and update the selectors.
- **Intermediate CSV:** `Dataset-Cleaning-Round1-part1.ipynb` expects `smartprix_smartphone.csv`. Generate it by running `Web-Scraping.ipynb` first.
- **Notebook filename:** `Web-Scraping-using-selenium.ipynb` does not implement Selenium in the inspected version; its implementation is BeautifulSoup-based.
- **Data quality:** The cleaning notebooks contain manual row-specific corrections. Such corrections are specific to this dataset snapshot and should be reviewed before applying the workflow to new data.
- **Imputation:** Review the feature selection and train/test separation before using imputed data in a predictive model. Fit imputers only on training data to avoid data leakage.
- **Encoding:** The wide 88-column datasets contain one-hot encoded features. Preserve the exact feature schema when using them for model training or inference.
- **Reproducibility:** Some notebook cells rely on variables created in earlier cells. Run notebooks from top to bottom in a fresh kernel.

---

## Skills Demonstrated

- HTML parsing with BeautifulSoup and `lxml`
- Web data extraction and tabular data creation
- Data quality and tidiness assessment
- Data cleaning and manual correction
- Feature extraction and feature engineering
- Categorical transformation and one-hot encoding
- Missing-value analysis and KNN imputation
- Exploratory data analysis
- Statistical summaries and data visualization
- CSV export and multi-stage data workflows

---

## Responsible Scraping

Use only publicly accessible pages and follow the website's terms of use, robots directives, and applicable laws. Avoid excessive requests, do not bypass access controls, and prefer saved HTML snapshots for repeatable learning exercises.
