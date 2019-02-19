# Author:GaoYuCai
#name2=name
#name="Paochen Ge"
#姓名="Alex Li"
#print("My name is",name2,name,姓名)
#name把字符串的内存地址给name2，所以name2 没有发生改变。
#变量是 数字，字母 ，下划线
#变量不能是特殊字符“-” ，@等
#变量的开头不能是数字，但是可以是下划线。
#变量不能是保留字符
#变得的编写要有含义的，不要写拼音和汉字（很low），python支持汉语变量。
#gf_of_friend
#python 没有常量的概念，有全局变量和局部变量
#表示常量 PIE（大写代表常量，可以修改）
#字符编码————python对.py文件进行编码，默认是ascill。
#二进制  -->  字符编码（ascill 八位（255））-->GB2312(1980年七千多个汉字)  -->GBK(1995年)  -->GB18030(2000年)
#unicode(万国码16位字符)
#utf-8（可变长的编码格式）
#注释：# 当行注释
#     ''','''  段落注释,还可以赋值给变量 打印多行，python单引号，双引号一样。
#python3 默认utf8编码
#python2  ascill编码 （#-*-coding：utf-8-*-）告诉python解释器使用utf8执行编码
#用户输入：
#username=input("What is  your name?")
#age=int(input("Age:"))
#job=input("Job:")
#salary=input("Salary:")
#info='''
#-------------info of %s -------------
#Name:%s
#Age:%d
#Job:%s
#Salary: %s
#'''%(username,username,age,job,salary)
#print(info)
#字符创格式化
#第一种：%s,%d 占位符   %（变量）
#python3 input
#python2  raw_input
#第二种：“+变量名”，格式化输出
#第三种：
#info2='''
#----------info of {_name} -----------
#Name:{_name}
#Age:{_age}
#Job：{job}
#Salary:{salary}
#'''.format(_name=name,_age=age,job=job,salary=salary)
#info3='''
#----------- info  of  {0} -----------
#Name:{0}
#Age:{1}
#Job:{2}
#Salary:{3}
#'''.format(name,age,job,salary)
import getpass
_username='Alex'
_password="abc123"
username=input("username:")
password=input("password:")
if _username==username and _password==password:
    print('Welcome user {name} login'.format(name=username))
else:
    print("Error!")







