# Author:GaoYuCai
#位置参数--实参和形参一一对应，多了少了都不行
'''def test(x,y):
    print(x)
    print(y)

test(y=2,x=1)#关键字调用
test(1,2)
'''
#既有关键字调用，又有位置参数（首先尊重位置参数）
#关键参数  不能写在位置参数之前
'''
默认参数：调用函数时，默认参数非必须传递
用途：1.默认安装值
      2.默认端口号
 '''
'''
参数组

'''

#def test(*args):
 #3   print(args)

#test(1,2,3,4,5,6,7,8,9)
#test(*[1,2,3,4 ])

def test(**kwargs):
    print(kwargs)

test(name='alex',age=8,sex="F")
test(**{'name':"alex","age":8})


















