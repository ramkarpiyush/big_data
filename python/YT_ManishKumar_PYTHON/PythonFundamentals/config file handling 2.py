from configparser import ConfigParser

config_filepath = (r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\YT_ManishKumar_PythonFundamentals\src\resources\config_file.ini")

config = ConfigParser()

with open(config_filepath, "r") as f:
    config.read_file(f)

port = config["oracle_database"]["port"]
print(f"{port}")