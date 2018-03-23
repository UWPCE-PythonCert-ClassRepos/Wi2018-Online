#!/usr/bin/env python3
"""
Mail Room program to catch exceptions
__author__ = "Padmaja Peri"
"""

import sys

# Pre-populate a list of donors
donation_dict = {'William Gates III': [22000, 653784.49], 'Mark Zuckerberg':
                [2500, 16396.10], 'Jeff Bezos': [800, 877.33], 'Larry Page':
    [1, 20000, 40000, 90000], 'Steve Jobs': [30000, 30000]}


def donor_names():
    """ Return a list of donor names """
    return donation_dict.keys()


def send_thank_you():
    """
    Function to get print thank you note based on donor name.
    :return:
    """
    name = input("Enter the full name of the donor:")
    if name.lower() == 'main menu':
        return
    else:
        if name == 'list':
            print("Donors are:{}".format(donor_names()))
            send_thank_you()
        elif name not in donor_names():
            # New donor, get his info and print thank you note
            while True:
                try:
                    amount = float(input("New Donor.Enter the "
                                         "donation amount:"))
                except ValueError:
                    print("Invalid donation amount.Enter again")
                else:
                    donation_dict[name] = [amount]
                    print_thank_you(name)
                    break
        elif name in donor_names():
            print_thank_you(name)


def print_thank_you(name, write_to_file=0):
    """ Function to print Thank You note taking the donor name as input """
    notes_text = "Dear  {} , \nThank you very much for your recent donation" \
                 " to XYZ Charity for an amount of {}. \n" \
                 "The funds raised will go towards X, Y and Z. Thank You " \
                 "again for your kindness.\nSincerely,\nThe Team\n".\
                format(name, sum(donation_dict[name]))
    if not write_to_file:
        print(notes_text)
    else:
        write_text_to_file(name, notes_text)
    return notes_text


def write_text_to_file(name, text):
    file_name = "_".join(name.split()) + '.txt'
    with open(file_name, 'w') as fd:
        fd.write(text)


def send_thank_you_to_all_donors():
    """
    Create a text file with the name of the donor. The text in the file is the
    thank you note to that donor
    :return:
    """
    for donor in donor_names():
        file_name = "_".join(donor.split()) + '.txt'
        with open(file_name, 'w') as fd:
            fd.write(print_thank_you(donor, write_to_file=1))


def create_report():
    """
    Print a summary of all donors, their donations, number of donations.
    :return:
    """
    print("{:25s}|{:15s}|{:12s}|{:15s}".format("Donor Name", "Total Given",
                                                 "Num Gifts", "Average Gift"))
    print("-" * 70)
    for donor in donation_dict:
        total_given = sum(donation_dict[donor])
        num_gifts = len(donation_dict[donor])
        average_gift = total_given / num_gifts
        print("{:25s}${:13.2f} {:12d}  ${:13.2f}".format(donor, total_given
                                                , num_gifts, average_gift))


def main_menu():
    """ Main Menu of the program """
    print("Choose from one of the following options: At any point enter "
          "main menu to return to main menu")
    print("1. Send a Thank You Note")
    print("2. Create a Report")
    print("3. Send Thank You Note to all Donors")
    print("4. Quit")

if __name__ == "__main__":
    """ Get input from user and call the respective functions """
    option_dict = {1: send_thank_you, 2: create_report,
                   3: send_thank_you_to_all_donors, 4: sys.exit}
    while True:
        main_menu()
        try:
            option_chosen = int(input("Choose from one of the following: "))
        except ValueError:
            # Raised if the user enters an invalid integer
            print("Invalid Option. Choose an option between 1 through 4")
        else:
            try:
                option_dict.get(option_chosen)()
            except TypeError:
                # Raised if user enters valid int but invalid option ex: 80
                print("Invalid Option. Choose an option between 1 through 4")

