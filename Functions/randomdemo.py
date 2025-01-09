from random import *


print(random()) #random number between 0 and 1

for i in range(10):
    print(random())

for i in range(10):
    print(randint(1,50))

for i in range(10):
    print(uniform(1,50))

for i in range(10):
    print(randrange(10) )
    print(randrange(1,14,6))

list=["java","javascript","c++"]

for i in range(2):
    print(choice(list))