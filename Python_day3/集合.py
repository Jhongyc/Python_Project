# Author:GaoYuCai
list_1=[1,4,5,7,3,6,7,9]
list_1=set(list_1)
list_2=set([2,6,0,66,22,8,4])
#交集
#print(list_1.intersection(list_2))
#并集
#print(list_1.union(list_2))
#差集   我有你没有
print(list_1.difference(list_2))
print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))
#反向差集两个互相都没有的取出来即对称差集
print(list_1.symmetric_difference(list_2))
#如果两个集合没有交集返回为true
#list_2.isdisjoint()
#基本操作
#添加add (添加一项) update（添加多项）
list_1.add(666)
list_1.update([444,555,777])
print(list_1)
#remove可以删除一项
list_1.remove(444)
print(list_1)
#长度
print(len(list_1))
#测试是否是list_1的成员
#x  not  in  list_1
#x  in    list_1
#print(list_1.pop())
list_1.discard()

