#!/usr/bin/env python3

# Global data structure
patrons = {'Emma': [50.00, 150.00, 2000.00, 3000.00], 'Carolyn': [5000.25, 2500.00], 'Andres': [5015.00, 200.50, 35.50]}


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
    print(f'Thank you {choice} for you generous ${amount:,.2f} donation')
    print('-- Email Sent --\n')


# Called from menu_dictionary
def send_thanks():
    choice = input('Enter a patrons name or view to see all donors: ')
    if choice == 'view' or choice == 'View':
        print('Showing list of patrons in the database:')
        for key, value in patrons.items():
            print(key, end=', ')
    else:
        if choice in patrons:
            print(f'{choice} was found in the database')
        else:
            patrons[choice] = []
            print(f'{choice} was added to the database')

        amount = input('Please enter a donation amount: ')
        patrons[choice].append(float(amount))
        send_email(choice, float(amount))


def user_selection(user_prompt, queue_dict):
    # Runs until user inputs 'q'
    while True:
        response = input(user_prompt)
        if queue_dict[response]() == "exit menu":
            break


def quit_menu():
    print("Shutting down program, Goodbye", end='\n')
    return "exit menu"


def main():
    user_prompt = ("\nWelcome to the MailRoom Donar Program!\n"
                   "What would you like to do?\n"
                   "Type '1- Send a Thank You'\n"
                   "Type '2- To generate a report'\n"
                   "Type 'q- To end the program'\n"
                   "Enter value here >> ")
    """
    Use dictionary to create quasi elif
    structure
    """
    menu_dict = {"1": send_thanks,
                 "2": generate_report,
                 "3": "quit"}
    # Pass the user_prompt and menu_dict to the user_selection function
    user_selection(user_prompt, menu_dict)


if __name__ == "__main__":
    main()