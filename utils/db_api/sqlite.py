import sqlite3

class Database:
    def __init__(self, path_to_db = "main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone = False, fetchall = False, commit = False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data
    
    def create_table_users(self):
        print('creating')
        sql = """
        CREATE TABLE Users(
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit = True)
    
    @staticmethod
    def add_user(self, id: int, name: str, email: str = None):
        sql = """
        INSERT INTO Users(id, Name, email) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters = (id, name, email), commit = True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone = True)
    
    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit = True)

def logger(statement):
    print(f"""
    {statement}""")
