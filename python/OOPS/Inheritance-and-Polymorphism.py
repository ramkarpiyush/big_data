from loguru import logger

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@gmail.com"

    def print_details(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email}"
    
person1 = Person("Piyush", "Ramkar")
logger.info(person1.print_details())
            

class Labour1(Person):
    def __init__(self, first_name, last_name, wage):
        super().__init__(first_name, last_name)
        self.wage = wage

    def print_details(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email} and total wage is {self.wage}"

    pass

# class Labour():

obj = Labour1("Piyush", "Ramkar", 500)

logger.info(obj.print_details())


