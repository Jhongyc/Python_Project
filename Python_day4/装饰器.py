# Author:GaoYuCai
'''装饰器：本质是函数（装饰其他函数）
   为其他函数添加附加功能
   原则：1.不能修改被装饰函数的源代码
         2.不能修改被装饰的函数的调用方式
         总之一句话：装饰器对其被装饰的函数是 完全透明的
         被装饰的函数根本不会感知到装饰器发生的改变
def logger():
    print("Logging")
def test1():
    pass
    logger()

def test2():
    pass
    logger()

test1()

实现装饰器的知识储备：
1.函数即变量
2.高阶函数:
a.把一个函数名当做实参传给另外一个函数
(在不修改被装饰函数的源代码的情况下为期添加功能)
b.返回值中包含函数名
不修改函数的调用方式
3.嵌套函数

import time
def timer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the  func run time is %s"%(stop_time-start_time))
    return warpper()

@timer
def test1():
    time.sleep(3)
    print("In the Test1")
装饰器之函数即变量

def bar():
    print("in the bar")

def foo():
    print("in the foo")
    bar()

foo()
高阶函数：
import  time
def bar():
    time.sleep(3)
    print("in the bar")
def test2(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print(stop_time-start_time)

test2(bar)

import  time
def bar():
    time.sleep(3)
    print("in the bar")
def test2(func):
    print(func)
    return func#函数的返回值

#bar=test2(bar)
bar()
def foo():
    print("in the foo")
    def bar():
        print("in the bar")

    bar()
'''
import  time
def timer(func):
    def deco():
        start_time=time.time()
        func()
        stop_time=time.time()
        print("运行时间：%s"%(stop_time-start_time))
    return deco
@timer
def test1():
    time.sleep(3)
    print("in the test1")
@timer
def test2():
    time.sleep(3)
    print("in the test2")

#test1=deco(test1)
#test2=deco(test2)
#test1()
#test2()
#test1=timer(test1)
test1()
test2()