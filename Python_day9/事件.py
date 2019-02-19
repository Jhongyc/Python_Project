# Author:GaoYuCai
import threading
import time
event=threading.Event()
def lighter():
        count=0
        event.set()#设为绿灯
        while True:
                if count >5 and count <10:#改成红灯
                        event.clear()#把标志位清空
                        print("\033[41;1m red light is on...\033[0m ")
                        time.sleep(1)
                elif count >10:
                        event.set()#变绿灯
                        count=0
                else:
                        print("\033[42;1m green light is on...\033[0m")
                time.sleep(1)
                count+=1
def car(name):
        while True:
                if event.is_set():
                        print("[%s]running"%name)
                else:
                        print("[%s]see  red light,watting..."%name)
                        event.wait()
                        print("\033[34;1m[%s]green light is on,start going...\033[0m"%name)
light=threading.Thread(target=lighter,)
light.start()
car1=threading.Thread(target=car,args=("Tesla",))
car1.start()
