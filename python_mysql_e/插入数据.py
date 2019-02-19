# Author:GaoYuCai
import pymysql
db=pymysql.connect("localhost","root","","testdb")
cursor=db.cursor()
sql='''
insert into employee(first_name,last_name,age,sex,income)
values("MAX","Iphone",30,"F",8000)'''
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
finally:
    db.close()