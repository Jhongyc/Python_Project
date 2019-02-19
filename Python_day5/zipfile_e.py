# Author:GaoYuCai
import zipfile
z=zipfile.ZipFile("test.zip",'w')
z.write("test1")
print("----")
z.close()

f=zipfile.ZipFile("test.zip",'r')
z.extractall()
z.close()