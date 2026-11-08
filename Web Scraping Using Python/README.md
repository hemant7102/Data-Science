# Web Scraping Using Python

This module contains practice notebooks for extracting structured information from HTML pages using Python. It focuses on parsing saved HTML with **BeautifulSoup** and converting product information into a **Pandas DataFrame**.

## Folder Structure

```text
Web Scraping Using Python/
└── Smartprix Mobile/
    ├── 91mobiles.html
    ├── 91Mobiles.ipynb
    └── Web-Scraping-using-selenium.ipynb
```

## Files and Notebooks

### 1. `91mobiles.html`

A locally saved HTML page from 91mobiles. The page contains mobile-phone listing information and is used as the input source by `91Mobiles.ipynb`.

The HTML contains structured product-list data, including product names and image references. It is a saved page snapshot; it should not be treated as live or current product/price data.

### 2. `91Mobiles.ipynb`

This notebook begins an HTML-parsing exercise using:

- `BeautifulSoup` from `bs4`
- `NumPy`
- `Pandas`
- `lxml` as the HTML parser

Current workflow:
1. Import the required libraries.
2. Read `91mobiles.html` from the local directory.
3. Parse the HTML with `BeautifulSoup(html, "lxml")`.
4. Try selecting `div` elements by their class attribute.

**Current limitation:** The notebook is an incomplete starter exercise. Its selector `soup.find_all('div', {'class': ''})` finds 13 elements in the saved notebook output, but it does not yet extract phone names, prices, specifications, or build a dataset. The notebook name and source HTML refer to 91mobiles; do not assume the extraction is complete.

### 3. `Web-Scraping-using-selenium.ipynb`

Despite the filename, the inspected notebook's demonstrated extraction workflow uses **BeautifulSoup on a locally saved HTML file**. It does not currently demonstrate Selenium browser automation.

The notebook's workflow:
1. Imports Pandas, NumPy, `time`, and BeautifulSoup.
2. Attempts to load `smartprix.html`.
3. Parses the HTML with `BeautifulSoup`.
4. Selects product cards with the CSS class combination `sm-product has-tag has-features has-actions`.
5. Extracts product fields into Python lists.
6. Uses a helper function, `safe_text()`, to handle missing HTML elements.
7. Builds a Pandas DataFrame named `smartprix_smartphone`.
8. Displays the DataFrame and inspects its structure with `.info()`.

The intended DataFrame columns are:

| Column | Intended content |
|---|---|
| `model` | Smartphone model name |
| `price` | Listed price text |
| `star` | Rating value |
| `rating` | Number of ratings/reviews |
| `display` | Display highlight |
| `camera` | Camera highlight |
| `card` | Card/feature highlight as selected by the notebook |
| `os` | Operating-system highlight |

**Important file mismatch:** This notebook opens `smartprix.html`, but the folder listing supplied for this module contains `91mobiles.html`, not `smartprix.html`. The notebook will raise `FileNotFoundError` unless the expected Smartprix HTML file is added to this directory or the notebook is updated to use the correct source and selectors. The `91mobiles.html` file is not a drop-in replacement because the notebook searches for Smartprix-specific CSS classes.

**Data-quality / notebook caveats:**
- The notebook contains two consecutive extraction loops that append `model`, `price`, `star`, and `rating`. Running both loops in sequence can duplicate those four lists. Keep one extraction loop or reset the lists before rerunning.
- The saved notebook output reports 1,016 product cards, but its displayed DataFrame `.info()` output shows zero non-null values for several extracted fields. Treat the saved output as an unverified notebook state, not proof of a clean, complete dataset.
- The `safe_text()` helper is used for the highlight fields, but the first extraction loop accesses some tags directly with `.text`; missing tags can cause an `AttributeError`.
- HTML class names and page structure can change. Inspect the saved HTML and validate selectors before relying on the extraction.

## Setup

Run these commands from the project directory or an activated virtual environment:

```bash
pip install beautifulsoup4 lxml pandas numpy jupyter
```

If you later implement actual browser automation, install Selenium separately:

```bash
pip install selenium
```

A compatible browser and browser driver may also be required for Selenium-based automation. The current notebook does not yet contain Selenium setup or browser-control code.

## Running the Notebooks

Open a terminal in the `Smartprix Mobile` directory and start Jupyter:

```bash
jupyter notebook
```

Run `91Mobiles.ipynb` using the included `91mobiles.html`.

For `Web-Scraping-using-selenium.ipynb`, first provide the expected `smartprix.html` file in the same directory, or deliberately revise the notebook's input filename and selectors to match the actual HTML source. Do not simply rename `91mobiles.html` to `smartprix.html`; the page structures and CSS selectors differ.

## Key Concepts Practised

- Reading locally saved HTML files
- Parsing HTML with BeautifulSoup and `lxml`
- Finding elements using tags and CSS classes
- Extracting text from HTML elements
- Handling missing elements with a helper function
- Storing extracted attributes in Python lists
- Creating a structured Pandas DataFrame
- Inspecting dataset shape, columns, and null values
- Validating selectors and extraction quality

## Recommended Improvements

1. Complete `91Mobiles.ipynb` by identifying the actual product-card selectors in `91mobiles.html`, extracting relevant fields, and creating a DataFrame.
2. Resolve the `smartprix.html` versus `91mobiles.html` mismatch in the second notebook.
3. Remove the duplicate append loop and initialize extraction lists once before each run.
4. Use safe extraction consistently for every optional HTML element.
5. Add validation checks for row counts, missing values, duplicate rows, and representative extracted records.
6. Rename `Web-Scraping-using-selenium.ipynb` if it is intended to remain a BeautifulSoup-only notebook, or add actual Selenium browser automation if Selenium is the learning objective.
7. Record the source URL and collection date when saving HTML snapshots. Respect the website's terms, robots policy, rate limits, and applicable laws when collecting data.

## Notes

- The HTML file is a static snapshot and may become outdated.
- This folder currently demonstrates HTML parsing more clearly than end-to-end live web scraping.
- Do not publish or rely on extracted prices/specifications without validating them against the source page.
