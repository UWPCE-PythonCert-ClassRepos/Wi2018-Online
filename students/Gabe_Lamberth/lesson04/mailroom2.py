#!/usr/bin/env python3

from pathlib import Path

# Global data structure
patrons = {'Emma': [50.00, 150.00, 2000.00, 3000.00], 'Carolyn': [5000.25, 2500.00], 'Andres': [5015.00, 200.50, 35.50]}

# Called when user wants to see the list of donars
def display_donars():
    print('Showing list of patrons in the database:')
    for key, value in patrons.items():
        print(key, end=', ')


# Called from menu_dictionary in main()
def generate_report():
    header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print('{:25} |{:^15} |{:^15} |{:^15}'.format(*header))
    print('-' * 75)
    for key, value in patrons.items():
        print(f"{key:<30} ${sum(value):^,.2f}  {len(value):^20}  ${sum(value)/len(value):,.2f}")

    print('-- Report Finished --\n')


# Called from send_thanks function
def send_email(choice, amount):
    print(f"Thank you {choice} for your generous ${amount:,.2f} donation")
    print('-- Email Sent --\n')


# Called from menu_dictionary
def add_donar():
    while True:
        choice = input("Type a patrons name or 'view' to see donor list.\n"
                       "Type 'quit- to exit to main menu.\n"
                       "Enter value here >>  ")
        if choice.lower() == 'view':
            print('Showing list of patrons in the database:')
            display_donars()
        elif choice.lower() == 'quit':
            break
        elif choice not in patrons:
            patrons[choice] = []
            print(f'{choice} was added to the database')
            amount = input('Please enter a donation amount: ')
            patrons[choice].append(float(amount))
            send_email(choice, float(amount))
        else:
            selection = input(f'{choice} already found in database, add another donation? \n Enter Yes or No>> ')
            if selection.lower() == 'yes':
                amount = input('Please enter a donation amount: ')
                patrons[choice].append(float(amount))
                send_email(choice, float(amount))
            else:
                continue


def send_letters():
    for key, value in patrons.items():
        pth = Path.cwd() / f'{key}.txt'

        if pth.exists():
            print('Rebuilding the existing letter')
        else:
            print('Creating new letter')

        pth.write_text("""
                    Dear {},

                           Thank you for you donation of ${:,.2f}

                           It will be put to good use

                                            Sincerely,
                                                -The Team""".format(key, sum(value)))


def user_selection(user_prompt, queue_dict):
    # Runs until user inputs 'q'
    while True:
        # Make sure all Key values are capitalized
        response = input(user_prompt)
        if queue_dict[response]() == "exit menu":
            break


def quit_menu():
    print("Shutting down program, Goodbye", end='\n')
    return "exit menu"


def main():
    user_prompt = ("\n\nWelcome to the MailRoom Donar Program!\n"
                   "What would you like to do?\n"
                   "Type '1- To display donars'\n"
                   "Type '2- To generate a report'\n"
                   "Type '3- To add new donar'\n"
                   "Type '4- To send letters to donars'\n"
                   "Type 'q- To end the program'\n"
                   "Enter value here >> ")
    """
    Use dictionary to create quasi switch/case structure
    """
    menu_dict = {"1": display_donars,
                 "2": generate_report,
                 "3": add_donar,
                 "4": send_letters,
                 "q": quit_menu}
    # Pass the user_prompt and menu_dict to the user_selection function
    user_selection(user_prompt, menu_dict)


if __name__ == "__main__":
    main()