from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from datetime import datetime
import json
spark = SparkSession.builder.appName("Multi_Table_Reconciliation").getOrCreate()

# tables_config = [
#    {
#        "table_name": "customer",
#        "primary_key": "customer_id",
#        "source": {"path": r"D:\GitLocal\big_data\Databricks\Data Reconciliation\src_tables\customers", "format": "csv"},
#        "target": {"path": r"D:\GitLocal\big_data\Databricks\Data Reconciliation\tgt_tables\customers", "format": "delta"}
#    },
#    {
#        "table_name": "orders",
#        "primary_key": "order_id",
#        "source": {"path": r"D:\GitLocal\big_data\Databricks\Data Reconciliation\src_tables\orders", "format": "csv"},
#        "target": {"path": r"D:\GitLocal\big_data\Databricks\Data Reconciliation\tgt_tables\orders", "format": "delta"}
#    },
#    {
#        "table_name": "transactions",
#        "primary_key": "txn_id",
#        "source": {"path": r"D:\GitLocal\big_data\Databricks\Data Reconciliation\src_tables\transactions", "format": "csv"},
#        "target": {"path": r"D:\GitLocal\big_data\Databricks\Data Reconciliation\tgt_tables\transactions", "format": "delta"}
#    }
# ]

CONTROL_FILE_PATH = r"D:\GitLocal\big_data\Databricks\Data Reconciliation\control\multi_table_recon.json"


# 2️⃣ Safe Loader
def load_table(path, format):
   try:
       df = spark.read.format(format).load(path)
       return df, "SUCCESS"
   except Exception as e:
       return None, f"FAILED: {str(e)}"


# 3️⃣ Basic Metrics
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
       result["sql_validation"] = sql_validations(src_df, tgt_df, pk)
       result["hash_validation"] = hash_validation(src_df, tgt_df)
       if (
           result["sql_validation"]["record_count_match"]
           and result["hash_validation"]["checksum_match"]
       ):
           result["final_status"] = "PASS"
       else:
           result["final_status"] = "FAILED"
   except Exception as e:
       result["final_status"] = "FAILED"
       result["error"] = str(e)
   return result


# 7️⃣ Loop Over All Tables
final_report = {
   "job_name": "Multi_Table_ETL_Reconciliation",
   "run_time": str(datetime.now()),
   "tables": []
}
for table_cfg in tables_config:
   print(f"Running Reconciliation For : {table_cfg['table_name']}")
   res = reconcile_single_table(table_cfg)
   final_report["tables"].append(res)


# 8️⃣ Write Final Control File
try:
   path = "/dbfs" + CONTROL_FILE_PATH.replace("/mnt", "")
   with open(path, "w") as f:
       json.dump(final_report, f, indent=4)
   print("Multi-table control file generated successfully")
except Exception as e:
   print("Failed to write control file: ", str(e))


# # ✅ Sample Output JSON
# {
# "job_name": "Multi_Table_ETL_Reconciliation",
# "tables": [
#   {
#     "table_name": "customer",
#     "final_status": "PASS"
#   },
#   {
#     "table_name": "orders",
#     "final_status": "FAILED",
#     "missing_in_target": 120
#   }
# ]
# }