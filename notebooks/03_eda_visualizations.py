import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# 1. Load cleaned dataset
# =========================================================

df = pd.read_csv("data/cleaned_flipkart_laptops.csv")


# =========================================================
# 2. Brand Distribution
# =========================================================

brand_counts = df["Brand"].value_counts()

plt.figure(figsize=(10, 6))

brand_counts.plot(kind="bar")

plt.title("Number of Laptops by Brand")
plt.xlabel("Brand")
plt.ylabel("Number of Laptops")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "images/brand_distribution.png",
    dpi=300
)

plt.show()


# =========================================================
# 3. Selling Price Distribution
# =========================================================

plt.figure(figsize=(10, 6))

df["Selling_Price"].plot(
    kind="hist",
    bins=10
)

plt.title("Selling Price Distribution")
plt.xlabel("Selling Price (INR)")
plt.ylabel("Number of Laptops")

plt.tight_layout()

plt.savefig(
    "images/selling_price_distribution.png",
    dpi=300
)

plt.show()


# =========================================================
# 4. Rating Distribution
# =========================================================

plt.figure(figsize=(10, 6))

df["Rating"].plot(
    kind="hist",
    bins=8
)

plt.title("Laptop Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Laptops")

plt.tight_layout()

plt.savefig(
    "images/rating_distribution.png",
    dpi=300
)

plt.show()


print("\nEDA charts created successfully.")

print("\nFiles saved:")
print("images/brand_distribution.png")
print("images/selling_price_distribution.png")
print("images/rating_distribution.png")