def display():
    def message(): #inner function
        return "Hello"
    return message

func=display()
print(func())


