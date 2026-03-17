# =====================================
# ANALYTICS + SERVING LAYER
# =====================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum, avg, desc
import os
import time

# START
start_time = time.time()
print("=== ANALYTICS START ===")

# INIT SPARK
spark = SparkSession.builder \
    .appName("AnalyticsLayer") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# BUAT FOLDER SERVING
if not os.path.exists("data/serving"):
    os.makedirs("data/serving")

# LOAD DATA
print("Loading data...")
df = spark.read.parquet("data/clean/parquet/")
print("Jumlah data:", df.count())

# =========================
# TOTAL REVENUE
# =========================
print("Hitung Total Revenue...")
total_revenue = df.agg(_sum("total_amount").alias("total_revenue"))

total_revenue.show()

total_revenue.write.mode("overwrite") \
    .option("header", True) \
    .csv("data/serving/total_revenue")

# =========================
# TOP PRODUCT
# =========================
print("Top Products...")
top_products = df.groupBy("product") \
    .agg(_sum("quantity").alias("total_quantity")) \
    .orderBy(desc("total_quantity"))

top_products.show()

top_products.write.mode("overwrite") \
    .option("header", True) \
    .csv("data/serving/top_products")

# =========================
# CATEGORY REVENUE
# =========================
print("Category Revenue...")
category = df.groupBy("category") \
    .agg(_sum("total_amount").alias("category_revenue"))

category.show()

category.write.mode("overwrite") \
    .option("header", True) \
    .csv("data/serving/category_revenue")

# =========================
# AVG TRANSACTION
# =========================
print("Average Transaction...")
avg_trans = df.groupBy("customer_id") \
    .agg(avg("total_amount").alias("avg_transaction"))

avg_trans.show()

avg_trans.write.mode("overwrite") \
    .option("header", True) \
    .csv("data/serving/avg_transaction")

# STOP
spark.stop()

print("=== ANALYTICS SELESAI ===")
print("Waktu:", round(time.time() - start_time, 2), "detik")