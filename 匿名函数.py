def calc(n):
    return n**n
print(calc(10))


calc=lambda n:n**n
print(calc(10))

res=map(lambda x:x**2,[1,5,7,4,8])
for i in res:
    print(i)