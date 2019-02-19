# Author:GaoYuCai
# Author:GaoYuCai
import  threading,time
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n=n
    def run(self):
        lock.acquire()
        global num
        num+=1
        time.sleep(1)
        lock.release()
lock=threading.Lock()
num=0
t_obj=[]
for  i  in  range(100):
    t=MyThread("t-%s"%i)
    t.start()
    t_obj.append(t)
for t  in t_obj:
    t.join()

print("num",num)
