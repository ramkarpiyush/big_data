print("My home is of 2bhk Area of total home is 800 square feet")

print("Apchr Spark is a unified computing engine and a set of libraries for paraller data processing on computer clusters.")

# ===================================================================================================== #
# Escape Sequence:

# For new line we have to use "\n" 
print("Apchr Spark is a unified computing engine \nand a set of libraries for paraller data processing on computer clusters.")

# To write multline print statemnt use tripple quote (''' text ''')
print('''1. Spark employs a cluster manager that keep track of the resources available.
2. The driver process is resposible for executing thr drivers programs command across the executors to complete a given task.      
''')

# backslash (\) is used as an escape character to allow special characters to be included in strings.
print("My home is of \"2bhk\"")

# "\t" Horizontal tab
print("My home is \t of 2bhk")

# ===================================================================================================== #

# String formatting:
unit_cost = 100

# method 1
print("Cost of brick per unit is",unit_cost, "rupees only...")

# method 2
print("cost of brick per unit is {} rupees only...".format(unit_cost))

# method 3
print(f"Cost of brick per unit is {unit_cost} rupees only...")

# ===================================================================================================== #
#Logging:

import logging
from loguru import logger
logger.info(f"value of _var variable is {unit_cost} only...")