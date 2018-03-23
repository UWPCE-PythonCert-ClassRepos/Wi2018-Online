#!/usr/bin/env python3

"""Mailroom - Part 1."""

donors = ["Wassily Kandinsky", "Marc Chagall", "Kazimir Malevich",
          "El Lissitzky", "Aristarkh Lentulov"]
donors_sums = [[75.0, 50.5, 60.4], [148.75, 155.0], [15.0, 20.25, 12.25],
               [34.20, 30.0, 35.5], [4.5, 5.0]]


# Sending a Thank You.
def existing_donor_interaction():
    """Ask for old donor name, donation amount, print a thank-you email."""
    prompt_name = "Type full name of the old donor or 0 to abort > "
    old_donor_name = input(prompt_name)
    if old_donor_name == "0":
        return
    while old_donor_name not in donors:
        old_donor_name = input(prompt_name)
        if old_donor_name == "0":
            return

    prompt_amount = "Enter the donation amount or 0 to abort > "
    donation_amount = input(prompt_amount)
    if donation_amount == "0":
        return

    # Add the donation amount to the list.
    donor_index = donors.index(old_donor_name)
    donors_sums[donor_index].append(float(donation_amount))

    print_email(old_donor_name, float(donation_amount))


def new_donor_interaction():
    """Ask for new donor name, donation amount, print a thank-you email."""
    prompt_name = "Type full name of the new donor or 0 to abort > "
    new_donor_name = input(prompt_name)
    if new_donor_name == "0":
        return

    prompt_amount = "Enter the donation amount or 0 to abort > "
    donation_amount = input(prompt_amount)
    if donation_amount == "0":
        return

    # Add the donor and the donation amount to the list.
    donors.append(new_donor_name)
    donors_sums.append([float(donation_amount)])

    print_email(new_donor_name, float(donation_amount))


def print_donor_names():
    """Print existing donor names on screen."""
    print()
    for name in donors[:-1]:
        print(name, end=', ')
    print(donors[-1])
    print()


def print_email(name, amount):
    """Print a thank-you email on screen."""
    email_text = ("\nDear {},\n"
                  "\nI would like to thank you for your donation of ${:,}.\n"
                  "\nWe appreciate your support.\n"
                  "\nSincerely,\n"
                  "The Organization\n"
                  )
    print(email_text.format(name, amount))


def print_send_thank_you_menu():
    """Print the send-thank-you menu on screen."""
    msg = ("\nThis is the Send-Thank-You Menu\n"
           "\n1 - See the list of donors\n"
           "2 - Add a new donor and a donation amount\n"
           "3 - Choose an existing donor\n"
           "4 - Quit\n"
           )
    print(msg)


def send_thank_you_interaction():
    """Send a thank you letter."""
    while True:
        print_send_thank_you_menu()
        prompt = input("Type your choice > ")
        if prompt == "1":
            print_donor_names()
        elif prompt == "2":
            new_donor_interaction()
        elif prompt == "3":
            existing_donor_interaction()
        elif prompt == "4":
            break


# Creating a Report.
def get_total_given(donor_name):
    """Return total amount of donations for the given donor."""
    donor_index = donors.index(donor_name)
    return sum(donors_sums[donor_index])


def get_donations(donor_name):
    """Return a list of the specified donor's donations."""
    donor_index = donors.index(donor_name)
    return donors_sums[donor_index]


def sort_donors_by_total():
    """Return a list of donor names sorted by total donations, max to min."""
    # Create a list in the form [['Donor Name', total_donated], etc.].
    donors_totals = []
    for name in donors:
        donors_totals.append([name, get_total_given(name)])

    # Sort the above list by the total_donated.
    donors_totals.sort(key=lambda x: x[1])
    donors_totals = donors_totals[::-1]

    # Get rid of the total_donated in the list.
    sorted_donor_names = []
    for item in donors_totals:
        sorted_donor_names.append(item[0])

    # Return a list containing the names of donors only.
    return sorted_donor_names


def create_report_main():
    """Create a report."""
    title_line_form = "{:<26}{:^3}{:>13}{:^3}{:>13}{:^3}{:>13}"
    title_line_text = ('Donor Name', '|', 'Total Given', '|',
                       'Num Gifts', '|', 'Average Gift'
                       )
    print()
    print(title_line_form.format(*title_line_text))
    print('- ' * 38)
    form_line = "{:<26}{:>3}{:>13}{:>3}{:>13}{:>3}{:>13}"
    for name in sort_donors_by_total():
        total = get_total_given(name)
        num_gifts = len(get_donations(name))
        mean = round((total / num_gifts), 2)
        print(form_line.format(str(name), '$', str(total), ' ',
                               str(num_gifts), '$', str(mean)
                               )
              )
    print()


# Main menu.
def print_main_menu():
    """Print the menu on screen."""
    main_menu = ("\nThis the Main Menu\n"
                 "\n1 - Send a Thank You\n"
                 "2 - Create a Report\n"
                 "3 - Quit\n"
                 )
    print(main_menu)


def main_menu_interaction():
    """Control the main flow of the user interaction."""
    while True:
        print_main_menu()
        prompt = input("Please choose an option > ")
        if prompt == "1":
            send_thank_you_interaction()
        elif prompt == "2":
            create_report_main()
        elif prompt == "3":
            break


if __name__ == "__main__":
    main_menu_interaction()
