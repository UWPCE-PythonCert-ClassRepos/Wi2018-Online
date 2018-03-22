#!/usr/bin/env python3
import datetime

"""Contribution Mail Room"""
"""Data structure that holds a list of your donors and a history of the amounts they have donated"""

contributor_list = [('Ken','Murray','10.00', '4.00'),('Tew','Tangsuk','2.68','78268','265.68'),('Joe','joe','5.50','57.89'),('Tina','Tangsuk','29.02'),('Nathan','Merrill','20.00')]


def donor_list():
    """Returns a list of donors sorted by first name"""
    names_of_donors = []
    for name in contributor_list:
        names_of_donors.append(name[0]+" "+name[1])
    return names_of_donors

def add_donor(name):
    """Adds a first and last name to the list"""
    contributor_list.append(tuple(name.split(" ")))
    return contributor_list

def is_donor(check_name):
    """Return true or false"""
    names_of_donors = []
    for name in contributor_list:
        names_of_donors.append(name[0]+" "+name[1])
    for fullname in names_of_donors:
        if fullname.casefold() == check_name.casefold():
            return "true"


def new_donation(donation,donor_name):
    """Adds a new donation to the contribution list"""
    fullname = tuple(donor_name.split(" "))
    firstname = fullname[0]
    lastname = fullname[1]
    counter = 0
    while counter <= len(contributor_list) - 1:
        if (contributor_list[counter])[0] == firstname and (contributor_list[counter])[1] == lastname:
            index = counter
            contributor_list[index] = contributor_list[index] + (str(donation),)
        counter = counter + 1


def thankyou_email(donation,donor_name):
    print(f"Dear {donor_name}:")
    print()
    print()
    print(f"Thank you for your donation of ${donation}. Your gift is greatly appreciated.")
    print(f"Your generosity and thoughtfulness means so much to all of us.")
    print()
    print()
    print("Sincerely,")
    print("Kenneth Murray")


def print_report():
    print()
    print()
    print('{:25} |  {:12} |   {:12} | {:13}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print("-" * 65)
    index = 0
    for donor_report in contributor_list:
        report_fullname = donor_report[0] + " " + donor_report[1]
        report_num_gifts = int(len(donor_report) - 2)
        report_total_given = '{:,.2f}'.format(float(donor_report[2]))
        if report_num_gifts > 1:
            given_counter = 3
            while given_counter < len(donor_report):
                report_total_given = float("{:.2f}".format(float(report_total_given))) + float("{:.2f}".format(float(donor_report[given_counter])))
                given_counter = given_counter + 1
        report_average = float(report_total_given) / int(report_num_gifts)
        report_average = "{:.2f}".format(report_average)
        report_total_given = "{:.2f}".format(float(report_total_given))
        print(f'{report_fullname:25} | $ {report_total_given:12} |  {report_num_gifts:12} | $ {report_average:13}')
        index = index + 1
    print()
    print()




if __name__ == '__main__':
    begin = 0
    while begin == 0:
        '''Send a Thank You”, “Create a Report” or “quit'''
        response = input("Hello, please select what you would like to do: (1)Thank a donor (2)Create a report. Type exit at any time to end the program. > ")  #user will pick the activity
        if response.lower() == "exit":
            exit()
        if int(response) == int(1):
            name_list = input('To see a list of names please type \"list\" or press enter to continue.  > ')  # If the user types ‘list’, show them a list of the donor names and re-prompt
            if name_list.lower() == "list":
                names_of_donors=donor_list()
                names_of_donors.sort()
                print(names_of_donors)
            response_donor_name = input('Please enter the FIRST and LAST name of a new or existing donor  > ')
            if not is_donor(response_donor_name) == "true":  # If the user types a name not in the list, add that name to the data structure and use it.
                add_donor(response_donor_name)
            response_new_donation = input(f'what is the amount that {response_donor_name} would like to donate?  > ')  # Once a name has been selected, prompt for a donation amount.
            donation_amount = '{:,.2f}'.format(float(response_new_donation))  # Turn the amount into a number
            donor_new_list = new_donation(donation_amount,response_donor_name)
            print(f'I have recorded a donation in the amount of ${donation_amount}')
            thankyou_email(donation_amount,response_donor_name)  # compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
            begin = 1
        if int(response) == int(2):  #Create a Report
            print_report()
            begin = 1


