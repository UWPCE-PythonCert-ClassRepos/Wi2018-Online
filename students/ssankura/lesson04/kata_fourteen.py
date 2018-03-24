#!/usr/bin/env python3

#Lesson4 - kata_fourteen.py

#Global variables
file_name = "sherlock_small.txt" #file name for input
words_file = [] #list of strings with all the words in the input file
trigrams_in_file_dict = {} #stores Key: tuple - word pair ('word1','word2') and value as list of next words ('word3','word4')
new_story_lst = [] #Stores the words in the same order as in the global new_story string. This is used to generate the next word pair
new_story = '' #Stores the newly generated story

''' strip_punctuation
	Method takes an input a string and returns string after stripping the puncuation
'''
from string import punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


'''
	read_file
	reads the input file whose name is stored in the global variable file_name
	and stores the contents in a global list - words_file
'''
def read_file():
	with open(file_name) as f:
	    for line in f:
	    	global words_file
	    	words_file = words_file + line.strip().split()

'''
	read_trigrams_into_dict
	read all the words in the global list - words_file 
	get the first, second and third word
	create a tuple with the first and second as word pair (word1,word2)
	using this tuple as key, insert the tuple into global dict trigrams_in_file_dict
	value as third word (next word). If the word pair already exists as key in Dict,
	then append the next word's list value to add to the list
'''
def read_trigrams_into_dict():
	for index in range(len(words_file) - 2):
		first_word = strip_punctuation(words_file[index])
		second_word = strip_punctuation(words_file[index+1])
		third_word = strip_punctuation(words_file[index+2])

		word_pair = tuple([first_word])+ tuple([second_word])
		next_word = [third_word]

		if word_pair in trigrams_in_file_dict:
			trigrams_in_file_dict[word_pair].append(str(third_word))
		else:
			#add new item
			trigrams_in_file_dict[word_pair] = next_word
	

'''
	Randomly select the first word pair from the global dict
	Get the value for the word pair (next word) from the global dict
	if the next words is a list of words, randonly pick one word,
		else, pick the only next word
	Add the first 2 words and the next value into the new_story global string
		and to the new_story_lst 
'''
def add_first_words_to_story():
	import random
	global new_story #need to use global keyword to allow modify the global string, otherwise, run into compile error

	rand_word_pair = random.choice(list(trigrams_in_file_dict))
	value_list = trigrams_in_file_dict[rand_word_pair]	
	if len(value_list) <= 1:
		value_picked = value_list[0]
	else:
		value_picked = random.choice(value_list)

	new_story_lst.append(rand_word_pair[-2])
	new_story_lst.append(rand_word_pair[-1])
	new_story_lst.append(value_picked)

	new_story += " " + str(rand_word_pair[-2])
	new_story += " " + str(rand_word_pair[-1])
	new_story += " " + value_picked

'''
	generate the next word pair tuple using the last 2 words in the new_story_lst
	while the next word pair is in the global trigrams_in_file_dict
		get the next word (value from dict) or next words list
			if the next word - happens to be  a list, then randomly select one of the words
			if not, select the only option for next word
		Add the selected next word into the new_story and new_story list global variables
	print the story
'''
def trigrams_make_story():
	import random
	global new_story #need to use global keyword to allow modify the global string, otherwise, run into compile error

	next_word_for_story = tuple([new_story_lst[-2]]) + tuple([new_story_lst[-1]]) 
	while (next_word_for_story in trigrams_in_file_dict):
		value = trigrams_in_file_dict[next_word_for_story]
		if len(value) <= 1:
			selected_next_word = value[0]
		else:
			selected_next_word = random.choice(value)
		new_story += " " + selected_next_word
		new_story_lst.append(selected_next_word)

		next_word_for_story = tuple([new_story_lst[-2]]) + tuple([selected_next_word])
	print (new_story)

'''
	Main Method
'''
if __name__ == "__main__":
	read_file()
	read_trigrams_into_dict()
	add_first_words_to_story()
	trigrams_make_story()
