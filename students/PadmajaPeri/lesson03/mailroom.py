#!/usr/bin/env python3
"""
A simple program to keep track of donations for the charity. The program
provides option to 1) Create report of all donations and donor details
2) Send Thank You Notes 3) Add new donors 4) Query for donors
__author__ = "Padmaja Peri"
"""

import sys

# Pre-populate a list of donors
donation_list = [['William Gates, III', 22000, 653784.49], ['Mark Zuckerberg',
                    2500, 16396.10], ['Jeff Bezos', 800, 877.33], ['Larry Page'
    , 1, 20000, 40000, 90000], ['Steve Jobs', 30000, 30000]]


def donor_names():
    """ Return a list of donor names """
    names = []
    for donor in donation_list:
        names.append(donor[0])
    return names


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
            amount = input("New Donor. Enter the donation amount:")
            amount = float(amount)
            donation_list.append([name, amount])
            print_thank_you(name)
        elif name in donor_names():
            print_thank_you(name)


def print_thank_you(name):
    """ Function to print Thank You note taking the donor name as input """
    notes_text = "Dear  {} , \nThank you very much for your recent donation" \
                 " to XYZ Charity. \n" \
                 "The funds raised will go towards X, Y and Z. Thank You " \
                 "again for your kindness.".format(name)
    print(notes_text)


def create_report():
    """
    Print a summary of all donots, their donations, number of donations.
    :return:
    """
    print("{:25s}|{:15s}|{:12s}|{:15s}".format("Donor Name", "Total Given",
                                                 "Num Gifts", "Average Gift"))
    print("-" * 70)
    for record in donation_list:
        total_given = sum(record[1:])
        num_gifts = len(record[1:])
        average_gift = total_given / num_gifts
        print("{:25s}${:13.2f} {:12d}  ${:13.2f}".format(record[0], total_given
                                                , num_gifts, average_gift))


def main_menu():
    """ Main Menu of the program """
    print("Choose from one of the following options: At any point enter "
          "main menu to return to main menu")
    print("1. Send a Thank You Note")
    print("2. Create a Report")
    print("3. Quit")

if __name__ == "__main__":
    """ Get input from user and call the respective functions """
    while True:
        main_menu()
        option_chosen = input("Choose from one of the following: ")
        if int(option_chosen) == 1:
            send_thank_you()
        elif int(option_chosen) == 2:
            create_report()
        elif int(option_chosen) == 3:
            break
    sys.exit()

