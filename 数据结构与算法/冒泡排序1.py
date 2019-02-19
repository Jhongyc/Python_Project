# Author:GaoYuCai
data=[2,3,1,3,5,6,8,5,34,89,78,90,90,1,8]
def bobblu_sort(l):
    for i in range(len(l)-1):
        for j  in  range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]


bobblu_sort(data)
print(data)