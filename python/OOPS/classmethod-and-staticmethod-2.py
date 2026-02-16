from loguru import logger

class Labour:
    total_cnt = 0
    def __init__(self, first_name, last_name, wage, role, crud):
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage
        self.role = role
        self.crud = crud
        # self.__save_to_database(self.crud)
        Labour.total_cnt += 1

    def __save_to_database(self, crud):
        query = f"select id from home.labours where lower(first_name) = '{self.first_name}' and lower(last_name) = '{self.last_name}';"
        result = crud.read_from_mysql(query)

        if result:
            logger.info(f"Labout already exists with ID: {result[0][0]}")
            return result[0][0]
        
    def login(self):
        pass

    @classmethod
    def total_no_of_labours(cls):
        return Labour.total_cnt 
    

    @staticmethod
    def is_valid_wage(your_wage):
        if your_wage <= 200: 
            logger.info("Ask for a fair wage")
        else:
            logger.info("Your wage is more than minimum")

print(Labour.total_no_of_labours())
print(Labour.is_valid_wage(400))




