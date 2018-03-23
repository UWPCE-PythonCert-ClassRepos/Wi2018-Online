#break_me by Sam Cooper

#Write four simple Python functions that cause exceptions

#Main Function calls each function; uncomment the function call if you want to see a particular error type. 
def main():
	#print('This program gives a whole bunch of errors')
	#NameError()
	#TypeError()
	#SyntaxError()
	#AttributeError()

#NameError function
def NameError():
	print(NonExistent)

#TypeError function
def TypeError():
	value1 = "ethereum"
	value2 = 100000
	print(value2 + value1)

#SyntaxError function
def SyntaxError: #invalid syntax
	error = 0
	if error == 0: 
		print(error)

#AttributeError function
def AttributeError():
	example_integer = 2
	example_integer.append(4) #the append attribute belongs to the list object type; you cannot append to an integer. This creates an attribution error. 

main()