# Author:GaoYuCai
def quick_sort_x(data,left,right):
    if left < right:
        mid=partition(data,left,right)
        quick_sort_x(data,left,mid-1)
        quick_sort_x(data,mid+1,right)
def partition(data,left,right):
    tmp=data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right-=1
        data[left]=data[right]
        while left <right and data[left] <= tmp:
            left+=1
        data[right]= data[left]
    data[left]=tmp
    return left

def quick_sort(data):
    return quick_sort_x(data,0,len(data)-1)

data=[43,7,4,2,0,10,9]
quick_sort(data)
print(data)
