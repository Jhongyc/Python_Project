# Author:GaoYuCai
import  threading,time
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n=n
    def run(self):
        print("runnint task:",self.n)
        #time.sleep(2)
start_time=time.time()
t_obj=[]
for  i  in  range(50):
    t=MyThread("t-%s"%i)
    t.setDaemon(True)#把当前线程设置为守护线程，一定在start之前
    t.start()
    t.join()
 #   t_obj.append(t)
#for t  in t_obj:
#    t.join()
print("cost:",time.time()-start_time)