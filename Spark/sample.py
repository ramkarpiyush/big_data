from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Read-parquet-app")
    .config("spark.hadoop.io.native.lib.available", "false")        # This tells Spark: Don’t use Windows native Hadoop libraries
    .getOrCreate()
)

df = spark.read.format("parquet").load(r"D:/gitlocal/Spark-The-Definitive-Guide/data/flight-data/parquet/2010-summary.parquet")
df.show()