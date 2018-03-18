#!/usr/bin/env python3
"""Contribution Mail Room"""
"""Data structure that holds a list of your donors and a history of the amounts they have donated"""


def contributors() -> object:
    contributor_list = [('Ken','Murray','10.00'),('Ken','Murray','4.00'),('Tew','Tangsuk','2.68'),('Joe','joe','550'),('Tina','Tangsuk','2902'),('Tew','Tangsuk','26568'),('Nathan','Merrill','2000'),('Joe','joe','5789'),('Tew','Tangsuk','78268')]
    return contributor_list
#def user_contibution_record(first_name, last_name, donation_amount):


#'${:,.2f}'.format(float(tup[2]))












if __name__ == '__main__':
    contributor_list = contributors()
    response = input("Hello, please select what you would like to do: (1)Thank a donor (2)Create a report (3)Quit > ")  #user will pick the activity
    if int(response) == int(1):
        name_list = input('Please type the name of a donor or type \"list\" to see a list of donors.  > ')
        if not name_list == "list":
            #do stuff here
            print(contributor_list)
        else:
            names_of_donors = ()
            for name in contibutor_list:
                names_of_donors.__add__(name[0]+" "+name[1])
            print(names_of_donors)
#                    '''Send a Thank You”, “Create a Report” or “quit'''

#                    '''Send a Thank You'''
                     # If the user types ‘list’, show them a list of the donor names and re-prompt

                     # If the user types a name not in the list, add that name to the data structure and use it.
                     # If the user types a name in the list, use it.
                     # Once a name has been selected, prompt for a donation amount.
                     # Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
                     # Once an amount has been given, add that amount to the donation history of the selected user.
                     # compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

#                     '''Create a Report'''
#print a list of your donors, sorted by total historical donation amount.
#Include Donor Name, total donated, number of donations and average donation
#After printing this report, return to the original prompt.
#At any point, the user should be able to quit their current task and return to the original prompt.
#From the original prompt, the user should be able to quit the script cleanly.

