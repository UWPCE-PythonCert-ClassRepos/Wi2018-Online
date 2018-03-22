#!/usr/bin/env python3

"""Mailroom - Lesson 10 - Functional."""
import os
import datetime
import tkinter as tk
from tkinter import filedialog


def load_donors():
    """Create the database (dict)."""
    donors = {'Aristarkh Lentulov': [4.5, 5.0],
              'El Lissitzky': [34.2, 30.0, 35.5],
              'Kazimir Malevich': [15.0, 20.25, 12.25],
              'Marc Chagall': [148.75, 155.0],
              'Wassily Kandinsky': [75.0, 50.5, 60.4],
              }
    return donors


# DONOR-RELATED FUNCTIONS
def add_donation(donors, name, amount):
    """Add a donation for an existing or newly created donor."""
    try:
        donors[name].append(amount)
    except KeyError:
        donors[name] = [amount]

    return donors


def get_last_donation(donors, name):
    """Return a float -- the last donation of the given donor."""
    return donors[name][-1]


def get_donations(donors, name):
    """Return a list of the specified donor's donations."""
    return donors[name]


def get_total_given(donors, name):
    """Return total amount of donations for the given donor."""
    return sum(get_donations(donors, name))


def sort_donors_by_total(donors):
    """Return a list of donor names sorted by total donations, max to min."""
    donors_L = list(donors.items())
    donors_sorted = sorted(donors_L, key=lambda x: sum(x[1]), reverse=True)
    sorted_donor_names = [item[0] for item in donors_sorted]

    return sorted_donor_names


