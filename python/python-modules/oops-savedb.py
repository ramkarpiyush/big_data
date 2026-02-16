class Labour:
    # total_cnt = 0
    def __init__(self, first_name, last_name, wage):
        self.first = first_name
        self.last = last_name
        self.wage = wage
        # Labour.total_cnt += 1

def save_to_database(self):
    query = "select id from home.labours where lower(first_name) = %s and lower(last_name) = %s;"
    result = self.crud.read_from
    print(self.__wage)
    pass