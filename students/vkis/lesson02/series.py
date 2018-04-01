# n'th number of Fibonacci Series 0, 1, 1, 2, 3, 5, 8, 13, ... 
#f(n) = f(n-2) + f(n-1) where the first 2 are 0, 1

print()
print("--> Call the n'th number of fibonacci series via function: fibonacci(int)")

fib = 0, 1
def fibonacci(n):
	return custom(n)

print()
print("--> Call the n'th number of lucas number via function: lucas(int)")

def lucas(n):
	return custom(n,2,1)

print()
print("--> Call the n'th number of a custom sum series via function:")
print("--> custom(req:nth number, optional (def 0): 1st, optional (def 1): 2nd number")
print()


def custom(n,first=0,second=1):
	for index in range(1,n+1):				# n'th number in list
		if index == 1:						# calling for 1st in list
			back2 = first
			out = first
		if index == 2:						# calling for 2nd in list
			back1 = second
			out = second
		if index > 2:						# calling for n'th in list
			out = back2 + back1				# f(n) = f(n-2) + f(n-1)
			back2 = back1					# next iteration new2 = old1 (old2 gets dumped)
			back1 = out						# next iteration new1 = f(n) (old1 is now new2)
	return out

if __name__ == "__main__":
	assert fibonacci(1) == 0					# 0, 1, 1, 2, 3, 5, 8
	assert fibonacci(2) == 1					# 0, 1, 1, 2, 3, 5, 8
	assert fibonacci(3) == 1					# 0, 1, 1, 2, 3, 5, 8
	assert fibonacci(7) == 8					# 0, 1, 1, 2, 3, 5, 8
	
	assert lucas(1) == 2						# 2, 1, 3, 4, 7, 11, 18
	assert lucas(2) == 1						# 2, 1, 3, 4, 7, 11, 18
	assert lucas(3) == 3						# 2, 1, 3, 4, 7, 11, 18
	assert lucas(7) == 18					# 2, 1, 3, 4, 7, 11, 18
	
	assert custom(7,2,1) == 18				# custom 7th term def as lucas = lucas 7th term
	
	