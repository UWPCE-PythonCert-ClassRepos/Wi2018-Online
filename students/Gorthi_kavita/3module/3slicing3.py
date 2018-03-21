# delete first and last four items and every other item in between for the numbers

def alter(x):
    l = len(x)
    p = list(x)
    print(p)
    p = p[0:l - 4]
    return p[4:l:2]


x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
k = alter(x)
print(k)
