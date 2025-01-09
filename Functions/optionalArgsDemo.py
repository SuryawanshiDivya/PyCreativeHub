def myfunc(x, *args,**kwargs): #* (positional) AND **(keyword args ) is optional positional parameter pass any number of values stored as tuple
    print(x)
    for each_arg in args:
        print(each_arg)
    for each_kwrg in kwargs.items():
        print(each_kwrg)
    for key, value in kwargs.items():
        print(key, value)


print(myfunc(10, 20, name="Aisha"))