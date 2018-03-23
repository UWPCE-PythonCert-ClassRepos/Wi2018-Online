#!/usr/bin/env python
import random
import re

# prepare to read the (first 500 lines of) Japanese Fairy Tail file
# establish file path and header size
file_path = '/Users/davidrusso/Documents/Classes/Python Certificate/Introduction to Python/Wi2018-Online/students/david_russo/lesson4/japanese_fairy_tails.txt' 
# file_path = '/Users/davidrusso/Documents/Classes/Python Certificate/Introduction to Python/Wi2018-Online/students/david_russo/lesson4/heart_of_darkness.txt'

# read the file
with open(file_path, 'r') as f:
	read_file = f.read()


# create a word list from the file
def create_word_list(file_name):
	word_list = []
	for word in file_name.split():
		word_list.append(word)
	return word_list

read_file_words = create_word_list(file_name = read_file)

# create a trigram dictionary from a word list
def create_trigram_dictionaries(word_list):
	trigram_dict = {}
	num_words = len(word_list)
	for idx in range(2, num_words):
		word_tuple = (word_list[idx - 2].lower(), word_list[idx - 1].lower())
		trigram_key = " ".join(word_tuple)
		trigram_dict.setdefault(trigram_key, []).append(word_list[idx].lower())
	return trigram_dict

read_file_trigram_dict = create_trigram_dictionaries(word_list = read_file_words)

# generate text from the trigram dictionary
def generate_text(trigram_dictionary):
	# initialize the new text by picking a random start point
	generated_story = random.choice(list(trigram_dictionary.keys()))
	while len(generated_story.split()) <= 250:
		generated_story_as_words = generated_story.split()
		num_words = len(generated_story_as_words)
		last_two_words = generated_story_as_words[num_words - 2] + ' ' + generated_story_as_words[num_words - 1]
		next_part_of_story = random.choice(list(trigram_dictionary[last_two_words]))
		generated_story = generated_story + ' ' + next_part_of_story
	return generated_story

print(generate_text(read_file_trigram_dict))





		







