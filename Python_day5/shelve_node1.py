# Author:GaoYuCai
import shelve
d=shelve.open("file.txt")
print(d.get("info"))
print(d.get("date"))
print(d.get("test"))