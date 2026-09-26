import pandas as pd
import numpy as np

# =========================================================
# 1. Load raw dataset
# =========================================================

input_file = "data/raw_flipkart_laptops.csv"

df = pd.read_csv(input_file)

print("Raw shape:", df.shape)


# =========================================================
# 2. Clean text columns
# =========================================================

text_columns = [
    "Product_Name",
    "Brand",
    "Processor",
    "RAM",
    "Storage",
    "Screen_Size",
    "Operating_System",
    "Product_URL"
]

for column in text_columns:
    df[column] = df[column].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )


# =========================================================
# 3. Convert RAM to numeric GB
# =========================================================

df["RAM_GB"] = pd.to_numeric(
    df["RAM"].str.extract(r"(\d+(?:\.\d+)?)")[0],
    errors="coerce"
)


# =========================================================
# 4. Convert Screen Size to numeric inches
# =========================================================

df["Screen_Size_Inches"] = pd.to_numeric(
    df["Screen_Size"].str.extract(r"([\d.]+)")[0],
    errors="coerce"
)


# =========================================================
# 5. Convert Storage to numeric GB
# =========================================================

storage_value = pd.to_numeric(
    df["Storage"].str.extract(r"([\d.]+)")[0],
    errors="coerce"
)

storage_unit = (
    df["Storage"]
    .str.extract(r"(GB|TB)", expand=False)
    .str.upper()
)

df["Storage_GB"] = np.where(
    storage_unit == "TB",
    storage_value * 1024,
    storage_value
)


# =========================================================
# 6. Ensure numeric columns are numeric
# =========================================================

numeric_columns = [
    "Rating",
    "Ratings_Count",
    "Reviews_Count",
    "Selling_Price",
    "Original_Price",
    "Discount"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# =========================================================
# 7. Remove duplicate rows
# =========================================================

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print("\nDuplicates removed:",
      before_duplicates - after_duplicates)


# =========================================================
# 8. Create price difference
# =========================================================

df["Price_Difference"] = (
    df["Original_Price"] - df["Selling_Price"]
)


# =========================================================
# 9. Display cleaned information
# =========================================================

print("\nCleaned shape:", df.shape)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nCleaned preview:")
print(df.head().to_string(index=False))


# =========================================================
# 10. Save cleaned dataset
# =========================================================

output_file = "data/cleaned_flipkart_laptops.csv"

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("\nCleaned dataset saved to:")
print(output_file)