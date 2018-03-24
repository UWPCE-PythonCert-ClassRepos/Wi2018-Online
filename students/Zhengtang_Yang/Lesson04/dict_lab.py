Dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(Dict1)

Dict1.pop('cake')
print(Dict1)

Dict1['fruit'] = 'Mango'
print(Dict1)

print(Dict1.keys())

print(Dict1.values())

print('cake' in Dict1.keys())

print('Mango' in Dict1.values())

Dict2 = {}
for item in Dict1.keys():
	Dict2[item] =  Dict1[item].count('t')
print(Dict2)

s2, s3, s4 = (set() for i in range(3))
for i in range(20):
	if i % 2 == 0:
		s2.add(i)
	if i % 3 == 0:
		s3.add(i)
	if i % 4 == 0:
		s4.add(i)
print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))