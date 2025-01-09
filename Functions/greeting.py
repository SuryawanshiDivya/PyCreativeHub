def display(name):
    def message(): #inner function
        return "Hello"
    result=message()+name
    return result

print(display(" Aisha "))

