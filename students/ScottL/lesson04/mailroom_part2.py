#!/usr/bin/env python3

#-------------------------------------------------#
# Title: Mailroom Part-2 Assignment
# Dev: Scott Luse
# Date: Feb 10, 2018
#-------------------------------------------------#



# -- Data --#
DONOR_HISTORY_DICT = {
    'Peter Parker': [288.09, 9.01, 61288.09],
    'Iron Man': [1238.09, 8199.01, 1468.07],
    'Captain Marvel': [43188.09, 1288.09],
    'Black Widow' : [1272.09],
}

# -- Processing --#
def GetUserChoice():

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
    if (menu_item == '1'):
        send_thanks()
        return
    elif (menu_item == '2'):
        format_charity_structure()
        return
    elif (menu_item == '3'):
        create_individual_letters()
        return

def send_thanks():
    while (True):
        thank_you_name = input("Please enter full name, enter 'list' for names, or 'main' for menu: ")
        if (thank_you_name.lower() == "list"):
            print_donors()
            print(' ')
        elif (thank_you_name.lower() == "main"):
            return
        else:
            process_input_name(thank_you_name.title())
            return

def process_input_name (name):
    '''Ask for a donation amount and look for user input name in donor dictionary.
    If you find the name and the amount to the donor ledger and print a letter to the screen.
    If you don't find the name create a new key value pair'''

    gift_amount = input("Please enter $$ donation $$ amount for " + name + ":")
    if (name in DONOR_HISTORY_DICT.keys()):
        #We found the name so update the giving values
        #Is this the best way to manage appending the list?
        original_list = DONOR_HISTORY_DICT.get(name)
        original_list.append(int(gift_amount))
        DONOR_HISTORY_DICT[name] = original_list
        thank_you_printing(name, gift_amount)
        return
    else:
        #We didn't find the name so create a new key value pair
        DONOR_HISTORY_DICT[name] = [int(gift_amount)]
        thank_you_printing(name, gift_amount)
        return

def thank_you_printing(name, amount):
    print("*" * 50)
    print(f"{name}")
    print("Address")
    print(' ')
    print(f"Dear {name}, Thank you for your charitable gift of ${amount}.")
    print("*" * 50)

def print_donors():
    for key in DONOR_HISTORY_DICT:
        print(key)
    return

def format_charity_structure():
    print('')
    print('{:20}{:>15}{:>10}{:>10}'.format('Donor Name', '| Total Gifts', '| Num Gifts', '| Ave Gift'))
    print('-' * 55)
    for key in DONOR_HISTORY_DICT:
        donor_list = DONOR_HISTORY_DICT.get(key)
        sum_values = "{:.2f}".format(sum(donor_list))
        ave_values = "{:.2f}".format(sum(donor_list) / len(donor_list))
        print('{:20}{:>15}{:>10}{:>10}'.format(key, sum_values, len(donor_list), ave_values))


def create_individual_letters():
    try:
        for key in DONOR_HISTORY_DICT:
            donor_list = DONOR_HISTORY_DICT.get(key)
            sum_values = "{:.2f}".format(sum(donor_list))
            report_text = f"Dear {key}," + "\n" + "\n" + "Thank you for your charitable gift of $" + sum_values + "."
            report_text = report_text  + "\n" + "\n" + "\tIt will be put to very good use."
            report_text = report_text  + "\n" + "\n" + "\t\tSincerely,"
            report_text = report_text + "\n" + "\t\t\t--The Team"

            key.replace(" ", "_")
            objFileName = key.replace(" ", "_") + ".txt"
            objMyFile = open(objFileName, "w")
            objMyFile.write(report_text)
            objMyFile.close()
            print(objFileName + " file saved.")
    except:
        print("\n" + "File error!")

# -- Presentation (Input/Output) --#
if __name__ == '__main__':
    '''Prompt the user to choose from a menu of 3 actions: Send a Thank You, Create a Report or quit'''

    while (True):
        get_user_action = GetUserChoice()
        if (get_user_action == "4"):
            print("Goodbye!")
            break
        else:
             process_menu(get_user_action)