def print_donor_names(donors):
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
                  """).format(name, amount)
    return email_text


def create_report(donors):
    """Create and print a report."""
    report = ""
    title_line_form = "\n{:<26}{:^3}{:>13}{:^3}{:>13}{:^3}{:>13}\n"
    title_line_text = ('Donor Name', '|', 'Total Given', '|',
                       'Num Gifts', '|', 'Average Gift'
                       )
    report += title_line_form.format(*title_line_text)
    report += str('- ' * 38)
    form_line = "\n{:<26}{:>3}{:>13}{:>3}{:>13}{:>3}{:>13}"
    for donor in sort_donors_by_total(donors):
        report += (form_line.format(donor,
                                    '$',
                                    sum(get_donations(donors, donor)),
                                    ' ',
                                    len(get_donations(donors, donor)),
                                    '$',
                                    round((sum(get_donations(donors, donor)) /
                                           len(get_donations(donors, donor))),
                                          2)
                                    )
                   )
    report += "\n"
    print(report)


def get_total(donors):
    """Return the aggregate amount of donations for all donors."""
    return sum([sum(donors[donor]) for donor in donors])


# MANAGING MENUS
# Main menu
def main_menu(donors):
    """Provide the main menu and call relevant functions."""
    prompt = ("\nMain Menu\n"
              "\n1 - Send a Thank You\n"
              "2 - Create a Report\n"
              "3 - Send letters to everyone\n"
              "4 - Match donations\n"
              "5 - Run a projection\n"
              "0 - Quit\n"
              ">> "
              )
    while True:
        response = input(prompt)
        if response == "1":
            send_thank_you_sub_menu(donors)
        elif response == "2":
            create_report(donors)
        elif response == "3":
            send_all_sub_menu(donors)
        elif response == "4":
            donors = challenge(donors)
        elif response == "5":
            run_projection(donors)
        elif response == "0":
            return
        else:
            pass


# Send-a-Thank-You Sub-Menu
def send_thank_you_sub_menu(donors):
    """Provide a sub menu and call relevant functions."""
    prompt = ("\nSend-Thank-You Sub-Menu\n"
              "\n1 - See the list of donors\n"
              "2 - Add a new donor and a donation amount\n"
              "3 - Choose an existing donor\n"
              "0 - Quit\n"
              ">> "
              )

    while True:
        response = input(prompt)
        if response == "1":
            print_donor_names(donors)
        elif response == "2":
            old_donor_interaction(donors, old=False)
        elif response == "3":
            old_donor_interaction(donors)
        elif response == "0":
            return
        else:
            pass


def input_donation(donors, name):
    """Obtain the donation amount from the user."""
    prompt_amount = "Enter the donation amount or 0 to abort > "
    while True:
        try:
            donation_amount = float(input(prompt_amount))
        except ValueError:
            print("Input must be a number")
        else:
            if donation_amount == 0.0:
                return False
            elif donation_amount < 0:
                print("Input must not be negative")
            else:
                add_donation(donors, name, donation_amount)
                return True


def old_donor_interaction(donors, old=True):
    """Ask for donor name, donation amount, print a thank-you email."""
    prompt_name = "Type the donor's full name or 0 to abort > "
    if old:
        name = ""
        while name not in donors:
            name = input(prompt_name)
            if name == "0":
                return False
    else:
        while True:
            name = input(prompt_name)
            if name == "0":
                return False
            elif name == "":
                print("Name must not be empty!")
            else:
                break

    if input_donation(donors, name):
        print(get_email(name, get_last_donation(donors, name)))


#  Send-letters-to-everyone Sub-Menu - Writing to files
def send_all_sub_menu(donors):
    """Provide a sub menu and call relevant functions."""
    prompt = ("\nSend to everyone sub-menu\n"
              "\n1 - Write to current working directory\n"
              "2 - Choose a directory to write\n"
              "0 - Quit\n"
              ">> "
              )
    while True:
        response = input(prompt)
        if response == "1":
            write_cwd(donors)
        elif response == "2":
            write_select_dir(donors)
        elif response == "0":
            return
        else:
            pass


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


def write_cwd(donors):
    """Write all emails to the current working directory."""
    cwd = os.getcwd()
    for donor in donors:
        text = get_email(donor, get_last_donation(donors, donor))
        write_file(get_full_path(cwd, donor), text)

    print("\nAll letters saved in {}\n".format(cwd))


def ask_user_dir():
    """Get a directory from the user."""
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()


def write_select_dir(donors):
    """Write all emails to a dir selected by the user."""
    target_dir = ask_user_dir()
    if not target_dir:  # If the user hits cancel.
        return
    for donor in donors:
        text = get_email(donor, get_last_donation(donors, donor))
        write_file(get_full_path(target_dir, donor), text)

    print("\nAll letters saved in {}\n".format(target_dir))


####################
# Matching donations
####################
def multiplier_factory(factor, min_donation, max_donation):
    """Create the multiplier function.

       Args:
            factor (float): the multiplier to be locked in the return function
            min_donation (float or None): a condition to be locked in the return function
            max_donation (float or None): a condition to be locked in the return function
        Returns:
              a function which will multiply its argument by factor subject to conditions.
    """
    # Several safeguards
    if type(factor) is str or factor <= 1:
        raise ValueError("Factor must be a number > 1")
    elif type(min_donation) is str or type(max_donation) is str:
        raise ValueError("Input must be a number")
    elif min_donation is not None and max_donation is not None:
        raise ValueError("Min and max must not be both defined")

    def func(value):
        def subject_to_increase(value):
            """Decide if the donation (the value must be increased)."""
            if min_donation is not None:
                return value > min_donation
            elif max_donation is not None:
                return value < max_donation
            else:
                return True

        if subject_to_increase(value):
            return factor * value
        else:
            return value

    return func


def do_challenge(donors, factor, min_donation, max_donation, projection):
    """Return projected contribution (float) or an updated donor_db (dict)."""
    multiplier = multiplier_factory(factor, min_donation, max_donation)
    new_db = dict()

    for donor in donors:
        new_db[donor] = list(map(multiplier, donors[donor]))

    if projection:
        return get_total(new_db) - get_total(donors)
    else:
        return new_db


def validate_user_input(msg, factor=False):
    """Helper functon for challenge to get factor, min or max."""
    while True:
        value = input(msg)
        if value == "" and not factor:  # User hits Enter to skip min/max
            return None
        else:
            try:
                value = float(value)
            except ValueError:
                print("Input must be a number")
            else:
                if value == 0:  # User chooses to quit
                    return False
                elif value <= 1 and factor:
                    print("Factor must be greater than 1")
                else:
                    return value


def challenge(donors, projection=False):
    """Get info from user, return a donors db or a projected contibution."""
    if projection:
        print("(This is a projection)")
    else:
        print("(This is NOT a projection!)")
    # factor: False or float > 1
    factor = validate_user_input(("Type a matching factor > 1 "
                                  "or 0 to quit >>> "),
                                 factor=True)
    if factor is False:  # User chooses to quit this sub-menu
        return False

    # minim: False, None, or float (except 0.0)
    minim = validate_user_input(("Type MIN donation, "
                                 "0 to quit, "
                                 "or Enter to skip >>> "))
    if minim is False:  # User chooses to quit this sub-menu
        return False

    if minim is None:  # User may choose only min or max, not both
        maxim = validate_user_input(("Type MAX donation, "
                                     "0 to quit, "
                                     "or Enter to skip >>> "))
        if maxim is False:  # User chooses to quit this sub-menu
            return False
    else:
        maxim = None

    # result: a number or a new donors database
    result = do_challenge(donors, factor, minim, maxim, projection)
    return result


def run_projection(donors):
    """Run challenge in projection mode, print projected contribution."""
    estimate = challenge(donors, projection=True)
    if estimate > 0:
        print("\nYour contribution would total ${:.2f}".format(estimate))


# Load data and run
if __name__ == "__main__":
    donors = load_donors()
    main_menu(donors)
