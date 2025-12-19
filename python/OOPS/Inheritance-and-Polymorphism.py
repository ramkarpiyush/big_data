from loguru import logger

# Inheritance:
# Inheritance allows one class (called the child or subclass) to acquire properties and methods from another class (called the parent or superclass).

# Python uses MRO (Method Resolution Order) to resolve method calls in multiple inheritance. 
# super() is used to call a method from the parent class.


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@gmail.com"

    def print_details(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email}"
    
person1 = Person("Piyush", "Ramkar")
# logger.info(person1.print_details())            

class Labour1(Person):
    def __init__(self, first_name, last_name, wage):
        super().__init__(first_name, last_name)
        self.wage = wage

    def print_details(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email} and total wage is {self.wage}"

    pass

class Mistri(Labour1):
    def __init__(self, first_name, last_name, wage, skills):
        super().__init__(first_name, last_name, wage)
        self.skills = skills

    def print_details(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email} and total wage is {self.wage} for skillset of {self.skills}"

# class Labour():

obj = Labour1("Piyush", "Ramkar", 500)

# print(help(obj))        # The built-in help() function is used to display documentation 
                        # about objects, modules, classes, functions, or keywords. 

# logger.info(obj.print_details())

obj2 =  Mistri("Piyush", "Ramkar", 1000, "Plumber")
# print(help(obj2))

logger.info(obj2.print_details())






# POLYMORPHISM:
# Polymorphism means "many forms"
# In Python, Polymorphism allows the same function or method name 
# to work in different ways depending on the object or data type.

