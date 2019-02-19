# Author:GaoYuCai
import calendar
yy=int(input("输入年份："))
mm=int(input("输入月份："))
dd=int(input("输入天："))
print(calendar.month(yy,mm))
print(calendar.weekday(yy,mm,dd))