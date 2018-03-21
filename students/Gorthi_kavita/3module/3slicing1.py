#String exchange of first and last characters
def func(x):
 k = x
 l=len(k)
 return  (k[l-1]+k[1:l-1]+k[0])


x=("Happy Birthday")
print(x)
print("After exchange of last and first characters")
y=func(x)
print(y)
