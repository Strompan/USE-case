import os

import sqlite3

BASE_DIR = "C:/Users/Winner/Desktop/server/Use-case/server"
DATABASE_DIR = "C:/Users/Winner/Desktop/server/Use-case/server/database"

class DBManager: 
    def connect(self, db_path: str) -> None:
        self.__connection = sqlite3.connect(db_path,check_same_thread= False)

    def close(self) -> None:
        self.__connection.close()
        self.__connection = None

    def execute(self, query: str, params: tuple[str] = (), many: bool = False):
        cursor = self.__connection.cursor()
        try:
            result = cursor.execute(query, params)
            self.__connection.commit()
            if not result:
                return 
            if many:
                return result.fetchall()
            return result.fetchone()
        except sqlite3.Error as e:
            self.close()
            raise e


def get_db_manager() -> DBManager:
    db_manager = DBManager()
    db_manager.connect(BASE_DIR + '/zoo.db')
    return db_manager


def create_database(db_path: str) -> None:
    create_tables_file = DATABASE_DIR + '/scripts.sql'
    with open(create_tables_file, 'r') as file:
        create_tables_script = file.read()
        connection = sqlite3.connect(db_path)
        try:
            cursor = connection.cursor()
            cursor.executescript(create_tables_script)
            connection.commit()
        except sqlite3.Error as e:
            print(e)
            
        finally:
            connection.close()


def drop_database(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)
    else:
        print('Не существует базы данных с таким путем')


if __name__ == '__main__':
    create_database(BASE_DIR + '/zoo.db')