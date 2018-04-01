#!/usr/bin/env python3

# -------------------------------------------------#
# Title: Mailroom Refactor Assignment
# Dev: Scott Luse
# Date: Mar 17, 2018
# -------------------------------------------------#

import Donors as dr
import Reporting as rp

# -- Processing --#
def get_user_choice():
    '''Generates a main menu selection (1-4) for user actions.'''
    print("""
    MailRoom OOP Menu Options
    1) Send a Thank You
    2) Create a Report
    3) Send Letters To Everyone
    4) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 4]: ")
    return (user_choice.strip())

def process_menu(menu_item):
    '''Process the main menu selection from user action.
    Item-1 continues into the thank you letter prompts, Item-2 creates a list
    of donors and a donation report on the screen, Item-3 saves individual giving
    reports to disk as text files.'''
    if menu_item == '1':
        send_thanks()
    elif menu_item == '2':
        dr.Donor_object.print_screen_report(donor_obj)
    elif menu_item == '3':
        print(dr.Donor_object.create_individual_letters(donor_obj))

def send_thanks():
    '''Prompts the user for a donor name, pre-existing or new.'''
    while (True):
        name = input("Please enter FULL NAME, enter 'LIST' for names, or 'MAIN' for menu: ")
        if name.lower() == "list":
            print(str(donor_obj) + "\n")
        elif name.lower() == "main":
            return
        else:
            process_thank_you(name)

def process_thank_you(name):
    '''Prompt the user for a donation amount following the prompt for donor name.'''
    try:
        gift_amount = int(input("Please enter donation $$ AMOUNT for " + name + ":"))
        if name in donor_dict.keys():
            original_list = donor_dict.get(name)
            original_list.append(gift_amount)
            donor_dict[name] = original_list
            rp.Reports.thank_you_printing(name, gift_amount)
        else:
            # new name
            donor_dict[name] = [gift_amount]
            rp.Reports.thank_you_printing(name, gift_amount)

    except ValueError as e:
        print("\n Error: " + str(e) + "\nPlease enter a number amount:\n ")
        process_thank_you(name)

# -- Presentation (Input/Output) --#
if __name__ == '__main__':

    donor_dict = {
        'Peter Parker': [288.09, 9.01, 61288.09],
        'Iron Man': [1238.09, 8199.01, 1468.07],
        'Captain Marvel': [43188.09, 1288.09],
        'Black Widow': [10.00, 10.00]}
    donor_obj = dr.Donor_object(donor_dict)

    while (True):
        get_user_action = get_user_choice()
        if get_user_action == "4":
            print("Goodbye!")
            break
        else:
            process_menu(get_user_action)