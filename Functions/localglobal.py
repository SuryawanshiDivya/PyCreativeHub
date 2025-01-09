x=123 #global variable

def display():
    y=678 #local variable
    x=345
    print(y)
    print(x)
    print(globals()['x']) #to get global value of same name variable

print(x)
#display()
z=display
z()

