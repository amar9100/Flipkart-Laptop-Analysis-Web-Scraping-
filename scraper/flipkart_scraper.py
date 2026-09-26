import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlsplit
import re
import pandas as pd


# =========================================================
# 1. Flipkart URL
# =========================================================

url = "https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g"


# =========================================================
# 2. Browser headers
# =========================================================

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/140.0.0.0 Safari/537.36"
    )
}


# =========================================================
# 3. Request page
# =========================================================

response = requests.get(
    url,
    headers=headers,
    timeout=20
)

print("Status Code:", response.status_code)

if response.status_code != 200:
    raise Exception(
        f"Failed to download Flipkart page. "
        f"Status code: {response.status_code}"
    )


# =========================================================
# 4. Parse HTML
# =========================================================

soup = BeautifulSoup(
    response.text,
    "lxml"
)


# =========================================================
# 5. Find all links
# =========================================================

links = soup.find_all("a")


# =========================================================
# 6. Storage
# =========================================================

products = []

seen_urls = set()

seen_products = set()


# =========================================================
# 7. Process links
# =========================================================

for link in links:

    href = link.get("href")
    text = link.get_text(" ", strip=True)

    # -----------------------------------------------------
    # Basic validation
    # -----------------------------------------------------

    if not href or not text:
        continue

    if "/p/" not in href:
        continue


    # -----------------------------------------------------
    # Skip unavailable listings
    # -----------------------------------------------------

    if re.match(
        r"^Currently unavailable\b",
        text,
        re.IGNORECASE
    ):
        continue


    # -----------------------------------------------------
    # Remove Add to Compare
    # -----------------------------------------------------

    text = text.replace(
        "Add to Compare",
        "",
        1
    ).strip()


    if not text:
        continue


    # =====================================================
    # 8. Rating / Reviews
    #
    # Rating information is optional.
    # =====================================================

    rating_match = re.search(
        r"(\d(?:\.\d)?)\s*"
        r"([\d,]+)\s+Ratings\s*&\s*"
        r"([\d,]+)\s+Reviews",
        text
    )


    if rating_match:

        rating = float(
            rating_match.group(1)
        )

        ratings_count = int(
            rating_match.group(2).replace(",", "")
        )

        reviews_count = int(
            rating_match.group(3).replace(",", "")
        )

        # Product name is before the rating
        product_name = text[
            :rating_match.start()
        ].strip()

        # Details are after the rating/reviews
        details = text[
            rating_match.end():
        ].strip()


    else:

        # ---------------------------------------------
        # Product has no rating/review information
        # ---------------------------------------------

        rating = None
        ratings_count = None
        reviews_count = None

        # Find the first "Processor"
        processor_marker = re.search(
            r"\bProcessor\b",
            text,
            re.IGNORECASE
        )

        if processor_marker:

            product_name = text[
                :processor_marker.start()
            ].strip()

            details = text[
                processor_marker.start():
            ].strip()

        else:

            # Fallback: use text before first ₹
            price_marker = re.search(
                r"₹",
                text
            )

            if price_marker:

                product_name = text[
                    :price_marker.start()
                ].strip()

                details = text[
                    price_marker.start():
                ].strip()

            else:

                product_name = text.strip()

                details = ""


    # =====================================================
    # 9. Clean numbered prefixes
    # =====================================================

    product_name = re.sub(
        r"^\d+\.\s*",
        "",
        product_name
    ).strip()


    if not product_name:
        continue


    # =====================================================
    # 10. Brand
    # =====================================================

    brand = (
        product_name.split()[0]
        if product_name
        else "Unknown"
    )


    # =====================================================
    # 11. Processor
    # =====================================================

    processor_match = re.search(
        r"(.+?)\s+Processor\b",
        details,
        re.IGNORECASE
    )

    processor = (
        processor_match.group(1).strip()
        if processor_match
        else None
    )


    # =====================================================
    # 12. RAM
    # =====================================================

    ram_match = re.search(
        r"(\d+)\s*GB\s+.*?RAM",
        details,
        re.IGNORECASE
    )

    ram = (
        ram_match.group(1) + " GB"
        if ram_match
        else None
    )


    # =====================================================
    # 13. Operating System
    # =====================================================

    os_match = re.search(
        r"RAM\s+(.+?)\s+Operating System",
        details,
        re.IGNORECASE
    )

    if os_match:

        operating_system = (
            os_match.group(1)
            .strip()
        )

    elif re.search(
        r"Chrome\s+OS",
        product_name,
        re.IGNORECASE
    ):

        operating_system = "Chrome OS"

    else:

        operating_system = None


    # Remove "64 bit"
    if operating_system:

        operating_system = re.sub(
            r"^64\s*bit\s+",
            "",
            operating_system,
            flags=re.IGNORECASE
        ).strip()


    # Normalize Chrome
    if (
        operating_system
        and operating_system.lower() == "chrome"
    ):

        operating_system = "Chrome OS"


    # =====================================================
    # 14. Storage
    # =====================================================

    storage = None


    # -----------------------------------------------------
    # Search details
    # -----------------------------------------------------

    storage_match = re.search(
        r"(\d+(?:\.\d+)?)\s*"
        r"(GB|TB)\s+"
        r"(SSD|EMMC|HDD)\b",
        details,
        re.IGNORECASE
    )

    if storage_match:

        storage = (
            f"{storage_match.group(1)} "
            f"{storage_match.group(2)} "
            f"{storage_match.group(3)}"
        )


    # -----------------------------------------------------
    # Search product name
    # -----------------------------------------------------

    if storage is None:

        storage_match = re.search(
            r"(\d+(?:\.\d+)?)\s*"
            r"(GB|TB)\s+"
            r"(SSD|EMMC|HDD)\b",
            product_name,
            re.IGNORECASE
        )

        if storage_match:

            storage = (
                f"{storage_match.group(1)} "
                f"{storage_match.group(2)} "
                f"{storage_match.group(3)}"
            )


    # -----------------------------------------------------
    # Primebook-style storage
    #
    # Example:
    # (8 GB/128 GB/Android 15)
    # -----------------------------------------------------

    if storage is None:

        title_storage_match = re.search(
            r"\(\s*"
            r"\d+\s*GB\s*/\s*"
            r"(\d+(?:\.\d+)?)\s*"
            r"(GB|TB)\s*/",
            product_name,
            re.IGNORECASE
        )

        if title_storage_match:

            storage = (
                f"{title_storage_match.group(1)} "
                f"{title_storage_match.group(2)}"
            )


    # =====================================================
    # 15. Screen Size
    # =====================================================

    screen_match = re.search(
        r"(\d+(?:\.\d+)?)\s*cm\s*"
        r"\(([\d.]+)\s*inch",
        details,
        re.IGNORECASE
    )

    screen_size = (
        screen_match.group(2) + " inch"
        if screen_match
        else None
    )


    # =====================================================
    # 16. Selling Price / Original Price / Discount
    # =====================================================

    price_match = re.search(
        r"₹\s*([\d,]+)"
        r"(?:\s*₹\s*([\d,]+)\s*"
        r"(\d+)%\s*off)?",
        text,
        re.IGNORECASE
    )


    if price_match:

        selling_price = int(
            price_match.group(1).replace(",", "")
        )


        if price_match.group(2):

            original_price = int(
                price_match.group(2).replace(",", "")
            )

        else:

            original_price = None


        if price_match.group(3):

            discount = int(
                price_match.group(3)
            )

        else:

            discount = None

    else:

        selling_price = None
        original_price = None
        discount = None


    # =====================================================
    # 17. Clean Product URL
    # =====================================================

    raw_product_url = urljoin(
        "https://www.flipkart.com",
        href
    )

    parsed_url = urlsplit(
        raw_product_url
    )

    product_url = (
        f"{parsed_url.scheme}://"
        f"{parsed_url.netloc}"
        f"{parsed_url.path}"
    )


    # =====================================================
    # 18. Remove duplicate URL paths
    # =====================================================

    if product_url in seen_urls:
        continue

    seen_urls.add(product_url)


    # =====================================================
    # 19. Remove repeated product records
    #
    # Same brand + product name + selling price
    # =====================================================

    product_key = (
        brand.strip().lower(),
        product_name.strip().lower(),
        selling_price
    )

    if product_key in seen_products:
        continue

    seen_products.add(
        product_key
    )


    # =====================================================
    # 20. Store record
    # =====================================================

    products.append({

        "Product_Name": product_name,

        "Brand": brand,

        "Processor": processor,

        "RAM": ram,

        "Storage": storage,

        "Screen_Size": screen_size,

        "Operating_System": operating_system,

        "Rating": rating,

        "Ratings_Count": ratings_count,

        "Reviews_Count": reviews_count,

        "Selling_Price": selling_price,

        "Original_Price": original_price,

        "Discount": discount,

        "Product_URL": product_url

    })


# =========================================================
# 21. Create DataFrame
# =========================================================

df = pd.DataFrame(
    products
)


# =========================================================
# 22. Save raw dataset
# =========================================================

output_file = (
    "data/raw_flipkart_laptops.csv"
)

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


# =========================================================
# 23. Summary
# =========================================================

print("\n" + "=" * 40)
print("SCRAPING COMPLETED")
print("=" * 40)

print(
    "Products collected:",
    len(df)
)

print(
    "Columns:",
    len(df.columns)
)

print("\nColumns collected:")

for column in df.columns:
    print("-", column)


print("\nMissing values:")

print(
    df.isnull().sum()
)


print("\nDataset preview:")

print(
    df.head().to_string(
        index=False
    )
)


print("\nSaved to:")

print(
    output_file
)