# Author:GaoYuCai
def count_sort(li,max_num):
    count=[0 for i in range(max_num+1)]
    for num in li:
        count[num]+=1
    i=0
    for num,m in enumerate(count):
        for j in range(m):
            li[i]=num
            i+=1



