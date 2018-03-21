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
    y1 = float(y)
    if(y1 >0):
                c = (x,y1,1)
                c1 =(x,y1)
                ldonationlistentered.append(c1)
                ltn.append(c)
                fask()
    else:
                print("enter donation amount mimimum 1Cent")
                fdonate()


def  fask():
    print("do you want donate: y/n")
    c1 = 'n'
    if(c1 == 'y' or c1 =='Y'):
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

 fdata()
 fappend()
 fdupname()
 fsumcount()
 fcountname()
 ffinal()
 ftablehead()
 ffinalreport(lfinalname_amount_count)


def fprintreport():
 fall()
 l = ldonationlistentered
 for i in l:
     a = '4' + i[0].upper()
     b = '$' + str(i[1])
     c = i[0].upper()
     file = open("{}"".txt".format(a), 'a+')
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

def fmenu1():

    i = int(1)
    if (i == 1):
        fdata()
        fappend()
        fdupname()
        fsumcount()
        fcountname()
        ffinal()
        luni = funiname()
        print("This is the  list of all the donars")
        for i in luni:
            print("{: >20}".format(i.upper()))
        for i in lfinalname_amount_count:
            a = '4' + i[0].upper()
            b = '$' + str(i[1])
            c = i[0].upper()
            file = open("{}"".txt".format(a), 'a+')
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
        print("Thank you mail has been send to all the donars")


def  donar():
       k = 2
       if (k == 2):
         fask()
         fprintreport()


def fmenureport():
    #print("Menu:")
   # print("1.Send Thank you mail")
   # print("2.Create report")
   # print("3.Quit")

            i = int(2)
            if(i == 1):

                fmenu1()


            elif(i == 2):
                  fdata()
                  fappend()
                  fdupname()
                  fsumcount()
                  fcountname()
                  ffinal()
                  ftablehead()
                  ffinalreport(lfinalname_amount_count)

def  menuprint():

            i = int(1)
            if (i == 1):

                fmenu1()


            elif (i == 2):
                fdata()
                fappend()
                fdupname()
                fsumcount()
                fcountname()
                ffinal()
                ftablehead()
                ffinalreport(lfinalname_amount_count)

def thankmail():
     fmenu1()

def fmenu3():
    print("Menu:")
    print("1.Send Thank you mail")
    print("2.Create report")
    print("3.Quit")
    try :
          #  k = input("enter your choice 1 or 2 or 3 ..   " )
            i = int(3)
            if(i == 1):

                fmenu1()


            elif(i == 2):
                  fdata()
                  fappend()
                  fdupname()
                  fsumcount()
                  fcountname()
                  ffinal()
                  ftablehead()
                  ffinalreport(lfinalname_amount_count)


    except Exception as e:
             print(e)
             print("Enter the Valid integer value")
             print("Enter the Menu Options")
             fmenu3()





fprintreport()
thankmail()
fask()
fmenu3()



