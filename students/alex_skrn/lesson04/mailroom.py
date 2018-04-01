#!/usr/bin/env python3

"""Mailroom - Part 2 - Dicts, Files."""
import os
import datetime
import tkinter as tk
from tkinter import filedialog

donors = {'Aristarkh Lentulov': [4.5, 5.0],
          'El Lissitzky': [34.2, 30.0, 35.5],
          'Kazimir Malevich': [15.0, 20.25, 12.25],
          'Marc Chagall': [148.75, 155.0],
          'Wassily Kandinsky': [75.0, 50.5, 60.4],
          }


# DONOR-RELATED FUNCTIONS
def add_donation(name, amount):
    """Add a donation for a named donor."""
    if name in donors:
        donors[name].append(float(amount))
    else:
        donors[name] = [float(amount)]


def get_last_donation(name):
    """Return a float -- the last donation of the given donor."""
    return donors[name][-1]


def get_total_given(name):
    """Return total amount of donations for the given donor."""
    return sum(donors[name])


def get_donations(name):
    """Return a list of the specified donor's donations."""
    return donors[name]


def sort_donors_by_total():
    """Return a list of donor names sorted by total donations, max to min."""
    donors_L = list(donors.items())
    donors_sorted = sorted(donors_L, key=lambda x: sum(x[1]), reverse=True)
    sorted_donor_names = []
    for item in donors_sorted:
        sorted_donor_names.append(item[0])

    return sorted_donor_names


def print_donor_names():
    """Print existing donor names on screen."""
    print()
    donors_L = list(donors.keys())
    for name in donors_L[:-1]:
        print(name, end=', ')
    print(donors_L[-1])
    print()


def get_email(name, amount):
    """Return a str containing a thank-you email."""
    d = dict(key1=name, key2=amount)
    # Can't figure out how to combine {:,} and {key2} below.
    # Used a dict here 'cos the assignment seems to ask for it.
    email_text = ("\nDear {key1},\n"
                  "\nI would like to thank you for your donation of ${key2}.\n"
                  "\nWe appreciate your support.\n"
                  "\nSincerely,\n"
                  "The Organization\n"
                  )
    return email_text.format(**d)


def print_email(name, amount):
    """Print a thank-you email on screen."""
    print(get_email(name, amount))


def create_report():
    """Create a report."""
    title_line_form = "{:<26}{:^3}{:>13}{:^3}{:>13}{:^3}{:>13}"
    title_line_text = ('Donor Name', '|', 'Total Given', '|',
                       'Num Gifts', '|', 'Average Gift'
                       )
    print()
    print(title_line_form.format(*title_line_text))
    print('- ' * 38)
    form_line = "{:<26}{:>3}{:>13}{:>3}{:>13}{:>3}{:>13}"
    for name in sort_donors_by_total():
        total = get_total_given(name)
        num_gifts = len(get_donations(name))
        mean = round((total / num_gifts), 2)
        print(form_line.format(str(name), '$', str(total), ' ',
                               str(num_gifts), '$', str(mean)
                               )
              )
    print()


# PRINT ON SREEN A THANK YOU LETTER TO SOMEONE WHO JUST MADE A DONATION
def existing_donor_interaction():
    """Ask for old donor name, donation amount, print a thank-you email."""
    prompt_name = "Type full name of the old donor or 0 to abort > "
    old_donor_name = input(prompt_name)
    if old_donor_name == "0":
        return
    while old_donor_name not in donors:
        old_donor_name = input(prompt_name)
        if old_donor_name == "0":
            return

    prompt_amount = "Enter the donation amount or 0 to abort > "
    donation_amount = input(prompt_amount)
    if donation_amount == "0":
        return

    # Add the donation amount to the dict.
    add_donation(old_donor_name, donation_amount)

    print_email(old_donor_name, get_last_donation(old_donor_name))


def new_donor_interaction():
    """Ask for new donor name, donation amount, print a thank-you email."""
    prompt_name = "Type full name of the new donor or 0 to abort > "
    new_donor_name = input(prompt_name)
    if new_donor_name == "0":
        return

    prompt_amount = "Enter the donation amount or 0 to abort > "
    donation_amount = input(prompt_amount)
    if donation_amount == "0":
        return

    # Add the donor and the donation amount to the dict.
    add_donation(new_donor_name, donation_amount)

    print_email(new_donor_name, get_last_donation(new_donor_name))


#  WRITE ALL LETTERS TO FILES
def write_file(destination, name, text):
    """Write text to destination/name.txt."""
    date = str(datetime.date.today())
    # path = "{}/{}-{}.txt".format(destination, date, name)
    filename = "{}-{}.txt".format(date, name)
    path = os.path.join(destination, filename)
    with open(path, "w") as toF:
        toF.write(text)


def write_cwd():
    """Write all emails to the current working directory."""
    cwd = os.getcwd()
    for name in donors:
        text = get_email(name, get_last_donation(name))
        write_file(cwd, name, text)

    print("\nAll letters saved in {}\n".format(cwd))


def write_select_dir():
    """Write all emails to a dir selected by the user."""
    root = tk.Tk()
    root.withdraw()

    # Get the target directory from the user.
    target_dir = filedialog.askdirectory()
    for name in donors:
        text = get_email(name, get_last_donation(name))
        write_file(target_dir, name, text)

    print("\nAll letters saved in {}\n".format(target_dir))


# MANAGING MENUS
def quit():
    """Provide an exit option for menus."""
    return "exit menu"


def send_all_menu():
    """Initiate the send-all-letters sub-sub-menu."""
    menu_selection(write_file_prompt, write_file_dispatch)


def send_thank_you_interaction():
    """Initiate the send-thank-you sub-menu."""
    menu_selection(send_thanks_prompt, send_thanks_dispatch)


def menu_selection(prompt, dispatch_dict):
    """Provide a template for using dispatch dicts to switch through menus."""
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print("\nInvalid choice. Try again")
            pass


if __name__ == "__main__":
    #  Write to files
    write_file_prompt = ("\nSend to everyone sub-menu\n"
                         "\n1 - Write to current working directory\n"
                         "2 - Choose a directory to write\n"
                         "3 - Quit\n"
                         ">> "
                         )
    write_file_dispatch = {"1": write_cwd,
                           "2": write_select_dir,
                           "3": quit,
                           }
    # Print on screen
    send_thanks_dispatch = {"1": print_donor_names,
                            "2": new_donor_interaction,
                            "3": existing_donor_interaction,
                            "4": quit,
                            }
    send_thanks_prompt = ("\nSend-Thank-You Sub-Menu\n"
                          "\n1 - See the list of donors\n"
                          "2 - Add a new donor and a donation amount\n"
                          "3 - Choose an existing donor\n"
                          "4 - Quit\n"
                          ">> "
                          )
    # Main menu
    main_dispatch = {"1": send_thank_you_interaction,
                     "2": create_report,
                     "3": send_all_menu,
                     "4": quit,
                     }
    main_prompt = ("\nMain Menu\n"
                   "\n1 - Send a Thank You\n"
                   "2 - Create a Report\n"
                   "3 - Send letters to everyone\n"
                   "4 - Quit\n"
                   ">> "
                   )
    menu_selection(main_prompt, main_dispatch)
