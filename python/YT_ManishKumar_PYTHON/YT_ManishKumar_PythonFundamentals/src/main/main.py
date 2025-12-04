from src.main.databases.mysql_connector import read_from_mysql
import configparser
from loguru import logger

config = configparser.ConfigParser()

config_filepath = (r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\YT_ManishKumar_PythonFundamentals\src\resources\config_file.ini")
config.read(config_filepath)

def main():
    query = "select * from gdb041.dim_customer limit 10;"
    final_result = read_from_mysql(config=config, query=query)
    logger.info(f"{final_result}")
    

if __name__ == "__main__":
    main()