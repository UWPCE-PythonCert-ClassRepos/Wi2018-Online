print("PydPiper Product Loaded")
############################################
i = 0
ii = 0
all_errors = False
while all_errors == False:
	try:
		a = name_error()
		if i != 1:
			b = a + 5
#		if ii != 1:
#			print 'this is a syntax error'
		a.attribute_error()
	except NameError:
		print("---> NAME ERROR: function name_error() is undefined")
		def name_error():
			print("function name_error works")
			return
		print("function: name_error() is now defined.")
	except TypeError:
		print("---> TYPE ERROR: can't add a function + integer, what are you thinking?")
		i = 1
	except SyntaxError:
		print("---> SYNTAX ERROR: try google-ing how to print properly in python...")
		ii = 1	
	except AttributeError:
		print("---> ATTRIBUTE ERROR: variable attribute .attribute_error is undefined")
		def attribute_error():
			print("attribute .attribute_error works")
		print("attribute: .attribute_error is now defined.")
		all_errors = True

