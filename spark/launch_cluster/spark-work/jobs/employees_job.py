from pyspark.sql import SparkSession

# create SparkSession
spark = SparkSession.builder.appName("avg-salary-per-dept").getOrCreate()

input_path = "/opt/spark/work/data/employees.csv"
output_path = "/opt/spark/work/output/avg_salary"

df = spark.read.csv(input_path, header=True, inferSchema=True)

(df.groupBy("dept")
   .avg("salary")
   .withColumnRenamed("avg(salary)", "avg_salary")
   .write
   .mode("overwrite")
   .csv(output_path))

spark.stop()