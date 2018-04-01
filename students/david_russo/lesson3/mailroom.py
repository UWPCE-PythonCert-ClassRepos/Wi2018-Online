#!/usr/bin/env python
from sys import exit

donors = [["Walter White", "Ray Donovan", "John Snow", "Walter White", "Ray Donovan", "John Snow", "Walter White", "Ray Donovan", "John Snow", "Walter White", "Ray Donovan", "John Snow", "Walter White", "Ray Donovan", "John Snow"],
          [10000, 2500, 10, 15000, 6500, 5, 20000, 10500, 3, 25000, 15000, 2, 30000, 19500, 1]]

# define a function to prompt the user for their desired action
def prompt_user():
    print("What would you like to do? Your options are: 1) Send a Thank You, 2) Create a Report, 3) quit")
    response = input("Please type your selection > ")
    while(response not in ("Send a Thank You", "Create a Report", "quit")):
        print("Please enter one of 'Send a Thank You', 'Create a Report', or 'quit' > ")
        response = input("Please type your selection > ")
    return response

# define a function to send a thank you card
def send_a_thank_you():
    unique_donors = list(set(donors[0]))
    print("You selected Send a Thank You.")
    donor = input("To whom would you like to send a thank you? > ")
    # list the possible candidates within the donors list    
    if donor == "list":
        # cycle through unique names in donor list with set() function
        for names in unique_donors:
            print(names)
        donor = input("To whom would you like to send a thank you? > ")
    # prompt the user for a donation amount
    donation_amount = int(input("How much would you like to donate? > "))
    # add the donor and the donation amount to the donors list
    donors[0].append(donor)
    donors[1].append(donation_amount)
    
    print("Dear {:s}, Thank you for your generous donation of ${:.2f}.".format(donors[0][-1], donors[1][-1]),
          "Best, The Donation Foundation.")
    
    handle_response(prompt_user())
   

# define a function to create a donation report
def create_a_report():
    unique_donors = list(set(donors[0]))
    print("You selected create a report." )
    # print the header of the report 
    header_tuple = ("Donor Name", "Total Given", "Num Gifts", "Average Gift Size")
    print("{:20s} | {:10s} | {:10s} | {:15s}".format(*header_tuple))
    print("-" * 70)
    # create a tuple of name, total donation amount, numbers of gifts, and average gift size for each donor
    for donor in unique_donors:
        indices = [i for i, x in enumerate(donors[0]) if x == donor]
        donor_name = donor
        num_donations = int(len(indices))
        sum_donations = 0
        for index in indices:
            sum_donations += donors[1][index]
        mean_gift_size = sum_donations/num_donations
        donor_tuple = (donor_name, sum_donations, num_donations, mean_gift_size)
        print("{:20s} ${:10.2f}   {:10d}   ${:15.2f}".format(*donor_tuple))

    handle_response(prompt_user())
        


# define a function to quit the program
def quit_program():
    print("You selected quit. The program is quitting. ")
    exit(0)

def handle_response(user_input):
    if user_input == "Send a Thank You":
        send_a_thank_you()
    elif user_input == "Create a Report":
        create_a_report()
    elif user_input == "quit":
        quit_program()
    else:
        print("Something went wrong, the program is quitting.")
        quit_program()
    
if __name__ == '__main__':
    handle_response(prompt_user())