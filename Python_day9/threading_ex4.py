# Author:GaoYuCai
import  threading
num,num2=0,0
local=threading.RLock()
for i in range(10):
    t=threading.Thread(target=run3)
    t.start()
while threading.active_count()!=1:
    print(threading.active_count())
else:
    print("---all  threads  done---")
    print()