class LabourService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_labour(self, labour):
        cursor = self.db_connection.cursor()
        query= """
        INSERT INTO home.labours (first_name, last_name, wage, role, email)
        VALUES (%s, %s, %s, %s, %s);
        """
        values = (labour.first_name, labour.last_name, labour.wage, labour.role, labour.email)
        cursor.execute(query, values)
        self.db_connection.commit()
        return cursor.lastrowid