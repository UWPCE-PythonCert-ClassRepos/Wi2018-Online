#printing alter numbers
def alter(x):
 l=len(x)
 p = list(x)
 k=tuple(p[0:l:2])
 return k

x=(0,1,2,3,4,5,6,7,8,9,10,11,12,13)
print(x)
y=alter(x)
print(y)
