from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("5 Basic Structured Operations").getOrCreate()

df = spark.read.format("json").load("D:\GitLocal\Spark-The-Definitive-Guide\data\flight-data\json\2015-summary.json")

df.printSchema()

print(spark.read.format("json").load("Spark-The-Definitive-Guide\data\flight-data\json\2015-summary.json").schema)


from pyspark.sql.types import StructType, StructField, StringType, LongType
my_manual_schema = StructType([
    StructField("DEST_COUNTRY_NAME", StringType(), True),
    StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
    StructField("count", LongType(), False, metadata={"hello":"world"})
])

df = spark.read.format("json").schema(my_manual_schema).load("spark_book/Spark-The-Definitive-Guide/data/flight-data/json/2015-summary.json")
#df.show()
df.printSchema()

"""
root
 |-- DEST_COUNTRY_NAME: string (nullable = true)
 |-- ORIGIN_COUNTRY_NAME: string (nullable = true)
 |-- count: long (nullable = true)

#Why nullable=True Despite False in Schema?
When you provide a schema using .schema(...), Spark uses it as a guideline, but it still validates it against the actual data. 
If the data contains any null values in the count column, Spark will override your nullable=False and mark it as nullable=True to avoid runtime errors.
"""

null_count = df.filter(df["count"].isNull()).count()
print(null_count)
print(my_manual_schema)


from pyspark.sql.functions import col, column
from pyspark.sql import functions as F

print(spark.read.format("json").load("spark_book/Spark-The-Definitive-Guide/data/flight-data/json/2015-summary.json").columns)

df.select(F.col("count")).show()

print(df.first())

from pyspark.sql import Row
my_row = Row("Hello", None, 1, False)
print(my_row[0])



from pyspark.sql.types import StructType, StructField, StringType, LongType
from pyspark.sql import Row

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("5 Basic Structured Operations").getOrCreate()

my_schema = StructType([
    StructField("some", StringType(), True),
    StructField("colu", StringType(), True),
    StructField("name", LongType(), False)
    ])

my_row = Row("Hello", None, 1)

my_df = spark.createDataFrame([my_row], my_schema)
my_df.show()