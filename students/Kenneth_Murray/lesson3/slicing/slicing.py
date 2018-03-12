def exchange_first_last(seq):
	"""returns a sequence with the first and last characters swapped"""
	first = seq[0]
	mid = seq[1:-1]
	last = seq[-1]
	
	if type(seq) == str:
		return last + mid + first
	else:
		eos=len(seq)
		mid.insert(0,last)
		mid.insert(eos,first)
		return mid
		
"""testing the exchange function"""
if __name__ == "__main__":
	string = "the string test is good"
	list = [1,2,3,4,5,6,7]
	assert exchange_first_last(list) == [7,2,3,4,5,6,1]
	assert exchange_first_last(string) == "dhe string test is goot"
	print ("the exchange test is complete")
		
			
def return_every_other(seq, i=2):
	"""returns every other character in a sequence"""
	return seq[::2]
	
"""testing "return_every_other" function"""
if __name__ == "__main__":
	list = [1,2,3,4,5,6,7]
	assert return_every_other(list) == [1, 3, 5, 7]
	print("The return_every_other function test has competed successfully")
	

def remove_some_with_step(seq, r=4, i=2):
	"""This will remove the first and last four characters along with every other character."""
	"""A minimum of 10 characters are required."""
	eos = len(seq)
	if len(seq) > 9:
		mid = seq[4:-4]
		return mid[::2]
	else:
		print("this requires a minimum of 10 characters")
		
"""testing remove_some_with_step"""
if __name__ == "__main__":
	list = [0,1,2,3,4,5,16,17,8,9,10,12]
	string = "the string test is good"
	assert remove_some_with_step(list) == [4, 16]
	assert remove_some_with_step(string) == 'srn eti '
	print("The remove_some_with_step test has competed successfully")



def reverse_slice(seq):
	return seq[::-1]
	
"""testing reverse_slice"""
if __name__ == "__main__":
	list = [0,1,2,3,4,5,16,17,8,9,10,12]
	string = "the string test is good"
	assert reverse_slice(list) == [12, 10, 9, 8, 17, 16, 5, 4, 3, 2, 1, 0]
	assert reverse_slice(string) == 'doog si tset gnirts eht'
	print("The reverse_slice test has competed successfully")



def seq_shell_game(seq):
	"""this will return the middle third first, the last third second and the first third last."""
	"""if the number of characters is not divisible by 3, the first third will be short"""
	length = len(seq)
	i = round(len(seq) / 3)
	first = seq[:i]
	mid = seq[i:-i]
	last = seq[length-i:]
	return mid + last + first
	
"""testing seq_shell_game"""
if __name__ == "__main__":
	list = [0,1,2,3,4,5,16,17,8,9,10,12]
	string = "the string test is good"
	assert seq_shell_game(list) == [4, 5, 16, 17, 8, 9, 10, 12, 0, 1, 2, 3]
	assert seq_shell_game(string) == 'ng test is goodthe stri'
	print("The seq_shell_game test has competed successfully")
	






	