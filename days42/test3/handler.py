import pymysql
from days42.test3 import setting

class Mysql:
    __instance=None
    def __init__(self):
        self.conn=pymysql.connect(
            host=setting.host,
            user=setting.user,
            password=setting.password,
            database=setting.database,
            charset=setting.charset,
            autocommit=setting.autocommit
        )
        self.cursor=self.conn.cursor(pymysql.cursors.DictCursor)

    def select(self,sql,args):
        self.cursor.execute(sql,args)
        res = self.cursor.fetchall()
        return res

    def execute(self,sql,args):
        try:
            self.cursor.execute(sql,args)
            row=self.cursor.rowcount
        except Exception as e:
            print(e)
        return row

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            cls.__instance=cls()
        return cls.__instance