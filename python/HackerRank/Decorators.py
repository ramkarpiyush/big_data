from loguru import logger

people = [
    ["Piyush", "Ramkar", "30", "M"],
    ["Shivani", "Yadav", "26", "F"],
    ["Akanksha", "Ramkar", "25", "F"],
    ["Arnav", "Ramkar", "10", "M"]
]

def person_lister(func):
    def inner(people):
        # Sort a list by Age in ascending order
        sorted_list = sorted(people, key=lambda x:int(x[2]))
        logger.info(sorted_list)

        # Apply the formatting function to each person i.e. i and collect the result
        res = []
        for i in sorted_list:
            formatted_name = func(i)        # func is the original function (name_format)
            res.append(formatted_name)
        
        logger.info(res)
        return res
    
    logger.info(inner.__class__)
    return inner

@person_lister
def name_format(person):
    if person[3] == "M":
        title = "Mr. "
    else:
        title = "Ms. "

    out_format = title + person[0] + " " + person[1]
    return out_format

output = name_format(people)

for i in output:
    print(i)
