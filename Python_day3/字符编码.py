# Author:GaoYuCai
'''ascill 一个字节 不能存 汉字
unicode  中文字符三个字节，
python3默认是 unicode'''
s="你好"
s_gbk=s.encode()
print(s)
print(s.encode())