# Author:GaoYuCai
count=0
age_of_oldboy=56
while count <3:
    guess_age=int(input("guess age:"))
    if guess_age== age_of_oldboy:
        print("Yes,you are right!")
        break
    elif guess_age< age_of_oldboy:
        print("Think smaller!")
    else:
        print("think biggest!")
    count=count+1
    if count==3:
        sw=input("Do you want continue? y/n:")
        if sw=="y":
            count=0
        else:
            break


