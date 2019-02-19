# Author:GaoYuCai
import yaml
f=open(r"c:\file3.ini")
x=yaml.load(f)
print(x)
print("------------")
f.close()
a=open(r"c:\file3.ini",'w')
aproject={'name':'Silenthand Olleander',
          'race':'Human',
          'traits':['ONE_HAND','ONE_EYE']
          }
yaml.dump(aproject,a)
aproject=('a','b','c')
yaml.dump(aproject,a)
aproject={'a':1,"b":2}
yaml.dump(aproject,a)
