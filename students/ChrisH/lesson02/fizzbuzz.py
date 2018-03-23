# -----------------------------------------------------------
# fizzbuzz.py
#  Print Fizz for multiples of 3, or Buzz for multiples of 5,
#  Print FizzBuzz, instead, for multiples of both 3 & 5
# -----------------------------------------------------------


def fizzbuzz(num):
    """
    Determines string to return based on the FizzBuzz rules:
        return FizzBuzz if a multiple of both 3 & 5
        return Fizz if only a multiple of 3
        return Buzz if only a multiple of 5
        return the number if none of the rules apply
    :param num: integer number to test
    :return: string if multiple, the original number otherwise
    """
    result = ""
    if num % 3 == 0:
        result += 'Fizz'
    if num % 5 == 0:
        result += 'Buzz'
    if result == "":
        return num
    return result


def main():
    """
    Print results of fizzbuzz function.
    :return: None
    """
    for num in range(1, 101):
        print(fizzbuzz(num))


if __name__ == "__main__":
    main()
