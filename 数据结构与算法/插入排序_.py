# Author:GaoYuCai
def insert_sort(li):
    for i in range(1,len(li)):
        tmp=li[i]
        j=i-1
        while j>= 0 and li[j] >tmp:
            li[j+1]=li[j]
            j=j-1
        li[j+1]=tmp

data=[2,53,7,12,9]
insert_sort(data)
print(data)