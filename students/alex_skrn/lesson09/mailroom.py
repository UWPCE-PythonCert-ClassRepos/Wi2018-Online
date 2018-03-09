#!/usr/bin/env python3

"""Mailroom - Lesson 9 - Object Orientation."""
import os
import datetime
import tkinter as tk
from tkinter import filedialog

data = {'Aristarkh Lentulov': [4.5, 5.0],
        'El Lissitzky': [34.2, 30.0, 35.5],
        'Kazimir Malevich': [15.0, 20.25, 12.25],
        'Marc Chagall': [148.75, 155.0],
        'Wassily Kandinsky': [75.0, 50.5, 60.4],
        }


####################
# SINGLE DONOR CLASS
####################
class SingleDonor(object):
    """Provide a class for a single donor."""

    def __init__(self, name, donation):
        """Instantiate a SingleDonor class object."""
        self._name = name
        if isinstance(donation, list):  # what if a tuple is passed?
            self._donations = donation
        else:
            self._donations = [donation]

    @property
    def name(self):
        """Provide a getter method for the name property."""
        return self._name

    @property
    def donations(self):
        """Provide a getter method for the name property."""
        return self._donations

    def __str__(self):
        return self._name

    def __repr__(self):
        if len(self._donations) == 1:
            return 'SingleDonor("{}", {})'.format(self._name,
                                                  self._donations[0]
                                                  )
        else:
            return 'SingleDonor("{}", {})'.format(self._name,
                                                  self._donations
                                                  )

    def __eq__(self, other):
        return (self._name, self._donations) == (other.name, other.donations)

    def __lt__(self, other):  # may work incorrectly if values are equal ?
        return ((self._name, self._donations) <
                (other.name, other.donations)
                )

    def add_donation(self, amount):
        """Add a donation."""
        self._donations.append(amount)

    @staticmethod
    def sort_by_total(self):
        """Provide a sort_key for sorting by total donations."""
        return sum(self._donations)

    @staticmethod
    def sort_by_name(self):
        """Provide a sort_key for sorting by name."""
        return self._name

    def get_total(self):  # Can't I use sum(donor.donations) everywhere?
        """Return the sum of donations."""
        return sum(self._donations)

    def get_last_donation(self):
        """Return the last donation."""
        return self._donations[-1]


##############
# DONORS CLASS
##############
class Donors(object):
    """Provide a class to handle a collection of donors."""

    def __init__(self, donors):
        """Instantiate a Donors class object with a list of SingleDonors."""
        self._donors = donors

    # @property
    # def donor(self, name):
    #     """Return a donor object for the given name."""
    #     for donor in donors:  # must be self._donors
    #         if donor.name == name:
    #             return donor
    def get_donor(self, name):
        """Return a donor object for the given name."""
        for donor in self._donors:
            if donor.name == name:
                return donor

    def append(self, donor):
        """Append a donor object to the list of donors."""
        self._donors.append(donor)

    def __iter__(self):
        """Make the Donors class object iterable."""
        return iter(self._donors)

    def __contains__(self, donor):
        """Provide a method to check if donor (expected a str) is in donors."""
        return donor in [donor.name for donor in self._donors]

    def print_donor_names(self):
        """Print existing donor names on screen in alphabetical order."""
        donors_L = [donor.name for donor in sorted(self._donors,
                                                   key=SingleDonor.sort_by_name
                                                   )
                    ]
        num = len(donors_L)
        donors_S = (("\n" + ", ".join(["{}"] * num)).format(*donors_L))
        print(donors_S)

    def create_report(self):
        """Create and print a report."""
        report = ""
        title_line_form = "\n{:<26}{:^3}{:>13}{:^3}{:>13}{:^3}{:>13}\n"
        title_line_text = ('Donor Name', '|', 'Total Given', '|',
                           'Num Gifts', '|', 'Average Gift'
                           )
        report += title_line_form.format(*title_line_text)
        report += str('- ' * 38)
        form_line = "\n{:<26}{:>3}{:>13}{:>3}{:>13}{:>3}{:>13}"
        donors_list = sorted(self._donors,
                             key=SingleDonor.sort_by_total,
                             reverse=True)
        # donors_list = [donor.name for donor in sorted_copy]
        for donor in donors_list:
            total = donor.get_total()
            num_gifts = len(donor.donations)
            mean = round((total / num_gifts), 2)
            report += (form_line.format(str(donor.name), '$', str(total), ' ',
                                        str(num_gifts), '$', str(mean)
                                        )
                       )
        report += "\n"
        print(report)


