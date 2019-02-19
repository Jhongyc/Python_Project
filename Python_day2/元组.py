# Author:GaoYuCai
#names的方法  count和index
shopping_list= []
product_list=[
    ("Iphone",5800),
    ("Mac Pro",9800),
    ("Bike",800),
    ("Watch",10600),
    ("Coffee",31),
    ("Alex  Python",120),
]
salary=input("Input your salary:")
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice=input("选择要买的商品》》》：")
        if  user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice <len(product_list) and user_choice >= 0:
                p_item=product_list[user_choice]
                if p_item [1] <= salary:
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print("Added %s into shoping cart,your current balance is\033[31;1m %s\033[0m"%(p_item,salary))
                else:
                    print("你的余额剩余%s"%(salary))
        elif user_choice =="q":
            print("---------shopping list -----------")
            for p in shopping_list:
                print(p)
            print("你的余额是：",salary)
            exit()

        else:
            print("invalid  option")





