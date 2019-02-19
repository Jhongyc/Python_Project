# Author:GaoYuCai
class People(object):
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def Work(self):
        print("%s工作在网络公司,收入为%s"%(self.name,self.salary))
class Relation(object):
    def Makefriend(self,obj):
        print("%s make friend with %s"%(self.name,obj.name))
class Man(People,Relation):
    def __init__(self,name,age,salary,cate):
        super(Man,self).__init__(name,age,salary)
        self.cate=cate
    def Smoking(self):
        print("%s一天抽%s包烟"%(self.name,self))
    def Work(self):
        People.Work(self)
        print("好辛苦！")
class Woman(People,Relation):
    def __init__(self,name,age,salary):
        People.__init__(self,name,age,salary)
    def Wish(self):
        print("%s wish will has a boyfriend"%self.name)

B=Man("Tan",24,3000,1)
G=Woman("Cheng",24,3000)
G.Wish()
B.Work()
B.Makefriend(G)
