# Author:GaoYuCai
import  json
import pickle
info={
    'name':"gyc",
    "age":23
}
f=open("c:\\file.json",'w')
f.write(json.dumps(info))
f.close()
#f.write(pickle.dumps(info))
#f.close()