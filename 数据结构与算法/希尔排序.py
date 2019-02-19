# Author:GaoYuCai
def shell_sort(li):
    gap =len(li)//2
    while gap >=1:
        for i in range(gap,len(li)):
            tmp=li[i]
            j=i-gap
            while j > 0 and tmp <li[j]:
                li[j+gap]=li[j]
                j-=gap
            li[i-gap]=tmp
            gap/=2 