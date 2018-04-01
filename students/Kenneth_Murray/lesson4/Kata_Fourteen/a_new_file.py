#!/usr/bin/env python3
"""perform trigram processing to manipulate new text.the text will be read from the source folder and is named input.txt"""


def kata_lines():
    """
    # find lines in a text file.
    # rearrange the lines using the trigram method
    """
    paragraph_list = kata_paragraphs()
    for item in paragraph_list:  #itterate through the paragraphs
        start = 0
        count = 0
        trigram_new_list= [[]]
        while start < len(item):
            first = start
            second = first + 1
            third = second + 1
            if third < len(item):
                trigram_new_list[count].append([item[first], item[second], item[third]])
                trigram_new_list.append([])
            trigram_new_list.append([])
            start = start + 1
            count = count + 1  # now we have a list of sentence trigrams
    # print (trigram_new_list) - this was here to test the output of the last step
        import datetime
        datestr = str(datetime.datetime.now())
        dt = datestr[0:4]
        with open(f'output_sentence_trigram_{dt}.txt', 'w') as trigram_sentence_txt:
            for item in trigram_new_list:  #itrerate through the items in the list and write them to the new file.
                trigram_sentence_txt.writelines(item)
            trigram_sentence_txt.close()
        print(f'The trigram file is trigram_sentence_txt{dt}.txt')
        return trigram_new_list


def kata_paragraphs(input_text='input.txt', kata = False):
    """
    the default name for the input file.
    to create a trigram, set KATA to True
    to return a list of paragraphs, just leave the default to false
    """
    count = 0  # create a list of lists of paragraphs
    paragraph_list = [[]]
    with open(input_text, 'r') as orig_text:
        for lines in orig_text:
            if not lines == '\n':
                paragraph_list[count].append(lines)
            else:
                paragraph_list.append([])
                paragraph_list[count].append(lines)
                count = count + 1  # now I have a list of lists of the paragraphs.
            # create the trigrams
        start = 0
        count = 0
        trigram_new_list = [[]]
        while start < len(paragraph_list):
            first = start
            second = first + 1
            third = second + 1
            if third < len(paragraph_list):
                trigram_new_list[count].append([paragraph_list[first], paragraph_list[second], paragraph_list[third]])
                trigram_new_list.append([])
            start = start + 1
            count = count + 1  # now we have a list of paragraph trigrams
            # print (trigram_new_list) - this was here to test the output of the last step
        import datetime
        datestr = str(datetime.datetime.now())
        dt = datestr[0:4] + datestr[-6:]
        with open(f'output_parg_trigram_{dt}.txt', 'w') as trigram_parg_txt:
            for item in trigram_new_list:  #itrerate through the items in the list and write them to the new file.
                trigram_parg_txt.writelines(item)
            trigram_parg_txt.close()
        print(f'The trigram file is output_parg_trigram_{dt}.txt')
    if kata:
        return paragraph_list
    else:
        return True


def kata_string():
    """Manipulate strings within a paragraph .A minimum of four are required to produce any result."""
    kata_lines()
    return True


def kata_par():
    """manipulate paragraphs within a body of text. A minimum of four are required to produce any result."""
    kata_paragraphs('input.txt', True)
    return True


def kata_menu(prompt, dispatch_dict):
    while True:  # loop until quit
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break
    return True


def quit():
    print("You are now leaving the KATA room")
    return "exit menu"


main_prompt = ('\nWelcome text switcher.\n'
               'Please select and action from the menu.\n'
               '1 - Generate new strings\n'
               '2 - Generate new paragraphs\n'
               'q - Quit\n'
               )
main_dispatch = {'1': kata_par,
                 '2': kata_string,
                 'q': quit
                 }

if __name__ == '__main__':
    """Kata Trigrams"""
    kata_menu(main_prompt, main_dispatch)
