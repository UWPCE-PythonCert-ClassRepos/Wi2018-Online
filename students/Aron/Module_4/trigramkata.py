#import a file
#clean up the file so we only have keywords

#f=open('sample.txt', 'r')
#print(f.read())
#content = f.readlines()

import string

def strip_chara(str):
    return''.join(char for char in str if char not in (string.punctuation + string.whitespace + string.digits))

def create_list(filename):
    result = []
    i=0
    with open(filename, 'r') as myfile:
        for line in myfile:
            for word in line.split():
                result.append(strip_chara(word))
    return result


from itertools import islice

triplets = zip(f.read(), islice(f.read(), 1, None), islice(f.read(), 2, None))

for triplet in triplets:
    print(triplet)
