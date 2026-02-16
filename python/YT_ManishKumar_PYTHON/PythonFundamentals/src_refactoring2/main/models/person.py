class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@gmail.com"

    def print_details(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email}"

    def to_dict(self):
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email": self.email
        }

