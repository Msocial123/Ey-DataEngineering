# transactions_etl.py
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, year, month, col, when
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

raw_path = "ss3://murali-20-retail/raw/transactions/"
curated_path = "s3://murali-20-retail/curated/transactions/"

df = spark.read.option("header","true").option("inferSchema","true").csv(raw_path)
df = df.toDF(*[c.replace('\ufeff','') for c in df.columns])

# parse timestamp and filter failures if you want only Success for revenue
df = df.withColumn("txn_time_ts", to_timestamp(col("txn_time"), "yyyy-MM-dd HH:mm:ss"))

# cast other columns
df = df.withColumn("transaction_id", col("transaction_id").cast("string")) \
       .withColumn("user_id", col("user_id").cast("string")) \
       .withColumn("product_id", col("product_id").cast("string")) \
       .withColumn("amount", col("amount").cast("double")) \
       .withColumn("quantity", col("quantity").cast("int")) \
       .withColumn("status", col("status").cast("string"))

# create year/month partitions for faster queries
df = df.withColumn("year", year(col("txn_time_ts"))) \
       .withColumn("month", month(col("txn_time_ts")))

# write partitioned parquet
df.write.mode("overwrite").partitionBy("year","month").parquet(curated_path)