##############
# START MENU CLASS
##############
class StartMenu(object):
    """Provide a class for user ineraction via prompts and menus."""

    def __init__(self, donors):
        """Instantiate a StartMenu class object with a donors object."""
        self._donors = donors
        self.menu_selection(self.main_prompt(), self.main_dispatch())

    def get_email(self, name, amount):
        """Return a str containing a thank-you email."""
        email_text = ("""\nDear {},\n
                      \nI would like to thank you for your donation of ${}.\n
                      \nWe appreciate your support.\n
                      \nSincerely,\n
                      \nThe Organization\n
                      """).format(name, amount)
        return email_text

    # MANAGING MENUS
    #  Write to files
    def write_file_dispatch(self):
        """Return a dispatch dict for the send-to-everyone sub-menu."""
        return {"1": self.write_cwd,
                "2": self.write_select_dir,
                "0": self.quit,
                }

    def write_file_prompt(self):
        """Return a prompt str for the send-to-everyone sub-menu."""
        return ("\nSend to everyone sub-menu\n"
                "\n1 - Write to current working directory\n"
                "2 - Choose a directory to write\n"
                "0 - Quit\n"
                ">> "
                )

    # Print on screen
    def send_thanks_dispatch(self):
        """Return a dispatch dict for the send-thank-you sub-menu."""
        return {"1": donors.print_donor_names,
                "2": self.new_donor_interaction,
                "3": self.old_donor_interaction,
                "0": self.quit,
                }

    def send_thanks_prompt(self):
        """Return a prompt str for the send-thank-you sub-menu."""
        return ("\nSend-Thank-You Sub-Menu\n"
                "\n1 - See the list of donors\n"
                "2 - Add a new donor and a donation amount\n"
                "3 - Choose an existing donor\n"
                "0 - Quit\n"
                ">> "
                )

    # Main menu
    def main_dispatch(self):
        """Return a dispatch dict for the main menu."""
        return {"1": self.send_thank_you_interaction,
                "2": donors.create_report,
                "3": self.send_all_menu,
                "0": self.quit,
                }

    def main_prompt(self):
        """Return a prompt str for the main menu."""
        return ("\nMain Menu\n"
                "\n1 - Send a Thank You\n"
                "2 - Create a Report\n"
                "3 - Send letters to everyone\n"
                "0 - Quit\n"
                ">> "
                )

    def quit(self):
        """Provide an exit option for menus."""
        return "exit menu"

    def send_all_menu(self):
        """Initiate the send-all-letters sub-sub-menu."""
        self.menu_selection(self.write_file_prompt(),
                            self.write_file_dispatch())

    def send_thank_you_interaction(self):
        """Initiate the send-thank-you sub-menu."""
        self.menu_selection(self.send_thanks_prompt(),
                            self.send_thanks_dispatch()
                            )

    def menu_selection(self, prompt, dispatch_dict):
        """Provide a template for using dispatch dicts to go through menus."""
        while True:
            response = input(prompt)
            try:
                if dispatch_dict[response]() == "exit menu":
                    break
            except KeyError:
                print("\nInvalid choice. Try again")

    # PRINT ON SREEN A THANK YOU LETTER TO SOMEONE WHO JUST MADE A DONATION
    def input_donation(self, name):
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
                    if name in donors:
                        donors.get_donor(name).add_donation(donation_amount)
                    else:
                        donors.append(SingleDonor(name, donation_amount))
                    return True

    def old_donor_interaction(self):
        """Call any_donor() for the old donor functionality."""
        self.any_donor()

    def new_donor_interaction(self):
        """Call any_donor() for the new donor functionality."""
        self.any_donor(old=False)

    def any_donor(self, old=True):
        """Ask for donor name, donation amount, print a thank-you email."""
        prompt_name = "Type the donor's full name or 0 to abort > "
        if old:
            name = ""
            while name not in donors:
                name = input(prompt_name)
                if name == "0":
                    return
        else:
            name = input(prompt_name)
            if name == "0":
                return

        if self.input_donation(name):
            print(self.get_email(name,
                                 donors.get_donor(name).get_last_donation()
                                 )
                  )

    #  WRITE ALL LETTERS TO FILES
    def get_full_path(self, destination, name):
        """Construct a full path including date and name."""
        date = str(datetime.date.today())
        filename = "{}-{}.txt".format(date, name)
        path = os.path.join(destination, filename)
        return path

    def write_file(self, destination, text):
        """Write text to destination path."""
        with open(destination, "w") as toF:
            toF.write(text)

    def write_cwd(self):
        """Write all emails to the current working directory."""
        cwd = os.getcwd()
        for name in donors:
            text = self.get_email(name,
                                  donors.get_donor(name).get_last_donation()
                                  )
            self.write_file(self.get_full_path(cwd, name), text)

        print("\nAll letters saved in {}\n".format(cwd))

    def ask_user_dir(self):
        """Get a directory from the user."""
        root = tk.Tk()
        root.withdraw()
        return filedialog.askdirectory()

    def write_select_dir(self):
        """Write all emails to a dir selected by the user."""
        target_dir = self.ask_user_dir()
        if not target_dir:  # If the user hits cancel.
            return
        for name in donors:
            text = self.get_email(name, donors.get_donor(name).get_last_donation())
            self.write_file(self.get_full_path(target_dir, name), text)

        print("\nAll letters saved in {}\n".format(target_dir))

# Load data and run
if __name__ == "__main__":
    donors = Donors([SingleDonor(name, data[name]) for name in data])
    s = StartMenu(donors)
