def fizzBuzz(num):
    # First test the condition for multiples of 30
    # Doing this helps avoid multiples of 30 being picked off
    # by 3 or 5 first
    if (num % 15 == 0):
        return "FizzBuzz: Multiple of 3 & 5"
    elif (num % 5 == 0):
        return "Buzz: Multiple of 5"
    elif (num % 3 == 0):
        return "Fizz: Multiple of 3"
    else:
        return num

def main():
    for i in range(1, 101):
        print("{}: {}".format(str(i),fizzBuzz(i)))
        

if __name__ == "__main__":
    main()