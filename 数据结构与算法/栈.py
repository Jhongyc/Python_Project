# Author:GaoYuCai
def quick_sort_x(li,left,right):
    if left < right:
        mid=partition(li,left,right)
        quick_sort_x(li,left,mid-1)
        quick_sort_x(li,mid+1,right)

def partition(li,left,right):
    while left < right:
        tmp=li[left]
        while left <right and li[right] >= tmp:
            right-=1
        li[left]=li[right]
        while left < right and li[left] < tmp:
            left+=1
        li[right]=li[left]
    li[left]=tmp
    return left

def quick_sort(li):
    return quick_sort_x(li,0,len(li)-1)

data=[3,1,6,34,12]
quick_sort(data)
print(data)

