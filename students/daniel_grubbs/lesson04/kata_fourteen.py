#!/usr/bin/env python3

# Kata Fourteen Assignment
# Daniel Grubbs
import random

file_name = 'sherlock_small.txt'
contents = []
trigrams_dict = {}

# Grab the contents of the file and update the contents list
with open(file_name) as f:
    for line in f:
        contents += line.strip().split()


def main():
    print_header()
    trigrams(contents)
    random_lookup(random.choice(list(trigrams_dict)))


def print_header():
    """Print the header of the program."""
    print('------------------------------------')
    print('             Lesson04')
    print('     Kata Fourteen Assignment')
    print('------------------------------------\n')


def trigrams(content):
    """Take the contents from file and create the trigrams."""
    for item in range(len(content) - 2):
        two_words = tuple(contents[item: item + 2])
        # test to make sure that two items are in a tuple
        # print(two_words)
        next_word = [contents[item + 2]]
        # print(next_word)

        if two_words in trigrams_dict:
            trigrams_dict[two_words].append(next_word)
        else:
            trigrams_dict[two_words] = next_word

        # print(trigrams_dict)


def random_lookup(word_pair):
    """Build a new block of text from the trigram dictionary."""
    word_pair = tuple(word_pair)
    # print(word_pair)
    next_text = []
    text = ''

    while word_pair in trigrams_dict:
        next_text.append(random.choice(trigrams_dict[word_pair]))
        word_pair = (word_pair[-1], text[-1][-1])
    for item in range(len(next_text)):
        text += next_text[item][0]
    print(text)


if __name__ == '__main__':
    main()
