# Author:GaoYuCai
# #列表生成式
#生成器 generator:只有在调用时才会生成相应的数据
#只记录当前的位置
#生成器的  next方法循环自动调用next方法
#斐波拉契数列
#yield 保存函数终端状态
#L=(i*2 for i in range(10))
'''def fib(max):
    n,a,b=0,0,1
    while n<max:
        #print(b)
        yield b
        a,b=b,a+b
        n=n+1
    return "done"#异常返回值也就是异常打印的消息
f=fib(3)
print(f.__next__())
print(f.__next__())
print(f.__next__())
'''

