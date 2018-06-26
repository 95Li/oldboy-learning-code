import pymysql
from DBUtils.PooledDB import PooledDB
POOL=PooledDB(
    creator=pymysql,  #使用连接数据库的模块
    maxconnections=6,  #连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  #初始化时，连接池中至少创建的空闲连接数，0表示不创建
    maxcached=5,    #连接池中最多闲置的连接，0和None不限制
    maxshared=0,    # 链接池中最多共享的链接数量，0和None表示全部共享。
                    # PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  #一个连接最多被使用的次数，None表示无限制
    setsession=[],  #会话开始前执行的命令列表
    ping=0,         # ping MySQL服务端，检查是否服务可用。
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='db1',
    charset='utf8',
    autocommit=True
)

