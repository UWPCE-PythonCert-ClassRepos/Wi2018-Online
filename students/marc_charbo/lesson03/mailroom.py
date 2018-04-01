#!/usr/bin/env python3

DONOR_LIST = {'Jim':[25.00,150.00,2000.00,100000.00],'Linda':[10000.25],'Bob':[5.03,100.01,6.00]}

def create_report():
    header = ('Donor Name','Total Given','Num Gifts','Average Gift')
    print ('{:25} |{:^15} |{:^15} |{:^15}'.format(*header))
    print ('-'*75)
    for key, value in DONOR_LIST.items():
        print('{:25} ${:^15.2f} {:^15d} ${:^15.2f}'.format(key,sum(value),len(value),sum(value)/len(value)))

    print('-- End Report --\n')

def send_email(selection,amount):
    print ('Thank you {} for you generous ${:.2f} donation'.format(selection,amount))
    print('-- Email Sent --\n')


def send_thank_you():
    selection = input('Enter a donors name or list to see all donors: ')
    if selection == 'list':
        print('Here is the list of donors in the database')
        for key, value in DONOR_LIST.items():
            print (key)
    else:
        if selection in DONOR_LIST:
            print ('{} was found in the database'.format(selection))
        else:
            DONOR_LIST[selection] = []
            print('{} was added to the database'.format(selection))

        amount = input('Please enter a donation amount: ')
        amount = float(amount)
        DONOR_LIST[selection].append(amount)
        send_email(selection,amount)

def prompt_user():
    print ('Please select one of three options: ')
    print ('1- Send a Thank You')
    print ('2- Create a Report')
    print ('3- Quit')
    selection = input('Enter your selection: ')
    
    return int(selection)

def run():
    run_program = True
    print ("Welcome to Donation Manager")
    while run_program:
        selection = prompt_user()
        if selection == 1:
            send_thank_you()
        elif selection == 2:
            create_report()
        elif selection == 3:
            run_program = False
            print (3)
        else:
            selection = prompt_user()

def main():
    try:
        run()
    except:
        print ('error with task running program')

if __name__ == "__main__":
    main()