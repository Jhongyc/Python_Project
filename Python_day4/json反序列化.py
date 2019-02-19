# Author:GaoYuCai
#不同语言进行数据交互将取代XML
#处理简单的数据类型
#处理复杂的数据类型使用pickle默认二进制
#函数序列化  是整体的序列化（name）pickle仅仅用在python中
import  json
import pickle
f=open("c:\\file.json",'rb')
data=json.loads(f.read())
print(data["age"])
#data=pickle.loads(f.read())
#print(data["age"])