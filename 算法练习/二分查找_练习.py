# Author:GaoYuCai
import time
def cal_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        finish_time=time.time()
        print("时长：",func.__name__,finish_time-start_time)
        return  result
    return wrapper

@cal_time
def bin_search(l,val):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==val:
            return mid
        elif l[mid] < val:
            low=mid+1
        else:
            high=mid-1
    print("没有找到%s"%val)
data=[1,2,3,4,5,6,7,8,9]
bin_search(data,2)





