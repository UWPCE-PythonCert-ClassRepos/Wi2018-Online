#!/usr/bin/env python3
# -----------------------------------------------------------
# trigram_kata.py
#  Implements a trigram algorithm that generates a couple of
#  hundred words of text using a book-sized file as input
# -----------------------------------------------------------
import random

random.seed()

# global data
trigram = {}
# Trigram dictionary: word pair as key in the form 'word1 word2'
#   { 'word pair': ['list of possible next words']}


def generate_trigram(book):
    """
    Fills in the global trigram dictionary with values determined by the input book.
    :param book: the filename of a text document, preferably a book
    :return: None, fills the trigram dictionary global object, prints stats on the book
    """
    word1 = ''
    word2 = ''

    with open(book, 'r') as f_name:
        book_text = f_name.read()
        book_text = book_text.replace('\n', ' ')
        book_text = book_text.replace('  ', ' \n ')   # See double new lines as word choices

        words = book_text.split(' ')

        for word in words:

            if word1 and word2:
                new_key = "{} {}".format(word1, word2)
                if new_key not in trigram:
                    trigram[new_key] = [word]
                else:
                    trigram[new_key].append(word)
                word1 = word2
                word2 = word

            elif not word1:     # used only once to initialize start words
                word1 = word
            elif not word2:
                word2 = word

    count = 0
    singles = 0
    for key in trigram:
        if len(trigram[key]) > 1:
            # print(repr(key), repr(trigram[key]))
            count += 1
        else:
            singles += 1
    print(f"Trigrams stats: multiple choices: {count}, single word choices: {singles}\n")


def get_new_word(keypair):
    """
    Given a starting keypair, makes a random choice from the options in that keypair.
    :param keypair: a keypair in the global trigram dictionary
    :return: a new keypair string, and a string of a chosen word, None for both if keypair is not found
    """
    keylist = trigram.get(keypair, None)
    newkeypair = None
    newword = None
    if keylist:
        newword = random.choice(keylist)
        newkeypair = keypair.split(' ')[1] + ' ' + newword

    return newkeypair, newword


def generate_new_book(word_count):
    """
    Generates a new book from the global trigram data, and prints it to screen.
    :param word_count: approximate count of words that should be generated
    :return: None, prints the new text to screen, with stats on count of dead ends hit
    """
    keypair = random.choice(list(trigram))
    new_book = ""
    run_length = 0
    deads = 0
    for _ in range(word_count):
        keypair, newword = get_new_word(keypair)
        if not keypair:                                     # dead end hit
            keypair = random.choice(list(trigram))          # opted to just grab a new keypair if a dead end is hit
            deads += 1
        else:
            new_book = new_book + newword
            run_length = run_length + len(newword)
            if '\n' in newword:                             # Handles paragraph CR
                run_length = 0
                new_book += '\n'
            elif run_length > 80:                           # Handles keeping lines of text to ~80 columns
                new_book += '\n'
                run_length = 0
            else:
                new_book += ' '                             # If no other action, adds a space to prep for next word
    print(new_book)
    print(f"\nDead ends hit: {deads}")


if __name__ == "__main__":
    generate_trigram('TSAHA.txt')
    generate_new_book(350)

    trigram = {}                        # Unintended side effect: if global data not cleared, it gets interesting...
    generate_trigram('sherlock.txt')
    generate_new_book(350)
