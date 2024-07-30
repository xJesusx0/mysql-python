import pymysql
from pymysql.cursors import DictCursor

from rich.console import Console
from rich.table import Table

import dotenv
import readline
import os

dotenv.load_dotenv()

console = Console()
def get_db_connection():
    connection = pymysql.connect(
        host = os.getenv('MYSQL_HOST'),
        user = os.getenv('MYSQL_USER'),
        password = os.getenv('MYSQL_PASSWORD'),
        db = os.getenv('MYSQL_DB'),
        port = int(os.getenv('MYSQL_PORT')),
        cursorclass=DictCursor
    )
    return connection

connection = get_db_connection()
cursor = connection.cursor()
def get_columns(data: dict) -> list:
    if not data:
        return []
    columns = data[0].keys()
    return list(columns)

def generate_table(data: dict):
    table = Table(show_header=True, header_style="bold magenta")
    
    columns = get_columns(data)
    for column in columns:
        table.add_column(column)
    
    for element in data:
        values = element.values()
        str_list = [str(item) for item in values]
        table.add_row(*str_list)
    
    console.print(table)

def main():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        while True:
            try:
                
                query = input("mysql $ ")

                if query.lower() == 'exit':

                    break

                if query.lower() == 'clear':
                    console.clear()
                    continue

                cursor.execute(query)
                connection.commit()

                data = cursor.fetchall()
                generate_table(data)

            except Exception as error:
                connection.rollback()
                print("Error:", error)
    
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
        main()
