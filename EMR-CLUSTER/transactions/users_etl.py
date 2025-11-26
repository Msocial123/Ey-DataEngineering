# users_etl.py
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

raw_path = "s3://murali-20-retail/raw/users/"
curated_path = "s3://murali-20-retail/curated/users/"

# read csv with header, allow malformed rows to be dropped if any
df = spark.read.option("header","true") \
               .option("inferSchema","true") \
               .csv(raw_path)

# fix BOM in header if exists (common when file saved from Excel)
new_cols = [c.replace('\ufeff','') for c in df.columns]
df = df.toDF(*new_cols)

# rename columns if header row was read as data (very defensive)
# If first row contains header string values as first row, remove it:
first_row = df.first()
if first_row["user_id"] == "user_id"
df=df.filter(df["user_id"] != "user_id")

# if all(str(first_row[c]).lower().startswith(c.lower()) for c in df.columns):
#     df = df.filter(~(col(df.columns[0]) == first_row[df.columns[0]]))

# cast types and cleanup
df2 = df.withColumn("user_id", col("user_id").cast("string")) \
        .withColumn("name", col("name").cast("string")) \
        .withColumn("email", col("email").cast("string")) \
        .withColumn("city", col("city").cast("string")) \
        .withColumn("signup_date", col("signup_date").cast("date"))

# write parquet
df2.repartition(1).write.mode("overwrite").parquet(curated_path)
