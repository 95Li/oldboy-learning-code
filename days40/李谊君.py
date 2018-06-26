
import pymysql

conn=pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    charset='utf8',
    database='db42'
)

cursor=conn.cursor(pymysql.cursors.DictCursor)

cursor.callproc('p1',(2,4,10)) #@_p1_0=2,@_p1_1=4,@_p1_2=10


print(cursor.fetchall())

cursor.execute('select @_p1_2;')
print(cursor.fetchone())

cursor.close()
conn.close()
