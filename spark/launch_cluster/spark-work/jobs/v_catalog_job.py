from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import json
import requests

# -------------------------------
# Step 1: Spark Session
# -------------------------------
spark = SparkSession.builder \
    .appName("Catalog CSV to Vespa") \
    .getOrCreate()

# -------------------------------
# Step 2: Read CSV
# -------------------------------
df = spark.read.csv(
    "/opt/spark/work/data/catalog.csv",
    header=True,
    inferSchema=True
)

df = df.toDF("id", "name", "category", "price", "brand")

# -------------------------------
# Step 3: Transform
# -------------------------------
clean_df = df.select(
    col("id"),
    col("name"),
    col("category"),
    col("brand"),
    col("price").cast("int")
)

# -------------------------------
# Step 4: Push to Vespa
# -------------------------------

VESPA_URL = "http://vespa-feed:8080"

for row in clean_df.collect():

    doc_id = row["id"]

    vespa_doc = {
        "fields": {
            "id": row["id"],
            "name": row["name"],
            "category": row["category"],
            "brand": row["brand"],
            "price": row["price"]
        }
    }

    url = f"{VESPA_URL}/document/v1/catalog/catalog/docid/{doc_id}"

    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(vespa_doc)
    )

    print(doc_id, response.status_code)

spark.stop()
