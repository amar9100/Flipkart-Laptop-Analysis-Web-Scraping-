import sqlite3


# =========================================================
# 1. Connect to database
# =========================================================

connection = sqlite3.connect("data/flipkart_laptops.db")
cursor = connection.cursor()


# =========================================================
# 2. Brand listing count
# =========================================================

print("\n" + "=" * 60)
print("1. NUMBER OF LISTINGS BY BRAND")
print("=" * 60)

query = """
SELECT
    Brand,
    COUNT(*) AS Laptop_Count
FROM laptops
GROUP BY Brand
ORDER BY Laptop_Count DESC;
"""

cursor.execute(query)

for brand, count in cursor.fetchall():
    print(f"{brand}: {count}")


# =========================================================
# 3. Average selling price by brand
# =========================================================

print("\n" + "=" * 60)
print("2. AVERAGE SELLING PRICE BY BRAND")
print("=" * 60)

query = """
SELECT
    Brand,
    COUNT(*) AS Laptop_Count,
    ROUND(AVG(Selling_Price), 2) AS Average_Price,
    MIN(Selling_Price) AS Minimum_Price,
    MAX(Selling_Price) AS Maximum_Price
FROM laptops
GROUP BY Brand
ORDER BY Average_Price DESC;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(
        f"{row[0]} | "
        f"Count: {row[1]} | "
        f"Average: ₹{row[2]:,.2f} | "
        f"Min: ₹{row[3]:,.0f} | "
        f"Max: ₹{row[4]:,.0f}"
    )


# =========================================================
# 4. Average price by RAM
# =========================================================

print("\n" + "=" * 60)
print("3. AVERAGE SELLING PRICE BY RAM")
print("=" * 60)

query = """
SELECT
    RAM_GB,
    COUNT(*) AS Laptop_Count,
    ROUND(AVG(Selling_Price), 2) AS Average_Price
FROM laptops
WHERE RAM_GB IS NOT NULL
GROUP BY RAM_GB
ORDER BY RAM_GB;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(
        f"RAM: {row[0]:.0f} GB | "
        f"Count: {row[1]} | "
        f"Average Price: ₹{row[2]:,.2f}"
    )


# =========================================================
# 5. Average discount by brand
# =========================================================

print("\n" + "=" * 60)
print("4. AVERAGE DISCOUNT BY BRAND")
print("=" * 60)

query = """
SELECT
    Brand,
    COUNT(Discount) AS Products_With_Discount,
    ROUND(AVG(Discount), 2) AS Average_Discount
FROM laptops
WHERE Discount IS NOT NULL
GROUP BY Brand
ORDER BY Average_Discount DESC;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(
        f"{row[0]} | "
        f"Products: {row[1]} | "
        f"Average Discount: {row[2]}%"
    )


# =========================================================
# 6. Largest price differences
# =========================================================

print("\n" + "=" * 60)
print("5. TOP 5 PRICE DIFFERENCES")
print("=" * 60)

query = """
SELECT
    Brand,
    Product_Name,
    Selling_Price,
    Original_Price,
    Price_Difference
FROM laptops
WHERE Price_Difference IS NOT NULL
ORDER BY Price_Difference DESC
LIMIT 5;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(
        f"{row[0]} | "
        f"Selling: ₹{row[2]:,.0f} | "
        f"Original: ₹{row[3]:,.0f} | "
        f"Difference: ₹{row[4]:,.0f}\n"
        f"Product: {row[1]}\n"
    )


# =========================================================
# 7. High-rated laptops below ₹80,000
# =========================================================

print("\n" + "=" * 60)
print("6. HIGH-RATED LAPTOPS BELOW ₹80,000")
print("=" * 60)

query = """
SELECT
    Brand,
    Product_Name,
    Rating,
    Selling_Price,
    RAM_GB,
    Storage_GB
FROM laptops
WHERE Rating >= 4.4
  AND Selling_Price < 80000
ORDER BY Rating DESC, Selling_Price ASC;
"""

cursor.execute(query)

for row in cursor.fetchall():

    # Handle missing RAM safely
    if row[4] is not None:
        ram_display = f"{row[4]:.0f} GB"
    else:
        ram_display = "N/A"

    # Handle missing storage safely
    if row[5] is not None:
        storage_display = f"{row[5]:.0f} GB"
    else:
        storage_display = "N/A"

    print(
        f"{row[0]} | "
        f"Rating: {row[2]} | "
        f"Price: ₹{row[3]:,.0f} | "
        f"RAM: {ram_display} | "
        f"Storage: {storage_display}\n"
        f"Product: {row[1]}\n"
    )


# =========================================================
# 8. Close connection
# =========================================================

connection.close()

print("=" * 60)
print("BUSINESS SQL ANALYSIS COMPLETED")
print("=" * 60)