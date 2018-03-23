#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#Shayna Anderson-Hill
#Mailroom Part 2
#03-04-2018

import sys
from datetime import datetime
import collections

donations = {'Shayna Hill': [['01/01/2017', 50], ['02/01/2017', 50],
    ['06/02/2017', 50]], 'Brandon Aleson': [['05/17/2017', 200]],
        'Lisa Rodriguez': [['09/30/2017', 10], ['07/07/2017', 20]],
        'Marge Simpson': [['10/13/2017', 100]],
        'Charlie Smith': [['12/25/2017', 4]]}

name_list = [name for name in donations]

total_donation = {}
for key, value in donations.items():
    total_sum = 0
    for donation in value:
        total_sum += donation[1]
    total_donation.update({key: total_sum})

count_donation = {}
for key, value in donations.items():
    count = 0
    for donation in value:
        count += 1 
    count_donation.update({key: count})

average_donation = {}
for key, value in donations.items():
    total_sum = 0
    count = 0
    for donation in value:
        total_sum += donation[1]
        count += 1
    average = total_sum/count
    average_donation.update({key: average})

def report():
    heading = ['Donor Name', '| Total Given', '| Num Gifts', '| Average Gift']
    print('{:20}{:>15}{:>15}{:>15}'.format(*heading))
    print('------------------------------------------------------------------')
    for (donor, total), (donor, count), (donor, average) in zip(total_donation.items(),
            count_donation.items(), average_donation.items()):
        print('{:20}    ${:12.2f}{:>12}     ${:>12.2f}'.format(donor,
            total, count, average))

    print("\n")

def thank_you():
    while True: 
        name = input('Full Name:')
        if name == 'list':
            print(name_list)
            continue
        date = input('Date of Donation:')
        donation = int(input('Donation Amount:'))
        if name in name_list:
            donations[name].append([date, donation])  
        else: 
            donations[name] = [[date, donation]]
        print(f'Dear {name},\nThank you so much for your donation of ${donation}. We appreciate your continual support.\nBest,\nShayna\n')
        break

def send_letters():
    letter_dictionary = {}
    try:
        { letter_dictionary.update({ donor: f'Dear {donor},\nThank you so much for your donation of ${donation[-1][1]}. We appreciate your continual support.\nBest,\nShayna\n'}) for donor, donation in donations.items() } 
    except TypeError:
        pass

    for donor, letter in letter_dictionary.items():
        with open(donor.replace(" ", "_")+'.txt', 'w+') as f:
            f.write(letter)
    
    print("Letter Files Made\n")

def main():
    menu_choice = {
        1: thank_you,
        2: report,
        3: send_letters,
        4: sys.exit
    }

    while True:
        response = input('Would you like to:\n1. Send a Thank You\n2. Create a Report\n3. Send Letters to Everyone\n4. Quit\n>')
        try:
            menu_choice.get(int(response))()
        except ValueError:
            print("Input must be an integer, try again.")

if __name__ == "__main__":
    main()

