number=int(input("Enter a number \n"))

pimeFlag='true'

for i in range(2, number-1):
    if number%i==0:
        primeFlag=False
    if primeFlag=='true':
        print(number,"_Prime No")
    else:
        print("Not prime")
        break