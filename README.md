# 🧹 Data Cleaning and Quality Analysis Pipeline (Housing Dataset)

## 📌 Project Overview

Real-world datasets are often messy, inconsistent, and unreliable for analysis.
This project demonstrates an **end-to-end data cleaning and quality analysis pipeline** built using Python to transform raw housing data into a clean, structured dataset ready for analysis and modeling.

The pipeline identifies data quality issues such as missing values, inconsistent categorical entries, invalid records, and outliers, and applies systematic cleaning techniques to improve data reliability.

---

## 🎯 Objectives

* Detect and analyze data quality issues in raw datasets
* Perform automated data cleaning using Python
* Standardize categorical variables
* Handle missing and invalid values
* Remove outliers and duplicates
* Engineer useful features
* Generate visual insights from cleaned data

---

## 📂 Dataset Description

The dataset contains housing information across multiple cities with the following attributes:

* `area_sqft` — Property size in square feet
* `bedrooms` — Number of bedrooms
* `bathrooms` — Number of bathrooms
* `location` — City name (categorical)
* `year_built` — Construction year
* `price` — Property price

The raw dataset intentionally contains inconsistencies to simulate real-world data challenges.

---

## ⚠️ Problems Identified in Raw Data

Several data quality issues were detected:

* Missing values in multiple columns
* Inconsistent location names (e.g., "LA", "l.a.", "Los Angeles")
* Incorrect data types
* Invalid values (zero bedrooms, unrealistic years)
* Outliers in property prices
* Duplicate records
* Text placeholders such as `"N/A"` instead of null values

---

## 🛠️ Data Cleaning Steps

The cleaning pipeline performs:

1. Column name standardization
2. Missing value treatment using median imputation
3. Data type conversion to numeric formats
4. Location normalization using mapping rules
5. Removal of invalid records
6. Outlier detection using IQR method
7. Duplicate removal
8. Feature engineering:

   * House age
   * Price per square foot

---

## 📊 Before vs After Cleaning

| Metric         | Raw Data | Cleaned Data |
| -------------- | -------- | ------------ |
| Rows           | 420      | 297          |
| Missing Values | 107      | 0            |
| Duplicates     | 20       | 0            |

---

## 📈 Visualizations

The project includes multiple visual analyses:

* Price distribution
* Area vs price relationship
* Price variation by location
* Correlation heatmap
* Outlier detection plots

### Example

![Price Distribution](outputs/Data_after_cleaning/Price_Distribution.png)

---

## 💡 Key Insights

* Property price strongly correlates with area and number of bedrooms.
* Certain locations show significantly higher median prices.
* Price per square foot varies considerably across cities.
* Outlier removal improves data distribution consistency.

---

## 🏗️ Project Structure

```
Data-Cleaning-and-Quality-Analysis-Pipeline/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebook/
│   └── exploration.ipynb
│
├── src/
│   └── cleaner.py
│   
├── outputs/
│   └── Data_after_cleaning/
│   └── Data_before_cleaning/
|
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Static1016/Data-Cleaning-and-Quality-Analysis-Pipeline.git
cd Data-Cleaning-and-Quality-Analysis-Pipeline

pip install -r requirements.txt
```

---

## ▶️ Usage

Run the cleaning pipeline:

```bash
python main.py
```

The cleaned dataset will be saved in:

```
data/cleaned/
```

---

## 🧠 Skills Demonstrated

* Python programming
* Pandas & NumPy
* Data preprocessing
* Data quality assessment
* Feature engineering
* Data visualization
* Problem solving with real-world datasets
* Project structuring and documentation

---

## 🚀 Future Improvements

* Automated data validation using schema checks
* CLI interface for pipeline execution
* Logging and monitoring
* Integration with machine learning models
* Interactive dashboard (Streamlit/Power BI)

---

## 👤 Author

**Yash Mhaparle**
[LinkedIn](https://www.linkedin.com/in/yash-mhaparle-b52034217/)
[GitHub](https://github.com/Static1016)

---

## ⭐ Acknowledgment

This project is created for learning and portfolio demonstration purposes to showcase practical data cleaning and analysis skills.

---
