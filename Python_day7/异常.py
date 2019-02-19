# Author:GaoYuCai
data={}
name=["alex","jack"]
try:
    data['name']
    name[3]
#except (KeyError,IndexError )as e:
    #print("没有这个Key",e)
#except IndexError as e:
    #print("列表操作错误",e)
except Exception as e:
    print("出错了",e)

    print("位置错误")
else:
    print("一切正常")
finally:
    print("不管有没有错，都要执行")