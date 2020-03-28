import sqlite3
from variables import *


def create_database():
    with sqlite3.connect(DATABASE) as conn:
        pass

def create_table(table):
    print(f'I would create the table: {table}')