#/usr/bin/env python3

"""
Program to generate new text given an input text. It uses a dictionary to
build  trigrams of current text.
__author__ == 'Padmaja Peri'
"""

import random


def build_trigram_dict(fd):
    """ Method to build dictionary of trigrams from a text file """
    words_dict = {}
    text = fd.read().split()
    idx = 0
    # Stop looping when we have only two words left
    while idx < len(text) - 2:
        first_word = text[idx]
        second_word = text[idx + 1]
        third_word = text[idx + 2]
        dict_key = first_word + ' ' + second_word
        if dict_key in words_dict:
            words_dict[dict_key] += [third_word]
        else:
            words_dict[dict_key] = [third_word]
        idx += 1
    return words_dict


def generate_new_text(words_dict):
    """
    Method to generate text based on a trigrams dictionary. The Algorithm
    picks a random key from the dict. It looks up the value for the key. For
    the next iteration we use the last word from the key and the value and form
    a new word. We repeat this process till we dont find a key in the dict.
    :param words_dict:
    :return: Text String
    """
    # Get a random key from dict to start
    next_words = random.choice(list(words_dict.keys()))
    # Variable that holds the text accumulated
    text_so_far = next_words

    # Keep repeating the algorithm as long as we find a key in the dict
    while next_words in words_dict:
        value_in_dict = random.choice(words_dict[next_words])
        text_so_far = text_so_far + ' ' + value_in_dict
        # New key is concat of last word from current key and the value
        next_words = next_words.split()[-1] + ' ' + value_in_dict
    return text_so_far


if __name__ == '__main__':
    with open('sherlock.txt', 'r') as fd:
        trigram_dict = build_trigram_dict(fd)
    print(generate_new_text(trigram_dict))
