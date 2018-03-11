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
		
"""testing return_every_other function"""
if __name__ == "__main__":
	list = [0,1,2,3,4,5,16,17,8,9,10,12]
	string = "the string test is good"
	assert return_every_other(list) == [4,16]
	assert return_every_other(string) == 'srn eti '
	print("The return_every_other function test has competed successfully")
"""


def reverse_slice(seq):



def seq_shell_game(seq):







	