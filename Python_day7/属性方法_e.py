# Author:GaoYuCai
#属性方法：把一个方法变成一个静态属性
class Flight(object):
    def __init__(self,name):
        self.name=name
    def cheching_status(self):
        print("checking flight %s status"%self.name)
        return 1
    @property
    def fright_status(self):
        status=self.cheching_status()#重点
        if status==0:
            print("flight got canceled...")
        elif status==1:
            print("flight is arrived...")
        elif status==2:
            print("flight has departured already...")
        else:
            print("Cannot confirm the flight status...please check later")

f=Flight("CA980")
f.fright_status
