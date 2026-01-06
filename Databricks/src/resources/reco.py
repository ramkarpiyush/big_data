from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from datetime import datetime
from loguru import logger
import json


spark = SparkSession.builder.appName("Multi_Table_Reconciliation").getOrCreate()

CONTROL_FILE_PATH = r"D:\GitLocal\big_data\Databricks\src\control\multi_table_recon.json"

config_file_path = r"D:\GitLocal\big_data\Databricks\src\resources\config.json"
with open(config_file_path, "r") as f:
    tables_config = json.load(f)
    # logger.info(tables_config)

# Safe Loader
def load_table(path, format):
   try:
       df = (spark.read.format(format)
            .option("header", "true")
            .option("inferSchema", "true")
            .load(path))

    #    logger.info(df.show(3))
       return df, "SUCCESS"
   except Exception as e:
       return None, f"FAILED: {str(e)}"
   
# Basic Metrics
def get_basic_metrics(df, table_name, pk):
   try:
       return {
           "table": table_name,
           "record_count": df.count(),
           "distinct_pk": df.select(pk).distinct().count(),
           "null_pk_count": df.filter(col(pk).isNull()).count(),
           "min_pk": df.agg(min(pk)).first()[0],
           "max_pk": df.agg(max(pk)).first()[0],
           "status": "SUCCESS"
       }
   except Exception as e:
       return {"table": table_name, "status": "FAILED", "error": str(e)}

def data_validations(src_df, tgt_df, pk: str):
    """
    Validates:
      1) Count parity between src_df and tgt_df
      2) Missing keys in target (src minus tgt) using left_anti join

    Args:
        src_df: Source Spark DataFrame
        tgt_df: Target Spark DataFrame
        pk:     Primary key column name (string)

    Returns:
        dict: {
            "src_count": int,
            "tgt_count": int,
            "record_count_match": bool,
            "missing_in_target": int,
            "status": "SUCCESS" | "FAILED",
            "error": str (only when FAILED)
        }
    """
    result = {}
    try:
        # 0) Validate primary key presence
        for name, df in [("src_df", src_df), ("tgt_df", tgt_df)]:
            if pk not in df.columns:
                raise ValueError(f"Primary key '{pk}' not found in {name} columns: {df.columns}")

        # 1) Counts
        src_count = src_df.count()
        tgt_count = tgt_df.count()
        result["src_count"] = src_count
        result["tgt_count"] = tgt_count
        result["record_count_match"] = (src_count == tgt_count)

        # 2) Missing PKs in target: src - tgt
        # Use distinct on PK to avoid duplicate counting from either side
        src_keys = src_df.select(pk).distinct()
        tgt_keys = tgt_df.select(pk).distinct()

        missing_keys_df = src_keys.join(tgt_keys, on=pk, how="left_anti")
        result["missing_in_target"] = missing_keys_df.count()

        result["status"] = "SUCCESS"
        return result

    except Exception as e:
        result["status"] = "FAILED"
        result["error"] = str(e)
        return result



# 4️⃣ SQL Validations
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


# 5️⃣ Hash Check Validation
def hash_validation(src_df, tgt_df):
   try:
       src_hash = src_df.withColumn("hash", sha2(concat_ws("||", *src_df.columns), 256))
       tgt_hash = tgt_df.withColumn("hash", sha2(concat_ws("||", *tgt_df.columns), 256))
       extra_src = src_hash.select("hash").subtract(tgt_hash.select("hash")).count()
       extra_tgt = tgt_hash.select("hash").subtract(src_hash.select("hash")).count()
       return {
           "checksum_match": (extra_src == 0 and extra_tgt == 0),
           "extra_in_source": extra_src,
           "extra_in_target": extra_tgt,
           "status": "SUCCESS"
       }
   except Exception as e:
       return {"status": "FAILED", "error": str(e)}


config_file_path = r"D:\GitLocal\big_data\Databricks\src\resources\config.json"

with open(config_file_path, "r") as f:
    tables_config = json.load(f)

# 6️⃣ Reconciliation Logic Per Table
def reconcile_single_table(cfg):
    result = {
        "table_name": cfg["table_name"],
        "run_time": str(datetime.now())
    }
    try:
        src_df, src_status = load_table(cfg["source"]["path"], cfg["source"]["format"])
        tgt_df, tgt_status = load_table(cfg["target"]["path"], cfg["target"]["format"])
        if "FAILED" in src_status or "FAILED" in tgt_status:
            result["status"] = "FAILED"
            result["error"] = f"SOURCE:{src_status}, TARGET:{tgt_status}"
            return result
        pk = cfg["primary_key"]
        result["source"] = get_basic_metrics(src_df, "source", pk)
        result["target"] = get_basic_metrics(tgt_df, "target", pk)
        result["data_validation"] = data_validations(src_df, tgt_df, pk)
        result["hash_validation"] = hash_validation(src_df, tgt_df)
        if (
            result["sql_validation"]["record_count_match"]
            and result["hash_validation"]["checksum_match"]
        ):
            result["final_status"] = "PASS"
        else:
            result["final_status"] = "FAILED"
        logger.info(result)

    except Exception as e:
        result["final_status"] = "FAILED"
        result["error"] = str(e)
        logger.info(result)
    return result


# 7️⃣ Loop Over All Tables
final_report = {
   "job_name": "Multi_Table_ETL_Reconciliation",
   "run_time": str(datetime.now()),
   "tables": []
}

config_file_path = r"D:\GitLocal\big_data\Databricks\src\resources\config.json"
with open(config_file_path, "r") as f:
    tables_config = json.load(f)

for table_cfg in tables_config:
   print(f"Running Reconciliation For : {table_cfg['table_name']}")
   res = reconcile_single_table(table_cfg)
   final_report["tables"].append(res)

logger.info(final_report)


# 8️⃣ Write Final Control File
try:
   path = CONTROL_FILE_PATH
   with open(path, "w") as f:
       json.dump(final_report, f, indent=4)
   print("Multi-table control file generated successfully")
except Exception as e:
   print("Failed to write control file: ", str(e))