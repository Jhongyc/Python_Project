# Author:GaoYuCai
# def insert_sort(list):
#     for i in range(1,len(list)):
#         vlaue=list[i]
#         for j in range(i,-1,-1):
#             if vlaue < list[j-1]:
#                 list[j]=list[j-1]
#             else:
#                 break
#         list[j]=vlaue
#     return list

def insert_sort(list):
    for i in range(1,len(list)):
        vlaue=list[i]
        j=i-1
        while j>=0 and vlaue < list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=vlaue
    return list
print(insert_sort([3,4,1,0,5]))

