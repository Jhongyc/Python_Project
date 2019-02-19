# Author:GaoYuCai
#装饰器又叫 语法糖
import time
user,passwd="Alex",'abc123'

def auth(func):
    def wrapper(*args,**kwargs):
        username=input("Username: ".strip())
        Password=input("Password: ".strip())

        if user==username and passwd==Password:
            print("\033[32;1mUser has passwd authentication\033[0m")
            func(*args,**kwargs)
        else:
            exit("\033[31;1mInvaild \033[0m")
    return wrapper
@auth
def index():
    print("Welcome to index page")
@auth
def home():
    print("Welcome to home page")
@auth
def bbs():
    print("Welcome to bbs page")

bbs()