#lesson 1 create functions that return errors
#KTMurray

#wnter 1 for k to see my name. all other entries will result in a name error because of an undefined variable
def funNameError(k):
	if k == 1:
		name = "ken"
		return name
	else:
		name = k
		return mane
#five is a string. input a number for x to get a TypeError

def funTypeError(x):
	return five*x

#input a long number for i to recieve a SyntaxError in Python 3
def funSyntaxError(i):
	return iL

#input 4 to return a uuid4 value. any other number will produce an attribute error becault there is no .uuid0 attribute.
def funAttributeError(g):
	import uuid
	if g == 4:
		return uuid.uuid4()
	else:
		return uuid.uuid0()
		

