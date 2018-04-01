import sys, random

def read_file(path):
	f = open(path, 'r', encoding='utf-8')
	return(f)

def userinput(argv):
    if len(argv) != 3:
    	sys.stderr.write('Please enter filename and number of words\n')
    	sys.exit(1)
    filename = argv[1]
    num_words = int(argv[2])
    return filename, num_words

def make_trigram(text):
	tri_dict = {}
	while len(text.split()) > 2:
		split_words = text.split(' ', 3)
		textkeys = (split_words[0], split_words[1])
		textvalue = split_words[2]
		if textkeys not in tri_dict:
			tri_dict[textkeys] = [textvalue]
		else:
			tri_dict[textkeys] = tri_dict.get(textkeys).append(textvalue)
		text = text[len(split_words[0])+1:]
	return tri_dict

def make_story(dict, num_words):
	story = []
	rand_words(dict, story)
	while len(story) < num_words:
		last_words = (story[-2], story[-1])
		if last_words in dict:
			get_lastword = random.choice(dict[last_words])
			story.append(get_lastword)
		else:
			rand_words(dict, story)
	return " ".join(story)

def rand_words(dict, story):
	rand_key = random.choice(list(dict))
	first = str(rand_key[0])
	second = str(rand_key[1])
	third = random.choice(dict[rand_key])
	story.extend([first, second, third])
	return story

if __name__ == "__main__":
	filename, num_words = userinput(sys.argv)
	text = read_file(filename).read()
	trigrams = make_trigram(text)
	print(trigrams)
	new_story = make_story(trigrams, num_words)
	print(new_story)

