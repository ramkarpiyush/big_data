from pyspark.sql import SparkSession
import os
from loguru import logger
from pyspark.sql.functions import count
import re
import mysql.connector


spark = SparkSession\
    .builder\
    .appName("read-mysqldb-pyspark")\
    .config("spark.jars.packages", "com.mysql:mysql-connector-j:8.3.0")\
    .getOrCreate()

folder_path = r"D:\gitlocal\big_data\Dataset"

jdbc_url = (
    "jdbc:mysql://127.0.0.1:3306/myschema"
    "?useSSL=false"
    "&allowPublicKeyRetrieval=true"
    "&serverTimezone=UTC"
)

def detect_format(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    format_map = {
        ".csv": "csv",
        ".json": "json",
        ".parquet": "parquet"
    }
    return format_map.get(ext, "unknown")

def read_data(file_path):
    file_format = detect_format(file_path)
    if file_format == "csv":
        df = spark.read.format("csv") \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .load(file_path)
    elif file_format == "json":
        df = spark.read.option("multiLine", "false").option("inferSchema", "true").json(file_path)
    elif file_format == "parquet":
        df = spark.read.parquet(file_path)
    else:
        raise ValueError(f"Unknown file format: {file_format}")
    return df


DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"       
DB_PASSWORD = "12345678"  
# DB_NAME = "gdb041"

def mysql_conn(database_name):
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=database_name,
    )
    return conn

def get_total_records(database_name, table_name):
    with mysql_conn(database_name) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {database_name}.{table_name}")
            count = [row[0] for row in cur.fetchall()]
            return count


for file_name in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file_name)

    if os.path.isfile(full_path):
        logger.info(f"File Path: {full_path}\nFormat: {detect_format(full_path)}")

        supported_formats = {"csv", "parquet", "json"}

        if detect_format(full_path) not in supported_formats:
            print(f"Skipping unsupported file: {file_name}")
            continue

        df = read_data(file_path=full_path)
        df.select(count("*").alias("total_rows")).show()
        df.printSchema()

        # Clean table name
        table_name = os.path.splitext(file_name)[0]
        table_name = re.sub(r'[^a-zA-Z0-9_]', '_', table_name).lower()

        mysql_table_name = table_name + "_" + detect_format(full_path)

        logger.info(f"Writing to table: myschema.{mysql_table_name}")

        # Clean columns
        clean_columns = [re.sub(r'[^a-zA-Z0-9_]', '_', c).lower() for c in df.columns]
        df = df.toDF(*clean_columns)
        df.show(1)

        # Write to MySQL
        df.write \
            .format("jdbc") \
            .option("url", jdbc_url) \
            .option("dbtable", f"{table_name}_{detect_format(full_path)}") \
            .option("user", "root") \
            .option("password", "12345678") \
            .option("driver", "com.mysql.cj.jdbc.Driver") \
            .option("batchsize", 1000) \
            .option("truncate", "true") \
            .mode("overwrite") \
            .save()

        logger.info(f"{file_name} successfully written to MySQL")

        logger.info(get_total_records("myschema", mysql_table_name))



