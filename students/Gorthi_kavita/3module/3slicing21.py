#string prints alternate characters
def falters(x):
 k = x
 l=len(k)
 m = k[0:l:2]
 return m


x=("this is a string")
print(x)
a =falters(x)
print(a)
