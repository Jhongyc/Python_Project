# Author:GaoYuCai
#def bulk(self):
    #print("%s is yelling..."%self.name)
class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print("%s is eating.."%self.name,food)
d=Dog("小明")
choice=input(">>:").strip()
if hasattr(d,choice):
    #delattr(d,choice)
    atbbtr=getattr(d,choice)
    setattr(d,choice,"RongHua")
else:
    #setattr(d,choice,bulk)
    #d.talk(d)
    setattr(d,choice,22)
    print(getattr(d,choice))
print(d.name)