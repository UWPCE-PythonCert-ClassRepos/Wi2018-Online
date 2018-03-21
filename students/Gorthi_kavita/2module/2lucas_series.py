#lucas series for integer 20
def  lucas(x):
    if(x==2):
     return 1
    elif(x==1):
     return 2
    else :
     return lucas(x-1)+lucas(x-2)

x=20
for i in range(1,x+1,1):
 z=lucas(i)
 print(z)
