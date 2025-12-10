from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("5 Basic Structured Operations").getOrCreate()

from pyspark.sql.types import StructType, StructField, StringType, LongType
my_manual_schema = StructType([
    StructField("DEST_COUNTRY_NAME", StringType(), True),
    StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
    StructField("count", LongType(), False, metadata={"hello":"world"})
])

df = spark.read.format("json").schema(my_manual_schema).load("D:\\GitLocal\\Spark-The-Definitive-Guide\\data\\flight-data\\json\\2015-summary.json")
df.printSchema()