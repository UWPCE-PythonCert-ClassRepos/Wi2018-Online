#This script is for slicing exercise

def first_last_exchange(a):
    actual_string = a
    if (isinstance(actual_string, str) and (len(a) > 1)):
        print("This is the original string: {} \n".format(actual_string))
        print("This is the first {} and last {} elements to be swapped".format(actual_string[0], actual_string[(len(actual_string))-1]))
        swap_string = actual_string[(len(actual_string))-1] + actual_string[1:-1] + actual_string[0]
        print("This is the swapped String: {}".format(swap_string))
        return swap_string
    elif (isinstance(a, list) and (len(a) > 1)):
        print("This is the original list: {}".format(a))
        swap_list = a
        swap_list[0] , swap_list[-1] = swap_list[-1] , swap_list[0]
        print("This is the swapped list: {}".format(swap_list))
        return swap_list
    else:
        return a

def every_other_item(a):
    actual_string = a
    if (isinstance(actual_string, str) and (len(a) > 1)):
        every_other_string = a[::2]
        print("This is the original string {} \n".format(actual_string))
        print("This is every other item {}".format(every_other_string))
        return every_other_string
    elif (isinstance(a, list) and (len(a) > 1)):
        swap_list = a[::2]
        print("This is the every other item list: {}".format(swap_list))
        return swap_list
    else:
        return a

def first_4_last_4_every_other(a):
    actual_string = a
    actual_string = a[4::]
    actual_string = actual_string[0:-4]
    b = every_other_item(actual_string)
    return b

def rev_string(a):
    actual_string = a[::-1]
    print("The reversed string is: {}".format(actual_string))
    return actual_string

def third_string(a):
    """ Logic is: Take middle third of the sequence,
    then take the last third of the sequence
    and put it in a new sequence in that order.
    Now get first third in the new sequence"""
    t = int(len(a)/3)
    third_string = a[t:(2*t)] + a[(2*t):]
    print third_string
    t1 = int(len(third_string)/3)
    final_string = third_string[:t1]
    print("Final string is: {}".format(final_string))
    return final_string

#Check first last exchange
assert first_last_exchange("This is go") == "ohis is gT"
assert first_last_exchange([-1, 2, 3, 4]) == [4, 2, 3, -1]
assert first_last_exchange([]) == []
assert first_last_exchange("") == ""

#Check if every other item missing
assert every_other_item("This is go time") == "Ti sg ie"
assert every_other_item([1, 2, 3, 4]) == [1, 3]
assert every_other_item([]) == []
assert every_other_item("") == ""

#Check if first and last 4 items are removed. And every other item in between
assert first_4_last_4_every_other("abcdefghijk") == "eg"
assert first_4_last_4_every_other([12, 13, 14, 15, 16, 18, 17, 18, 19, 20]) == [16]
assert first_4_last_4_every_other("") == ""
assert first_4_last_4_every_other([]) == []

#Check reverse string
assert rev_string("abcdefg") == "gfedcba"
assert rev_string([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert rev_string("") == ""
assert rev_string([]) == []

#Check third string problem
assert third_string("abcdefghi") == "de"
