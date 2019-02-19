# Author:GaoYuCai
import pickle
def sayhi(name):
    print("sayhi",name)
f=open("c:\\file.txt","rb")
data=pickle.load(f)
f.close()
print(data["name"])