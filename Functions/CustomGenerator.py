def cust(x,y):
    while x<y:
        yield x
        x+=1

res=cust(12,56)

for i in res:print(i)