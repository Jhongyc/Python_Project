# Author:GaoYuCai
import  queue
q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())
p=queue.PriorityQueue()
p.put((10,"alex"))
p.put((1,"gao"))
p.put((14,"cai"))
print(p.get())