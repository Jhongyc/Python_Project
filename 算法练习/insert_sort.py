# Author:GaoYuCai
def insert_sort(list):
    for i in range(1,len(list)):
        vlaue=list[i]
        for j in range(i,-1,-1):
            if vlaue < list[j-1]:
                list[j]=list[j-1]
            else:
                break
        if list[j-1]!=vlaue:
            list[j]=vlaue
    return list
print(insert_sort([2,5,1,3,8]))
# def insert_sort(list):
#     for i in range(1,len(list)):
#         key=list[i]
#         j=i-1
#         while j>= 0 and list[j]>key:
#             list[j+1]=list[j]
#             j-=1
#         list[j+1]=key
#     return list
