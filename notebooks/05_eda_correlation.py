import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# 1. Load cleaned dataset
# =========================================================

df = pd.read_csv("data/cleaned_flipkart_laptops.csv")


print("=" * 60)
print("CORRELATION AND GROUPED PRICE ANALYSIS")
print("=" * 60)


# =========================================================
# 2. Select numerical columns
# =========================================================

numeric_columns = [
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

numeric_df = df[numeric_columns]


# =========================================================
# 3. Correlation matrix
# =========================================================

correlation_matrix = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))


# =========================================================
# 4. Correlation with Selling Price
# =========================================================

price_correlation = (
    correlation_matrix["Selling_Price"]
    .sort_values(ascending=False)
)

print("\nCorrelation with Selling Price:")
print(price_correlation.round(2))


# =========================================================
# 5. Average price by RAM
# =========================================================

ram_price = (
    df.groupby("RAM_GB", dropna=True)["Selling_Price"]
    .agg(["count", "mean", "min", "max"])
    .round(2)
)

print("\nSelling Price by RAM:")
print(ram_price)


# =========================================================
# 6. Average price by Storage
# =========================================================

storage_price = (
    df.groupby("Storage_GB", dropna=True)["Selling_Price"]
    .agg(["count", "mean", "min", "max"])
    .round(2)
)

print("\nSelling Price by Storage:")
print(storage_price)


# =========================================================
# 7. Average price by Brand
# =========================================================

brand_price = (
    df.groupby("Brand")["Selling_Price"]
    .agg(["count", "mean", "min", "max"])
    .sort_values("mean", ascending=False)
    .round(2)
)

print("\nSelling Price by Brand:")
print(brand_price)


# =========================================================
# 8. Correlation Heatmap
# =========================================================

plt.figure(figsize=(12, 9))

plt.imshow(
    correlation_matrix,
    interpolation="nearest",
    aspect="auto"
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.title("Correlation Matrix - Flipkart Laptops")

plt.tight_layout()

plt.savefig(
    "images/correlation_matrix.png",
    dpi=300
)

plt.close()


print("\nCorrelation chart saved:")
print("images/correlation_matrix.png")