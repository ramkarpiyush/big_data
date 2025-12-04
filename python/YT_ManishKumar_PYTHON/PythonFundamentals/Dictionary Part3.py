from loguru import logger

data = {
    "Python": 7, "SQL": 8, "Spark": 6, "AWS": 4, "Power BI": 2 
}

# Get Method:
print(data.get("Python"))
logger.info(data.get("Spark"))

# Keys and Values:
logger.info(data.keys())

logger.info(data.values())

# Items:
logger.info(data.items())

# Add/Update:
data.update({"SQL": 11, "New": 11})
print(data)


# Merge dictionary
new_dict = {"git": 4, "jira": 3}

merge_dic = {**data, **new_dict}

print(merge_dic)

# Pop and Popitem:
logger.info(merge_dic.pop("git"))

print(merge_dic.popitem())

print(merge_dic.popitem())

# Copy:
data_copy = data.copy()

print(id(data_copy))
print(id(data))

# Clear:
_dict = {"Piyush": 87, "Akshat": 15.5}
print(_dict)

_dict.clear()
print(_dict)

# clear :
_dict = {"Shivani": 23}