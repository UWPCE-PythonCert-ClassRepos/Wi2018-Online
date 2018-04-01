# example functions for slicing sequences

print()
print("Imported functions: first_is_last, rm_even, rm_0_last4_even, rev, wild_slice")
print()


def converter(original_type,data):
	if type(original_type) == tuple:
		return tuple(data)
	elif type(original_type) == str:
		return "".join(data)
	else:
		return data

def first_is_last(seq):
	mylist = list(seq)
	newlist = mylist[:]
	newlist[0] = mylist[-1]
	newlist[-1] = mylist[0]
	return converter(seq,newlist)

def rm_even(seq):
	mylist = list(seq)
	newlist = mylist[::2]
	return converter(seq,newlist)

def rm_0_last4_even(seq):
	mylist = list(seq)
	newlist = mylist[1:-4]
	newlist = newlist[::2]
	return converter(seq,newlist)

def rev(seq):
	mylist = list(seq)
	newlist = mylist[::-1]
	return converter(seq,newlist)


def wild_slice(seq):
	mylist = list(seq)
	int1_3 = int(1/3*len(mylist))
	int2_3 = int(2/3*len(mylist))
	newlist1_3 = mylist[:int1_3]
	newlist2_3 = mylist[int1_3:int2_3]
	newlist3_3 = mylist[int2_3:]
	newlist = newlist2_3 + newlist3_3 + newlist1_3
	return converter(seq,newlist)


# validations
		   #0123456789012345
a_string = "this is a string"
		  #0  1  2  3 4  5
a_tuple = (2,54,13,12,5,32)

assert first_is_last(a_string) == "ghis is a strint"
assert first_is_last(a_tuple) == (32,54,13,12,5,2)

assert rm_even(a_string) == "ti sasrn"
assert rm_even(a_tuple) == (2,13,5)

assert rm_0_last4_even(a_string) == "hsi  t"
assert rm_0_last4_even(a_tuple) == (54,)

assert rev(a_string) == "gnirts a si siht"
assert rev(a_tuple) == (32,5,12,13,54,2)

assert wild_slice(a_string) == "is a stringthis "
assert wild_slice(a_tuple) == (13,12,5,32,2,54)