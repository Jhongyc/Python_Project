# Author:GaoYuCai
items=[2,35,2,45,90]
def sum(items):
    head,*tail=items
    return head+sum(tail) if tail else head

print(sum(items))