-- =========================================================
-- FLIPKART LAPTOP SQL ANALYSIS
-- Basic Queries
-- =========================================================


-- 1. View all laptops
SELECT *
FROM laptops;


-- 2. Count total laptops
SELECT COUNT(*) AS Total_Laptops
FROM laptops;


-- 3. Show unique brands
SELECT DISTINCT Brand
FROM laptops
ORDER BY Brand;


-- 4. Show laptops from highest to lowest selling price
SELECT
    Product_Name,
    Brand,
    Selling_Price
FROM laptops
ORDER BY Selling_Price DESC;


-- 5. Show laptops with rating 4.5 or higher
SELECT
    Product_Name,
    Brand,
    Rating,
    Selling_Price
FROM laptops
WHERE Rating >= 4.5
ORDER BY Rating DESC;