# Author:GaoYuCai
import time
username="sunli"
password="123"
def auth(ac):
    if ac=="local":
        def out_wrapper(func):
            print("请输入你的用户名和密码")
            username=input("username:")
            password=input("password:")
            if username =="sunli" and password=="123":
                def wrapper(*args, **kwargs):
                    start_time = time.time()
                    func(*args, **kwargs)
                    finish_time = time.time()
                    print("登录花费时间为：", finish_time - start_time)
                return wrapper
            else:
                print("登录失败！")

        return out_wrapper

@auth(ac="local")
def bbs(name):
    print("欢迎进入%s的BBS界面！"%name)

bbs("sunli")

#第一步：
#bbs=auth(bbs)  #bbs=wrapper
#bbs()
#第二步
#bbs("sunli")
#可以理解为使用者参数，和实际者参数。
#第三步

