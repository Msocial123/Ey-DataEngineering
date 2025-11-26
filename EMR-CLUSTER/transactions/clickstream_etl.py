# clickstream_etl.py
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, col
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

raw_path = "s3://murali-20-retail/raw/clickstream/"
curated_path = "s3://murali-20-retail/curated/clickstream/"

df = spark.read.json(raw_path)
# optional: normalize fields, parse time
df = df.withColumn("time_ts", to_timestamp(col("time"), "yyyy-MM-dd HH:mm:ss"))
df2 = df.select(col("user_id").cast("string"), col("page").cast("string"), col("time_ts"))

df2.repartition(1).write.mode("overwrite").parquet(curated_path)
