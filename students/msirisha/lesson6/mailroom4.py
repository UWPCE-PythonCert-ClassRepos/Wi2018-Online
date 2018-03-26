# Mailroom script
# part4. send a thank you note to donors.
# add exceptions concept.

import sys

#global data structure
donor_data = { "sai emani": [20.23, 30.456, 50.786],
               "sirisha marthy": [67.89, 45.89],
               "ani emani": [12.789, 5.456],
               "charles dickens" : [15.89, 89.20, 345.67],
               "mark twain": [678.986]
               }


def menu():
    """ Select one of the four items in the menu
        And returns the number """
    print("1) send a thank you")
    print("2) create a report")
    print("3) send letters to every one")
    print("4) quit")
    while True:
        choice = input("Please enter your choice(1/2/3/4) >")
        try:
            choice = int(choice)
        except ValueError:
            print("please enter choice as integer")
            continue
        else:
            return choice


def send_a_thankyou():
    """ Sends thank you message for the donors
    """
    donor_names = donor_data.keys()
    while True:
        choice = str(input("Please enter donor name (enter \"list\" to show list of donor names, enter \"q\" to quit)"))
        if choice == "q":
            return
        elif choice == "list":
            print("List of donor names")
            print(("{}\n" * len(donor_data)).format(*donor_data.keys()))
            continue
        else:
            if len(choice) == 0:
                print("name can not be empty")
                continue
            elif choice in donor_names:
                print("Donor already in the donor names list.. using existing donor name")
            elif len(choice) > 0:
                donor_data[choice] = []

        break

    while True:
        try:
            amount = input("Please enter donation amount")
            if float(amount) <= 0:
                print("amount donated must be a +ve number")
            else:
                break
        except ValueError:
            print("Enter positive number")

    donor_data[choice].append(float(amount))
    print(generate_letter(choice))

def generate_letter(donor):
    """ Generate letter for donor """
    return "Dear {},\n \nThank you for your generous donation {}.\n \n\n\t\tSincerely, \n\t\tLocal Charity".\
        format(donor, donor_data[donor][-1])

def create_a_report():
    """ Prints donor information for all donors
    """
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    for donor in donor_data:
        print(f"{donor:26} $ {sum(donor_data[donor]):>10.2f}   {len(donor_data[donor]):9} "
              f"${sum(donor_data[donor])/len(donor_data[donor]):>12.2f}")


def send_letters():
    """ Send letters to every one, the letters will be stored as text files on disk """
    for donor in donor_data:
        file_name = donor + ".txt"
        letter = generate_letter(donor)
        with open(file_name, "w") as f:
            f.write(letter)


if __name__ == "__main__":
    choice_dict = {1: send_a_thankyou, 2: create_a_report, 3: send_letters, 4: sys.exit}
    while True:
        try:
            choice_dict[menu()]()
        except TypeError:
            continue
        except ValueError:
            continue

