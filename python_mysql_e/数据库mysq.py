# Author:GaoYuCai
import pymysql
db=pymysql.connect("localhost","root","","testdb")
cursor=db.cursor()
cursor.execute("select  version()")
data=cursor.fetchone()
print("Database  version:%s"%data)
db.close()