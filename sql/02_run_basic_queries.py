import sqlite3


# =========================================================
# 1. Connect to SQLite database
# =========================================================

connection = sqlite3.connect("data/flipkart_laptops.db")

cursor = connection.cursor()


# =========================================================
# 2. Query 1 - Total laptops
# =========================================================

print("\n" + "=" * 60)
print("1. TOTAL LAPTOPS")
print("=" * 60)

query = """
SELECT COUNT(*) AS Total_Laptops
FROM laptops;
"""

cursor.execute(query)

result = cursor.fetchone()

print("Total laptops:", result[0])


# =========================================================
# 3. Query 2 - Unique brands
# =========================================================

print("\n" + "=" * 60)
print("2. UNIQUE BRANDS")
print("=" * 60)

query = """
SELECT DISTINCT Brand
FROM laptops
ORDER BY Brand;
"""

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row[0])


# =========================================================
# 4. Query 3 - Highest priced laptops
# =========================================================

print("\n" + "=" * 60)
print("3. TOP 5 MOST EXPENSIVE LAPTOPS")
print("=" * 60)

query = """
SELECT
    Product_Name,
    Brand,
    Selling_Price
FROM laptops
ORDER BY Selling_Price DESC
LIMIT 5;
"""

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(
        f"Brand: {row[1]} | "
        f"Price: ₹{row[2]:,.0f} | "
        f"Product: {row[0]}"
    )


# =========================================================
# 5. Query 4 - Highly rated laptops
# =========================================================

print("\n" + "=" * 60)
print("4. LAPTOPS WITH RATING 4.5 OR HIGHER")
print("=" * 60)

query = """
SELECT
    Product_Name,
    Brand,
    Rating,
    Selling_Price
FROM laptops
WHERE Rating >= 4.5
ORDER BY Rating DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(
        f"Brand: {row[1]} | "
        f"Rating: {row[2]} | "
        f"Price: ₹{row[3]:,.0f} | "
        f"Product: {row[0]}"
    )


# =========================================================
# 6. Close database connection
# =========================================================

connection.close()

print("\n" + "=" * 60)
print("SQL ANALYSIS COMPLETED")
print("=" * 60)