# Author:GaoYuCai
import  time
def cal_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        finish_time=time.time()
        print("时长：",func.__name__,finish_time-start_time)
        return result
    return wrapper


def quick_sort_x(l,left,right):
    if left <right:
        mid=partition(l,left,right)
        quick_sort_x(l,left,mid-1)
        quick_sort_x(l,mid+1,right)
def partition(l,left,right):
    tmp=l[left]
    while left < right:
        while left < right and l[right] >=tmp:
            right-=1
        l[left]=l[right]
        while left <right and  l[left] < tmp:
            left+=1
        l[right]=l[left]
    l[left]=tmp
    return left

def quick_sort(l):
    return quick_sort_x(l,0,len(l)-1)


data=[2,4,1,9,7,5]
quick_sort(data)
print(data)