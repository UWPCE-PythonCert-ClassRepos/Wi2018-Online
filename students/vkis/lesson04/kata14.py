# Lesson 04 - Kata14
# Objective: look at all 3 adjacent words in a textfile,
# treat the first 2 as KEYS and the last as a VALUE
# try to construct the longest string-of-combinations 
# =================================================================

# plug-ins
import os

# declarations
dict = {}




def formatter(myline):
    # clean-up text for splitting
    myline = myline.replace("-", " ")
    myline = myline.replace(",", " ")
    myline = myline.replace("(", " ")
    myline = myline.replace(")", " ")
    myline = myline.replace("\n", " ")
    return myline


def f_load(file):
    # local variable assignment
    value = []
    exiting = False
    # read initial line
    myline = file.readline()
    # format, and split line to words
    words = formatter(myline).split()
    index = 0
    # while loop for iteration since loop has a unknown length
    while True:
        # check for enough words in read line, read more if needed
        # while loop keeps reading new lines until condition is met
        while True:
            try:
                key1 = words[index]
                key2 = words[index + 1]
                value.append(words[index + 2])
            except IndexError:
                bufferline = file.readline()
                # the end of the file was read
                if bufferline == "": 
                    exiting = True
                    break
                # clear previous words memory up to failure
                words = words[index:]
                # list was reset, we also need to reset index
                index = 0
                # add more words +=  format and split line to words
                words += formatter(bufferline).split()
            else:
                break
        # end of the file was read from try loop
        if exiting == True: break
         
         
        # check if the sentence has 3 words left, if not, no keys/values are loaded
        if key1[-1] == "." or key2[-1] == ".":
            # end of the sentence doesnt meant end of the list, value still gets
            # loaded, this causes a overload on value (ie, loads 2-3 values
            # at once
            value = []
            index += 1
        else:
            # conditions met, load keys and value into dictionary
            
            # if key1 + key2 already exist, append new value to existing value list
            if dict.__contains__(key1 + " " + key2) == True:
                oldvalue = dict[key1 + " " + key2]
                value += oldvalue
            dict_load = {(key1 + " " + key2): value}
            dict.update(dict_load)
            index += 1
            # reset value container
            value = []
    print("File successfully loaded")
            

def f_input():
    # get input file name
    while True:
        filename = input("\n[IN]: Enter file name: ")
        try:
            os.listdir().index(filename)
        except ValueError:
            print("File does not exist. Files in current dir:\n", os.listdir())
            continue
        else: break
    # read in file line by line
    with open(filename, "r") as file:
        f_load(file)
        file.close

        
def f_export():    
    with open("kata14_out.txt", "w") as out:
        dict2 = dict.copy()        
        
        # User input format
        while True:
            word1 = input("Input starting word: ")
            word2 = input("Input second word: ")
            try:
                dict[word1 + " " + word2]
            except KeyError:
                print("\nWord(s) are not in the read text. Try again.")
                continue
            else:
                break
        
        out.write(word1 + " " + word2)
        
        
        # empty the dict out, loop with changing index
        while True:
            # break top while from nested while
            return_break = False
            
            # with last 2 words, look up the first value in list
            temp = dict2[word1 + " " + word2][0]
            
            index = 0
            # if dict has multiple values, test ahead for one that works
            while True:
                try:
                    # check current index forward
                    testing_temp = dict2[word1 + " " + word2][index]
                    testing_word1 = word2
                    testing_word2 = testing_temp
                    # forward check for error, on first of index
                    dict2[testing_word1 + " " + testing_word2][0]
                except KeyError:
                    # look ahead use of temp[index] fails on next set of
                    # key1 and key2, index fwd on current key1 and key2 list
                    # of values
                    index += 1
                except IndexError:
                    # dict list of values exceeded, end write-out
                    return_break = True
                    break
                else:
                    temp = dict2[word1 + " " + word2][index]
                    break
            
            
            # write new word out
            out.write(" " + temp)
            
            # remove used word from dict
            dict2.pop(word1 + " " + word2)
            # moving fwd, old 2 is new 1
            word1 = word2
            word2 = temp
             
            # break out last in loop to catch current key's value (last) output
            if return_break == True:
                break
        out.close()    



def f_exit():
    return "exiting"


prompt_main = \
"""
Menu - Main
    1) Enter File Name (current dir) and read inputs
    2) Export Kata14
    q) Quit

[IN]: """

dict_main = {"1": f_input, "2": f_export, "q": f_exit}

if __name__ == "__main__":  
    while True:
        if dict_main[input(prompt_main)]() == "exiting":break
        else: continue
        