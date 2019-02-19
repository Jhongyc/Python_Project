# Author:GaoYuCai
list=[9,5,3,1,6,0,4,2,8,7]
def shell_sort(list):
    step=int(len(list)/2)
    for i in range(len(list)):
        if i+step < len(list):
            vlaue=list[i]
            if list[i]>list[i+step]:
                list[i],list[i+step]=list[i+step],list[i]
        step=int(step/2)
    else:
        for v in range(1,len(list)):
            key=list[v]
            for j in range(v,-1,-1):
                if key <list[j-1]:
                    list[j+1]=list[j-1]
                else:
                    break
                list[j]=key
            return  list

print(shell_sort(list))