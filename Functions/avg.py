def average(a,b):
    print("Average of two numbers is",(a+b)/2)
    ###OR##
    return (a+b)/2

result=average(10,4) 
print(result)
#OR#
print(average(b=10,a=4))#key arguments
print(result)

def sum(a=10,b=5):#defalut values set while defining func
    print("Sum of two numbers is",(a+b))
    ###OR##
res=sum()
print(res)