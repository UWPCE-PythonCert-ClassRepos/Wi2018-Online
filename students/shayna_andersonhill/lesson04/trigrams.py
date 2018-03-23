#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#Shayna Anderson-Hill
#Trigrams
#03-20-2018
import random

def build_trigram(filepath):
    file = open(filepath)
    data = file.read()
    file.close()
    data = data.replace('\n', ' ').replace('\r',
        '').replace('--', ' ')
    word_list = data.split()
    trigram_list = []
    for n in range(len(word_list)):            
        try:
            trigram_list.append(list([word_list[n],
                word_list[n+1]]))
        except IndexError:
            pass

    tuple_list = []
    for i in trigram_list:
        tuple_list.append(tuple(i))

    trigram_dictionary = {}
    for n in range(len(tuple_list)-2): 
        try:
            if tuple_list[n] in trigram_dictionary:
                trigram_dictionary[tuple_list[n]].append(word_list[n+2])
            else:
                trigram_dictionary[tuple_list[n]] = [word_list[n+2]]
        except IndexError:
            pass

    key = random.choice(list(trigram_dictionary))
    trigram = [key[0], key[1], random.choice(trigram_dictionary[key])]
    for n in range(0,500):
        try:
            key = (trigram[n+1], trigram[n+2])
            trigram.append(random.choice(trigram_dictionary[key]))
        except IndexError:
            pass
    print(" ".join(trigram))


def main():
    build_trigram('sherlock.txt')

if __name__ == "__main__":
    main()
