# Author:GaoYuCai
f="c:\\file.txt"
f=open(f,'rb')#data文件句柄，文件的内存对象大小，文件的内存起始位置
'''for index,line in enumerate(f.readlines()):
    if index==9:
        print("----------")
        continue
    print(line.strip())



    for  i in  range(5):
    print(f.readline())
count =0
for line  in f:
    print(line)
print(f.readline())
print(f.tell())
f.seek(10)
print(f.readline())
print(f.encoding)
print(f.fileno())
print(f.flush())
print(f.buffer)'''
#print(f.truncate())#截断字符数
#读写r+读和追加
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.tell())
#f.write("------------diao-----------")
#print(f.readline())
#写读W+ 先创建文件，再读
#a+追加读写
#网络传输 使用“rb”格式--二进制模式
#二进制写入“wb”










