#!/usr/bin/env python3

#-------------------------------------------------#
# Title: Trigram Assignment
# Dev: Scott Luse
# Date: Feb 13, 2018
#-------------------------------------------------#


# -- Data --#
USER_TEXT_FILE = ""
TRIGRAM_LIST = []

# -- Processing --#
def load_user_file():
    file_name = input("\n" + "Please enter name of text file (sherlock.txt): ")
    object_file = open(file_name, "r")
    object_file.seek(0)
    user_txt = object_file.read()
    if (object_file != None):
        object_file.close()
    return(user_txt)

def create_trigram_list(seq, i=0):
    '''Bring in a really long sequence of words, the length of the sequence is the word count.
    Group the first three words starting with index 0. For example, the first three words will be [0:3]
    since the finish value is not included. The second group is [1:4], third is [2:5]. Also note
    yield function will return a generator.'''

    print("Your word count is: " + str(len(seq)))
    while len(seq[i:i + 3]) == 3:
        yield seq[i:i + 3]
        i += 1


def create_trigram_story(seq, i=0):
    a_list = []
    while len(seq[i:i + 3]) == 3:
        a_list.append(seq[i+2:i + 3])
        i += 1
    return(a_list)



# -- Presentation (Input/Output) --#
if __name__ == '__main__':
    USER_TEXT_FILE = load_user_file()

    TRIGRAM_LIST = create_trigram_list(USER_TEXT_FILE.split())
    print(list(TRIGRAM_LIST))

    print(create_trigram_story(USER_TEXT_FILE.split()))
