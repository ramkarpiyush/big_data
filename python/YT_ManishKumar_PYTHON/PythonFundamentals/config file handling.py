from loguru import logger

import configparser

config = configparser.ConfigParser()

config_filepath = (r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\YT_ManishKumar_PythonFundamentals\src\resources\config_file.ini")

config.read(r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\YT_ManishKumar_PythonFundamentals\src\resources\config_file.ini")

host_name = config["oracle_database"]["host"]
logger.info(f"Host Name: {host_name}")

oracledb_port = config["oracle_database"]["port"]
logger.info(f"Port Number:{oracledb_port}\nData Type:{type(oracledb_port).__name__}")

port = config.getint("oracle_database", "port")
logger.info(f"Port Number: {port}\nData Type:{type(port).__name__}")




