#!/usr/bin/env python3

import sys

# Define and global variables and constants
donors = {'Jimmy Nguyen': [100, 1350, 55],
          'Steve Smith': [213, 550, 435],
          'Julia Norton': [1500, 1500, 1500],
          'Ed Johnson': [150],
          'Elizabeth McBath': [10000, 1200]
          }


class Donor(object):
    """
    Hold all the donor objects, amd also methods to add a new donor,
    search for a given donor, etc...
    """

    # def __init__(self):
    #     """Initializes the Donor object with a given name and list of donations."""
    #     self.name = name

    def show_donor_names(self):
        """Shows a listing of the current donors. For use when listing out current donors."""
        donor_names = []
        for k in donors.keys():
            donor_names.append(k)
        return donor_names

    def donor_lookup(full_name):
        """Search the dictionary keys and look for a donor by their full name."""
        donor = full_name.strip()
        for k in donors.keys():
            if donor in donors:
                return donor
            else:
                return None

    def add_new_donor(full_name):
        """Adds a new donor to the donor dictionary."""
        full_name = full_name.strip()
        new_donor = (full_name, [])
        donors[full_name] = new_donor
        return new_donor

    def create_donor_report(self):
        """Create a report of the donors and donation amounts."""
        donations = []

        print("{:26s} | {:13s} | {:9s} | {:13s}".format("Donor name", "Total Donation", "Number of Gifts",
                                                        "Average Gifts"))
        print("-" * 80)

        for donor, gift in donors.items():
            total_given = sum(gift)
            number_gifts = len(gift)
            average_gift = total_given / number_gifts
            donations.append((donor, total_given, number_gifts, average_gift))

        for amount in donations:
            print("{:26s} | {:14.2f} | {:15d} | {:13.2f}".format(*amount))
        print()

    def letter_template(self, donor):
        """Template for writing a letter to a donor, thanking them for their donation."""
        return """Dear {},\nThank you for your very kind donation of {:.2f}.\n\nIt will be put to very good use.\n\n \t\tSincerely,\n\t\t\t-The Team""".format(
            donor, donors[donor][-1])

    def send_letter_file(self):
        """Write a thank you letter and save to file."""
        for k, v in donors.items():
            file_name = k + '.txt'
            text = self.letter_template(k)
            with open(file_name, 'w') as f:
                f.write(text)

        print('Completed creating letters to send out to donors.')


def thank_you():
    """Function for Thank you. Prompts for a donors name."""
    while True:
        full_name = input(
            "Please enter a donor's name or type 'list' for list of donors ('menu' to return to menu): ").strip()

        if full_name == 'list':
            print('Below is the current donor list:')
            donor = Donor.show_donor_names(donors)
            for i in donor:
                print(i)
            print()
        elif full_name == 'menu':
            return
        else:
            break

    # Enter a donation amount
    while True:
        try:
            donation = int(input("Please enter a donation amount. 'menu' to return to original menu: "))
            if donation == 'menu':
                return
            else:
                break
        except ValueError:
            print('Please enter a valid amount.')

    # Enter a new donor
    donor = Donor.add_new_donor(full_name)
    if donor is None:
        donor = full_name
        donors[donor] = []

    donors[donor].append(donation)

    print(Donor.letter_template(donor_obj, donor))


def print_header():
    """Prints the menu items to choose from and returns the selection."""
    print('------------------------------------------')
    print('       Donation Management System')
    print('                 v0.1.5\n')
    print('       1: Send A Thank You')
    print('       2: Create A Report')
    print('       3: Send Letters To Everyone')
    print('       4: Quit\n')
    print('------------------------------------------\n')

    try:
        selection = int(input('Please select a menu item: '))
    except ValueError:
        print('Your selection is invalid. Please make a selection from the menu.')
        selection = int(input('Please select a menu item: '))

    return selection


def main():
    """Main mneu of the program."""
    while True:
        try:
            menu_selection[print_header()]()
        except KeyError:
            print('Your selection did not match any item in the menu. Please make another selection.')
            continue


if __name__ == '__main__':
    donor_obj = Donor()
    menu_selection = {
        1: thank_you,
        2: donor_obj.create_donor_report,
        3: donor_obj.send_letter_file,
        4: sys.exit
    }
    main()
