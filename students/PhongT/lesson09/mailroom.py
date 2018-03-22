"""
Lesson 09 Assignment - Object Oriented Mailroom
Refactor the mailroom program using classes to help organize the code.
Uses an OO approach to better structure the code to make it more extensible.
"""
import sys


class Donor:
    """
    Keep track of individual donors and history of donations
    This includes attributes and methods to provide access
    to the donor specific information that is needed.
    """
    def __init__(self, name, donations=None):
        """
        init Donor object
        :param name: Donor's name
        :param donations: donation amount items
        """
        self.name = name
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    @property
    def count_donations(self):
        return len(self.donations)

    @property
    def total_donations(self):
        """ get Sum property  of all existing donations """
        return sum(self.donations)

    @property
    def average_donations(self):
        """ get Average property  of all existing donations """
        return self.total_donations / len(self.donations)
        try:
            avg = self.total_donations / len(self.donations)
        except ZeroDivisionError as e:
            avg = None
            print("\n{} - No donation found!".format(e))
        finally:
            return avg

    @property
    def latest_donation(self):
        """ get Latest donation amount property """
        try:
            donation = self.donations[-1]
        except IndexError as e:
            donation = None
            print("\n{} - Invalid donation!".format(e))
        finally:
            return donation

    def add_donation(self, amount):
        """ Add new donation amount to existing donations """
        try:
            if amount <= 0.0:
                raise ValueError("Can't add donation amount <= 0.0!")
        except ValueError as e:
            print("\n{} - Invalid donation amount!".format(e))
        finally:
            self.donations.append(amount)


class DonorDB(object):
    """ Collection of Donor objects and their property/attribute """

    def __init__(self):
        self.donors_container = []

    def get_donor(self, name):
        for donor in self.donors_container:
            if donor == name:
                return donor
        d = Donor(name)
        return d

    def add_donor(self, name, amount):
        """
        Add donor to donor collection
        :param name: donor's name
        :param amount: donation amount
        :return: the new added donor
        """
        donor = self.find_donor(name)
        if donor:  # add amount to existing donor record
            donor.add_donation(amount)
        else:      # add name, amount to a new donor record
            donor = Donor(name)
            donor.add_donation(amount)
            self.donors_container.append(donor)
        return donor

    def find_donor(self, name):
        """
        Find whether or not the input donor is in the db.
        :param name: the donor to search for in donor db
        :return: donor if there is existing one in db. Otherwise return None
        """
        for donor in self.donors_container:
            if donor.name == name:
                return donor
        return None

    def get_thankyou_message(self, donor):
        """ generate a formatted thank you letter message"""
        message = '''Dear {}, 
                Thank you so much for your generosity with your most recent donation of ${}. 
                It will be put to very good use.
                Sincerely.'''
        return message.format(donor.name, donor.latest_donation)

    def print_donor_list(self):
        """ print out list of current donors"""
        print('Below are the existing donors: ')
        for donor in self.donors_container:
            print('\t- ', donor.name, ' ', donor.donations)

    def print_report(self):
        """ print a list of your donors, sorted by total historical donation amount. """
        width = 68
        dash = "-" * width
        print(dash)
        header = ("Donor Name", "Total Given", "Num Gifts", "Average Gift")
        print("{:20} | {:15} | {:10} | {:12}".format(*header))
        print(dash)
        for donor in self.donors_container:
            name = donor.name
            total = donor.total_donations
            num_gift = donor.count_donations
            average = total/num_gift
            print("{:22} ${:12,.2f} {:12d}     ${:12,.2f}".format(name, total, num_gift, average ))
        print(dash)

    def write_letters_to_file(self):
        """
        goes through all the donors in donor data structure, generates a thank you
        letter, and writes it to disk as a text file.
        :return: n/a
        """
        for donor in self.donors_container:
            message = self.get_thankyou_message(donor)
            filename = donor.name.replace(" ", "_") + ".rpt"
            with open(filename, 'w') as outfile:
                outfile.write(message)


# function for main loop transaction.......
donors_data = DonorDB()


def print_thank_you():
    """ Add or Update a donor record, then print a Thank You letter """
    while True:
        print()
        response = input(''' sub_menu --- Donation Entries ---
        Type your Full Name,
        or 'list' to display list of the donor names,
        or 'quit' to quit and return to main program prompt.
        Enter your choice here: > ''')

        if response.lower().strip() in ["q", "quit"]:
            break
        elif response.lower().strip() in ["l", "list"]:
            donors_data.print_donor_list()
            continue
        else:

            amount = input("Enter Donation amount: ")
            try:
                donate_amount = float(amount)
            except ValueError as e:
                print("{} - The donation amount must be numeric!".format(e))
            else:  # nothing went wrong: add or update a record
                donor_to_print = donors_data.add_donor(response, donate_amount)

                # now print a thank you letter
                print(donors_data.get_thankyou_message(donor_to_print))


def exit():
    sys.exit(0)


def print_report():
    donors_data.print_report()


def write_letters_to_file():
    donors_data.write_letters_to_file()


def main_menu():
    menu_dict = {"1": print_thank_you,
                "2": print_report,
                "3": write_letters_to_file,
                "4": exit}
    while True:
        print()
        answer = str(input('''Please choose from one of the following options:
        (1) Send a Thank You
        (2) Create a Report
        (3) Send letters to everyone
        (4) Exit
        Enter your choice here: > '''))
        try:
            menu_dict[answer]()
        except KeyError as e:
            print("\n{} - Invalid input! Please type 1, 2, 3, or 4".format(e))


if __name__ == '__main__':
    main_menu()


