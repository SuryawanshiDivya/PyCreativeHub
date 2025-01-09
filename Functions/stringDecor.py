'''The hello function takes a name and it will return Hello under that name and then even create a decorator

function called How are you that will take the result of the hello function and it will append a string
'''

def decorfunc(func):
    def inner(n):
        result=func(n)
        result=result+"how are you?"
        return result
    return inner

@decorfunc
def hello(name):
    return "hello "+name
print(hello(" Aisha "))