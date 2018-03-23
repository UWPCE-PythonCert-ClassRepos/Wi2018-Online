#!/usr/bin/env python
from sys import exit
import random

# construct list of donors with a frozen set, to later be used as keys in the dictionary
donor_names = frozenset(("Daniel Ocean", "Rusty Ryan", "Linus Caldwell", "Ruben Tishkoff", "Basher Tarr"))

# create donors with dict comprehension 
donors = {donor: [1000, 2000] for donor in donor_names}

# define a function to prompt the user for their desired action
def prompt_user():
    print("Choose an action. ")
    print()
    print("1 - Send a Thank You")
    print("2 - Create a Report")
    print("3 - Send letters to everyone")
    print("4 - Quit")

    # Lesson6 Update: Added a while True block to hold the try exceot 
    while True:
        try:
            response = int(input(" > "))
        except ValueError:
            print("You must enter an *integer* value. ")
            continue
        else:
            return response

# define a function to send a thank you card
def send_a_thank_you():

    # get a list of unique donors
    unique_donors = donors.keys()

    # prompt the user for a donor
    donor = input("To whom would you like to send a thank you? > ")

    # list the possible candidates within the donors list    
    if donor.lower() == "list":

        # print the donors in the dict
        print(', '.join(list(unique_donors)))

        donor = input("To whom would you like to send a thank you? > ")

    # prompt the user for a donation amount
    try:
        donation_amount = int(input("How much would you like to donate? > "))
    except ValueError:
        print("The donation amount must be numeric.")
        donation_amount = int(input("How much would you like to donate? > "))

    # add the donor and the donation amount to the donors list
    donors.setdefault(donor, []).append(donation_amount)

    # Print the thank you note
    print("Dear {:s}, \n Thank you for your generous donations totaling ${:.2f}. \n".format(donor, sum(donors[donor])),
          "Best, \n The Donation Foundation.")

# define a function to create a donation report
def create_a_report():
    # unique_donors = list(set(donors[0]))
    print("You selected create a report." )
    # print the header of the report 
    header_tuple = ("Donor Name", "Total Given", "Num Gifts", "Average Gift Size")
    print("{:20s} | {:10s} | {:10s} | {:15s}".format(*header_tuple))
    print("-" * 70)
    # cycle through the donors and print their statistics
    for donor, donations in donors.items():
        print("{:20s} ${:10.2f}   {:10d}   ${:15.2f}".format(donor, sum(donations), len(donations), sum(donations)/len(donations)))


def send_letters_to_everyone():
    # create a thank you dictionary to populate with cusotmized thank you notes to each donor
    thank_you_dict = {}
    # cycle through the donors dictionary and get the keys and associated total donations
    for donor, donations in donors.items():
        thank_you_dict.setdefault(
            donor,
            "Dear {:s}, \n\n Thank you for your generous donations totaling ${:.2f}. \n\n Best, \n The Donation Foundation. \n\n".format(donor, sum(donations)))
        name_length = len(donor)
        file = open("thank_you_{name:{width}}.txt".format(name = donor, width = name_length), "w")
        file.write(thank_you_dict[donor])
        file.close()
    

        
# define a function to quit the program
def quit_program():
    print("You selected quit. The program is quitting. ")
    exit(0)
    
if __name__ == '__main__':
    # Create a switch dictionary
    switch_response_dictionary = {
    1: send_a_thank_you,
    2: create_a_report,
    3: send_letters_to_everyone,
    4: quit_program
    }
    while True:
        try:
            switch_response_dictionary.get(prompt_user())()
        except TypeError:
            print("You must enter a positive integer from one of 1, 2, 3, or 4.")
            continue