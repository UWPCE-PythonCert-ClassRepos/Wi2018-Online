#!/usr/local/bin/python3
import datetime
import os  # this is required to write files to ~/Downloads. os.path.expanduser


##############
#    DATA    #
##############

d = {'jack': [100, 200, 300, 400],
     'mary': [3000, 5000],
     'frank': [29.50, 31],
     'jane': [3000, 5000],
     'scrouge': [1, 2, 3],
     'bob': [60000, 70000, 7668, 4]}


#####################
#  HELPER FUNCTIONS #
#####################


def seperator(str):
    # return line that equals string length ignoring newline.
    return "-" * (len(str) - str.count('\n'))

def list_donors():
    print("\nExisting donors\n-" + "\n-".join(d.keys()))


def add_donation(donor_name, exsting_donor):
    while True:
        donation = input(
            f"\nEnter a donation amount for {donor_name.capitalize()}: ")
        if donation.isnumeric() and exsting_donor:
            d[donor_name].append(int(donation))
            break
        elif donation.isnumeric():
            d[donor_name] = [int(donation)]
            break

def send_to_screen():
    for k, v in d.items():
        print(f"thanks {k}")

def send_to_file():
    target_folder = '~/Downloads/'
    now = datetime.datetime.now()
    file_append = now.strftime("%Y-%m-%d")
    for k,v in d.items():
        f = open(os.path.expanduser(target_folder + k + file_append + '.txt'), "w+")  # w+ will create file and write
        f.write(f"Dear {k}, thanks\n\n"
                f"Your donation of ${'{:,}'.format(sum(v))} is appreciated\n\n"
                 "It will be put to good use.\n\n"
                 "THANKS")
        f.close()



#####################
#  MAIN FUNCTIONS #
#####################


def sub_menu():
    options_dict = {'l': list_donors, 'q': quit}
    options_prompt = 'l - list donors\n'\
                     'q - return to main menu\n'
    menu_selection(options_prompt, options_dict)


def send_letters():
    options_dict = {'s': send_to_screen, 'f': send_to_file, 'q': quit}
    options_prompt = 's - send to screen\n'\
                     'f - send to file\n'\
                     'q - return to main menu\n'
    menu_selection(options_prompt, options_dict)

def send_thank_you():
    # donor_names = get_names()  # create a list of names only
    while True:
        response = input("\nEnter the name of a donor "
                         "('l' -> list of donors | 'q' -> "
                         "main menu)\n")
        if response == 'l':
            list_donors()
        elif response == 'q':
            break
        elif response in d.keys():  # i.e. existing donor
            add_donation(response, exsting_donor=True)
            break
        elif response.isalpha():  # new donor
            add_donation(response, exsting_donor=False)
            break


def create_report():
    heading = "Donor Name | Total Given | Num Gifts | Average Gift\n"
    print(heading + seperator(heading))
    for k, v in d.items():
        print("{:10} ${:10.2f} {:10} {:15.2f}".format(k,
                                                      sum(v),
                                                      len(v),
                                                      (sum(v) / len(v))))


def quit():
    print('goodbye')
    return 'exit'  # return this to break out of while loop.  More elegant


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict.get(response)() == 'exit':
            #  otherwise i want to return the response to the calling function
            #  how...???
            break


####################
# GLOBAL VARIABLES #
####################


main_response_dict = {'1': send_thank_you,
                      's': sub_menu,
                      '2': create_report,
                      '3': send_letters,
                      'q': quit}

menu_prompt = '\nMAIN MENU\n'\
              '1 - send thank you\n'\
              '2 - create report\n'\
              '3 - send letters to everyone\n'\
              's - sub menu\n'\
              'q - quit\n'


if __name__ == "__main__":
    menu_selection(menu_prompt, main_response_dict)
