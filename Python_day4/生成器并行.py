# Author:GaoYuCai
import time
def consumer(name):
    print("%s 准备吃包子啦！"%name)
    while True:
        baozi=yield #
        print("包子[%s]来了，被[%s]吃了！"%(baozi,name))

#c=consumer("g")
#c.__next__()#调用Yield不传值
#b1="韭菜馅"
#c.send(b1)#调用yield，并传值

def producer(name):
    c=consumer("A")
    c2=consumer('B')
    c.__next__()
    c2.__next__()
    print("准备吃包子了！")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半")
        c.send(i)
        c2.send(i)

producer("alex")
