from src_refactoring2.main.models.labour import Labour

class Mistri(Labour):
    def __init__(self, first_name, last_name, wage, role, skill, crud):
        super().__init__(first_name, last_name, wage, role, crud)
        self.skill = skill
        self.__save_to_skill_table()

    def __save_to_skill_table(self):
        insert_query = f""" INSERT INTO skills (labour_id, skill)
                VALUES ({self.id}, '{self.skill}') """
        
        self.crud.inser_from_mysql(insert_query)

    def to_dict(self):
        data = super().to_dict()
        data.update({"skill": self.skill})
        return data