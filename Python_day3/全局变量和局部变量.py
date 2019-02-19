# Author:GaoYuCai
'''
程序的执行时从上到下的，一定要先定义后调用
局部变量：只在函数里生效，这个函数就是这个函数的作用域
全局变量：
如果在函数中改全局变量  必须声明 global school
school =  oldboy
'''
def change_name(name):
    print("before changename,",name)
    name="Alex Li"
    print("after change,",name)


name="alex"
change_name(name)
print(name)
#非常不建议在局部变量中改全局变量
#字符串和整数不可以改
#列表，字典，集合，类可以在局部变量中改变全局变量
