alist = []
lfw = []


st = "hello good morning this is a good day morning this is a start and hello good is a things."


def ftwo():
  ct = 0
  for i in st:
      file = open("4assign42.txt", 'a+')
      file.write(i)
      if(i == ' ' or i == '.'):
        ct = ct+1
        if(ct == 2):
            file.write("\n")
            ct =0

def fread():
    file = open("4assign42.txt", "r")
    for line in file:
         c = (line)
         alist.append(c)
    file.close

def indexall(a, value):
   return [i for i, v in enumerate(a) if v == value]


def fnextword1(alist,i):
  k = indexall(alist,i)
  for i in k:
       c = alist[i+1]
       for k in c:
         print(k,end ='')
         if(k == ' '):
           print(',',end ='')
           break


fread()
s = len(alist)
k = set(alist)
print(st)
for i in k:
    print("\n")
    print(i, '----------->', end='')
    fnextword1(alist, i)