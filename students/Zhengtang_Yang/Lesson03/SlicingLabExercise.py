def exchange_first_last(seq):
	'''first and last items exchanged'''
	seq0 = list(seq)
	temp, seq0[0] = seq[0], seq[-1]
	seq0[-1] = temp
	if type(seq) == tuple:
		return tuple(seq0)
	elif type(seq) ==str:
		return ''.join(seq0) 

def everyother_removed(seq):
	''' every other item removed'''
	seq0 = seq[::2]
	return seq0

def remove4_everyother(seq):
	'''first and last 4 items removed, and every other item in between'''
	seq0 = seq[4:-4]
	seq0 = seq0[::2]
	return seq0

def reverse(seq):
	'''elements reveresed(just with slicing)'''
	seq0 = seq[::-1]
	return seq0

def midlastfirst_third(seq):
	'''middle third, then last third, then first third in the new order'''
	temp = seq[:len(seq)//3]
	seq0 = seq[len(seq)//3:]
	seq0 = seq0 + temp
	return seq0

a_string = "This is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strinT"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert everyother_removed(a_string) == "Ti sasrn"
assert everyother_removed(a_tuple) == (2, 13, 5)

aa_tuple = (1, 2, 3, 4, 2, 54, 13, 12, 5, 32, 4, 3, 2, 1)
assert remove4_everyother(a_string) == " sas"
assert remove4_everyother(aa_tuple) == (2, 13, 5)

assert reverse(a_string) == "gnirts a si sihT"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

aa_string = "abcdefghijklmnopqrstu"
assert midlastfirst_third(aa_string) == "hijklmnopqrstuabcdefg"
assert midlastfirst_third(a_tuple) == (13, 12, 5, 32, 2, 54)