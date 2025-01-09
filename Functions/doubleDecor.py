def decor(func):
    def inner():
        result=func()
        return result*2
    return inner

@decor #automatically applied to function
def num():
    return 5

#res= decor(num)
print(num())   
