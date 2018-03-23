def febonnaci(x):
	a=0
	b=1
	if x==0:
		return a
	elif x==1:
		return b
	else:
		for i in range(2,x):
			c=a+b
			a=b
			b=c
		return b

print(febonnaci(9))