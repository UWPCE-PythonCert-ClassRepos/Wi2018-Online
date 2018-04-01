# ============================= #
# fizbuzz.py
# prints Fizz for numbers multiples of 3
# prints Buzz for numbers multiples of 5
# prints FizzBuzz for numbers multiples of 3 & 5
# ============================== #

def fiz_buzz(num=100):
    """
    prints strings or numbers for numbers 1 to num inclusive based on fizzbuzz rules.
    prints Fizz if number is multiple of 3.
    prints Buzz if number is multiple of 5.
    prints FizzBuzz if number is multiple of 3 &5.
    If not the above conditions then prints the number.
    :param num: Takes number as an input
    :return: No return value
    """
    for i in range(1, num+1):
        if (i % 3 == 0) and (i % 5 == 0):
                print("FizzBuzz")
        elif i % 3 == 0:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fiz_buzz(100)