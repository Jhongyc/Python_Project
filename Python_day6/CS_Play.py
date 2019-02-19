# Author:GaoYuCai
class Role:
    n=123#类变量(类的内存里)
    name='类变量'
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        #构造函数
        #在实例化时做一些类的初始化工作
        #r1=Role__init__0x232542345
        #r1=Role(r1,Alex,Plice,AK47)
        self.name=name#实例变量，（静态属性）作用域是实力本身
        self.role=role
        self.weapon=weapon
        self.life_value=life_value
        self.money=money
    def shot(self):#类的方法，功能（动态属性）
        print("ah..,I got shot...")
    def buy_gun(self,gun_name):
        print("%s just bought %s"%(self.name,gun_name))

r1=Role('Alex','Plice','AK47')#（实例）实例化（初始化一个类，相当于造了一个对象）
r2=Role('Jock','Terrorist','B22')#生成一个角色
r1.buy_gun('AK47')#Role.buy_gun(r1)
r1.bullet_prove=True
#print(r1.weapon)
#del r1.weapon#删除属性
#print(r1.weapon)
r1.n='改类变量'
print("r1:",r1.n)
print("r2",r2.n)
print(r1.n,r1.name,r1.bullet_prove)
print(Role.n)
Role.n="ABC"
