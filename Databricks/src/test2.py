
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from loguru import logger

spark = SparkSession.getActiveSession() or SparkSession.builder.getOrCreate()

def sql_validations(src_df, tgt_df, pk: str):
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

src_df = (spark.read.format("csv")
            .option("header", "true")
            .option("inferSchema", "true")
            .load(r"D:\GitLocal\big_data\Databricks\data_reconciliation\src_tables\transactions.csv"))
tgt_df = (spark.read.format("csv")
            .option("header", "true")
            .option("inferSchema", "true")
            .load(r"D:\GitLocal\big_data\Databricks\data_reconciliation\tgt_tables\transactions.csv"))


logger.info(sql_validations(src_df, tgt_df, pk="txn_id"))