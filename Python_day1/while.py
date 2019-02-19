# Author:GaoYuCai
count=0
age_of_oldboy=56
while  count <4:
    guess_age =int(input("guess age:"))
    if guess_age==age_of_oldboy:
        print("yes")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller..")
    else:
        print("think biggest!")
    count=count+1
else:
    print("You have tried many time..fuck off")
#while..else:如果while中的不对，则执行else中的。