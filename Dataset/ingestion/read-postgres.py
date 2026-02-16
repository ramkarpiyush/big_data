from pyspark.sql import SparkSession
import os
from loguru import logger
from pyspark.sql.functions import count
import re

spark = SparkSession.builder \
    .appName("Load-CSV-Pg")\
    .config("spark.jars.packages", "org.postgresql:postgresql:42.6.0")\
    .getOrCreate() 

jdbc_url = "jdbc:postgresql://localhost:5432/postgres"

properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
}

# df = spark.read.jdbc(
#     url=jdbc_url,
#     table="public.your_table_name",
#     properties=properties
# )

df = (
    spark.read.format("jdbc")
    .option("url", jdbc_url)
    .option("dbtable", "myschema.products")
    .option("user", "postgres")
    .option("password", "postgres")
    .option("driver", "org.postgresql.Driver")
    .option("partitionColumn", "Index")     # Must be numeric column
    .option("lowerBound", 1)
    .option("upperBound", 1000000)
    .option("numPartitions", 8)
    .load()
)

df.show(1)
df.printSchema()

query2 = """
(
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'myschema'
) AS tbl
"""

# df = spark.read.jdbc(
#     url=jdbc_url,
#     table=query2,
#     properties=properties
# )

# df.show()
# df.printSchema()

import psycopg

def pg_conn():
    conn = psycopg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres"
    )
    return conn


def execute_query(query):
    with psycopg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()



with pg_conn() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'myschema'
        """)
        
        for row in cur.fetchall():
            print(row[0])


tables = execute_query("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'myschema'
""")

for table in tables:
    print(table[0])





# try:
#     with psycopg.connect(
#         host="localhost",
#         dbname="postgres",
#         user="postgres",
#         password="postgres"
#     ) as conn:
        
#         with conn.cursor() as cur:
#             cur.execute("""
#                 SELECT table_name
#                 FROM information_schema.tables
#                 WHERE table_schema = 'myschema';
#             """)
            
#             for row in cur.fetchall():
#                 print(row[0])

# except Exception as e:
#     print("Error:", e)

