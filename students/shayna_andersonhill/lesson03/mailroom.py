#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#Shayna Anderson-Hill
#Mailroom Part 1
#03-04-2018

donations = [['Shayna Hill', [50, 50, 50]], ['Brandon Aleson', [200]],
        ['Lisa Rodriguez', [10, 20]], ['Marge Simpson', [100]],
        ['Charlie Smith', [40]]]

def print_names():
    print(name_list)

def add_name(name):
    name_list.append(name)
    donations.append([name, []])

def add_new_name_donation(name, donation):
    if donations[-1][0] == name:
        donations[-1][1].append(donation)

def add_old_name_donation(name, donation):
    donations[counts][1].append(donation)

def formatter():
    heading = ['Donor Name', '| Total Given', '| Num Gifts', '| Average Gift']
    print('{:20}{:>15}{:>15}{:>15}'.format(*heading))
    print('------------------------------------------------------------------')
    for donor, total, num, average in zip(donors, total_given, num_gifts,
        average_gifts):
        print('{:20}    ${:12.2f}{:>12}   ${:>12.2f}'.format(donor, total, num, average))





if __name__ == '__main__':
    response = input('Would you like to "Send a Thank You", "Create a Report", or "quit"?')
    name_list = [i[0] for i in donations]

    donors = []
    for i,j in donations:
        donors.append(i)

    total_given =[]
    for i,j in donations:
        total_given.append(sum(j))

    num_gifts = []
    for i,j in donations:
        num_gifts.append(len(j))

    average_gifts = []
    for i,j in donations:
        average_gifts.append(sum(j)/len(j))


    while response != 'quit':
        if response == 'Send a Thank You':
            name = input('Full Name:')
            while name == 'list':
                print_names()
                name = input('Full Name:')
                continue
            donation = int(input('Donation Amount:'))
            if name in name_list:
                counts = -1
                for i,j in donations:
                    counts += 1
                    if name == i:
                        break
                add_old_name_donation(name, donation)
            while name not in name_list:
                add_name(name)
                continue
            add_new_name_donation(name, donation)
            nl = '\n'
            print(f'Dear {name},{nl}Thank you so much for your donation of ${donation}. We appreciate your continual support. {nl}Best,{nl}Shayna')
            response = input('Would you like to "Send a Thank You", "Create a Report", or "quit"?')
        if response == 'Create a Report':
            formatter()
            response = input('Would you like to "Send a Thank You", "Create a Report", or "quit"?')
     
