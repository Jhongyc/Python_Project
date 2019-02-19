# Author:GaoYuCai
name="Alex"
print(name.capitalize())#首字母大写
print(name.count("a"))#计算重复出现的字符
print(name.center(50,"-"))
print(name.endswith("ex"))#判断字符串以什么结尾
print(name.expandtabs(tabsize=30))#打印多少个空格
print(name.find("name"))#查找字符开头的索引
print(name.format())#格式化输出
print(name.isalnum())#是不是阿拉伯数字
print(name.isalpha())#是否是纯英文字符
print(name.isdecimal())#是否是十进制
print(name.isidentifier())#判断是不是一个合法的变量名
print(name.isdigit())#是否是一个整数
print(name.isnumeric())#是否是个只有数字
print(name.istitle())#每个首字母大写
print(name.isprintable())
print(':'.join(['1','2','3','4']))
print(name.ljust(50,"*"))
print(name.rjust(50,'*'))
print(name.lstrip())#去除空格或者回车
p=str.maketrans("abcdef","123456")
print("alex li".translate(p))
print("alex".replace("l","L",1))#替换
print("alex Li".rfind("e"))
print("Al ex".split())#以空格分成列表
print('Alex'.splitlines())#按照换行分割
print("Alex".swapcase())#大写变小写
print(name.title())
print(name.zfill(50))
print(name.upper())
print(name.lower())
