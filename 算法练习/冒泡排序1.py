# Author:GaoYuCai
def bobblu_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] >li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]

data=[2,4,7,6,1,9,0,10]
bobblu_sort(data)
print(data)
