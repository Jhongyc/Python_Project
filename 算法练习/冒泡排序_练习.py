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

@cal_time
def bobblu_sort(l):
        for i in range(len(l)-1):
            for j  in range(len(l)-i-1):
                if l[j] > l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]



data=[2,83,87,65,45]
bobblu_sort(data)
print(data)

