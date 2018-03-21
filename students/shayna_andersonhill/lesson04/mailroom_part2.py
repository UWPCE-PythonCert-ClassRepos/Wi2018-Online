#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#Shayna Anderson-Hill
#Mailroom Part 2
#03-04-2018

import sys


donations = {'Shayna Hill': [50, 50, 50], 'Brandon Aleson': [200],
        'Lisa Rodriguez': [10, 20], 'Marge Simpson': [100],
        'Charlie Smith': [4]}

name_list = [name for name in donations]

def report():
    heading = ['Donor Name', '| Total Given', '| Num Gifts', '| Average Gift']
    print('{:20}{:>15}{:>15}{:>15}'.format(*heading))
    print('------------------------------------------------------------------')
    for donor, donation in donations.items():
        print('{:20}    ${:12.2f}{:>12}     ${:>12.2f}'.format(donor,
            sum(donation), len(donation), sum(donation)/len(donation)))

    print("\n")

def thank_you():
    while True: 
        name = input('Full Name:')
        if name == 'list':
            print(name_list)
            continue
        donation = int(input('Donation Amount:'))
        if name in name_list:
            donations[name].append(donation)  
        else: 
            donations[name] = [donation]
        
        print(f'Dear {name},\nThank you so much for your donation of ${donation}. We appreciate your continual support.\nBest,\nShayna\n')
        break

#def send_letters():
#    print('letters')

def main():
    menu_choice = {
        1: thank_you,
        2: report,
        3: sys.exit
    }

    while True:
        response = input('Would you like to:\n1. Send a Thank You\n2. Create a Report\n3. Quit\n>')
        
        if response in ("1", "2", "3"):
            menu_choice.get(int(response))()
        else:
            print("Invalid Selection")
        

if __name__ == "__main__":
    main()
