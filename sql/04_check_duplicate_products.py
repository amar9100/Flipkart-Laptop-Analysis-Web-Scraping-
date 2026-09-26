import sqlite3


connection = sqlite3.connect("data/flipkart_laptops.db")
cursor = connection.cursor()


print("\n" + "=" * 60)
print("CHECKING FOR REPEATED PRODUCTS")
print("=" * 60)


query = """
SELECT
    Brand,
    Product_Name,
    Selling_Price,
    COUNT(*) AS Occurrences
FROM laptops
GROUP BY
    Brand,
    Product_Name,
    Selling_Price
HAVING COUNT(*) > 1
ORDER BY Occurrences DESC;
"""


cursor.execute(query)

results = cursor.fetchall()


if results:

    print("\nRepeated products found:\n")

    for row in results:

        print(
            f"Brand: {row[0]}\n"
            f"Product: {row[1]}\n"
            f"Selling Price: ₹{row[2]:,.0f}\n"
            f"Occurrences: {row[3]}\n"
        )

else:

    print("\nNo repeated products found.")


connection.close()