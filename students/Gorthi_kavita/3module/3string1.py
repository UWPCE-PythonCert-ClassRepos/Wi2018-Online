# print number formatting

def nformat(x):
    l1 = x
    n1 = l1[0]
    n2 = l1[1]
    n3 = l1[2]
    n4 = l1[3]

    s = str(n1)
    x1 = "file_00" + s
    num1 = n2
    x2 = '{:0.2f}'.format(num1)
    num2 = n3
    x3 = "%.2e" % num2
    num = n4
    x4 = "%.2e" % num
    b = (x1, x2, x3, x4)
    return b


num = (2, 123.4567, 10000, 12345.67)
print(num)
a = nformat(num)
print(a)
