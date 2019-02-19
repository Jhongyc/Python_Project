# Author:GaoYuCai
import json#字典，列表，字符串
def sayhi(name):
    print("sayhi",name)
info={
    "name":"Alex",
    "age":25,

}
f=open("c:\\file.txt","w")#打开，存储字符串
f.write(json.dumps(info))
info["age"]=21
f.write(json.dumps(info))
f.close()

