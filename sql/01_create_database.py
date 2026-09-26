import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("data/cleaned_flipkart_laptops.csv")

# Create SQLite database
connection = sqlite3.connect("data/flipkart_laptops.db")

# Write dataframe to SQL table
df.to_sql(
    "laptops",
    connection,
    if_exists="replace",
    index=False
)

# Check number of rows
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM laptops")

row_count = cursor.fetchone()[0]

print("Database created successfully.")
print("Rows loaded into laptops table:", row_count)

connection.close()