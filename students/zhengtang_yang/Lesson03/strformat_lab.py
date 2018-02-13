fnames = [2,123.4567,10000,12345.67]

print('Task One')
print('file_{:03}: {:5.2f} {:3.2e} {:3.2e}\n'.format(fnames[0],fnames[1],fnames[2],fnames[3]))

print('Task Two')
print(f"file_{fnames[0]:03}: {fnames[1]:5.2f} {fnames[2]:3.2e} {fnames[3]:3.2e}\n")

print('Task Three')
a = (2,3,5)
b = (2,3,5,7,9)
def formatter(nums):
	temp = f'the {len(nums)} numbers are:' + ' {:d}'
	for i in range(len(nums)-1):
		temp += ', {:d}'
	return print(temp.format(*nums))
formatter(a)
formatter(b)

print('\nTask Four')
print('(4,30,2017,2,27)')
c = (4,30,2017,2,27)
print(f'{c[3]:02} {c[4]} {c[2]} {c[0]:02} {c[1]}')

print('\nTask Five')
print('[\'oranges\', 1.3, \'lemons\', 1.1]')
temp = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {temp[0][:-1]} is {temp[1]} and the weight of a {temp[2][:-1]} is {temp[-1]}')
print(f'The weight of an {temp[0][:-1].upper()} is {1.2*temp[1]} and the weight of a {temp[2][:-1].upper()} is {1.2*temp[-1]}')

print('\nTask Six')
names = ('IronMan','BatMan','Hulk')
ages = ('29','30','31')
costs = (1,2,3)
row_format = '{:>15}'*3
print(row_format.format(*('Name','Age','Cost')))
for i in range(len(names)):
	print(row_format.format(names[i],ages[i],costs[i]))

temp = (1,2,3,4,5,6,7,8,9,10)
print(''.join('{:>5}'.format(item) for item in temp))