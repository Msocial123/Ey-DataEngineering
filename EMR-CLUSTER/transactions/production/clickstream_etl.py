from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("TransactionAnalytics").getOrCreate()

# Read curated data
txn = spark.read.parquet("s3://murali-20-retail/curated/transactions/")
users = spark.read.parquet("s3://murali-20-retail/curated/users/")
prod = spark.read.parquet("s3://murali-20-retail/curated/products/")

# Join
df_join = txn.join(users, "user_id").join(prod, "product_id")

# Daily revenue
daily_rev = df_join.groupBy(to_date("txn_time").alias("day")) \
                   .agg(sum("amount").alias("total_revenue"))

# Top categories
top_categories = df_join.groupBy("category").agg(sum("amount").alias("cat_revenue"))

# Save outputs
daily_rev.write.mode("overwrite").parquet("s3://murali-20-retail/aggregated/daily_revenue/")
top_categories.write.mode("overwrite").parquet("s3://murali-20-retail/aggregated/top_categories/")
