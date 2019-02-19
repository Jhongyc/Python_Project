# Author:GaoYuCai
def getTalk(type="shut"):
    def shut(word="yes"):
        return word.capitalize()+"!"
    def whisper(word="yes"):
        return  word.lower()+"..."
    if type=="shut":
        return shut
    else:
        return whisper


talk=getTalk()

print(talk)
print(talk())
print(getTalk("whisper")())