# Author:GaoYuCai
#导入第三方库时，自动在里进行查找
#默认第三方库存放在site-packags中
#Python解释性语言
#数据类型初识
#1.数字
#2.type（）查看数据的数据类型
#bool类型  1表示True  0  表示 False
#三元运算
#例子： result= 值1  if 条件 else  值2
#进制 二进制  八进制   十进制  十六进制
#bytes 数据类型  字节数据类型不同于字符串
#把二级制 转换成字符串 --> decode
#把字符串 转换成 二进制  --> encode
#masg="我爱北京天安门"
#print(masg.encode(encoding="utf-8"))
#print(masg.encode().decode())
names=["zhangyang","guyun","xuliangchen","shhao"]
print(names[0])
print(names[1:2])#顾头不顾尾，切片
print(names[-2:])#机器数数是从左往右数的
names.append("leihaidong")
names.insert(0,"gaoyucai")
print(names)
#name=names.pop()
#del names[2]
#name=names.remove("gaoyucai")
#print(name)
#print(names)
#count=names.index("leihaidong")
#print(names[count])

#print(names.count("gaoyucai"))
#print(names.clear())#清空列表
#names.reverse()#翻转
#names.sort(reverse=True)
#print(names)
#names.extend(name2)
#del name2
#name2=names.copy()
#print(names)
#print(name2)
#names[0]="高宇才"
#print(names)
#print(name2)#浅copy仅仅copy第一层
#name3=names[:]
#print(name3)
#import copy
#name4=copy.copy(names)
#name5=copy.deepcopy(names)
#print(names[0:-1:2])#循环跳着打印
'''三种实现浅copy的方法：
import copy
person=['name',['a',100]]
p1=copy.copy(person)
p2=person[:]
p3=list(person)
'''




