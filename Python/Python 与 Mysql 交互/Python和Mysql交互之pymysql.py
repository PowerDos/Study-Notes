# pymysql
# 需要向安装pymysql
# 在cmd下用pip3 install pymysql
import pymysql
# 创建连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='abcdef123',db='mobliepay')
# 创建游标
cursor = conn.cursor()
# 查看数据
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from payinfo")
print("有多少行：",effect_row)
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print("打印剩下的全部")
print(cursor.fetchall())
# 插入单条
res = cursor.execute("insert into payinfo(consumeropenid,mcode_title,money) value(%s,%s,%s)",("test2","002","60"))
print("插入单条:",res)
# 插入多条
data = [
    ("test1","001","50"),
    ("test2","001","50"),
    ("test3","001","50"),
]
res = cursor.executemany("insert into payinfo(consumeropenid,mcode_title,money) value(%s,%s,%s)" ,data)
print("插入多条：",res)
# 提交事务
conn.commit()

cursor.close()
conn.close()




