def half(func):
    def inner():
        n=func()
        return n/2
    return inner

def square(func):
    def inner():
        n=func()
        return n*n
    return inner

#depending on order result will be displayed

@square
@half
def num():
    return 10

print(num())