from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from datetime import datetime
from loguru import logger
import json
spark = SparkSession.builder.appName("Multi_Table_Reconciliation").getOrCreate()


def sql_validations(src_df, tgt_df, pk):
   result = {}
   try:
       src_df.createOrReplaceTempView("src_tbl")
       tgt_df.createOrReplaceTempView("tgt_tbl")
       rec = spark.sql("""
           SELECT
             (SELECT COUNT(*) FROM src_tbl) AS src_count,
             (SELECT COUNT(*) FROM tgt_tbl) AS tgt_count
       """).first()
       result["record_count_match"] = (rec["src_count"] == rec["tgt_count"])
       missing = spark.sql(f"""
           SELECT COUNT(*) AS missing
           FROM (
               SELECT {pk} FROM src_tbl
               EXCEPT
               SELECT {pk} FROM tgt_tbl
           )
       """).first()[0]
       result["missing_in_target"] = missing
       result["status"] = "SUCCESS"
   except Exception as e:
       result["status"] = "FAILED"
       result["error"] = str(e)
   return result


src_df = (spark.read.format("csv")
            .option("header", "true")
            .option("inferSchema", "true")
            .load(r"D:\GitLocal\big_data\Databricks\data_reconciliation\src_tables\transactions.csv"))
tgt_df = (spark.read.format("csv")
            .option("header", "true")
            .option("inferSchema", "true")
            .load(r"D:\GitLocal\big_data\Databricks\data_reconciliation\tgt_tables\transactions.csv"))


logger.info(sql_validations(src_df, tgt_df, pk="txn_id"))