# Author:GaoYuCai
#变量可以指向函数，函数的参数可以就收变量。那么一个函数就可以接收
#另一个函数作为参数，这种函数就叫做  高阶函数
def add(x,y,f):
    return f(x)+f(y)


res=add(3,-6,abs)
print(res)

