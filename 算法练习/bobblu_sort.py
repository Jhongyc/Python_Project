# Author:GaoYuCai
def bobblu_sort(l):
    for i in range(len(l)-1):
        for j  in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

data=[2,1,3,5,7,0]
bobblu_sort(data)
print(data)