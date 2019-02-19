# Author:GaoYuCai
def shut(word="yes"):
    return word.capitalize()+"!"

#函数是对象！！！
#print(shut())
#scream=shut
#print(scream())
#函数可以被定义在另一个函数里面
def talk():
    def whisper(word="yes"):
        return word+'!'
    print(whisper())
talk()
