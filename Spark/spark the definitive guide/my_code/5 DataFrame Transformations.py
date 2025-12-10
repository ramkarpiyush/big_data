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

# my_df.show()
'''
+-----+----+----+
| some|colu|name|
+-----+----+----+
|Hello|null|   1|
+-----+----+----+
'''

# my_df.printSchema()
'''
root
 |-- some: string (nullable = true)
 |-- colu: string (nullable = true)
 |-- name: long (nullable = false)
'''

# Read data:
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("5 Basic Structured Operations").getOrCreate()
df = spark.read.format("json").load("D:\\GitLocal\\Spark-The-Definitive-Guide\\data\\flight-data\\json\\2015-summary.json")
#df.show()

# Schema enforcement:
from pyspark.sql.types import StructType, StructField, StringType, LongType
my_manual_schema = StructType([
    StructField("DEST_COUNTRY_NAME", StringType(), True),
    StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
    StructField("count", LongType(), False, metadata={"hello":"world"})
])


df = spark.read.format("json").schema(my_manual_schema).load("D:\\GitLocal\\Spark-The-Definitive-Guide\\data\\flight-data\\json\\2015-summary.json")
# df.show()
# df.printSchema()



# ======================================================================================================

data = [
    ("John", "USA", 30),
    ("Alice", "UK", 25),
    ("Bob", "Canada", 28),
    ("David", "Germany", 35),
    ("Eva", "France", 22),
    ("Frank", "Italy", 33),
    ("Grace", "Spain", 29),
    ("Helen", "Australia", 26),
    ("Ivan", "Russia", 31),
    ("Jane", "India", 27)
]

columns = ["name", "country", "age"]

df2 = spark.createDataFrame(data, columns)

# select and selectExpr:

df_select = df2.select("name", "age")

#
from pyspark.sql.functions import col, expr, column

# df2.select("name", "country", "age").show()


df2.select(
    expr("name AS full_name"),
    col("country"), 
    column("age")).show()

df2.select(
    expr("name AS full_name").alias("name"),
    col("country"), 
    column("age")).show(3)

# df.show(2)
df.select(expr("DEST_COUNTRY_NAME as destination")).show(1)

df.select(expr("DEST_COUNTRY_NAME as destination").alias("DEST_COUNTRY_NAME")).show(2)

# selectExpr:

df.selectExpr(
    "*", "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as within_country").show(3)


df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(4)


# =====================================================================================================
# Converting to Spark Types (Literals):

from pyspark.sql.functions import lit

df.select(expr("*"), lit(1).alias("One")).show()

df.withColumn("numberOne", lit(1)).show(2)

df.withColumn("within_country", expr("ORIGIN_COUNTRY_NAME = DEST_COUNTRY_NAME")).show(2)

df.withColumn("Destination", expr("DEST_COUNTRY_NAME")).show()

df.withColumn("Destination", expr("DEST_COUNTRY_NAME")).columns


# Reserved characters and keywords:

df_with_longname = df.withColumn("This Long Column-Name", expr("ORIGIN_COUNTRY_NAME"))

df_with_longname.selectExpr(
    "`This Long Column-Name`",
    "`This Long Column-Name` as `new col`"
).show(1)


df.drop("ORIGIN_COUNTRY_NAME").show()


# Changing a columns Type (Cast):
df.withColumn("count2", col("count").cast("long")).printSchema()

df.withColumn("count2", col("count").cast("integer")).printSchema()

df.withColumn("count2", col("count").cast("float")).printSchema()
df.withColumn("count2", col("count").cast("float")).show()


# Filtering Rows:
df.filter(col("count") < 2).show(2)

df.where("count < 2").show(2)

df.where(col("count")<2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia").show(2)

# Getting unique rows:

df.select("ORIGIN_COUNTRY_NAME").distinct().show()

print(df.select("ORIGIN_COUNTRY_NAME").distinct().count())                          # output: 125


print(df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count())     # output: 256


# Random Samples:

seed = 5
withReplacement = False
fraction = 0.5

df.sample(withReplacement, fraction, seed).show()
print(df.sample(withReplacement, fraction, seed).count())