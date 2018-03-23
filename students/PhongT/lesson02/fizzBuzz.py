"""
Lesson 02
fizz buzz Exercise
"""


def print_fizzbuzz():
    """
    program that prints the numbers from 1 to 100 inclusive.
    But for multiples of three print "Fizz" instead of the number.
    For the multiples of five print "Buzz" instead of the number.
    For numbers which are multiples of both three and five print "FizzBuzz" instead
    """

    for x in range (1,100):
        if x%3 == 0 and x%5==0 :
            print('FizzBuzz')
        elif x%3 == 0:
            print('Fizz')
        elif x%5 == 0:
            print('Buzz')
        else:
            print(x)


if __name__ == "__main__":
    print_fizzbuzz()
