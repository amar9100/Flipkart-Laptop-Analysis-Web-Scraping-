# Flipkart Laptop Analysis – Final Report

## 1. Executive Summary

This project presents an end-to-end analysis of laptop listings collected from Flipkart.

The workflow covers web scraping, data cleaning, exploratory data analysis, SQL analysis, Power BI visualization, and business insights.

A sample of 20 laptop listings was collected and transformed into a structured analytical dataset.

The analysis examines brand presence, pricing, RAM, storage, operating systems, ratings, discounts, and relationships between product specifications and selling price.

---

## 2. Project Objectives

The main objectives of the project were to:

1. Collect laptop listing information from Flipkart using Python.
2. Clean and transform the scraped data using Pandas.
3. Perform exploratory data analysis.
4. Analyze product pricing and specifications.
5. Perform SQL-based business analysis.
6. Build a Power BI dashboard.
7. Generate business-oriented insights from the collected sample.

---

## 3. Data Collection

Laptop listing information was collected using Python with:

- Requests
- BeautifulSoup
- Regular expressions
- Pandas

The scraper collected information including:

- Brand
- Product name
- Rating
- Ratings count
- Reviews count
- Processor
- RAM
- Operating system
- Storage
- Screen size
- Selling price
- Original price
- Discount
- Product URL

The scraper also handled unavailable listings, normalized product URLs, and removed duplicate products.

### Dataset Size

The final scraped dataset contains:

**20 laptop listings**

---

## 4. Data Cleaning and Transformation

The raw dataset was processed using Pandas.

The cleaning workflow included:

- Removing unnecessary whitespace
- Standardizing text fields
- Converting numeric fields into appropriate data types
- Extracting RAM in GB
- Extracting storage capacity in GB
- Extracting screen size in inches
- Calculating price difference
- Checking and removing duplicates

The cleaned dataset contains 18 analytical columns.

### Derived Variables

The following variables were created during cleaning:

- `RAM_GB`
- `Screen_Size_Inches`
- `Storage_GB`
- `Price_Difference`

No duplicate records were removed from the final 20-row dataset.

---

## 5. Exploratory Data Analysis

### 5.1 Brand Distribution

The number of listings by brand in the sample is:

| Brand | Listings |
|---|---:|
| Lenovo | 4 |
| Primebook | 3 |
| MOTOROLA | 2 |
| HP | 2 |
| DELL | 2 |
| Apple | 2 |
| Acer | 2 |
| Samsung | 1 |
| Neopticon | 1 |
| ASUS | 1 |

Lenovo has the largest number of listings in the collected sample.

---

### 5.2 Operating System Distribution

The operating systems represented are:

| Operating System | Listings |
|---|---:|
| Windows 11 Home | 8 |
| Windows 11 | 5 |
| Android | 3 |
| Mac OS | 2 |
| Chrome OS | 2 |

Windows-based laptops form the largest portion of the sample.

---

### 5.3 RAM Distribution

| RAM | Listings |
|---|---:|
| 4 GB | 3 |
| 8 GB | 7 |
| 16 GB | 10 |

The sample contains more 16 GB listings than 4 GB and 8 GB listings combined.

---

### 5.4 Storage Distribution

| Storage | Listings |
|---|---:|
| 64 GB | 1 |
| 128 GB | 4 |
| 256 GB | 2 |
| 512 GB | 13 |

512 GB is the most common storage category in the collected sample.

---

## 6. Price Analysis

### 6.1 Average Selling Price by Brand

| Brand | Average Selling Price |
|---|---:|
| Apple | ₹149,900 |
| Lenovo | ₹113,365 |
| DELL | ₹97,490 |
| MOTOROLA | ₹77,490 |
| ASUS | ₹70,990 |
| Samsung | ₹69,990 |
| Acer | ₹43,490 |
| HP | ₹41,418 |
| Primebook | ₹30,823.33 |
| Neopticon | ₹22,499 |

The sample shows substantial variation in average selling price across brands.

---

### 6.2 Average Selling Price by RAM

| RAM | Average Selling Price |
|---|---:|
| 4 GB | ₹21,826.33 |
| 8 GB | ₹38,053.29 |
| 16 GB | ₹119,713.30 |

The 16 GB category has a substantially higher average selling price in this sample.

---

### 6.3 Average Selling Price by Storage

| Storage | Average Selling Price |
|---|---:|
| 64 GB | ₹15,990 |
| 128 GB | ₹27,242.25 |
| 256 GB | ₹34,990 |
| 512 GB | ₹102,618.92 |

Higher storage categories are associated with higher average selling prices in this sample.

---

## 7. Rating Analysis

The highest-rated products in the sample include:

- Apple MacBook Air M5
- Lenovo Legion 5
- Motorola Motobook 60 Pro
- Motorola Motobook 60

The highest average brand rating in the sample is observed for Apple at 4.70.

Ratings should be interpreted together with ratings count, reviews count, product specifications, and price.

---

## 8. Discount and Price Difference Analysis

The largest price differences between original price and selling price include:

| Product | Price Difference |
|---|---:|
| Lenovo Legion 5 | ₹138,400 |
| Lenovo LOQ | ₹109,700 |
| Motorola Motobook 60 | ₹65,010 |
| Motorola Motobook 60 Pro | ₹60,010 |
| Acer Aspire 3 | ₹45,009 |

The largest average discounts among brands with available discount values include:

| Brand | Average Discount |
|---|---:|
| Lenovo | 45.75% |
| MOTOROLA | 44.50% |
| Acer | 38.50% |
| Primebook | 31.00% |
| DELL | 27.50% |
| Samsung | 24.00% |
| ASUS | 21.00% |
| Neopticon | 11.00% |

Original price and discount values are unavailable for some listings, so discount analysis is based only on records where those values were present.

---

## 9. Relationship and Correlation Analysis

Correlation with selling price in the sample includes:

| Variable | Correlation with Selling Price |
|---|---:|
| RAM_GB | 0.72 |
| Storage_GB | 0.59 |
| Rating | 0.69 |
| Screen_Size_Inches | 0.16 |
| Ratings_Count | -0.27 |
| Reviews_Count | -0.32 |
| Discount | -0.09 |

`Original_Price` and `Price_Difference` also show strong relationships with selling price, but both are pricing-derived variables rather than independent laptop specifications.

Correlation represents association and does not establish causation.

---

## 10. SQL Analysis

A SQLite database was created from the cleaned dataset.

The SQL analysis examined:

- Listings by brand
- Average selling price by brand
- Average selling price by RAM
- Average discount by brand
- Largest price differences
- High-rated laptops below ₹80,000
- Duplicate product checks

The database is stored as:

```text
data/flipkart_laptops.db