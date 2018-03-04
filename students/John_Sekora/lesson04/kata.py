# -- Data --
file_data = ""
trigram = []


# -- Processing --
def load_file():
    file_name = input("Please enter the name of a text file: ")
    object_file = open(file_name, 'r')
    object_file.seek(0)
    output_txt = object_file.read()
    if output_txt is not None:
        object_file.close()
    return output_txt


def trigram_list(stuff, i=0):
    print("Your word count is: " + str(len(stuff)))
    while len(stuff[i:i+3]) == 3:
        yield stuff[i:i+3]
        i += 1


def trigram_story(stuff, i=0):
    new_list = []
    while len(stuff[i:i + 3]) == 3:
        new_list.append(stuff[i+2:i + 3])
        i += 1
    return new_list


# -- Presentation --
if __name__ == '__main__':
    file_data = load_file()
    trigram = trigram_list(file_data.split())
    print(list(trigram))
    print(trigram_story(file_data.split()))

