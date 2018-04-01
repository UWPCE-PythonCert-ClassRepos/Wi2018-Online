#!/usr/bin/env python3
import sys


class Donor(object):
    """ Class that defines a Donor"""
    def __init__(self, name, donation):
        """ Instantiate new donor with name and list of donations"""
        self.name = name
        self.donations = donation

    def add_donation(self, name, donation):
        """ Add a new donation amount to existing list"""
        self.donations += [donation]

    def total_donation_amt(self):
        """ Total amount donated by the donor """
        return sum(self.donations)

    def number_of_donations(self):
        """ Return the number of donations """
        return len(self.donations)


class MailRoom(object):
    def __init__(self):
        """ Build a list of donors to start with """
        self.donor_dict= {"William Gates III": Donor('William Gates III',
                            [22000, 653784.49]),
                           'Mark Zuckerberg': Donor('Mark Zuckerberg',
                               [2500, 16396.10]),
                           'Jeff Bezos': Donor('Jeff Bezos', [800, 877.33]),
                           'Larry Page': Donor('Larry Page',
                               [1, 20000, 40000, 90000]),
                           'Steve Jobs': Donor('Steve Jobs', [30000, 30000])
                        }

    def add_donor(self, name, donation):
        """ Add a new donor. Create a Donor object and the donor to the list"""
        new_donor = Donor(name, donation)
        self.donor_dict[name] = new_donor

    def is_a_donor(self, name):
        """
        Return True if the name the user entered is already in our donor
        list
        """
        return name in self.donor_dict

    def get_donor_names(self):
        """ Return donor names"""
        return self.donor_dict.keys()

    def create_report(self):
        """
        Print a summary of all donors, their donations, number of
        donations.
        """
        print("{:25s}|{:15s}|{:12s}|{:15s}".format("Donor Name", "Total Given",
                                                   "Num Gifts",
                                                   "Average Gift"))
        print("-" * 70)
        for donor in self.donor_dict:
            total_donation = self.donor_dict[donor].total_donation_amt()
            num_gifts = self.donor_dict[donor].number_of_donations()
            average_gift = total_donation / num_gifts
            print("{:25s}${:13.2f} {:12d}  ${:13.2f}".format(donor,
                                                             total_donation,
                                                             num_gifts,
                                                             average_gift))

    def print_thank_you(self, donor, write_to_file=0):
        """ Function to print Thank You note taking the donor name as input """
        notes_text = "Dear {},\nThank you very much for your recent donation" \
                     " to XYZ Charity for an amount of {}. \n" \
                     "The funds raised will go towards X, Y and Z. Thank You" \
                     "again for your kindness.\nSincerely,\nThe Team\n". \
            format(donor, self.donor_dict[donor].total_donation_amt())
        if not write_to_file:
            print(notes_text)
        return notes_text

    def send_thankyou_to_all_donors(self):
        """
        Create a text file with the name of the donor. The text in the file is
        the thank you note to that donor
        :return:
        """
        for donor in self.donor_dict:
            file_name = "_".join(donor.split()) + '.txt'
            with open(file_name, 'w') as fd:
                fd.write(self.print_thank_you(donor, write_to_file=1))

    def send_thank_you(self):
        """
        Function to get print thank you note based on donor name.
        :return:
        """
        name = input("Enter the full name of the donor:")
        if name.lower() == 'main menu':
            return
        else:
            if name == 'list':
                print(self.get_donor_names())
                self.send_thank_you()
            elif name not in self.get_donor_names():
                # New donor, get his info and print thank you note
                amount = float(input("New Donor. Enter the donation amount:"))
                donor = Donor(name, [amount])
                self.donor_dict[name] = donor
                self.print_thank_you(name)
            elif name in self.get_donor_names():
                self.print_thank_you(name)


def main_menu():
    """ Main Menu of the program """
    print("Choose from one of the following options: At any point enter "
          "main menu to return to main menu")
    print("1. Send a Thank You Note")
    print("2. Create a Report")
    print("3. Send Thank You Note to all Donors")
    print("4. Quit")

if __name__ == '__main__':
    """ Get input from user and call the respective functions """

    mailroom_obj = MailRoom()
    option_dict = {1: mailroom_obj.send_thank_you,
                   2: mailroom_obj.create_report,
                   3: mailroom_obj.send_thankyou_to_all_donors,
                   4: sys.exit}

    while True:
        main_menu()
        option_chosen = int(input("Choose from one of the following: "))
        option_dict.get(option_chosen)()



