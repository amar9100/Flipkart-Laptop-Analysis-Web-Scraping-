# Flipkart Laptop Analysis – Web Scraping & Data Analytics Project

## Project Overview

This project is an end-to-end data analytics project based on laptop listings collected from Flipkart.

The workflow covers:

- Web scraping using Python
- Data cleaning and transformation using Pandas
- Exploratory Data Analysis (EDA)
- Data visualization using Matplotlib
- SQL analysis using SQLite
- Power BI dashboard development
- Business insights and recommendations

The project demonstrates how raw e-commerce data can be transformed into structured information and business insights.

---

## Objectives

The main objectives of this project are to:

1. Scrape laptop product information from Flipkart.
2. Clean and transform the collected data.
3. Perform exploratory data analysis.
4. Identify relationships between price and laptop specifications.
5. Perform business-focused SQL analysis.
6. Build an interactive Power BI dashboard.
7. Generate useful business insights from the dataset.

---

## Project Structure

```text
Flipkart/
│
├── data/
│   ├── raw_flipkart_laptops.csv
│   ├── cleaned_flipkart_laptops.csv
│   ├── data_dictionary.csv
│   └── flipkart_laptops.db
│
├── images/
│   ├── brand_distribution.png
│   ├── selling_price_distribution.png
│   ├── rating_distribution.png
│   ├── price_vs_ram.png
│   ├── price_vs_storage.png
│   ├── price_vs_rating.png
│   ├── selling_price_boxplot.png
│   └── correlation_matrix.png
│
├── notebooks/
│   ├── 01_data_cleaning.py
│   ├── 02_eda.py
│   ├── 03_eda_visualizations.py
│   ├── 04_eda_relationships.py
│   └── 05_eda_correlation.py
│
├── powerbi/
│
├── reports/
│
├── scraper/
│   └── flipkart_scraper.py
│
├── sql/
│   ├── 01_basic_queries.sql
│   ├── 01_create_database.py
│   ├── 02_run_basic_queries.py
│   ├── 03_business_analysis.py
│   └── 04_check_duplicate_products.py
│
├── .gitignore
└── README.md