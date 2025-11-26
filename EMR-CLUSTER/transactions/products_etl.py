# products_etl.py
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

raw_path = "s3://murali-20-retail/raw/products/"
curated_path = "s3://murali-20-retail/curated/products/"

df = spark.read.option("header","true").option("inferSchema","true").csv(raw_path)
df = df.toDF(*[c.replace('\ufeff','') for c in df.columns])

df2 = df.withColumn("product_id", col("product_id").cast("string")) \
        .withColumn("product_name", col("product_name").cast("string")) \
        .withColumn("category", col("category").cast("string")) \
        .withColumn("price", col("price").cast("double"))

df2.repartition(1).write.mode("overwrite").parquet(curated_path)
