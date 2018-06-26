import pymysql
from days42.test1 import setting

class Mysql:
    # __instance=None
    def __init__(self):
        self.conn=setting.POOL.connection()
        self.cursor=self.conn.cursor(pymysql.cursors.DictCursor)

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def select(self,sql,args):
        self.cursor.execute(sql,args)
        res=self.cursor.fetchall()
        return res

    def execute(self,sql,args):
        try:
            self.cursor.execute(sql,args)
            row=self.cursor.rowcount
        except BaseException as e:
            print(e)
        finally:
            self.close_db()
        return row

    # @classmethod
    # def singleton(cls):
    #     if not cls.__instance:
    #         cls.__instance=cls()
    #     return  cls.__instance