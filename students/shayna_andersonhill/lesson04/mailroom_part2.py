#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#Shayna Anderson-Hill
#Mailroom Part 2
#03-04-2018

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

def thank_you():
    name = input('Full Name:')
    while name == 'list':
        print(name_list)
        name = input('Full Name:')
        continue
    donation = int(input('Donation Amount:'))
    if name in name_list:
        donations[name].append(donation)  
    else: 
        donations[name] = donation
    nl = '\n'
    print(f'Dear {name},{nl}Thank you so much for your donation of ${donation}. We appreciate your continual support. {nl}Best,{nl}Shayna')

#def main():
response = input('Would you like to "Send a Thank You", "Create a Report", or "quit"?')

menu_choice = {'quit': quit, 'Send a Thank You': thank_you, 'Create a Report': report}

while response != 'quit': 
    menu_choice.get(response)()
    response = input('Would you like to "Send a Thank You", "Create a Report", or "quit"?')

#if __name__ == "__main__":
#    main()
    
