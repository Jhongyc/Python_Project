# Author:GaoYuCai
from gevent import monkey;monkey.patch_all()#把当前程序的的所有的io操作给单独的做上标记
import gevent
from urllib.request import  urlopen
def f(url):
    print("GET:%s"%url)
    resp=urlopen(url)
    data=resp.read()
    print("%d bytes received  from %s"%(len(data),url))
gevent.joinall([gevent.spawn(f,"https://www.baidu.com"),
                gevent.spawn(f,"https://www.yahoo.com"),
                gevent.spawn(f,"https://github.com"),])