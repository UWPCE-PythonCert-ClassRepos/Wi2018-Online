#!/usr/bin/env python3
# -----------------------------------------------------------
# mailroom.py
#  Script to automate writing thank you emails to donors.
# -----------------------------------------------------------

import time


class Donors(object):

    def __init__(self):
        self.donorlist = []

    def add_donor(self, donor):
        self.donorlist.append(donor)

    def print_report(self):
        """
        Prints a formatted report on the donors with name, amount given, number of gifts, and average gift.
        :return: None
        """
        # Find longest name in donor list, or use name_min value
        name_max = max(*[len(donor.name) for donor in self.donorlist], 25)

        rpt_title = "Donor Name" + ' ' * (name_max - 9) + "| Total Given | Num Gifts | Average Gift"
        print(rpt_title)
        print("-" * len(rpt_title))
        for donor in self.donorlist:
            print(f"{donor.name:{name_max}}  ", end='')
            ddons = donor.donations
            print(f"$ {sum(ddons):>10.2f}   {len(ddons):>9}  ${sum(ddons)/len(ddons):>12.2f}")

    def send_letters_all(self):
        """
            Runs through donor data structure, generates a thank you letter for each and saves it to
            the current working directory with in a date+donorname.txt file
            :return: None
            """
        for donor in self.donorlist:
            print(f'Generating letter for {donor.name}')
            now = time.localtime()
            f_name = f"{now.tm_year}{now.tm_mon:02}{now.tm_mday:02}_"
            f_name += donor.name.replace(" ", "_") + ".txt"
            with open(f_name, 'w') as file_out:
                file_out.write(donor.generate_letter())
        return None


class Donor(object):

    def __init__(self, name):
        if not name:
            raise ValueError("Donor name cannot be empty.")
        self.name = name
        self.donations = []

    @property
    def first(self):
        name_sp = self.name.split()
        if len(name_sp) == 1:
            return None
        else:
            return name_sp[0]

    @property
    def last(self):
        name_sp = self.name.split()
        if len(name_sp) == 1:
            return self.name
        else:
            return ' '.join(name_sp[1:])

    def add_donation(self, amount):
        if float(amount) <= 0:
            raise ValueError('Donation amount must be a positive number.')
        else:
            self.donations.append(amount)

    def generate_letter(self):
        """
        Generates a Thank You letter to send to a donor. Uses the last value in their donations list to
        mention their last donation amount.
        :param donor: a donor dictionary entry
        :return: string containing the text of the Thank You letter.
        """
        format_string = """
Dear {first_name} {last_name},

   Thank you for your donation of ${last_donation:.2f}.

            Warmest Regards,
                Local Charity
"""
        amount = self.donations[-1]
        return format_string.format(last_donation=float(amount), first_name=self.first, last_name=self.last)












def send_thank_you():
    """
    Prompts for donor name, if not present, adds user to data. Prompts for donation
    and adds it to donor's data. Prints a 'Thank You' email populated with the donor's data.
    :return: None
    """

    while True:
        name = input("Enter a Full Name ('list' to show list of donors, 'q' to quit): ")
        if name == 'q':
            return
        elif name == 'list':
            print(("{}\n" * len(donor_data)).format(*([get_donor_fullname(d) for d in donor_data])))
            continue
        else:
            donor = get_donor(name)
            if not donor:
                print("Name cannot be empty.")
                continue
            else:
                break

    while True:
        try:
            amount = input("Enter a donation amount for {} : ".format(get_donor_fullname(donor)))
            if float(amount) <= 0:
                print('Amount donated must be a positive number.')
            else:
                break
        except ValueError:
            print('Please enter a numerical value.')

    donor_data[donor].append(float(amount))
    print(generate_letter(donor))


def menu(menu_data):
    """
    Prints the main user menu & retrieves user selection.
    :param: a menu list, consisting of tuples with two values:
        [0]: text to be presented to user
        [1]: function that should be called for the menu item
    :return: the function corresponding to the user's selection, or None on a bad selection
        raises ValueError if choice is non-numeric
    """
    print("\nPlease choose one of the following options:")

    for index, menu_item in enumerate(menu_data):   # Prints the menu user text
        print(f"{index + 1}) {menu_item[0]}")

    choice = int(input("> ")) - 1

    if choice in range(len(menu_data)):             # Ensure that option chosen is within menu range
        return menu_data[choice][1]                 # this handles choosing 0, which would return menu_data[-1][1]

    return None



if __name__ == "__main__":

    # Global data structure
    donor_data = (
        ('Al Donor1', [10.00, 20.00, 30.00, 40.00, 50.00]),
        ('Bert Donor2' ,[10.00]),
        ('Connie Donor3', [10.00, 10.00, 10.01]),
        ('Dennis Donor4', [10.00, 20.00, 20.00]),
        ('Egbert Donor5', [10.39, 20.21, 10.59, 4000.40])
    )

    dl = Donors()
    for name, dons in donor_data:
        n = Donor(name)
        dl.add_donor(n)
        for d in dons:
            n.donations.append(d)

    dl.print_report()

    menu_functions = [
        ('Send a Thank You', send_thank_you),
        ('Print a report', dl.print_report),
        ('Send letters to everyone', dl.send_letters_all),
        ('Quit', quit),
    ]
    while True:
        try:
            menu(menu_functions)()
        except TypeError:
            continue
        except ValueError:
            continue
