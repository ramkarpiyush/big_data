### Read MySQL Db using Pyspark:
from pyspark.sql import SparkSession
spark = SparkSession\
    .builder\
    .appName("read-mysqldb-pyspark")\
    .config("spark.jars.packages", "com.mysql:mysql-connector-j:8.3.0")\
    .getOrCreate()
    # .config("spark.driver.extraClassPath", "/home/tuhin/mysql.jar")\

dataframe_mysql = spark.read\
    .format("jdbc")\
    .option("url", "jdbc:mysql://localhost/gdb041")\
    .option("driver", "com.mysql.jdbc.Driver")\
    .option("dbtable", "dim_customer").option("user", "root")\
    .option("password", "12345678").load()

dataframe_mysql.show(2)


### List all schemas from MySql Db:
jdbc_url = "jdbc:mysql://localhost:3306/information_schema?useSSL=false&allowPublicKeyRetrieval=true"

properties = {
    "user": "root",
    "password": "12345678",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Use a SELECT subquery wrapped in parentheses and give it an alias
query = """
(
  SELECT schema_name AS database_name
  FROM information_schema.schemata
  ORDER BY schema_name
) AS t
"""

query2 = """
(
SHOW SCHEMAS;
) AS tbl
"""

df = spark.read.jdbc(
    url=jdbc_url,
    table=query,     
    properties=properties
)

df.show(truncate=False)
df.printSchema()

### Read MySQL Db using Python:
import mysql.connector

DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"       
DB_PASSWORD = "12345678"  
DB_NAME = "gdb041"

def mysql_conn():
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    return conn

with mysql_conn() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SHOW TABLES;
        """)
        for row in cur.fetchall():
            print(row[0])