# Author:GaoYuCai
#静态方法只是名义上归管理，实际上在静态方法里，访问不了类或者实例中的任何属性
class Dog(object):
    n=33
    def __init__(self,name):
        self.name=name
        self.__food=None
    #@staticmethod#实际上和类没什么关系了，但必须经过类名调用
    #@classmethod#类方法只能访问类变量，不能访问实例变量
    @property#把一个方法变成一个静态属性
    def eat(self):
        print("%s  is eating %s"%(self.n,self.__food))
    @eat.setter
    def eat(self, food):
        print("set to food:", food)
        self.__food=food
d=Dog("chenronghua")
d.eat
d.eat="包子"