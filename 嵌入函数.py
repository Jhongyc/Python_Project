name="Alex"
def changename(name):
    name="Alex2"
    def changename2():
        name="Alex3"
        print("第三层打印：",name)
    changename2()
    print("第二层打印：",name)
changename(name)
print("最外层打印",name)