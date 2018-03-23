#!/usr/bin/env python3
#
# Assignment: Mailroom, Part 2
# Chay Casso
# 2/11/2018

import collections

# Initial donor table with the donation values.
donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                    "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21], "Steve Ballmer": [5198.96, 654.98]}
answer = ""


def thank_you(thank_you_dict):
    while True:
        full_name = input("Please enter a full name. >")
        if full_name.lower() == "quit": return(thank_you_dict)
        if full_name.lower() == "list":
            print("Donor list:")
            print(list(thank_you_dict.keys()))
        else:
            donation_value_str = input("Please enter a donation amount. >")
            if donation_value_str.lower() == "quit": return(thank_you_dict)
            try:
                donation_value_flt = float(donation_value_str)
                if full_name in thank_you_dict:
                    thank_you_dict[full_name].append(donation_value_flt)
                else:
                    thank_you_dict[full_name]=[]
                    thank_you_dict[full_name].append(donation_value_flt)
                print()
                print("\nDear {}:\n\n\tThank you for your generous donation of ${} to Save the Kids.\n\n-------------\n"
                      "Save the Kids\nsave@kids.org\n".format(full_name, donation_value_flt))
                return(thank_you_dict)
            except:
                print("Not entered. Please enter a numeric value for the donation amount.")


def sum(input_table):
    result = 0
    for i in input_table:
        result = result + i
    return result


def create_report(create_report_dict):
    print("{:<20} | {:<10} | {:<10} | {:<10}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("----------------------------------------------------------------------------")
    order_dict = collections.OrderedDict(sorted(create_report_dict.items()))
    for key in order_dict:
        print("{:<20}   ${:>10.2f}   {:>10d}   ${:>10.2f}".format(key, sum(order_dict[key]), len(order_dict[key]),
                                                             sum(order_dict[key]) / len(order_dict[key])))


def send_letters(send_letters_dict):
    for key in send_letters_dict:
        with open(key + ".txt", "w") as writefile:
            letter = "\nDear {}:\n\n\tThank you for your recent donation of ${} to Save the Kids.\nWe are grateful " \
                     "for your total donations of ${} to our organization.\n\n-------------\nSave the Kids\n" \
                     "save@kids.org\n".format(key, send_letters_dict[key][-1], sum(send_letters_dict[key]))
            writefile.write(letter)
    print("Letters have been created.\n")


# Main menu
if __name__ == "__main__":
    while True:
        print("Main Menu\n1. Send a Thank You\n2. Create a Report\n3. Send Letters to All\n4. Quit")
        answer_dict = {"1": thank_you,
                       "2": create_report,
                       "3": send_letters,
                       "4": "quit"}
        answer = input("Please select an option. >")
        if answer == "4":
            print("Have a nice day.")
            break
        else:
            answer_dict[answer](donor_table_dict)