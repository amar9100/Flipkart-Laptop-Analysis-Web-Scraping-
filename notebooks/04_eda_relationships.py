import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# 1. Load cleaned dataset
# =========================================================

df = pd.read_csv("data/cleaned_flipkart_laptops.csv")


# =========================================================
# 2. Selling Price vs RAM
# =========================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["RAM_GB"],
    df["Selling_Price"]
)

plt.title("Selling Price vs RAM")
plt.xlabel("RAM (GB)")
plt.ylabel("Selling Price (INR)")

plt.tight_layout()

plt.savefig(
    "images/price_vs_ram.png",
    dpi=300
)

plt.close()


# =========================================================
# 3. Selling Price vs Storage
# =========================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Storage_GB"],
    df["Selling_Price"]
)

plt.title("Selling Price vs Storage")
plt.xlabel("Storage (GB)")
plt.ylabel("Selling Price (INR)")

plt.tight_layout()

plt.savefig(
    "images/price_vs_storage.png",
    dpi=300
)

plt.close()


# =========================================================
# 4. Selling Price vs Rating
# =========================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Rating"],
    df["Selling_Price"]
)

plt.title("Selling Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Selling Price (INR)")

plt.tight_layout()

plt.savefig(
    "images/price_vs_rating.png",
    dpi=300
)

plt.close()


# =========================================================
# 5. Selling Price Box Plot
# =========================================================

plt.figure(figsize=(8, 6))

plt.boxplot(
    df["Selling_Price"].dropna()
)

plt.title("Selling Price Box Plot")
plt.ylabel("Selling Price (INR)")

plt.tight_layout()

plt.savefig(
    "images/selling_price_boxplot.png",
    dpi=300
)

plt.close()


print("Relationship charts created successfully.")

print("\nFiles saved:")
print("images/price_vs_ram.png")
print("images/price_vs_storage.png")
print("images/price_vs_rating.png")
print("images/selling_price_boxplot.png")