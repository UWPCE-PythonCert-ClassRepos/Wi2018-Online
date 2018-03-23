#!/usr/bin/env python3

"""Lesson04 - Activity 1: Dicts and Set Lab."""

# Dicts 1
d = {"name": "Chris",
     "city": "Seattle",
     "cake": "Chocolate",
     }


def run_dict1():
    """Execute Dict 1 series of actions."""
    print("\nDictionaries 1\n".upper())
    print(f"Create a dictionary and Display it:\n{d}")
    print("\nDelete the entry for 'cake' and display the dictionary:")
    del d["cake"]
    print(d)
    print("\nAdd an entry for 'fruit' with "
          "'Mango' and display the dictionary"
          )
    d["fruit"] = "Mango"
    print(d)
    print("\nDisplay the dictionary keys:")
    print(d.keys())
    print("\nDisplay the dictionary values:")
    print(d.values())
    print("\nDisplay whether or not 'cake' is a key "
          "in the dictionary (i.e. False):"
          )
    print("cake" in d)
    print("\nDisplay whether or not 'Mango' is a value"
          "in the dictionary (i.e. True)):"
          )
    print("Mango" in d.values())


def run_dict2():
    """Execute Dict 2 series of actions."""
    print("\nDictionaries 2\n".upper())
    print("Using the dictionary from item 1: "
          "Make a dictionary using the same keys but "
          "with the number of 't's in each value as the value:"
          )
    new_d = {}
    for key in d:
        new_d[key] = d[key].lower().count("t")
    print(new_d)


def run_set1():
    """Execute Set 1 series of actions."""
    print("\nSets 1\n".upper())
    print("Create sets s2, s3 and s4 that contain numbers "
          "from zero through twenty, divisible by 2, 3 and 4 and "
          "display the sets:"
          )
    s2 = set(i for i in range(21) if i % 2 == 0)
    s3 = set(i for i in range(21) if i % 3 == 0)
    s4 = set(i for i in range(21) if i % 4 == 0)
    for s in s2, s3, s4:
        print(s)

    print(f"\nDisplay if s3 is a subset of s2 (False):\n{s3.issubset(s2)}")
    print("\nand if s4 is a subset of s2 (True):")
    print(s4.issubset(s2))


def run_set2():
    """Execute Set 2 series of actions."""
    print("\nSets 2\n".upper())
    print("Create a set with the letters in 'Python' and add 'i' to the set.")
    s = set(list("Python"))
    s.add("i")
    print(f"The resulting set:\n{s}")
    print("\nCreate a frozenset with the letters in 'marathon'.")
    sf = frozenset(list("marathon"))
    print(f"The resulting set:\n{sf}")
    print("\ndisplay the union and intersection of the two sets:")
    print(s.union(sf))
    print(s.intersection(sf))


def run_all():
    """Execute all series of actions."""
    run_dict1()
    run_dict2()
    run_set1()
    run_set2()


if __name__ == "__main__":
    run_all()
