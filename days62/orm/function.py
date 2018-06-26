import pymysql
from days62.orm import DB


class Mysql:
    def __init__(self):
        self.conn = DB.POOL.connection()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def db_close(self):
        self.cursor.close()
        self.conn.close()

    def select(self, sql, args):
        self.cursor.execute(sql, args)
        res = self.cursor.fetchall()
        return res

    def execute(self, sql, args):
        try:
            self.cursor.execute(sql, args)
            row = self.cursor.rowcount
        except Exception as e:
            print(e)
        finally:
            self.db_close()
        return row
