from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import json
import requests

# -------------------------------
# Step 1: Spark Session
# -------------------------------
spark = SparkSession.builder \
    .appName("Catalog CSV to Solr") \
    .getOrCreate()

# -------------------------------
# Step 2: Read CSV (EXTRACT)
# -------------------------------
# df = spark.read.csv(
#     "/opt/spark/work/data/catalog.csv",
#     header=True,
#     inferSchema=True
# )

# df = spark.read \
#     .option("header", "true") \
#     .option("inferSchema", "true") \
#     .option("encoding", "UTF-8") \
#     .csv("/opt/spark/work/data/catalog.csv")


df = spark.read.csv(
    "/opt/spark/work/data/catalog.csv",
    header=True,
    inferSchema=True
)

# FORCE column names (this bypasses header issues entirely)
df = df.toDF("id", "name", "category", "price", "brand")


# -------------------------------
# Step 3: Transform Data (TRANSFORM)
# -------------------------------
clean_df = df.select(
    col("id"),
    col("name"),
    col("category"),
    col("brand"),
    col("price").cast("double")
)

# -------------------------------
# Step 4: Push to Solr (LOAD)
# -------------------------------
SOLR_URL = "http://host.docker.internal:8983/solr/catalog/update?commit=true"

docs = []
for row in clean_df.collect():   # small catalog → OK
    docs.append({
        "id": row["id"],
        "name": row["name"],
        "category": row["category"],
        "brand": row["brand"],
        "price": row["price"]
    })

headers = {"Content-Type": "application/json"}
response = requests.post(
    SOLR_URL,
    headers=headers,
    data=json.dumps(docs)
)

print("Solr response:", response.status_code)

spark.stop()
