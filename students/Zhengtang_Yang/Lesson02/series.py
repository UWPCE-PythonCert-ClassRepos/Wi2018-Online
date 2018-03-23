def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print('fib(8)') # test case
print(fib(8)) # test case

def lucus(n):
	if n == 1:
		return 2
	elif n == 2:
		return 1
	else:
		return lucus(n-1) + lucus(n-2)

print('lucus(8)') # test case
print(lucus(8)) # test case

def sum_series(n, m=0, u=1):
	if n == 1:
		return m
	elif n == 2:
		return u
	else:
		return sum_series(n-1, m, u) + sum_series(n-2, m, u)

print('sum_series(8)') # test case 
print(sum_series(8)) # test case
print('sum_series(8,2,1)') # test case
print(sum_series(8,2,1)) # test case