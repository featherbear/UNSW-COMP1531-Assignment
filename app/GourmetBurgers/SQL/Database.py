import re
import sqlite3

class Database():
    def __init__(self, db_file = None):
        if db_file is None:
            db_file = "database.sqlite3"
        self._db_file = db_file
        self._conn = sqlite3.connect(db_file)

    @property
    def db_file(self):
        return self._db_file

    def create_table(self, create_table_sql):
        create_table_sql = re.sub("\n|\s{2,}", "", create_table_sql)
        create_table_sql = re.sub(",(?=\S)", ", ", create_table_sql)

        try:
            c = self._conn.cursor()
            c.execute(create_table_sql)
        except sqlite3.Error as e:
            print("sqlite:", e)


    def fetchOne(self, *args, **kwargs):
        c = self._conn.cursor()
        c.execute(*args)
        result = c.fetchone()
        return result


    def fetchAll(self, *args, **kwargs):
        c = self._conn.cursor()
        c.execute(*args)
        result = c.fetchall()
        return result

    def insert(self, *args, commit=True, **kwargs):
        c = self._conn.cursor()
        c.execute(*args)
        if commit:
            self._conn.commit()
        return c.lastrowid


    def update(self, *args, commit=True, **kwargs):
        c = self._conn.cursor()
        c.execute(*args)
        if commit:
            self._conn.commit()
        return c.rowcount

