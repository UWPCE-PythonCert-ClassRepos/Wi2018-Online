"""
Lesson 3: Assignment: Mailroom, Part 1
"""

"""
data structure that holds a list of donors and a history of the amounts 
they have donated. This structure should be populated at first with at  
least five donors,  with between 1 and 3 donations each.
"""

donors_list = [("Ken Lenning", [1325, 1232.24, 16325.5]),
                ("Thomas Timmy",[521.3, 869.14]),
                ("Jane Chung",  [3259.3, 1282.74, 1525.5]),
                ("Lucy Nguyen", [5253.82]),
                ("Ben Cormack", [56230.25, 89532.0, 12025.8])]


def print_thank_you():
    """ Add or Update a donor record, and print a Thank You letter """
    while True:
        response = input(''' Donation Entries ---
        Type your Full Name,
        or 'list' to display list of the donor names,
        or 'quit' to quit and return to main prompt1
        Enter your choice here: ''')

        if response.lower().strip() in ["q", "quit"]:
            break
        elif response.lower().strip() in ["l", "list"]:
            print_donor_list()
            continue
        else:
            record_id = None
            for index, existing_donor in enumerate(donors_list):
                # get a match an existing record
                if existing_donor[0].lower().strip() == response.lower().strip():
                    record_id = index
                    break

            amount = input("Enter Donation amount: ")
            try:
                donate_amount = float(amount)
            except ValueError:
                print("The donation amount must be numeric!")

            # add or update a record
            if record_id is None:  # new record
                print('Add a new record entry')
                donors_list.append((response, [donate_amount]))
                donor_to_print = donors_list[-1]
            else:  # existing record
                print('Update an existing record entry')
                donors_list[record_id][1].append(donate_amount)
                donor_to_print = donors_list[record_id]

            # now print a thank you letter
            print_letter(donor_to_print)


def print_letter(donor):
    """ Generate a thank you note to a donor """
    message = "Dearest, {}. Thank you so much for your generosity with your most recent donation of ${}. \nSincerely."
    print(message.format(donor[0], donor[1][-1]))


def print_donor_list():
    """ print out list of current donors"""
    print('Below are the existing donors: ')
    for donor in donors_list:
        print('\t- ', donor[0], ' ', donor[1])


def print_report(donors_list):
    """ print a list of your donors, sorted by total historical donation amount. """
    width = 68
    print("-" * width)
    header = ("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print("{:20} | {:15} | {:10} | {:12}".format(*header))
    print("-" * width)
    for index, donor in enumerate(donors_list):
        name = donor[0]
        total = sum(donor[1])
        num_gift = len(donor[1])
        average = total/num_gift
        print("{:22} ${:12,.2f} {:12d}     ${:12,.2f}".format(name, total, num_gift, average ))
    print("-" * width)


def main_menu():
    while True:
        answer = str(input('''Please choose from one of the following options:
        (1) Send a Thank You
        (2) Create a Report
        (3) Exit
        Enter your choice here: '''))
        if answer == '1':
            print_thank_you()
        elif answer == '2':
            print_report(donors_list)
        elif answer == '3':
            break
        else:
            print("\nInvalid input! Please type 1, 2, or 3")


if __name__ == '__main__':
    main_menu()