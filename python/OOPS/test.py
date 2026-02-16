class Labour:
    def __init__(self, first_name, last_name, wage):
        self.first = first_name
        self.last = last_name
        self.wage = wage
        self.total_count += 1

manish_obj = Labour("Manish", "Kumar", 500)
ramesh_obj = Labour("Ramesh", "Singh", 750)

print(manish_obj.first)
