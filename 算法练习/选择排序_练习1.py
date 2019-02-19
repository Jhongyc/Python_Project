# Author:GaoYuCai
def select_sort(li):
    for i in range(len(li)-1):
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc=j
        li[i],li[min_loc]=li[min_loc],li[i]

data=[12,4,6,23,90,24]
select_sort(data)
print(data)