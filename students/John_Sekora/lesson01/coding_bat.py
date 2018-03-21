# http://codingbat.com/prob/p173401
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# BASICALLY, sleep_in when it is not a weekday, sleep in when we are on vacation

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

def sleep_in_2(weekday, vacation):
    return(not weekday or vacation)

print("Warmup-1 > sleep_in")
print(sleep_in(False,True))
print(sleep_in_2(False,True))
print(" ")


# http://codingbat.com/prob/p120546
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def  monkey_trouble (a_smile ,  b_smile) :
    if a_smile and b_smile:
        return(True)
    if not a_smile and not b_smile:
        return(True)
    else:
        return(False)

def monkey_trouble_2(a_smile, b_smile):
    return((a_smile and b_smile) or (not a_smile and not b_smile))

def monkey_trouble_3(a_smile, b_smile):
    return(a_smile == b_smile)

print("Warmup-1 > monkey_trouble")
print(monkey_trouble(True,False))
print(monkey_trouble_2(True,False))
print(monkey_trouble_3(True,False))
print(" ")


# http://codingbat.com/prob/p141905
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a == b:
        return 2*(a+b)
    else:
        return a+b

print("Warmup-1 > sum_double")
print(sum_double(3, 7))


# http://codingbat.com/prob/p197466
# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

print("Warmup-1 > diff21")
print(diff21(30))
print(" ")


# http://codingbat.com/prob/p166884
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False

def parrot_trouble_2(talking, hour):
    return talking and (hour < 7 or hour > 20)

print("Warmup-1 > parrot_trouble")
print(parrot_trouble(True, 3))
print(parrot_trouble_2(True, 9))
print(" ")


# http://codingbat.com/prob/p124984
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    if a + b == 10:
        return True
    else:
        return False

def makes10_2(a, b):
  return (a == 10 or b == 10 or a+b == 10)

print("Warmup-1 > makes10")
print(makes10(7,3))
print(makes10_2(2,7))
print(" ")


# http://codingbat.com/prob/p124676
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    if (abs(100 - n) <= 10) or (abs(200 - n) <= 10):
        return True
    else:
        return False

def near_hundred_2(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

print("Warmup-1 > near_hundred")
print(near_hundred(101))
print(near_hundred(50))
print(" ")


# http://codingbat.com/prob/p162058
# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
    if negative:
        return (a < 0) and (b < 0)
    else:
        return ((a < 0) and (b > 0)) or ((a > 0) and (b < 0))

print("Warmup-1 > pos_neg")
print(pos_neg(101, 1, True))
print(" ")


# http://codingbat.com/prob/p189441
# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    if len(str) >= 3 and str[:3] == "not": # str[:3] goes from the start of the string up to but not including index 3
        return str
    return "not " + str

print("Warmup-1 > not_string")
print(not_string("cat"))
print(" ")


# http://codingbat.com/prob/p149524
# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
    front = str[:n]       # up to but not including n
    back = str[n + 1:]    # n+1 through end of string
    return front + back

print("Warmup-1 > missing_char")
print(missing_char("hamster", 5))
print(" ")


# http://codingbat.com/prob/p153599
# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str) - 1]                  # can be written as str[1:-1]
    return str[len(str) - 1] + mid + str[0]    # last + mid + first


print("Warmup-1 > front_back")
print(front_back("zippi"))
print(" ")


# http://codingbat.com/prob/p147920
# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.

def front3(str):

    if len(str) < 3:
        return str + str + str
    else:
        return str[:3] + str[:3] + str[:3]

print("Warmup-1 > front3")
print(front3("Vechain"))
print(" ")


# http://codingbat.com/prob/p193507
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
    result = ""
    for i in range(n):           # range(n) is [0, 1, 2, .... n-1]
        result = result + str    # could use += here
    return result

print("Warmup-2 > string_times")
print(string_times("Loop", 3))
print(" ")


# http://codingbat.com/prob/p165097
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
    result = ""
    for i in range(n):
        result = result + str[:3]
    return result

print("Warmup-2 > front_times")
print(front_times("Loop", 3))
print(" ")


# http://codingbat.com/prob/p113152
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    result = ""                          # Many ways to do this. This uses the standard loop of i on every char,
    for i in range(len(str)):            # and inside the loop skips the odd index values.
        if i % 2 == 0:
            result = result + str[i]
    return result

print("Warmup-2 > string_bits")
print(string_bits("Mississippi"))
print(" ")


# http://codingbat.com/prob/p118366
# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    result = ""
    for i in range(len(str)):            # On each iteration, add the substring of the chars 0..i
        result = result + str[:i + 1]
    return result

print("Warmup-2 > string_splosion")
print(string_splosion("Code"))
print(" ")


# http://codingbat.com/prob/p145834
# Given a string, return the count of the number of times that a substring length 2 appears in the string and
# also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    if len(str) < 2:                    # Screen out too-short string case.
        return 0
    last2 = str[len(str) - 2:]          # last 2 chars, can be written as str[-2:]
    count = 0
    for i in range(len(str) - 2):       # Check each substring length 2 starting at i
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1
    return count

print("Warmup-2 > last2")
print(last2("hixxhi"))
print(" ")


# http://codingbat.com/prob/p166170
# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
    count = 0
    for num in nums:               # Standard loop to look at each value
        if num == 9:
            count = count + 1
    return count

print("Warmup-2 > array_count9")
print(array_count9([1, 2, 9]))
print(" ")


# http://codingbat.com/prob/p110166
# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.

def array_front9(nums):
    end = len(nums)          # First figure the end for the loop
    if end > 4:
        end = 4
    for i in range(end):     # loop over index [0, 1, 2, 3]
        if nums[i] == 9:
            return True
    return False

print("Warmup-2 > array_front9")
print(array_front9([1, 2, 3, 9, 5]))
print(" ")


# http://codingbat.com/prob/p193604
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
    for i in range(len(nums) - 2):           # Note: iterate with length-2, so can use i+1 and i+2 in the loop
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

print("Warmup-2 > array123")
print(array123([1, 2, 3, 9, 5]))
print(" ")



# http://codingbat.com/prob/p182414
# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings
# appear in the same place in both strings.

def string_match(a, b):
    shorter = min(len(a), len(b))        # Figure which string is shorter.
    count = 0
    for i in range(shorter - 1):    # Loop i over every substring starting spot....
        a_sub = a[i:i + 2]          # ... length-1 here, so can use char str[i+1] in the loop
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            count = count + 1
    return count

print("Warmup-2 > array123")
print(string_match("xxcaazz", "xxbaaz"))
print(" ")