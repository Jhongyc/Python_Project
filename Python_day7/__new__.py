# Author:GaoYuCai
class Foo(object):
    def __init__(self,name):
        self.name=name


f=Foo("Alex")
print(type(f))
print(type(Foo))


Too=type("Too",(object),{'fun':fun})