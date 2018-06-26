import pymysql

conn=pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='oldboy',
    charset='utf8')

cursor=conn.cursor(pymysql.cursors.DictCursor)
# cursor=conn.cursor()


sql='select * from class'
cursor.execute(sql)

cursor.scroll(1,'absolute')
print(cursor.fetchone())
cursor.scroll(1,'relative')
print(cursor.fetchone())
# print(cursor.fetchall())

cursor.close()
conn.close()


