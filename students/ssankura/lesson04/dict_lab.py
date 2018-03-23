
dict = {'name':'Chris','city':'Seattle','cake':'Chocolate'}


def task1_dict():
	print ("Created Dictionary: {}".format(dict))
	del dict['cake']
	print("Dictionary items after removing item - cake: {}".format(dict))

	dict['fruit']='Mango'
	print("Dictionary after adding the fruit Mango {}". format(dict))

	print ("Dictionary Keys: {}".format(dict.keys()))
	print ("Dictionary Values: {}".format(dict.values()))

	print("Is cake in Dictionary keys: {}".format("cake" in dict.keys()))

	print ("Is Mango is Dictionary Values: {}".format ("Mango" in dict.values()))

def task2_dict():
	dict2 = {}
	for key,value in dict.items():
		dict2[key] = value.count('t') + value.count('T')
	print ("Dictionary with the same keys as in the previous Dictionary with value as the count of t's is {}".format(dict2))


def task3_sets():
	set1 = set([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
	s2 = set([])
	s3 = set([])
	s4 = set([])
	for item in set1:
		if (item % 2 == 0):
			s2.add(item)
		if (item % 3 == 0):
			s3.add(item)
		if (item % 4 == 0):
			s4.add(item)
	print ("s2 : {}".format(s2))
	print ("s3 : {}".format(s3))
	print ("s4 : {}".format(s4))
	print ("Is s3 is a subset of s2: {}".format(s3 < s2))
	print ("Is s4 is a subset of s2: {}".format(s4 < s2))
 	

def task4_sets():
	set1 = set(['P','y','t','h','o','n'])
	print ("Set1 original values : {}".format(set1))
	set1.add('i')
	print ("Set1 values after adding 'i' : {}".format(set1))
	
	set2 = frozenset(['m','a','r','a','t','h','o','n'])
	print ("Set2 values : {}".format(set2))

	setunion = set1 | set2
	setintersect = set1 & set2

	print ("Union of Set1 and Set2 : {}".format(setunion))
	print("Intersection of Set1 and Set2 : {}".format(setintersect))

if __name__ == "__main__":
	task1_dict()
	task2_dict()
	task3_sets()
	task4_sets()