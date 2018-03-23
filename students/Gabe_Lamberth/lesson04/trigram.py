import random
import pathlib


def get_file(file_name):
    # Take in a file and return it as a string.
    f = pathlib.Path.cwd() / file_name
    string = f.read_text()
    return string


def dict_gen(str_list):
    """
    Take in a list of strings. Iterate through list of strings and concatenate
    focus item and item directly following it to create a dictionary key.
    Assign the next word as the value.
    """
    trigram = {}

    for i in range(len(str_list)-2):
        key = str_list[i] + ' ' + str_list[i + 1]
        val = str_list[i+2]
        trigram.setdefault(key, []).append(val)
    return trigram


def build_trigram(**kwargs):
    """
    Use random key to isolate arbitrary word pair as starting point.
    While loop iterates to append next words from new word pairs
    """
    dict_key = random.choice(list(kwargs.keys()))
    words_list = " ".join((dict_key, random.choice(kwargs[dict_key]))).split()
    word = " ".join((words_list[-2], words_list[-1]))

    while word in kwargs:
        words_list.append(random.choice(kwargs[word]))
        word = " ".join((words_list[-2], words_list[-1]))

    book = " ".join(words_list)
    return book


def main():
    # Calls methods and builds a trigram based on an input file.
    str_file = get_file('small_sherlock.txt')
    # Pass list of file to function to create dictionary
    tri_dict = dict_gen(list(str_file.split()))

    tri_book = build_trigram(**tri_dict)

    for word in tri_book:
        if '.' in word:
            print('\n'.join(word))
        else:
            print(f'{word}', end='')
    print("\n##########################READING NEW FILE###########################################")
    str_file1 = get_file('sherlock.txt')
    tri_dict = dict_gen(list(str_file1.split()))

    tri_book = build_trigram(**tri_dict)

    for word in tri_book:
        if '.' in word:
            print('\n'.join(word))
        else:
            print(f'{word}', end='')


if __name__ == '__main__':
    main()