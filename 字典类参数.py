def stu_register(name,age,*args,**kwargs):
    print(name,age,args,kwargs)


stu_register("Alex",22,"CN",'Python',sex="Male",province='shandong')