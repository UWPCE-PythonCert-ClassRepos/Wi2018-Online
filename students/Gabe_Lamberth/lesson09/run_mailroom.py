#!/usr/bin/env python3
from mailroom5 import *
from pathlib import Path
from random import randint


patrons = {'Emma Watson': [50.00, 150.00, 2000.00, 3000.00],
           'Jack Black': [5000.25, 2500.00],
           'Mel Gibson': [5015.00, 200.50, 35.50]
           }

# Pass dictionary to Donor Class and instantiate object mr
mr = Donor(patrons)


def generate_report():
    header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:25} |{:^15} |{:^15} |{:^15}'.format(*header))
    print('-' * 75)
    # mr.items uses get
    print(''.join({f"{k:<30} ${sum(v):^,.2f}  {len(v):^20}  ${sum(v)/len(v):,.2f}\n" for (k, v) in mr.items()}))
    print('-- Report Finished --\n')


# Called when user wants to see the list of donors makes call to __dict__ object
def display_donors():
    print('Showing list of patrons in the database:\n')
    print('\n'.join({k for k in mr}))


def send_email(choice, amount):
    print(f"Thank you {choice} for your generous ${amount:,.2f} donation")
    print('-- Email Sent --\n')


# Used to help add_donor menu validation for dictionary function call
def silent_quit():
    pass


# Called from menu_dictionary
def add_donor():
    # donor menu used to help validate choices
    donor_menu = {'1': display_donors, 'quit': silent_quit}

    while True:
        choice = input("""
        Type 1 - To display a list of donor's.
        Type quit - to exit to main menu.
        Enter value here >>  """)
        try:
            donor_menu[choice]()
        except KeyError:
            print("Not a valid choice, please try again")
        else:
            if choice == 'quit':
                break
            else:
                first, last = input("\nPlease enter the new Donor's First and Last name:  ").split()
                name = f'{first} {last}'.title()
                if name in mr.keys():
                    print("Donor's name already exists")
                    continue
                else:
                    mr[name] = []
                try:
                    amount = float(input('Please enter a donation amount: '))
                except ValueError:
                    print("The donation must be numeric like 1234.00")
                    # remove user's entry and start at top of menu
                    del mr[name]
                else:
                    mr.append(name, amount)
                    send_email(name, amount)


def write_letters(key, value):
    text = """
                    Dear {},

                           Thank you for you donation of ${:,.2f}

                           It will be put to good use

                                            Sincerely,
                                                -The Team""".format(key, sum(value))
    return text


def draft_letters():
    count = 0
    cwd = Path.cwd()
    for key, value in mr.items():
        pth = cwd / f'{key}.txt'
        if pth.exists():
            print(f'{key}.txt file Already Exists....\nCreating new file....\n')
            pth = cwd / f'{key}{randint(0,99)}.txt'
        pth.write_text(write_letters(key, value))
        count = count + 1

    print(f'{count} letters created\n')
    print(f'Letters located in {cwd}')


# Function will end if user select 'q' the main program
def quit_menu():
    print("Shutting down program, Goodbye", end='\n')
    return "exit menu"


# Run the program
def user_selection(user_prompt, queue_dict):
    # Runs until user inputs 'q'
    while True:
        try:
            response = input(user_prompt)
        except KeyError:
            print("Not a valid selection")
        else:
            if queue_dict[response]() == "exit menu":
                break


def main():
    """
    Function main drives the Donor program. It first prompts the user for a selection to pass to the correlated method.
    The program will end when the user selects the quit method
    """
    user_prompt = ("""\nWelcome to the MailRoom Donor Program!
                          What would you like to do?
                          Type 1 - To display donors'
                          Type 2 - To generate a report'
                          Type 3 - To add new donor'
                          Type 4 - To send letters to donors'
                          Type q - To end the program'
                          Enter value here >> """)

    # Use dictionary to create quasi switch/case structure
    menu_dict = {"1": display_donors,
                 "2": generate_report,
                 "3": add_donor,
                 "4": draft_letters,
                 "q": quit_menu}
    # Pass the user_prompt and menu_dict to the user_selection function
    user_selection(user_prompt, menu_dict)


if __name__ == "__main__":
    main()