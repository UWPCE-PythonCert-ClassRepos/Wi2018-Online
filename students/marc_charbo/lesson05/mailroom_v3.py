#!/usr/bin/env python3

import logging
import logging.config

#logging.cong file
logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('mailRoom')

DONOR_LIST = {'Jim':[25.00,150.00,2000.00,100000.00],'Linda':[10000.25],'Bob':[5.03,100.01,6.00]}

def send_letter():
    """write thank you note to all users in donor list"""
    for key, value in DONOR_LIST.items():
        file = open(key+'.txt', 'w')
        file.write('Dear {},\n'.format(key))
        file.write('\n')
        file.write('\tThank you for your very kind donation of ${:.2f},\n'.format(sum(value)))
        file.write('\n')
        file.write('\tIt will be put to very good use.\n')
        file.write('\n')
        file.write('\t\t\tSincerely,\n')
        file.write('\t\t\t\t-The Team')
        file.close()

    logging.info('Saved letter on disk')

def quit():
    print('Existing program\n')
    return 'quit'

def create_report():
    """ prints donnation report on sreen.
        for each user their name, sum of donnations, number of times they donnated 
        and avg donnation amount is displayed.
    """
    header = ('Donor Name','Total Given','Num Gifts','Average Gift')
    print ('{:25} |{:^15} |{:^15} |{:^15}'.format(*header))
    print ('-'*75)
    for key, value in DONOR_LIST.items():
        print('{:25} ${:^15.2f} {:^15d} ${:^15.2f}'.format(key,sum(value),len(value),sum(value)/len(value)))

    print('-- End Report --\n')
    logging.info('On screen print report')

def send_email(selection,amount):
    """ sends thank you email to donor with their name and donation amount"""
    print('-- Sending Email --\n')
    print ('Thank you {} for you generous ${:.2f} donation'.format(selection,amount))
    print('-- Email Sent --\n')
    logging.info('Sending Email')

def send_thank_you():
    """ donnor dict handling function"""
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

        try:
            amount = input('Please enter a donation amount: ')
            amount = float(amount)
            DONOR_LIST[selection].append(amount)
            send_email(selection,amount)
        except ValueError as e:
            print('error with task running program\n {}'.format(e))
            print('Returning to main menu\n')
            logging.debug('error with task running program\n {}'.format(e))
            return

def prompt_user():
    """ function which displays main menu and prompts user to enter selection"""
    print ('Please select one of three options: ')
    print ('1- Send a Thank You')
    print ('2- Create a Report')
    print('3- Send letters to everyone')
    print ('4- Quit')
    selection = input('Enter your selection: ')
    
    return int(selection)

dispatch_dict = {1:send_thank_you,2:create_report,3:send_letter,4:quit}

def run():
    """ function which runs program"""
    print ("Welcome to Donation Manager")
    while True:
        try:
            if dispatch_dict[prompt_user()]() == 'quit':
                break
        except KeyError as e:
            print('{} select not available please chose between menu options\n'.format(e))
            continue
        except ValueError as e:
            print('{} select not available please chose between menu options\n'.format(e))


def main():
    try:
        logging.info('Started Mailroom Program')
        run()
    except Exception as e:
        print ('error with task running program\n {}'.format(e))
        logging.debug('error with task running program\n %s' % e)
    finally:
        logging.info('Finished Mailroom Program')

if __name__ == "__main__":
    main()