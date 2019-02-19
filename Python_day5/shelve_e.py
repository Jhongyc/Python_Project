# Author:GaoYuCai
import shelve
f=shelve.open("file_test")
#info={"name":"gaoyucai","age":24}
#f["info"]=info
#f.close()
print(f.get("info"))