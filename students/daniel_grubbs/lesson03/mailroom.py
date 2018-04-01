#!/usr/bin/env python3

# Mailroom Assignment - Week 3

donors = [
    ('Jimmy Nguyen', [100, 1350, 55]),
    ('Steve Smith', [213, 550, 435]),
    ('Julia Norton', [1500, 1500, 1500]),
    ('Ed Johnson', [150]),
    ('Elizabeth McBath', [10000, 1200]),
]


def main():
    """Main mneu of the program."""
    print_header()

    while True:
        menu_items = ['Send a Thank You', 'Create a Report', 'Quit']
        for n, item in enumerate(menu_items, 1):
            print(n, item)
        print()
        selection = input('Please select a menu item: ')

        if selection == '1':
            thank_you(donors)
        elif selection == '2':
            create_report()
        elif selection == '3':
            break
        else:
            print('The item you have chosen is not in the list. Try again.')


def print_header():
    print('------------------------------------------')
    print('       Donation Management System')
    print('------------------------------------------\n')


def thank_you(donors):
    """Function for Thank you."""
    while True:
        full_name = input("Please enter your full name or type 'list' for list of donors ('menu' to return to menu): ")

        if full_name == 'list':
            print('Below is the current donor list.')
            for donor in donors:
                print(donor[0])
        elif full_name == 'menu':
            return
        else:
            break

    # Enter a donation amount
    while True:
        donation = int(input("Please enter a donation amount. 'menu' to return to original menu: "))
        if donation == 'menu':
            return
        else:
            break

    # Enter a new donor
    if full_name not in donors:
        donor_name = (full_name, [])
        donors.append(donor_name)

    # Write a thank you for the donor
    print()
    print('{}, Thank you for your donation in the amount of ${:.2f}'.format(full_name, donation))


def create_report():
    """Function for creating a report."""
    donations = []

    print("{:26s} | {:13s} | {:9s} | {:13s}".format("Donor name", "Total Donation", "Number of Gifts", "Average Gifts"))
    print("-" * 80)

    for donor, gift in donors:
        total_given = sum(gift)
        number_gifts = len(gift)
        average_gift = total_given / number_gifts
        donations.append((donor, total_given, number_gifts, average_gift))

    for amount in donations:
        print("{:26s} | {:13.2f} | {:9d} | {:13.2f}".format(*amount))
    print()


if __name__ == '__main__':
    main()
