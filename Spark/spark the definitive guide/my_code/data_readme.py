from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("5 Basic Structured Operations").getOrCreate()

# Schema Enforcement:
from pyspark.sql.types import StructType, StructField, StringType, LongType
my_manual_schema = StructType([
    StructField("DEST_COUNTRY_NAME", StringType(), True),
    StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
    StructField("count", LongType(), False)
])

# Read Data:
df = spark.read.format("json").schema(my_manual_schema).load("D:\\GitLocal\\Spark-The-Definitive-Guide\\data\\flight-data\\json\\2015-summary.json")

df_csv = spark.read.format("csv").option("header", "true").load("D:\\GitLocal\\Spark-The-Definitive-Guide\\data\\retail-data\\by-day\\2010-12-01.csv")

df.printSchema()
df_csv.printSchema()