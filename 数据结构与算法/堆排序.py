# Author:GaoYuCai
def sift(data,low,high):
    i=low
    j=2*i+1
    tmp=data[i]
    while j <= high:#左孩子在堆里
        if j+1 < high and data [j] < data[j+1]:#如果有右孩子，且有孩子比做孩子大
            j+=1 #j指向右孩子
        if data[j] > tmp:#孩子比最高领导大
            data[i]=data[j]#孩子填到父亲的空位上
            i=j#孩子成为新父亲
            j=2*i+1#新孩子
        else:
            break
    data[i]=tmp  #最高领导放到父亲的位置
def heap_sort(data):
    n=len(data)
    for i in range(n//2-1,-1,-1):
        sift(data,i,n-1)
    #堆建好了
    for i in range(n-1,-1):#i 指向堆得最后
        data[0],data[i]=data[i],data[0]#领导退休，刁民上位
        sift(data,0,i-1)#调整出新领导







