# Author:GaoYuCai
class   AlexException(Exception):
    def __init__(self,msg):
        self.message=msg
    #def __str__(self):
     #   return self.message

try:
    raise AlexException("数据库连接失败")#触发异常
except AlexException as  e:
    print(e)
