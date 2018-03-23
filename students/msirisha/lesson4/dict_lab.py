# ========================= #
# demonstrate dictionary    #
# ========================= #


def display_dictionaries():
    """ Display dictonaries """
    dict = {"name": "chris", "city": "seattle", "cake": "chocolate"}
    print("printing dictonary1\n")
    print(dict)
    print("removig the entry for cake\n")
    dict.pop("cake")
    print("Adding key fruit and value as Mango\n")
    dict["fruit"] = "Mango"
    print("Displaying dict1 keys and values\n")
    print("keys: {}, values: {}\n".format(dict.keys(), dict.values()))
    if not "cake" in dict.keys():
        print("Yes cake key does not exist in dictionary keys\n")
    if "Mango" in dict.values():
        print("Yes Mango values exists in dictionary values\n")

    new_dict = {}
    for key in dict:
        new_dict[key] = dict[key].lower().count("t")
    print("This is new dict {} with the keys same as original dict and with values having count of t".format(new_dict))


def display_sets():
    """ Display sets """
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set((range(0, 21, 4)))
    print("sets s2, divisible by 2 {}".format(s2))
    print("sets s3, divisible by 3 {}".format(s3))
    print("sets s4, divisible by 4 {}".format(s4))
    print("is s3 is a subset of s2 {}".format(s3.issubset(s2)))
    print("is s4 is a subset of s2 {}".format(s4.issubset(s2)))

if __name__ == "__main__":
    display_dictionaries()
    display_sets()