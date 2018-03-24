#!/usr/local/python3

import sys

#Initial Donors List
donors = {'Aron': [10000,300, 100], 'Joan':[100, 50, 65], 'Jean':[30,150], 'Scott':[200]}

#Thank You Functionality
##If the user types ‘list’, show them a list of the donor names and re-prompt
##If the user types a name not in the list, add that name to the data structure and use it.
##If the user types a name in the list, use it.
##Once a name has been selected, prompt for a donation amount.
##Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
##Once an amount has been given, add that amount to the donation history of the selected user.
##Compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

#creation of seperator
def seperator(str):
    # return line that equals string length ignoring newline.
    return "-" * (len(str) - str.count('\n'))

#Summary of donor giving
summary=[]
def donor_sum():
    #summary=[]
    #donor_summary={}
    for donor in donors:
        summary.append(sum(donors[donor]))
    #    donor_summary.append([donor](summary))
    return summary
    #return donor_summary

#list of donor names
names=[]
def donor_names():
    for donor in donors:
        names.append(donor)

def list_check():
    global y
    while True:
        x=input("Check user name: ")
        if x in names:
            print("We have a match")
        else:
            y = input("No match, adding to list. Please enter donation amount ")
        donors.update({x:y})

donor_list = donor_names() # create a list of names only

def send_thank_you():
    while True:
        response = input("Enter the name of a donor "
                         "('list' -> list of donors | 'main' -> "
                         "main menu)\n")
        try:
            if response == 'list':
                print("Existing donors - "+(str(donors)))
            elif response == 'main':
                init()
            elif response in donor_names:  # i.e. existing donor
                add_donation(response, exsting_donor=True)
                break
        except TypeError:
            print('Wrong choice, try again')
            continue
    init()

#Zip or donor names and summary dontations to one file
donor_data = []
donor_data = donor_sum()
donor_result = dict(zip(names, donor_data))

def create_report():
    heading = "Donor Name | Total Gifts | Num Gifts | Average\n"
    print(heading + seperator(heading))
    for k, v in donors.items():
        print("{:10} ${:10.2f}{:10}${:15.2f}".format(k, sum(v), len(v), (sum(v)/len(v))))
    init()

#donor_summary=dict(zip(names, summary))

def create_email():
    for k, v in donor_result.items():
        email_text=open(k+"final.txt", 'w')
        email_text.write('Dear '+k+',\n\nYour gift of $'+str(v)+' is greatly appreciated.\n\nSincerely,\nAron')
        email_text.close()
    init()

def exit():
    sys.exit()
    print('\n**exiting**')
    init()

def init():
    while True:
        heading = "Main Menu"
        print(heading)
        choice = input("1 - Check list for name\n" "2 - See list of donors\n" "3 - Create a Report\n" "4 - Create email to file\n" "5 - Quit\n")
        if choice == '1':
            list_check()
            break
        if choice == '2':
            send_thank_you()
            break
        elif choice == '3':
            create_report()
            break
        elif choice =='4':
            create_email()
            break
        elif choice == '5':
            exit()
            break



if __name__ == "__main__":
    init()
