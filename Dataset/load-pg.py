from pyspark.sql import SparkSession
from pyspark.sql.functions import count

spark = SparkSession.builder \
    .appName("Load-Csv-Pg") \
    .getOrCreate()

csv_path = r"D:\gitlocal\big_data\Dataset\products-1m.csv"

df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(csv_path)
# df.show(1, False)
# df.select(count("*").alias("total_rows")).show()
# df.printSchema()

jdbc_url = "jdbc:postgresql://localhost:5432/postgres"

# df.write \
#   .format("jdbc") \
#   .option("url", jdbc_url) \
#   .option("dbtable", "myschema.products") \
#   .option("user", "postgres") \
#   .option("password", "postgres") \
#   .option("driver", "org.postgresql.Driver") \
#   .option("batchsize", 100) \
#   .mode("append") \
#   .save()

# print("Data successfully written to PostgreSQL")

# Run spark-submit:
# spark-submit --packages org.postgresql:postgresql:42.6.0 load-pg.py


from pyspark.sql.functions import col
# clean_columns = [c.replace("-", "_").replace(" ", "_") for c in df.columns]
# df = df.toDF(*clean_columns)

df.show(1, False)
# df.printSchema()

