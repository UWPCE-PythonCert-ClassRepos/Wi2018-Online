# Write some functions that take a sequence as an argument, and return a copy of that sequence:
#
#     with the first and last items exchanged.
#     with every other item removed.
#     with the first and last 4 items removed, and every other item in between.
#     with the elements reversed (just with slicing).
#     with the middle third, then last third, then the first third in the new order.


def exchange_first_last(seq):
    ''' Exchanges the First and Last Items '''
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence


def every_other(seq):
    ''' Removes Every Other Item '''
    a_new_sequence = seq[::2]
    return a_new_sequence


def first4_and_last4_removed_every_other(seq):
    ''' Removes the First and Last Four, and Every Other Item in Between '''
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence


def elements_reversed_with_slicing(seq):
    ''' Reverses the Elements with Slicing '''
    a_new_sequence = seq[::-1]
    return a_new_sequence


def middle_last_first(seq):
    ''' Separates the Data Into Thirds and Reorders it to: Middle, Last, First '''
    third = round(len(seq) / 3)
    first = seq[:third]
    mid = seq[third:-third]
    last = seq[-third:]
    a_new_sequence = mid + last + first
    return a_new_sequence


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
string = "this is my favorite string"


assert exchange_first_last(numbers) == (16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
assert exchange_first_last(string) == "ghis is my favorite strint"

assert every_other(numbers) == (0, 2, 4, 6, 8, 10, 12, 14, 16)
assert every_other(string) == "ti sm aoiesrn"

assert first4_and_last4_removed_every_other(numbers) == (4, 6, 8, 10, 12)
assert first4_and_last4_removed_every_other(string) == " sm aoies"

assert elements_reversed_with_slicing(numbers) == (16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
assert elements_reversed_with_slicing(string) == "gnirts etirovaf ym si siht"

assert middle_last_first(numbers) == (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 1, 2, 3, 4, 5)
assert middle_last_first(string) == "y favorite stringthis is m"


print("Original Sequences:")
print("Numbers")
print(numbers)
print("String")
print(string)

print(" " + '\n')

print("Exchanges the First and Last Items")
print(exchange_first_last(numbers))
print(exchange_first_last(string))
print(" ")

print("Removes Every Other Item")
print(every_other(numbers))
print(every_other(string))
print(" ")

print("Removes the First and Last Four, and Every Other Item in Between")
print(first4_and_last4_removed_every_other(numbers))
print(first4_and_last4_removed_every_other(string))
print(" ")

print("Reverses the Elements with Slicing")
print(elements_reversed_with_slicing(numbers))
print(elements_reversed_with_slicing(string))
print(" ")

print("Separates the Data Into Thirds and Reorders it to: Middle, Last, First")
print(middle_last_first(numbers))
print(middle_last_first(string))

