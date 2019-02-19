# Author:GaoYuCai
#class People  经典类
class People(object):#新式类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("%s is eating ..."%self.name)
    def talk(self): 
        print("%s is talking..."%self.name)
    def sleep(self):
        print("%s is sleeping..."%self.name)
class Relation(object):
    def makefriends(self,obj):
        print("%s is making friends with %s"%(self.name,obj.name))
class Man(People,Relation):
        def __init__(self,name,age,money):
            #People.__init__(self,name,age)#经典类写法
            super(Man,self).__init__(name,age)#新式类写法
            self.money=money
            print("%s 有%s money"%(self.name,self.money))
        def paio(self):
            print("%s is piaoing....20s down"%self.name)
        def sleep(self):
            People.sleep(self)#保存新功能，并且保存父类方法
            print("man is sleeping...")

class Woman(People,Relation):
    def get_birth(self):
        print("%s is born a baby"%self.name)
#python2的经典类，是按照深度优先集成的，新式类是按照广度优先集成的

#python2经典类和新式类都是按照广度类继承的


m1=Man("Alex",22,10)
#m1.eat()
#m1.paio()
#m1.sleep()
w1=Woman("chengronghua",23)
#w1.get_birth()
m1.makefriends(w1)