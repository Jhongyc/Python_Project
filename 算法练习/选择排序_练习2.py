# Author:GaoYuCai
def seleect_sort(li):
    for i in range(len(li)):
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc=j
        li[i],li[min_loc]=li[min_loc],li[i]