# Author:GaoYuCai
import pymysql
db=pymysql.connect("localhost","root","","testdb")
cursor=db.cursor()
sql='''
select * from employee '''
try:
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
    for  row  in  result:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
    print("fname:%s,lname:%s,age:%d,sex:%s,income:%d"%(fname,lname,age,sex,income))
except:
    print("Error:unable to fecth data")
finally:
    db.close()