"""Assignment: Kata Fourteen: Tom Swift Under Milk Wood."""

import random
import tkinter as tk
from tkinter import filedialog


# INPUT FILE MANAGEMENT
def get_filepath():
    """Return the path to the source file obtained from the user."""
    # Get the name of the source file from the user.
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    return path


def load_file(source_path):
    """Return a list containing the whole book split on blank space."""
    # Container for the whole text of the loaded book.
    book = []

    # Convert the whole book into a list.
    with open(source_path, 'r') as fromF:
        for line in fromF:
            # Take care of paragraphs
            if line == "\n" or line == "\r\n":
                line = line.strip()  # Get rid of "\r" or "\n" if any
                line = line.split()
                line.append("\n\n")  # Use a double newline instead
            # Punctuation goes with the words to which it relates
            else:
                line = line.strip()
                line = line.split()
            book.extend(line)

    return book


# OUTPUT FORMAT MANAGEMENT
def formatter(a_list):
    """Return a string containing the formatted text."""
    result = ""
    for token in a_list:
        if token == "\n\n":  # Doesn't need a blank space before or after
            result += token
        else:
            result += (token + " ")
    return result


# MAIN PROCESSING
def get_dict(a_list):
    """Return a dict for trigram-style text generation."""
    d = {}
    for index, _ in enumerate(a_list):
        try:
            key = " ".join([a_list[index], a_list[index+1]])
            value = a_list[index+2]
            if key in d:
                d[key].append(value)
            else:
                d[key] = [value]
        except IndexError:
            break
    return d


def get_alt_value(a_dict, key, bad_value):
    """Return a random value (if any) but not the bad value."""
    if len(set(a_dict[key])) == 1:  # Exclude values like ["I", "I"]
        return False
    else:
        values = a_dict[key]
        values.remove(bad_value)
        return random.choice(values)


def get_next_value(a_dict, key):
    """Return a random value (if any) or False if no such key."""
    try:
        value = a_dict[key]  # The value here is a list, with 1 or more items
    except KeyError:
        return False

    return random.choice(value)


def get_seed(a_dict):
    """Choose randomly a key from a_dict as the first 2 words for my text."""
    while True:
        seed = random.choice(list(a_dict.keys()))
        # Want an upper case first word and no \n\n in the second position.
        if seed[0].isupper() and len(seed.split()) == 2:
            break
    return seed


def generate_text(source_dict, size):
    """Return a list with the generated text of the given size."""
    result = []

    # Choose the first 2 words for the text
    seed = get_seed(source_dict)
    result.extend(seed.split())

    # Make sure my list has 2 elements at the starting point
    assert len(result) == 2

    # Collect all the other words for the final text.
    while len(result) < size:
        # Take the last two items of the list and use them as a key
        key = ' '.join([result[-2], result[-1]])
        value = get_next_value(source_dict, key)
        # Handle the case where the dict has no such key; so the value is False
        if not value:
            counter = len(result)
            # Step backwards throu the result list to find a diff key/value
            while counter > 2:
                key = ' '.join([result[counter-3], result[counter-2]])
                value = get_alt_value(source_dict, key, result[counter-1])
                # If an alternative value is found
                if value:
                    # Start the result list anew from that point
                    # i.e. discord the items that led to a dead end
                    result = result[:counter-1]
                    break
                counter -= 1
        # The backtracking was not sucessful, a dead end can't be overcome
        if not value:
            print("Target length cannot be reached")
            return result
        # Everything goes fine so far
        result.append(value)

    return result


def process_main(size):
    """Process all operations to generate some trigram-style text."""
    # Get the input book file from the user
    path = get_filepath()
    # Convert the file into a list of strings
    book = load_file(path)
    # Generate the dict
    source_dict = get_dict(book)
    # Get the generated trigram text as a list
    text_L = generate_text(source_dict, size)
    # Format the list into a printable string and print on screen
    print(formatter(text_L))


# TESTING
def test_generate_text():
    """Run  generate_text() multiple times for errors."""
    path = "C:/Users/Alexey/Desktop/sherlock.txt"
    book = load_file(path)
    source_dict = get_dict(book)
    run_count = 0
    count_lengths = []
    runs = 100
    size = 1000
    for _ in range(runs):
        res = generate_text(source_dict, size)
        count_lengths.append(len(res))
        run_count += 1
    print("Num of runs = {}, output size = {}".format(run_count, size))


def test_generate_text2():
    """See how it behaves when the target size output cannot be reached."""
    source_d = {"A b": ["c", "d"]}
    res = generate_text(source_d, 10)  # Impossible case
    print(formatter(res))


if __name__ == "__main__":
    process_main(200)
    # test_generate_text()
    # test_generate_text2()
