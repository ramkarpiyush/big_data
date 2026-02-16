import json
from src.resources.reco import load_table, get_basic_metrics, data_validations, hash_validation, reconcile_single_table
from loguru import logger


config_file_path = r"D:\GitLocal\big_data\Databricks\src\resources\config.json"

with open(config_file_path, "r") as f:
    tables_config = json.load(f)
    cfg = json.load(f)

def main():
    for table in tables_config:
        path = table["source"]["path"]
        format= table["source"]["format"]
        table_name = table["table_name"]
        pk = table["primary_key"]

        _load_tbl = load_table(f"{path}", f"{format}")
        logger.info(_load_tbl)

        df, status = load_table(f"{path}", f"{format}")

        _get_basic_metrics = get_basic_metrics(df, table_name, pk)
        logger.info(_get_basic_metrics)

        src_path = table["source"]["path"]
        tgt_path = table["target"]["path"]
        src_format= table["source"]["format"]
        tgt_format= table["target"]["format"]

        logger.info(tgt_path)

        src_df, src_status = load_table(f"{src_path}", f"{src_format}")
        tgt_df, tgt_status = load_table(f"{tgt_path}", f"{tgt_format}")

        
        # src_df, src_status = load_table(src_path, src_format)
        # tgt_df, tgt_status = load_table(tgt_path, tgt_format)

        logger.info(src_df)
        logger.info(tgt_df)


        _sql_validations = data_validations(src_df, tgt_df, pk)
        logger.info(_sql_validations)

        _hash_validation = hash_validation(src_df, tgt_df)
        logger.info(_hash_validation)

        _reconcile_single_table = reconcile_single_table(cfg=cfg)
        logger.info(_reconcile_single_table)

if __name__ == "__main__":
    main()

    