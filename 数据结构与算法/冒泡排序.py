# Author:GaoYuCai
import random
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        if not exchange:
            break
#data=list(range(1000))
#random.shuffle(data)
data=[4,1,3,2,5,7,6,9,8]
bubble_sort(data)
print(data)