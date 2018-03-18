#Fibonaaci series for integer 20
def  fib(x):
    if(x==1):
     return 1
    elif(x==0):
     return 0
    else :
     return fib(x-1)+fib(x-2)

x=20
for i in range(0,x+1,1):
 z=fib(i)
 print(z)
