import donor as Donor
import donors_data as DonorData

DONOR_LIST = {'Jim':[25.00, 150.00, 2000.00, 100000.00],'Linda':[10000.25],'Bob':[5.03, 100.01, 6.00]}

def initial_donor_set():
    return [Donor.Donor('Jim', [25.00, 150.00, 2000.00, 100000.00]), Donor.Donor('Linda', [10000.25]),
            Donor.Donor('Bob', [5.03, 100.01, 6.00])]

donor_db = DonorData.DonorData(initial_donor_set())

def send_letter():
    """write thank you note to all users in donor list"""
    donor_db.save_letters()

def quit():
    print('Existing program\n')
    return 'quit'

def create_report():
    """ prints donnation report on sreen.
        for each user their name, sum of donnations, number of times they donnated
        and avg donnation amount is displayed.
    """
    print (donor_db.print_report())

    print('-- End Report --\n')

def send_email(selection,amount):
    """ sends thank you email to donor with their name and donation amount"""
    print('-- Sending Email --\n')
    print ('Thank you {} for you generous ${:.2f} donation'.format(selection,amount))
    print('-- Email Sent --\n')

def send_thank_you():
    """ donnor dict handling function"""
    selection = input('Enter a donors name or list to see all donors: ')
    if selection == 'list':
        print('Here is the list of donors in the database')
        print (donor_db.print_donor_names())
    else:
        donor = donor_db.find_donor(selection)
        if donor is not None:
            print ('{} was found in the database'.format(donor))
        else:
            donor = donor_db.add_donor(selection)
            print('{} was added to the database'.format(selection))

        try:
            amount = input('Please enter a donation amount: ')
            amount = float(amount)
            donor.donate(amount)
            send_email(selection,amount)
        except ValueError as e:
            print('error with task running program\n {}'.format(e))
            print('Returning to main menu\n')
            return



def prompt_user():
    """ function which displays main menu and prompts user to enter selection"""
    print('Please select one of three options: ')
    print('1- Send a Thank You')
    print('2- Create a Report')
    print('3- Send letters to everyone')
    print('4- Quit')
    selection = input('Enter your selection: ')

    return int(selection)

dispatch_dict = {1: send_thank_you, 2: create_report, 3: send_letter, 4: quit}

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
        run()
    except Exception as e:
        print ('error with task running program\n {}'.format(e))

if __name__ == "__main__":
    main()