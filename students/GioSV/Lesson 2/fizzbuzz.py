for i in range(1,101):
    fizz=0
    buzz=0
    if i%3==0 and i%5==0:
        i="fizzbuzz"
    elif i%3==0:
        i="fizz"
    elif i%5==0:
        i="buzz"
    print(i)