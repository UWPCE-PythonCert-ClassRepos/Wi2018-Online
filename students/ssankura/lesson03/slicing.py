"""
	LESSON03 - SLICING ASSIGNMENT
"""
"""
	exchange_first_last method
	Input: is a sequence - tuple , string etc.
	Ouput: returns a sequence with the first and last item(character) exchanged
"""
def exchange_first_last(seq):
	return seq[-1:] + seq[1:len(seq)-1] + seq[0:1]

"""
	remove_alternate_item method
	Input: is a sequence - tuple , string etc.
	Output: 
		returns a sequence with the first, third, fifth elements and so on - 
		removing the 2nd, 4th, etc. elements
"""
def remove_alternate_item(seq):
	return seq[0:len(seq):2]

"""
	remove_first_last_four method
	Input: sequence - tuple , string etc.
	Output: 
		returns an empty string if the length of the input is less than or equal to 8
		Else returns a sequence by removing the first four and last four elements
"""
def remove_first_last_four(seq):
	if len(seq) <=8: 
		return ""
	return seq[4:-4]

"""
	reverse_elements method
	Input: sequence - tuple , string etc.
	Output: 
		returns the elements in the reverse order
"""
def reverse_elements(seq):
	return seq[-1::-1]

"""
	print_thirds_difforder method
	Input: sequence - tuple , string etc.
	Output: 
		splits the input into 3 equal parts if the length of the input is divisible by 3
		if the length of input is not divisible by 3, the last part will contain the extra elements
		returns a new sequence with the midddle part and then the last part and then the first part
"""	
def print_thirds_difforder(seq):
	l = len(seq)
	i = l//3
	return seq[i:2*i] + seq[2*i:] + seq[:i]


"""
	main() method - invoked by if  __name__ == "__main__" to perform tests on the methods
"""
def main():

	print("Running tests for exchange_first_last")
	input = "abcd"
	assert(exchange_first_last(input) == "dbca")

	input = (1,2,3,4,5)
	assert(exchange_first_last(input) == (5,2,3,4,1))


	input = "this is a string for testing"
	assert(exchange_first_last(input) == "ghis is a string for testint")


	input = (1,"for testing","this","is",2,3,"some tuple")
	assert(exchange_first_last(input) == ("some tuple","for testing","this","is",2,3,1))

	print ("Ran tests for exchange_first_last - SUCCESS")


	print("Running tests for remove_alternate_item")

	input = "abcd"
	assert(remove_alternate_item(input) == "ac")

	input = (1,2,3,4,5)
	assert(remove_alternate_item(input) == (1,3,5))

	input = "this is a string for testing"
	assert(remove_alternate_item(input) == ("ti sasrn o etn"))

	input = (1,"for testing","this","is",2,3,"some tuple")
	assert(remove_alternate_item(input) == (1,"this",2,"some tuple"))

	print("Ran tests for remove_alternate_item - SUCCESS")


	print("Running tests for remove_first_last_four")

	input = "abcd"
	assert(remove_first_last_four(input) == "")

	input = (1,2,3,4,5)
	assert(remove_first_last_four(input) == "")

	input = "this is a string for testing"
	assert(remove_first_last_four(input) == " is a string for tes" )

	input = (1,"for testing","this","is",2,3,"some tuple")
	assert(remove_first_last_four(input) == "")

	input = (2, 54, 13, 12, 5, 32,345,123,1256,891,1231,901,66)
	assert(remove_first_last_four(input) == (5, 32, 345, 123, 1256))

	print("Ran tests for remove_first_last_four - SUCCESS")

	print("Running tests for reverse_elements")

	input = "abcd"
	assert(reverse_elements(input) == "dcba")

	input = (1,2,3,4,5)
	assert(reverse_elements(input) == (5,4,3,2,1))

	input = "this is a string for testing"
	assert(reverse_elements(input) == "gnitset rof gnirts a si siht" )

	input = (1,"for testing","this","is",2,3,"some tuple")
	assert(reverse_elements(input) == ('some tuple', 3, 2, 'is', 'this', 'for testing', 1))

	input = (2, 54, 13, 12, 5, 32,345,123,1256,891,1231,901,66)
	assert(reverse_elements(input) == (66, 901, 1231, 891, 1256, 123, 345, 32, 5, 12, 13, 54, 2))

	print("Ran tests for reverse_elements - SUCCESS")


	print("Running tests for print_thirds_difforder")

	input = "abcdefghi"
	assert(print_thirds_difforder(input) == "defghiabc")

	input = "ab"
	assert(print_thirds_difforder(input) == "ab")

	input = "abc"
	assert(print_thirds_difforder(input) == "bca")

	input = ""
	assert(print_thirds_difforder(input) == "")

	input = (1,2,3,4,5,6,7,8,9,10,11,12)
	assert(print_thirds_difforder(input) == (5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4))

	input = (1,2,3,4,5,6,7,8,9,10,11)
	assert(print_thirds_difforder(input) == (4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3))

	input = "this is a string for testing"
	#print ("Input = {0} Output = {1}".format(input, print_thirds_difforder(input)))
	assert(print_thirds_difforder(input) == " string for testingthis is a" )

	input = ('this1', 'test2', 'this3', 'test4', 'this5', 'test6', 'this7', 'test8', 'test9', 'this10')
	assert(print_thirds_difforder(input) == ('test4', 'this5', 'test6', 'this7', 'test8', 'test9', 'this10', 'this1', 'test2', 'this3'))

	input = (2, 54, 13, 12, 5, 32,345,123,1256,891,1231,901,66,18,20,67)
	assert(print_thirds_difforder(input) == (32, 345, 123, 1256, 891, 1231, 901, 66, 18, 20, 67, 2, 54, 13, 12, 5))

	input = (1,"TWO",3,"FOUR",5,6,"SEVEN")
	assert(print_thirds_difforder(input) == (3, 'FOUR', 5, 6, 'SEVEN', 1, 'TWO'))

	print("Ran tests for reverse_elements - SUCCESS")

"""
	__main__ method which invokes main() method to run the tests
"""
if __name__ == "__main__":
	main()
