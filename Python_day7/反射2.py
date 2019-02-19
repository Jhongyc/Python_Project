# Author:GaoYuCai
def bulk(self):
    print("wo...wo")
class Dog(object):
    def __init__(self):
        self.name='Alex'
    def eat(self):
        print("啃骨头!!!")
de=Dog()
print(hasattr(Dog,"eat"))

d=getattr(de,"nam",22)
print(d)
setattr(de,"eat",23)
c=getattr(de,"eat")
print(c)
print(de.name)
delattr(de,"name")
print(de.name)
