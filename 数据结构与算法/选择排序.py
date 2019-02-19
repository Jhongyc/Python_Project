# Author:GaoYuCai
def select_sort(li):
    for i in range(len(li)-1 ):
        min_loc=i
        for j  in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc=j
        li[i],li[min_loc]=li[min_loc],li[i]
data=[23,45,24,67,43]
select_sort(data)
print(data)



