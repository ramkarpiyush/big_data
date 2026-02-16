from loguru import logger
from fastapi import HTTPException

class LabourService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_labour(self, labour):
        cursor = self.db_connection.cursor()

        check_query = """
                    SELECT id FROM  home.labours WHERE LOWER(first_name) = %s AND LOWER(last_name) = %s;
                    """
        cursor.execute(check_query, (labour.first_name.lower(), labour.last_name.lower()))
        result = cursor.fetchall()

        if result:
            raise HTTPException(status_code=400, detail="User is already preseny")

        query= """
        INSERT INTO home.labours (first_name, last_name, wage, role, email)
        VALUES (%s, %s, %s, %s, %s);
        """
        values = (labour.first_name, labour.last_name, labour.wage, labour.role, labour.email)
        logger.info(f"Executing query: {query} with Values: {values}")
        cursor.execute(query, values)
        self.db_connection.commit()
        return cursor.lastrowid
    
    def get_labour(self, labour_id):
        cursor = self.db_connection.cursor()

        check_query = """
                    SELECT * FROM  home.labours WHERE id = %s;
                    """
        # logger.info(cursor.execute(check_query, ([labour_id])))
        cursor.execute(check_query, ([labour_id]))
        result = cursor.fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        
        columns = [desc[0] for desc in cursor.description]
        labour_data = dict(zip(columns, result))

        return labour_data
    
    def get_all_labour(self):
        cursor = self.db_connection.cursor()

        check_query = """
                    SELECT * FROM  home.labours;
                    """
        # logger.info(cursor.execute(check_query, ([labour_id])))
        cursor.execute(check_query)
        result = cursor.fetchall()

        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        
        columns = [desc[0] for desc in cursor.description]
        labour_data = [dict(zip(columns, row)) for row in result]

        return labour_data    