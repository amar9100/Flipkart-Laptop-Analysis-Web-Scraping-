import pandas as pd

# =========================================================
# 1. Load cleaned dataset
# =========================================================

df = pd.read_csv("data/cleaned_flipkart_laptops.csv")

print("=" * 60)
print("FLIPKART LAPTOP EDA")
print("=" * 60)


# =========================================================
# 2. Dataset overview
# =========================================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# =========================================================
# 3. Numerical summary
# =========================================================

print("\nNumerical Summary:")
print(
    df[
        [
            "Rating",
            "Ratings_Count",
            "Reviews_Count",
            "Selling_Price",
            "Original_Price",
            "Discount",
            "RAM_GB",
            "Storage_GB",
            "Screen_Size_Inches",
            "Price_Difference"
        ]
    ].describe()
)


# =========================================================
# 4. Brand distribution
# =========================================================

print("\nBrand Distribution:")
print(
    df["Brand"]
    .value_counts()
)


# =========================================================
# 5. Operating System distribution
# =========================================================

print("\nOperating System Distribution:")
print(
    df["Operating_System"]
    .value_counts(dropna=False)
)


# =========================================================
# 6. RAM distribution
# =========================================================

print("\nRAM Distribution:")
print(
    df["RAM_GB"]
    .value_counts()
    .sort_index()
)


# =========================================================
# 7. Storage distribution
# =========================================================

print("\nStorage Distribution:")
print(
    df["Storage_GB"]
    .value_counts()
    .sort_index()
)


# =========================================================
# 8. Average selling price by brand
# =========================================================

print("\nAverage Selling Price by Brand:")

brand_price = (
    df.groupby("Brand")["Selling_Price"]
    .mean()
    .sort_values(ascending=False)
)

print(brand_price)


# =========================================================
# 9. Average rating by brand
# =========================================================

print("\nAverage Rating by Brand:")

brand_rating = (
    df.groupby("Brand")["Rating"]
    .mean()
    .sort_values(ascending=False)
)

print(brand_rating)


# =========================================================
# 10. Most expensive laptops
# =========================================================

print("\nTop 5 Most Expensive Laptops:")

top_expensive = (
    df[
        [
            "Product_Name",
            "Brand",
            "Selling_Price",
            "Rating"
        ]
    ]
    .sort_values(
        "Selling_Price",
        ascending=False
    )
    .head(5)
)

print(
    top_expensive.to_string(index=False)
)


# =========================================================
# 11. Highest rated laptops
# =========================================================

print("\nTop 5 Highest Rated Laptops:")

top_rated = (
    df[
        [
            "Product_Name",
            "Brand",
            "Rating",
            "Ratings_Count"
        ]
    ]
    .sort_values(
        ["Rating", "Ratings_Count"],
        ascending=[False, False]
    )
    .head(5)
)

print(
    top_rated.to_string(index=False)
)