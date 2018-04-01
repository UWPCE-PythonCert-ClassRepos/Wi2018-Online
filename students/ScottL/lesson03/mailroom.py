#!/usr/bin/env python3

#-------------------------------------------------#
# Title: Mailroom Part-1 Assignment
# Dev: Scott Luse
# Date: Feb 06, 2018
#-------------------------------------------------#



# -- Data --#
DONOR_HISTORY_LIST = [['Peter Parker', [288.09, 9.01, 61288.09]],
                      ['Iron Man', [1238.09, 8199.01, 1468.07]],
                      ['Captain Marvel', [43188.09, 1288.09]],
                      ['Doctor Strange', [1272.09]]]

# -- Processing --#
def GetUserChoice():
    print("""
    MailRoom Menu Options
    1) Send a Thank You
    2) Create a Report
    3) Quit Program
    """)
    user_choice = str(input("Which option would you like to perform? [1 to 3]: "))
    return (user_choice.strip())


def process_menu(menu_item):
    if (menu_item == '1'):
        send_thanks()
        return
    elif (menu_item == '2'):
        format_charity_structure()
        return


def send_thanks():
    while (True):
        thank_you_name = input("Please enter full name, enter 'list' for names, or 'main' for menu: ")
        if (thank_you_name.lower() == "list"):
            print(' ')
            print(get_donor_list())
            print(' ')
        elif (thank_you_name.lower() == "main"):
            return
        else:
            process_thanks(thank_you_name)
            return

def process_thanks (name):
    donor_list = get_donor_list()
    gift_amount = input("Please enter $$ donation $$ amount for " + name + ":")
    if name in donor_list:
        for index, donor in enumerate(DONOR_HISTORY_LIST):
            if donor[0] == name:
                DONOR_HISTORY_LIST[index][1].append(int(gift_amount))
            thank_you_printing(name, gift_amount)
        return
    else:
        DONOR_HISTORY_LIST.append([name, [int(gift_amount)]])
        thank_you_printing(name, gift_amount)
        return

def thank_you_printing(name, amount):
    print("*" * 50)
    print(f"{name}")
    print(f"Address")
    print(' ')
    print(f"Dear {name}, Thank you for your charitable gift of ${amount}.")
    print("*" * 50)


def get_donor_list():
    names_list = []
    for donor in DONOR_HISTORY_LIST:
        names_list.append(donor[0])
    return names_list

def format_charity_structure():
    # Create a data structure that holds a list of your donors and a history of the amounts they have donated.
    # This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
    # You can store that data structure in the global namespace.
    print('')
    print('{:20}{:>15}{:>10}{:>10}'.format('Donor Name', '| Total Gifts', '| Num Gifts', '| Ave Gift'))
    print('-' * 55)
    for donor in DONOR_HISTORY_LIST:
        sum_values = "{:.2f}".format(sum(donor[1]))
        ave_values = "{:.2f}".format(sum(donor[1]) / len(donor[1]))
        print('{:20}{:>15}{:>10}{:>10}'.format(donor[0], sum_values, len(donor[1]), ave_values))


# -- Presentation (Input/Output) --#
if __name__ == '__main__':
    '''Prompt the user to choose from a menu of 3 actions: Send a Thank You, Create a Report or quit'''

    while (True):
        get_user_action = GetUserChoice()
        if (get_user_action == "3"):
            break
        else:
             process_menu(get_user_action)