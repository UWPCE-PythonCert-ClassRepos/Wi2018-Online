import os

# four simple Python functions: when called, causes an exception
# NameError, TypeError, SyntaxError, AttributeError


# 1) NameError
def name_test():
	"""tests NameError"""
	try:
		print(foo*3)
	except NameError as e:
		print("Error encountered: ", e)


# 2) TypeError
def type_test():
	""" test TypeError """
	try:
		result = '4'/4
	except TypeError as e:
		print("Error encountered: ", e)


# 3) SyntaxError
def syntax_test():
	"""test SyntaxError """
	try:
		a = 2
		if (a==2)
			print ("a = 2")
	except SyntaxError as e:
		print("Error encountered: ", e)


# 4) AttributeError
def attribute_test():
	""" test AttributeError """
	try:
		"hello".Capital()
	except AttributeError as e:
		print("Error encountered: ", e)



# Test ---

#name_test()
#type_test()
#syntax_test()
#attribute_test()

