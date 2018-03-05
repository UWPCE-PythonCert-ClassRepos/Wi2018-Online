#dictionary containing “name”, “city”, and “cake” for “Chris” 
#from “Seattle” who likes “Chocolate”

d={}
d['Name']='Chris'
d['City']='Seattle'
d['Cake']='chocolate'

d

#Delete the entry for “cake”
d.pop('Cake')

#Display the dictionary keys
d.keys()

#Display whether or not “cake” is a key in the dictionary (i.e. False) (now)
'Cake' in d

#Display whether or not “Mango” is a value in the dictionary (i.e. True)
'Mango' in d.values()

#Using the dictionary from item 1: Make a dictionary using the same keys but
#with the number of ‘t’s in each value as the value
#(consider upper and lower case?)

d2={}
d2['Name']='Chris'.count('t')
d2['City']='Seattle'.count('t')
d2['Cake']='chocolate'.count('t')


#Create sets s2, s3 and s4 that contain numbers from zero through twenty,
#divisible by 2, 3 and 4.
#Display the sets.
#Display if s3 is a subset of s2 (False)
#and if s4 is a subset of s2 (True).

#set 1

def sets():
    s2 = set()
    s3 = set()
    s4 = set()

    for i in range(20):
        if i % 2 == 0:
            s2.add(i)
        if i % 3 == 0:
            s3.add(i)
        if i % 4 == 0:
            s4.add(i)

    print(s2, "\n", s3, "\n", s4, "\n")
    print('s3 is subset of s2: ', s3.issubset(s2))
    print('s4 is subset of s2: ', s4.issubset(s2))

#Sets 2

#Create a set with the letters in ‘Python’ and add ‘i’ to the set.
#Create a frozenset with the letters in ‘marathon’.
#display the union and intersection of the two sets.

s2_python =set()
for i in ('python'):
    s2_python.add(i)

fs=frozenset(('marathon'))

#Write a program which prints the full path for all files in the current
#directory, one per line

#Write a program which copies a file from a source, to a destination
#(without using shutil, or the OS copy command).
