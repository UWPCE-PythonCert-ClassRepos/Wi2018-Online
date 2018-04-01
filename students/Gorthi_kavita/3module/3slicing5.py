#4. middle third,last third and first third in new sequence

def  neworder(x):
 a =[]
 lst = x
 l = len(lst)
 rd = int(l/2)
 l1 = list(lst)
 l2 = l1[rd+3]
 l3 = l1[l-3]
 l4 = l1[3]
 a.append(l2)
 a.append(l3)
 a.append(l4)
 b = tuple(a)
 return b


lst =(1,2,3,4,5,6,7,8,9,10)
print(lst)
print("print middle third,last third,first third in the new order")
y =neworder(lst)
print (y)
