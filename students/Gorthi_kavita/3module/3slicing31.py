#first and last four items removed and every other item in between for the string
def falters(x):
 k = x
 l=len(k)
 m = k[0:l-4]
 return m[4:l:2]


x=("This is a string.This can be a test")
print(x)
y=falters(x)
print(y)
