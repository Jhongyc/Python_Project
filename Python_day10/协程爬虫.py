# Author:GaoYuCai
from urllib  import request
def  f(url):
    print("GET:%s"%url)
    resp=request.urlopen(url)
    data=resp.read()
    print("%d bytes received from %s"%(len(data),url))

f("https://www.baidu.com")