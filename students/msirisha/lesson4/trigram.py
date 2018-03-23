##### trigram.py #######
# Takes book as an input and generates a trigram based dict and generates trigram based text #
# from based on trigram dict. #

import random

trigram_word_dict = {}


def flatten_words_from_input_book(book):
    """ Takes input as book and coverts it into list of words """
    with open(book, "r") as f:
        words = [word for line in f for word in line.split()]
    print(words)
    return words


def convert_words_into_trigram_dict(words):
    """ Takes list of words as input and generates a trigram word key pair"""
    for index in range(0, len(words)):
        if index < len(words) - 2:
            key = words[index] + " " + words[index + 1]
            # if key does not exist then create a key and initialize value to list type.
            if not trigram_word_dict.get(key, None):
                value = [words[index + 2]]
                trigram_word_dict[key] = value
            else:
                trigram_word_dict[key].append(words[index + 2])
    print(trigram_word_dict)


def generate_trigram_dict(book):
    """ This method takes input as a book name and calls the trigram based
     methods to generate trigram word key pair """
    words = flatten_words_from_input_book(book)
    convert_words_into_trigram_dict(words)


def get_key_value_from_dict(keypair):
    """ Takes the keypair as input and selects choice of word from the list of words.
        return latest keypair by combining the last word of keypair and word.
        keypair --> word1
        return keypair[-] + word1
    """
    latestkeypair = None
    latestword = None

    if trigram_word_dict.get(keypair, None):
        latestword = random.choice(trigram_word_dict.get(keypair, None))
        latestkeypair = keypair.split()[-1] + " " + latestword
    return latestkeypair, latestword


def generate_trigram_book(words_count):
    """ Reads trigram word pair dict and selects a arbitrary random
    two word key as a starting point and generates a new trigram book """
    key_pair = random.choice(list(trigram_word_dict))
    new_book = ""
    new_book += key_pair
    current_length = len(key_pair)
    paragraph_length = len(key_pair)

    for _ in range(words_count):
        key_pair, new_word = get_key_value_from_dict(key_pair)
        if not key_pair:
            key_pair = random.choice(list(trigram_word_dict))
        else:
            # Keeps length of paragraph is set to 500 long. if it greater then will append two lines to
            # split to a paragraph.
            if paragraph_length >= 500:
                new_book += "\n\n" + new_word
                paragraph_length = 0
            # checks length of line is higher than 80. If so, Adds new line and adds new word to new book.
            elif current_length >= 80:
                new_book += "\n" + new_word
                current_length = 0
            # checks existence of new word. If so if length of new book is less than 80 then adds space and
            # new word to book
            elif current_length < 80:
                current_length += len(" " + new_word)
                paragraph_length += len(" " + new_word)
                new_book += " " + new_word
    print(new_book)


if __name__ == "__main__":
    trigram_word_dict = {}
    generate_trigram_dict('sherlock_small.txt')
    generate_trigram_book(500)