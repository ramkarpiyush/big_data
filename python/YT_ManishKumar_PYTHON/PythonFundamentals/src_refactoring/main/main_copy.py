from src_refactoring.main.databases.mysql_connector import * #read_from_mysql, MySqlConnection, MySqlCrudOperations
from src_refactoring.main.encrypt_decrypt.AES_Encryption import decrypt
from src_refactoring.main.labours.labour_main4 import Labour, Person, Mistri
import configparser
from loguru import logger

config = configparser.ConfigParser()

config_filepath = (r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\PythonFundamentals\src_refactoring\resources\config_file.ini")
config.read(config_filepath)

decrypted_password = decrypt(config["mysql_database"]["password"])
config.set("mysql_database","password", decrypted_password)

# set() is a method of Python’s configparser.ConfigParser class 
# used to write/update an option (key-value) inside a section of an INI-style configuration.
# SYNTAX: ConfigParser.set(section, option, value=None)
# Parameters:
# section (str): The name of the section (e.g., "mysql_database").
# Must already exist, or NoSectionError is raised.
# option (str): The option/key name (e.g., "password").
# By default, ConfigParser normalizes option names to lowercase.
# value (str or None): The value to store.
# Must be a string unless allow_no_value=True was set when the parser was created.

def main():
    mysql_db_conn_obj = MySqlConnection(config=config)
    mysql_db_conn_obj.connect()
    crud = MySqlCrudOperations(mysql_db_conn_obj.connection)

    # Labour.login_and_logout(crud, first_name="Pip", last_name="Ramkar")
    # my_obj5 = Labour("Piyush", "Ramkar", 5000, "Civil", crud)

    mistri_obj = Mistri("Raju", "Mistri", 1000, "Mistri", "Brickwork, Plaster", crud)

if __name__ == "__main__":
    main()