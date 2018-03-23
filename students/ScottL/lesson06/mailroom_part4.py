#!/usr/bin/env python3

#-------------------------------------------------#
# Title: Mailroom Part-4 Assignment
# Dev: Scott Luse
# Date: Feb 22, 2018
# ChangeLog: (Who, When, What)
#   SLuse, 02/20/2018, added try block in process_input_name
#   SLuse, 02/20/2018, removed 'return' from functions, not needed
#   SLuse, 02/20/2018, add f-string with triple quotes to create_individual_letters, line 111
#   SLuse, 02/20/2018, add dict comp to print_donors
#   SLuse, 02/27/2018, add unit tests
#-------------------------------------------------#


# -- Data --#
donor_dict = {
    'Peter Parker': [288.09, 9.01, 61288.09],
    'Iron Man': [1238.09, 8199.01, 1468.07],
    'Captain Marvel': [43188.09, 1288.09],
    'Black Widow' : [1272.09],
}

# -- Processing --#
def get_user_choice():

    print("""
    MailRoom Part2 Menu Options
    1) Send a Thank You
    2) Create a Report
    3) Send Letters To Everyone
    4) Quit Program
    """)
    user_choice = input("Which option would you like to perform? [1 to 4]: ")
    return (user_choice.strip())

def process_menu(menu_item):
    if menu_item == '1':
        send_thanks()

    elif menu_item == '2':
        format_charity_structure()

    elif menu_item == '3':
        create_individual_letters()

def send_thanks():
    while (True):
        thank_you_name = input("Please enter FULL NAME, enter 'list' for names, or 'main' for menu: ")
        if thank_you_name.lower() == "list":
            print_donors()
            print(' ')
        elif thank_you_name.lower() == "main":
            return
        else:
            process_input_name(thank_you_name)


def process_input_name (name):
    '''Ask for a donation amount and look for user input name in donor dictionary.
    If you find the name and the amount to the donor ledger and print a letter to the screen.
    If you don't find the name create a new key value pair'''
    try:
        gift_amount = int(input("Please enter $$ donation $$ amount for " + name + ":"))
        if name in donor_dict.keys():
            #We found the name so update the giving values
            original_list = donor_dict.get(name)
            original_list.append(gift_amount)
            donor_dict[name] = original_list
            thank_you_printing(name, gift_amount)
        else:
            #We didn't find the name so create a new key value pair
            donor_dict[name] = [gift_amount]
            thank_you_printing(name, gift_amount)
    except ValueError as e:
        print("\n Error: " + str(e) + " Please enter a number amount.\n ")
        process_input_name(name)

def thank_you_printing(name, amount):
    line_divider = "*" * 50
    print(f'''
    {line_divider}
    {name}
    Address
    
    Dear {name},
    Thank you for your charitable gift of ${amount}.
    {line_divider}
    ''')

def print_donors():
    comp = {key for key in donor_dict.keys()}
    print(comp)

def format_charity_structure():
    print('')
    print('{:20}{:>15}{:>10}{:>10}'.format('Donor Name', '| Total Gifts', '| Num Gifts', '| Ave Gift'))
    print('-' * 55)
    for key in donor_dict:
        donor_list = donor_dict.get(key)
        sum_values = "{:.2f}".format(sum(donor_list))
        ave_values = "{:.2f}".format(sum(donor_list) / len(donor_list))
        print('{:20}{:>15}{:>10}{:>10}'.format(key, sum_values, len(donor_list), ave_values))

def create_individual_letters():
    try:
        for key in donor_dict:
            donor_list = donor_dict.get(key)
            sum_values = "{:.2f}".format(sum(donor_list))
            key.replace(" ", "_")
            objFileName = key.replace(" ", "_") + ".txt"
            objMyFile = open(objFileName, "w")
            objMyFile.write(gen_letter_body(key, sum_values))
            objMyFile.close()
            print(objFileName + " file saved.")
    except IOError:
        print("\n" + "File error!")

def gen_letter_body(name, amount):
    # line returns and tabs not required with f-string
    report_text = (f'''Dear {name},\n\nThank you for your charitable gift of ${amount}.
    \n\tIt will be put to very good use.
    \n\n\t\tSincerely, \n\t\t\t--The Cool Team''')
    return(report_text)

# -- UNIT TESTS --#
def test_gen_letter_body():
    name = "First Last"
    amount = 2020
    the_text = (f'''Dear {name},\n\nThank you for your charitable gift of ${amount}.
    \n\tIt will be put to very good use.
    \n\n\t\tSincerely, \n\t\t\t--The Cool Team''')
    assert gen_letter_body(name, amount) == the_text

def run_tests():
    test_gen_letter_body()

# -- Presentation (Input/Output) --#
if __name__ == '__main__':
    run_tests()
    while (True):
        get_user_action = get_user_choice()
        if get_user_action == "4":
            print("Goodbye!")
            break
        else:
             process_menu(get_user_action)