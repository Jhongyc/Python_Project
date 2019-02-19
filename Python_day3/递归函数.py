# Author:GaoYuCai
#必须要有结束
#效率不高
#时间复杂度
'''def calc(n):
    print(n)
    if int(n/2)==0:
        return n
    return calc(int(n/2))


calc(10)'''

def calc(n):
    print(n)
    if int (n/2)>0:
        return calc(int(n/2))


calc(10)