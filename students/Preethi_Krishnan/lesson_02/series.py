def fibo_series(n):
    f = [0,1]
    n = int(n)
    if (n >= 2):
        for i in range(n-1):
            a = f[i] + f[i+1]
            f.append(a)
            #print a
        print ("Fibonacci value for {}th element is {}".format(n,f[n]))
        return f[n]
    
    elif ((n == 0) or (n ==1)):
        print ("Fibonacci value for {}th element is {}".format(n, f[n]))
        return f[n]

    else:
        m = abs(n)
        print ("n is a negative value {} \n Try to make it positive and the fibonacci value of {}".format(n, m))
        return fibo_series(m)

def lucas_series(n):
    l = [2, 1]
    n = int(n)
    if (n >= 2):
        for i in range(n - 1):
            a = l[i] + l[i + 1]
            l.append(a)
            # print a
        print ("Lucas series value for {}th element is {}".format(n, l[n]))
        return l[n]

    elif ((n == 0) or (n == 1)):
        print ("Lucas series value for {}th element is {}".format(n, l[n]))
        return l[n]

    else:
        m = abs(n)
        print ("n is a negative value {} \n Try to make it positive and the lucas series value of {}".format(n, m))
        return lucas_series(m)


if __name__ == '__main__':
    assert fibo_series(4) == 3
    assert fibo_series(5) == 5
    assert fibo_series(10) == 55
    assert fibo_series(-6) == 8
    assert fibo_series(7.0) == 13
    assert lucas_series(0.0) == 2
    assert lucas_series(-5) == 11
    assert lucas_series(6) == 18
    assert lucas_series(7) == 29
    
