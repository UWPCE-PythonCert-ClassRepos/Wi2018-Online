#!/usr/bin/env python

# set up test strings and test tuples
a_string = "this is a string"
a_longer_string = "I met a traveller from an antique land Who said: Two vast and trunkless legs of stone"
a_tuple = (2, 54, 13, 12, 5, 32)
a_longer_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)

# 1) Write a function that exchanges the first and last items in a sequence 
def exchange_first_and_last(seq):
	if type(seq) == str:
		print(seq[-1]+seq[1:]+seq[0])
	if type(seq) == tuple:
		new_seq = []
		for i in range(0, len(seq)):
			if i == 0:
				new_seq.append(seq[-1])
			elif i == len(new_seq) - 1:
				new_seq.append(seq[0])
			else:
				new_seq.append(seq[i])
		print(new_seq)
	
exchange_first_and_last(a_string)
exchange_first_and_last(a_longer_string)
exchange_first_and_last(a_tuple)
exchange_first_and_last(a_longer_tuple)


# 2) Write a function that removes every other item from the sequence
def omit_every_other(seq):
	if type(seq) == str:
		new_seq = ""
		for i in range(0, len(seq)):
			if i % 2 == 0:
				new_seq += seq[i]
		print(new_seq)
	if type(seq) == tuple:
		new_seq = []
		for i in range(0, len(seq)):
			if i % 2 == 0:
				new_seq.append(seq[i])
		print(new_seq)

omit_every_other(a_string)
omit_every_other(a_longer_string)
omit_every_other(a_tuple)
omit_every_other(a_longer_tuple)

# 3) Write a function that removes the first and last 4 elements of a sequence, 
# and returns every other element in between
def trim_four_either_side_return_every_other(seq):
	relevant_seq = seq[4:-4:2]
	print(relevant_seq)

trim_four_either_side_return_every_other(a_longer_string)
trim_four_either_side_return_every_other(a_longer_tuple)


# 4) Write a function that reverses the elements of the sequence with just slicing
def reverse_elements(seq):
	print(seq[::-1])

reverse_elements(a_string)
reverse_elements(a_longer_string)
reverse_elements(a_tuple)
reverse_elements(a_longer_tuple)

# 5) Write a function that orders list as the middle third, last third, and first third of the list 
def order_middle_last_first(seq):
	if(type(seq) == str):
		print(seq[round(len(seq)/3):2*round(len(seq)/3)] + seq[2*round(len(seq)/3):] + seq[:round(len(seq)/3)])
	if(type(seq) == tuple):
		new_seq = seq[round(len(seq)/3):2*round(len(seq)/3)] + seq[2*round(len(seq)/3):] + seq[:round(len(seq)/3)]
		print(new_seq)


order_middle_last_first(a_string)
order_middle_last_first(a_longer_string)
order_middle_last_first(a_tuple)
order_middle_last_first(a_longer_tuple)

