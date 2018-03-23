#!/usr/bin/env python3

"""Mailroom - Part 4 - Unit testing."""
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
    """Add a donation for an existing or newly created donor."""
    try:
        donors[name].append(amount)
    except KeyError:
        donors[name] = [amount]


def get_last_donation(name):
    """Return a float -- the last donation of the given donor."""
    return donors[name][-1]


def get_donations(name):
    """Return a list of the specified donor's donations."""
    return donors[name]


def get_total_given(name):
    """Return total amount of donations for the given donor."""
    return sum(get_donations(name))


def sort_donors_by_total():
    """Return a list of donor names sorted by total donations, max to min."""
    donors_L = list(donors.items())
    donors_sorted = sorted(donors_L, key=lambda x: sum(x[1]), reverse=True)
    sorted_donor_names = [item[0] for item in donors_sorted]

    return sorted_donor_names


def print_donor_names():
    """Print existing donor names on screen in alphabetical order."""
    donors_L = sorted(donors.keys())
    num = len(donors_L)
    donors_S = (("\n" + ", ".join(["{}"] * num)).format(*donors_L))
    print(donors_S)


def get_email(name, amount):
    """Return a str containing a thank-you email."""
    email_text = ("""\nDear {},\n
                  \nI would like to thank you for your donation of ${}.\n
                  \nWe appreciate your support.\n
                  \nSincerely,\n
                  \nThe Organization\n
                  """)
    return email_text.format(name, amount)


def create_report():
    """Create and print a report."""
    report = ""
    title_line_form = "\n{:<26}{:^3}{:>13}{:^3}{:>13}{:^3}{:>13}\n"
    title_line_text = ('Donor Name', '|', 'Total Given', '|',
                       'Num Gifts', '|', 'Average Gift'
                       )
    report += title_line_form.format(*title_line_text)
    report += str('- ' * 38)
    form_line = "\n{:<26}{:>3}{:>13}{:>3}{:>13}{:>3}{:>13}"
    for name in sort_donors_by_total():
        total = get_total_given(name)
        num_gifts = len(get_donations(name))
        mean = round((total / num_gifts), 2)
        report += (form_line.format(str(name), '$', str(total), ' ',
                                    str(num_gifts), '$', str(mean)
                                    )
                   )
    report += "\n"
    print(report)


# PRINT ON SREEN A THANK YOU LETTER TO SOMEONE WHO JUST MADE A DONATION
def input_donation(name):
    """Obtain the donation amount from the user."""
    prompt_amount = "Enter the donation amount or 0 to abort > "
    while True:
        try:
            donation_amount = float(input(prompt_amount))
        except ValueError:
            print("Input must be a number")
            continue
        else:
            if donation_amount == 0.0:
                return False
            elif donation_amount < 0:
                print("Input must not be negative")
                continue
            else:
                add_donation(name, donation_amount)
                return True


def old_donor_interaction():
    """Call any_donor() for the old donor functionality."""
    any_donor()


def new_donor_interaction():
    """Call any_donor() for the new donor functionality."""
    any_donor(old=False)


def any_donor(old=True):
    """Ask for donor name, donation amount, print a thank-you email."""
    prompt_name = "Type the donor's full name or 0 to abort > "
    if old:
        donor_name = ""
        while donor_name not in donors:
            donor_name = input(prompt_name)
            if donor_name == "0":
                return
    else:
        donor_name = input(prompt_name)
        if donor_name == "0":
            return

    if input_donation(donor_name):
        print(get_email(donor_name, get_last_donation(donor_name)))


#  WRITE ALL LETTERS TO FILES
def get_full_path(destination, name):
    """Construct a full path including date and name."""
    date = str(datetime.date.today())
    filename = "{}-{}.txt".format(date, name)
    path = os.path.join(destination, filename)
    return path


def write_file(destination, text):
    """Write text to destination path."""
    with open(destination, "w") as toF:
        toF.write(text)


def write_cwd():
    """Write all emails to the current working directory."""
    cwd = os.getcwd()
    for name in donors:
        text = get_email(name, get_last_donation(name))
        write_file(get_full_path(cwd, name), text)

    print("\nAll letters saved in {}\n".format(cwd))


def ask_user_dir():
    """Get a directory from the user."""
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()


def write_select_dir():
    """Write all emails to a dir selected by the user."""
    target_dir = ask_user_dir()
    if not target_dir:  # If the user hits cancel.
        return
    for name in donors:
        text = get_email(name, get_last_donation(name))
        write_file(get_full_path(target_dir, name), text)

    print("\nAll letters saved in {}\n".format(target_dir))


# MANAGING MENUS
#  Write to files
def write_file_dispatch():
    """Return a dispatch dict for the send-to-everyone sub-menu."""
    return {"1": write_cwd,
            "2": write_select_dir,
            "0": quit,
            }


def write_file_prompt():
    """Return a prompt str for the send-to-everyone sub-menu."""
    return ("\nSend to everyone sub-menu\n"
            "\n1 - Write to current working directory\n"
            "2 - Choose a directory to write\n"
            "0 - Quit\n"
            ">> "
            )


# Print on screen
def send_thanks_dispatch():
    """Return a dispatch dict for the send-thank-you sub-menu."""
    return {"1": print_donor_names,
            "2": new_donor_interaction,
            "3": old_donor_interaction,
            "0": quit,
            }


def send_thanks_prompt():
    """Return a prompt str for the send-thank-you sub-menu."""
    return ("\nSend-Thank-You Sub-Menu\n"
            "\n1 - See the list of donors\n"
            "2 - Add a new donor and a donation amount\n"
            "3 - Choose an existing donor\n"
            "0 - Quit\n"
            ">> "
            )


# Main menu
def main_dispatch():
    """Return a dispatch dict for the main menu."""
    return {"1": send_thank_you_interaction,
            "2": create_report,
            "3": send_all_menu,
            "0": quit,
            }


def main_prompt():
    """Return a prompt str for the main menu."""
    return ("\nMain Menu\n"
            "\n1 - Send a Thank You\n"
            "2 - Create a Report\n"
            "3 - Send letters to everyone\n"
            "0 - Quit\n"
            ">> "
            )


def quit():
    """Provide an exit option for menus."""
    return "exit menu"


def send_all_menu():
    """Initiate the send-all-letters sub-sub-menu."""
    menu_selection(write_file_prompt(), write_file_dispatch())


def send_thank_you_interaction():
    """Initiate the send-thank-you sub-menu."""
    menu_selection(send_thanks_prompt(), send_thanks_dispatch())


def menu_selection(prompt, dispatch_dict):
    """Provide a template for using dispatch dicts to switch through menus."""
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print("\nInvalid choice. Try again")


if __name__ == "__main__":
    menu_selection(main_prompt(), main_dispatch())
