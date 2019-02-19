# Author:GaoYuCai
def insrt_sort(li):
    for i in range(1,len(li)):
        tmp=li[i]
        j=i-1
        while j >=0 and li[j]  >= tmp:
            li[j+1]=li[j]
            j=j-1
        li[j+1]=tmp
data=[32,65,46,88,32,53]
insrt_sort(data)
print(data)



