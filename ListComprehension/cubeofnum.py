'''list=[]

for x in range(1,11):
    list.append(x**3)
print(list)'''

#suing list comprehension

lst=[]

lst=[x**3 for x in range(1,11)]

print(lst)