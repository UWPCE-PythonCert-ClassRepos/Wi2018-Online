#!/usr/local/bin python3
import json
import re

TRIGRAM_DICT = {}

def add_to_trigram(word_list):
    """adds keys and values to TRIGRAM_DICT. Each value in the dictionary is a list"""
    end = len(word_list)
    for word in range(0,end):
        if word + 3 > end:
            break
        else:
            key = word_list[word]+' '+ word_list[word + 1]
            if (key in TRIGRAM_DICT):
                TRIGRAM_DICT[key].append(word_list[word+2])
            else:
                TRIGRAM_DICT[key] = []
                TRIGRAM_DICT[key].append(word_list[word + 2])

def read_line(line):
    """removes all non letter and number characters, split words and puts them into list"""
    line = re.sub('[^A-Za-z0-9]+', ' ', line)
    word_list = line.split()
    add_to_trigram(word_list)

def run():
    """ function which runs program. For each lines in file calls function read_line. Writes content of TRIGRAM_DICT
    to txt file using json.dump"""
    try:
        with open ('sherlock_small.txt', 'r') as file:
            for line in file:
                read_line(line)

        with open('trigram_results.txt', 'w') as file:
            file.write(json.dumps(TRIGRAM_DICT))

    except IOError as e:
        print('error number {}, error string {}\n'.format(e.errno,e))

def main():
    try:
        print("Welcome to Trigram Reader\n")
        run()
        print("Trigram Reader done\n")
    except Exception as e:
        print ('error with task running program\n {}'.format(e))

if __name__ == "__main__":
    main()