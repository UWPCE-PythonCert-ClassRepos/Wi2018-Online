#!/usr/bin/env python3

from pathlib import Path
from random import randint
import sys


class Donor(object):

    def __init__(self, dictionary):
        self.__dict__ = dictionary

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return ', '.join(self.__dict__.keys())

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def append(self, key, value):
        self.__setitem__(key, value)


class Menu:

    def __init__(self):

        self.mail = MailRoom()

        # Use dictionary to create quasi switch/case structure
        self.choices = {"1": self.mail.show,
                        "2": self.mail.give_report,
                        "3": self.mail.add_donor,
                        "4": self.mail.send_letter,
                        "q": self.end_menu}

    def display_menu(self):
        """
        Function main drives the Donor program. It first prompts the user for a selection to pass to the
        correlated method.The program will end when the user selects the quit method
        """
        print("""
        Welcome to the MailRoom Donor Program!
        What would you like to do?
        Type 1 - To display donors'
        Type 2 - To generate a report'
        Type 3 - To add new donor'
        Type 4 - To send letters to donors'
        Type q - To end the program'
        """)

    def end_menu(self):
        print("Shutting down program, Goodbye", end='\n')
        sys.exit(0)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter value here >> ")
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print(f'{choice} is not a valid choice')


class MailRoom:

    patrons = {'Emma Watson': [50.00, 150.00, 2000.00, 3000.00],
               'Carolyn Wilson': [5000.25, 2500.00],
               'Andres Dominguez': [5015.00, 200.50, 35.50]}

    donors = Donor(patrons)

    def show(self):
        print('Showing list of patrons in the database:\n')
        print(self.donors.keys())

    def give_report(self):
        header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        print('{:25} |{:^15} |{:^15} |{:^15}'.format(*header))
        print('-' * 75)
        # Uses composition from Donor class
        print(''.join({f"{k:<30} ${sum(v):^,.2f}  {len(v):^20}  ${sum(v)/len(v):,.2f}\n"
                       for (k, v) in self.donors.items()}))
        print('-- Report Finished --\n')

        # Method to send letters
    def send_email(self, name, amount):
        print(f"Thank you {name} for your generous ${amount:,.2f} donation")
        print('-- Email Sent --\n')

    def add_donor(self):
        # donor menu used to help validate choices
        values = ['N', 'n', 'No', 'NO']

        while True:
            choice = input("""
            Would you like to add a new donor, Yes or No?
            Enter value here >>  """)
            if choice in values:
                break
            else:
                first, last = input("\nPlease enter the new Donor's First and Last name:  ").split()
                name = f'{first} {last}'.title()

            if name in self.donors.keys():
                print("Donor's name already exists")
                continue
            else:
                self.donors[name] = []
                try:
                    amount = float(input('Please enter a donation amount: '))
                except ValueError:
                    print("The donation must be numeric like 1234.00")
                    # remove user's entry and start at top of menu
                else:
                    self.donors.append(name, amount)
                    self.send_email(name, amount)

    def send_letter(self):
            count = 0
            cwd = Path.cwd()
            for key, value in self.donors.items():
                pth = cwd / f'{key}.txt'
                if pth.exists():
                    print(f'{key}.txt file Already Exists....\nCreating new file....\n')
                    pth = cwd / f'{key}{randint(0,99)}.txt'

                text = """
                                            Dear {},

                                                   Thank you for you donation of ${:,.2f}

                                                   It will be put to good use

                                                                    Sincerely,
                                                                        -The Team""".format(key, sum(value))
                pth.write_text(text)
                count = count + 1

            print(f'{count} letters created\n')
            print(f'Letters located in {cwd}')














