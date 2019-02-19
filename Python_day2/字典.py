# Author:GaoYuCai
info={
    'stu1101':"TengLan Wu",
    'stu1102':"LongZe LuoLa",
    'stu1103':"XiaoZe MaliYa",
}
#字典是无序的，无下标

#print(info["stu1101"])
#info["stu1104"]="武藤兰"
#print(info["stu1104"])
#print(info)
#创建和修改info[]=""
#除del info['']
#删除pop（），info.pop('')
#删除 info.popitem()
#查找
#print(info.get('stu1103'))
#print('stu1103'  in  info)

#av_catalog=["大陆"]["1024"][1]
#setdefault()
b={
    'stu1101':"Alex",
    1:3,
    2:5,
}
info.update(b)
print(info)
print(info.items())
c=dict.fromkeys([6,7,8],'gyc')#初始化一个新的字典
print(c)
#字典的循环