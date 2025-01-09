from functools import reduce

lst=[3,6,1,7]

res= reduce(lambda x,y:x+y,lst)
print(res)