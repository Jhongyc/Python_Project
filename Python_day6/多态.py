# Author:GaoYuCai
#一个接口多种实现"实现接口的重用"
class Animal:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def animal_talk(obj):
        obj.talk()
class Dog(Animal):
    def talk(self):
        print("Woof  Woof!")
class Cat(Animal):
    def talk(self):
        print ("Miao  miao...")


d=Dog("xioaming")
Animal.animal_talk(d)