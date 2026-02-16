from pyspark.sql import SparkSession
import os
from loguru import logger
from pyspark.sql.functions import count
import re

spark = SparkSession.builder \
    .appName("Load-CSV-Pg") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.6.0").getOrCreate() 
# spark-submit --packages org.postgresql:postgresql:42.6.0
    

csv_path = r"D:\gitlocal\big_data\Dataset\products-1m.csv"
jdbc_url = "jdbc:postgresql://localhost:5432/postgres"
folder_path = r"D:\gitlocal\big_data\Dataset"

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
        df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)
    elif file_format == "json":
        df = spark.read.option("multiLine", "true").json(file_path)
    elif file_format == "parquet":
        df = spark.read.parquet(file_path)
    else:
        raise ValueError(f"Unknown file format: {file_format}")
    return df


for file_name in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file_name)        # os.path.join() is used to safely concatenate directory and file names into a valid file path 
                                                            # while handling OS-specific path separators automatically.
    if os.path.isfile(full_path):
        # logger.info(full_path)
        logger.info(f"File Path: {full_path}\nFormat: {detect_format(full_path)}")

        supported_formats = {"csv", "parquet", "json"}

        if detect_format(full_path) not in supported_formats:
            print(f"Skipping unsupported file: {file_name}")
            pass 
        else:    
            df = read_data(file_path=full_path)
            # df.show(1)
            df.select(count("*").alias("total_rows")).show()
            df.printSchema()

            # Create clean table name
            # Remove extension
            table_name = os.path.splitext(file_name)[0]

            # Replace special characters
            table_name = re.sub(r'[^a-zA-Z0-9_]', '_', table_name)

        # # Lowercase
            table_name = table_name.lower()
            logger.info(f"Writing to table: myschema.{table_name}")

            clean_columns = [c.replace("-", "_").replace(" ", "_") for c in df.columns]
            df = df.toDF(*clean_columns)
            df.show(1)

        df.write \
          .format("jdbc") \
          .option("url", jdbc_url) \
          .option("dbtable", f"myschema.{table_name}") \
          .option("user", "postgres") \
          .option("password", "postgres") \
          .option("driver", "org.postgresql.Driver") \
          .option("batchsize", 100) \
          .mode("overwrite") \
          .save()

        logger.info(f"{file_name} successfully written to PostgreSQL")        
