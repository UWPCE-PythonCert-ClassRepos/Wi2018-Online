
ltn =[]   # user entered donar names with duplicate name
lt = []   #donar names,amount of the donars with duplicate names
ldupname = [] # all the names of the donar with duplicates names
luniname = []  # no duplicate names
lcountname = []   #this will count the names how many times donar  donated
lfinal = []
lfinalname_amount_count = []  #this is final list of names ,total amount,number of times donated and average amount
ldonationlistentered = []


def  flist(x,y):
    name = x
    amount = y
    c =(name,amount,1)
    lt.append(c)

def fdonate():
    x = input("enter name :   ")
    y = input("enter amount:   ")
    y1 = int(y)
    c = (x,y1,1)
    c1 =(x,y1)
    ldonationlistentered.append(c1)
    ltn.append(c)
    fask()

def  fask():
  print("do you want donate: y/n")
  c1 = input("enter     ")
  if(c1 =='y' or c1 == 'Y'):
    fdonate()

def  fappend():
   for i in ltn:
       lt.append(i)

def  fdupname():
    for i in lt:
        ldupname.append(i[0])

def funiname():
    luniname = set(ldupname)
    return list(luniname)


def fsumcount():
    ltuni = funiname()
    for i in ltuni:
        lcount = 0
        lsum = 0
        for j in  lt:
          if(i == j[0]):
            lsum = lsum +j[1]
            lcount = lcount+j[2]
            ln = i
            lm = lsum
            lc = lcount
            c =(ln,lm,lc)
            lfinal.append(c)

def fcountname():
    from collections import Counter
    count_names = Counter(ldupname)
    for i in count_names:
        n = i
        c = count_names[i]
        f = (n, c)
        lcountname.append(f)

def ffinal():
       for  i in lcountname:
        for j in lfinal:
            if(i[0] == j[0] and i[1]== j[2]):
               ln = i[0]
               lm = j[1]
               lc = i[1]
               lv = int(lm/lc)
               c =(ln,lm,lc,lv)
               lfinalname_amount_count.append(c)

def ftablehead():
    print("+----------------------------+------------------+-------------------+-------------------+")
    print("|     Donar Name             |  Total given     | Number of gifts   |    Average gift   |")
    print("+----------------------------+------------------+-------------------+--------------------")



def  ffinalreport(x):
    lt = x
    for i in lt:
      name = i[0].upper()
      total = '$'+str(i[1])
      avg   = i[2]
      avgtotal ='$'+str(i[3])
      print("{: >20} {: >20} {: >20}{: >20}".format(name, total, avg, avgtotal))

def ffinaln_m_cl(x):
    lt = set(x)
    print(lt)



def fdata():
  flist("mike",100)
  flist("praveen",231)
  flist("praveen",35)
  flist("mike",50)
  flist("ravi",300)
  flist("praveen",4)
  flist("kelly",5)
  flist("mark zack hio",1.5)
  flist("joy",20007)


def  fall():
 fask()
 fdata()
 fappend()
 fdupname()
 fsumcount()
 fcountname()
 ffinal()
 ftablehead()
 ffinalreport(lfinalname_amount_count)




print("Menu:")
print("1.Send thank you mail")
print("2.Create report")
print("3.quit")
i = int(input("enter your choice 1 or 2 or 3:       "))
if(i == 1):
          print("Thank you")
          print("1.Do you want to see the donars list")
          print("2.Do you want to donate ")
          print("3.quit")
          k = int(input("enter your choice 1 or 2 or 3:       "))
          if(k == 1):
              fdata()
              fappend()
              fdupname()
              fsumcount()
              fcountname()
              ffinal()
              luni = funiname()
              print("The list of donars")
              for i in luni:
                  print("{: >20}".format(i.upper()))
          elif(k == 2):
              fall()
              l = ldonationlistentered
              for i in l:
                a = '4'+i[0].upper()
                b = '$'+str(i[1])
                c = i[0].upper()
                file = open("{}"".txt".format(a),'a+')
                file.write("  Dear  ""{}".format(c))
                file.write("\n")
                file.write(" \n")
                file.write("    Thank you for your very kind donation of ")
                file.write("{}".format(b))
                file.write(".\n")
                file.write("\n")
                file.write("    It will be used for very good cause.")
                file.write("\n")
                file.write("           Sincerely, \n")
                file.write("          -The Team  ")
                file.close




elif(i == 2):
      fdata()
      fappend()
      fdupname()
      fsumcount()
      fcountname()
      ffinal()
      ftablehead()
      ffinalreport(lfinalname_amount_count)
      print("DO you like to send thank you mail to donars")
      print("Enter y/n")
      i = input("enter      ")
      if(i == 'Y' or i == 'y'):
          for i in lfinalname_amount_count:
              a = '4'+i[0].upper()
              b = '$'+str(i[1])
              c = i[0].upper()
              file = open("{}"".txt".format(a),'a+')
              file.write("  Dear  ""{}".format(c))
              file.write("\n")
              file.write(" \n")
              file.write("    Thank you for your very kind donation of ")
              file.write("{}".format(b))
              file.write(".\n")
              file.write("\n")
              file.write("    It will be used for very good cause.")
              file.write("\n")
              file.write("           Sincerely, \n")
              file.write("          -The Team  ")
              file.close

