f= lambda x: 'Yes no is EVEN' if x%2==0 else 'No'
print(f(10))

#using filter getting even number

lst=[10,2,3,4,32]

result= list(filter(lambda x:x%2==0, lst))
print(result)