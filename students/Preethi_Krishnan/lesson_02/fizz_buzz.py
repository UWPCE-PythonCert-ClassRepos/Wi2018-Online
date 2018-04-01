def fizz_buzz(n):
    n = abs(n)
    for i in range(1, n+1):
        if ((i%3 == 0) and (i%5 ==0)):
            print("FizzBuzz")
        elif ((i%3 == 0)):
            print("Fizz")
        elif (i%5 == 0):
            print("Buzz")
        else:
            print ("{}".format(i))

if __name__ == "__main__":
    fizz_buzz(10)
    fizz_buzz(100)
    fizz_buzz(-3)
