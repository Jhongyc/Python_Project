# Author:GaoYuCai
import shelve
import datetime
d=shelve.open("file.txt")
info={
    'age':22,
    'job':"IT",
}
name=["name",'rain',"test"]
d["test"]=name
d["info"]=info
d["date"]=datetime.datetime.now()


d.close()