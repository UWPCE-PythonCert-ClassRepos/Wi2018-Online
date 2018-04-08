def print_grid2(o,p):
    #Where:
    #   o: number of rows and columns.
    #   p: number of elements between rows and columns.
    #This one is actually easier.    
    a="+"
    b="-"
    c="|"
    middle_line1=""
    middle_line2=""

    for k in range (o):
        middle_line1+=p*(b+" ") + a +" "
        middle_line2+=+ p*"  "+c+" "

    line_1=a +" "  + middle_line1
    line_2=c +" "  + middle_line2
    print (line_1)
    for j in range (o):
        for i in range(p):
            print (line_2)
        print (line_1)
