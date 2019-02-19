# Author:GaoYuCai
def shut(word="yes"):
    return word.capitalize()+"!"
def doSomethingBefore(func):
    print("I do something before then I call the function you gave me")
    print(func())

doSomethingBefore(shut)