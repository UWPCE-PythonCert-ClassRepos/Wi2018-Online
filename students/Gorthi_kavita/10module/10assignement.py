class donar():
    list =[]   #this is donar list adding  to the list
    allist =[]   #to keep track how many times the donar name in the list
    uniquename = []  # unique donar names
    listsum = []     # donar names and total amount and number of times donated
    listadd =[]
    finalsum = []

    def __data(self,name,amount):
        self.donarname = name
        self.donaramount = amount
        c = (name,amount,1)
        d = (name)
        self.list.append(c)
        self.allist.append(d)

    def donarname(self):
        self.__data("mike",8)
        self.__data("ketty",75)
        self.__data("john hoop",45)
        self.__data("ravi",10)
        self.__data("mike",6)
        self.__data("joy",55)
        self.__data("david",12)
        self.__data("david",4)


    def  countname(self):
        import collections
        k = self.allist
        counter = collections.Counter(k)       #how many times the donar name in the donation list
        uniname = set(self.allist)
        for i in uniname:
            self.uniquename.append(i)          #this is unique names of the donar

        for i in self.uniquename:        #this will find the sum of the donation amount and number of times donated
            sum = 0
            times = 0
            for j in self.list:
                 if(i == j[0]):
                    sum = sum+j[1]
                    times = times+j[2]
                    c =(j[0],sum,times)
                    if(counter[i] == times):
                      self.listsum.append(c)

    def  report(self):
         print("+----------------------------+------------------+-------------------+-------------------+")
         print("|     Donar Name             |  Total given     | Number of gifts   |    Average gift   |")
         print("+----------------------------+------------------+-------------------+--------------------")

         for i in self.listsum:
             name = i[0].upper()
             total = '$' + str(i[1])
             avg = i[2]
             k  = int(i[1]/i[2])
             avggift = '$' + str(k)
             print("{: >20} {: >20} {: >20} {: >20}".format(name, total, avg,avggift))

    def  sendmail(self,listm):
        listd = listm
        for i in listd:
            a = i[0].upper()
            b = '$' + str(i[1])
            file = open("{}"".txt".format(a), 'a+')
            file.write("  Dear  ""{}".format(a))
            file.write("\n")
            file.write(" \n")
            file.write("    Thank you for your very kind donation of ")
            file.write("{}".format(b))
            file.write("\n")
            file.write("\n")
            file.write("    It will be used for very good cause.")
            file.write("\n")
            file.write("           Sincerely, \n")
            file.write("          -The Team  ")
            file.close

class donarreport(donar):

    def menu(self):
        print("Menu:")
        print("1.Send thank you mail")
        print("2.Create report")
        print("3.Add donars")
        print("4.Projection report")
        print("5.quit")
        i = int(input("enter your choice 1/2/3/4/5 >:       "))
        if (i == 2):
            s = donar()
            s.donarname()
            s.countname()
            s.report()
        elif (i == 1):
            s = donar()
            s.donarname()
            s.countname()
            l = s.listsum
            s.sendmail(l)
            print("The Thank you mail has been send to the list of donars")
            for i in l:
                print(i[0].upper())


        elif (i == 3):
            self.add_donar()
            s = donar()
            s.donarname()
            s.countname()
            s.report()

        elif (i == 4):
            self.projectdata()

    def add_donar(self):
        n = input("enter name   ")
        m = int(input("enter amount to donate   "))
        c = (n, m, 1)
        d = (n)
        s = donar()
        s.listadd.append(c)
        s.list.append(c)
        s.allist.append(d)
        print("do you want to add any donars  ")
        k = input("enter y/n  ")
        if (k == 'y' or k == 'Y'):
            self.add_donar()
        elif (k == 'n' or k == 'N'):
            s.sendmail(s.listadd)

    def projectdata(self):
        s = donar()
        s.donarname()
        s.countname()
        self.listfilter(s.listsum)
        print("+----------------------------+------------------+-------------------+-------------------+")
        print("|     Donar Name             |  Total given     | Projected value   |  Number of times  |")
        print("+----------------------------+------------------+-------------------+--------------------")
        for i in self.finalsum:
            name = i[0].upper()
            total = '$' + str(i[1])
            Projected = '$'+str(i[2])
            times = i[3]
            print("{: >20} {: >20} {: >20} {: >20}".format(name, total, Projected, times))


    def  listfilter(self,listf):
        s = listf
        x1 = list(filter(lambda x:x[1]>50,s))
        for i in x1:
             x = i[0]
             x1 =i[1]
             x2 = int(x1)*2
             c =(x,x1,x2,"double")
             self.finalsum.append(c)

        x2 = list(filter(lambda x:x[1]<50 and x[1]>10 ,s))
        for i in x2:
            x = i[0]
            x1 = i[1]
            x2 = int(x1) *3
            c = (x, x1, x2, "triple")
            self.finalsum.append(c)








e = donarreport()
e.menu()
