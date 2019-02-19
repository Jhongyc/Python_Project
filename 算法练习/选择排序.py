# Author:GaoYuCai
def select_sort(li):
    for i in range(len(li)-1):
        mid_loc=i
        for j  in range(i+1,len(li)):
             if li[j] < li[mid_loc]:
                 mid_loc=j
        li[i],li[mid_loc]=li[mid_loc],li[i]


data=[3,1,4]
select_sort(data)
print(data)