import pyodbc
import json

class DataBase():
    def __init__(self, config:dict) -> None:
        self.__server = config['server']
        self.__database = config['database']
        self.__username = config['username']
        self.__password = config['password']
        self.__driver = config['driver']
        self.cursor = self.connect()

    def get_database_config(self):
        return {
            "server": self.__server,
            "database": self.__database,
            "username": self.__username,
            "password": self.__password,
            "driver": self.__driver
        }
    
    def connect(self):
        db_config = self.get_database_config()
        connection_data = f"""
            DRIVER={{{db_config['driver']}}};
            SERVER={db_config['server']};
            DATABASE={db_config['database']};
            UID={db_config['username']};
            PWD={db_config['password']};
        """
        
        conn = pyodbc.connect(connection_data)
        conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        conn.setencoding(encoding='utf-8')

        cursor = conn.cursor()
        return cursor

    def __create_table_products(self):
        self.cursor.execute("""CREATE TABLE produtos (
            id BIGSERIAL PRIMARY KEY,
            name VARCHAR(255),
            description TEXT,
            price NUMERIC(10, 2),
            quantity INTEGER
            );"""
        )
        self.cursor.commit()

if __name__ == '__main__':
    with open('config.json','r') as file:
        config = json.load(file)
    db = DataBase(config)
    cursor = db.cursor
