# Author:GaoYuCai
import  time
def cal_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        finish_time=time.time()
        print("时长",func.__name__,finish_time-start_time)
        return result
    return wrapper
@cal_time
def select_sort(li):
    for i in range(len(li)-1):
        min_loc=i
        for j  in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc=j



