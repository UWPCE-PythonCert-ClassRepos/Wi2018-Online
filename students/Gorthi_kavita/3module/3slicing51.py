# middle third,last third and first third in new sequence

def newsequence(x):

 lst = x
 l = len(lst)
 print(l)
 rd = int(l/2)
 b = lst[rd+3]+lst[l-3]+lst[3]
 return b



lst =("Welcome to Python class")
print(lst)
b = newsequence(lst)
print (b)
