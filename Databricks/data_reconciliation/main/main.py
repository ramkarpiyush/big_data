# from main.reco import load_table
import json

import sys
sys.path.append(r"D:\GitLocal\big_data\Databricks\data_reconciliation")
from main.reco import *

config_file_path = r"D:\GitLocal\big_data\Databricks\data_reconciliation\config\config.json"

# for table in config_tbl:
#     path = table["source"]["path"]
#     format= table["source"]["format"]
#     print(load_table(path, format))
with open(config_file_path, "r") as f:
    config_tbl = json.load(f)

def main():
    for table in config_tbl:
        path = table["source"]["path"]
        format= table["source"]["format"]
        print(load_table(path=path, format=format))

if __name__ == "__main__":
    main()