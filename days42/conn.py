from . import setting
import pymysql


class Mysql:
    # __instance=None    #声明一个类属性，用于存放单例对象
    def __init__(self):
        self.conn = pymysql.connect(  # 连接数据库
            host=setting.host,
            user=setting.user,
            password=setting.password,
            database=setting.database,
            charset=setting.charset,
            autocommit=setting.autocommit
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        # 创建一个游标，以字典形式获取返回值

    def close_db(self):  # 关闭数据库连接
        self.cursor.close()
        self.conn.close()

    def select(self, sql, args=None):  # 执行查询语句
        self.cursor.execute(sql, args)
        res = self.cursor.fetchall()
        return res

    def execut(self, sql, args):  # 执行 增删改等操作
        try:
            self.cursor.execute(sql, args)
            res = self.cursor.rowcount
        except BaseException as e:
            print(e)
        return res

    # @classmethod
    # def singleton(cls):
    # 如果不使用数据库连接池 则使用单例设计模式
    #     if not cls.__instance:
    #         cls.__instance=cls()
    #     return cls.__instance
