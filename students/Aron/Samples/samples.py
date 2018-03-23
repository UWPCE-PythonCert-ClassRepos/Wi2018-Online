
#The parameter weekday is True if it is a weekday, and the parameter vacation
#is True if we are on vacation. We sleep in if it is not a weekday or we're on
#vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  if vacation == True or weekday == False:
    return True
  elif weekday == True:
    return False

#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
#if each is smiling. We are in trouble if they are both smiling or if neither
#of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False


#Given two int values, return their sum. Unless the two values are the same,
#then return double their sum.
def sum_double(a, b):
  if (a==b):
    return (a+b) *2
  else:
    return a+b

#Given an int n, return the absolute difference between n and 21, except
#return double the absolute difference if n is over 21.

def diff21(n):
  if n>21:
    return (n-21) * 2
  else:
    return 21-n

#We have a loud talking parrot. The "hour" parameter is the current hour time
#in the range 0..23. We are in trouble if the parrot is talking and the hour is
#before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  return (talking and (hour>20 or hour<7))

#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
#computes the absolute value of a number.

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


def front_back(str):
  if len(str)<2:
    return str
  mid = str[1:len(str)-1]
  return str[len(str)-1] + mid + str[0]

  def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result

  def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

  def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

  def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

  def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[len(str)-2:]
  count = 0

  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1
  return count

  def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count = count + 1
  return count

  def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

  def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0

  for i in range(shorter -1):
    a_sub=a[i:i+2]
    b_sub=b[i:i+2]
    if a_sub==b_sub:
      count = count + 1

  return count
