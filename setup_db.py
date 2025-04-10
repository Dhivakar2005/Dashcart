import sqlite3
import pandas as pd

DB_PATH = "smart_shopping.db"

# Load CSV files
customer_df = pd.read_csv("Smart-Shopping-Data-and-AI-for-Personalized-E-Commerce\data\customer_data_collection.csv")
product_df = pd.read_csv("Smart-Shopping-Data-and-AI-for-Personalized-E-Commerce\data\product_recommendation_data.csv")

print("Original Customer Columns:", customer_df.columns.tolist())
print("Original Product Columns:", product_df.columns.tolist())

# Adjust columns for customers (modify as needed)
customer_df.columns = [
    "CustomerID", "Age", "Gender", "Location", 
    "BrowsingHistory", "PurchaseHistory", "CustomerSegment", 
    "LoyaltyScore", "Holiday", "Season", "ExtraInfo"
]
print("Updated Customer Columns:", customer_df.columns.tolist())

# Adjust columns for products (modify as needed)
cols_to_drop = ["Similar_Product_List", "Probability_of_Recommendation", "Unnamed: 13", "Unnamed: 14"]
product_df = product_df.drop(columns=[c for c in cols_to_drop if c in product_df.columns], errors='ignore')
product_df.columns = [
    "ProductID", "Category", "SubCategory", "Price", 
    "Brand", "AvgRatingSimilar", "ProductRating", 
    "ReviewSentiment", "Holiday", "Season", "GeoLocation"
]
print("Updated Product Columns:", product_df.columns.tolist())

# Create/Populate the SQLite DB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS customers;")
cursor.execute("DROP TABLE IF EXISTS products;")

cursor.execute("""
CREATE TABLE customers (
    CustomerID TEXT PRIMARY KEY,
    Age INTEGER,
    Gender TEXT,
    Location TEXT,
    BrowsingHistory TEXT,
    PurchaseHistory TEXT,
    CustomerSegment TEXT,
    LoyaltyScore INTEGER,
    Holiday TEXT,
    Season TEXT,
    ExtraInfo TEXT
);
""")

cursor.execute("""
CREATE TABLE products (
    ProductID TEXT PRIMARY KEY,
    Category TEXT,
    SubCategory TEXT,
    Price REAL,
    Brand TEXT,
    AvgRatingSimilar REAL,
    ProductRating REAL,
    ReviewSentiment REAL,
    Holiday TEXT,
    Season TEXT,
    GeoLocation TEXT
);
""")
conn.commit()

customer_df.to_sql("customers", conn, if_exists="append", index=False)
product_df.to_sql("products", conn, if_exists="append", index=False)

conn.commit()
conn.close()
print("Database setup complete and CSV data imported!")
