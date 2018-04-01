# Mailroom script
# part3. send a thank you note to donors.
# add exceptions concept.

import sys

#global data structure
donor_data = { "sai emani": {"first_name" : "sai", "last_name" : "emani", "donations" : [20.23, 30.456, 50.786]},
               "sirisha marthy": {"first_name" : "sirisha", "last_name" : "marthy", "donations" : [67.89, 45.89]},
               "ani emani": {"first_name" : "ani", "last_name" : "emani", "donations" : [12.789, 5.456]},
               "charles dickens" : { "first_name":  "charles", "last_name": "Dickens", "donations": [15.89, 89.20, 345.67]},
               "mark twain": {"first_name": "mark","last_name": "twain", "donations": [678.986]}}


def menu():
    """ Select one of the four items in the menu
        And returns the number """
    print("1) send a thank you")
    print("2) create a report")
    print("3) send letters to every one")
    print("4) quit")
    while True:
        choice = input("Please enter your choice(1/2/3/4) >")
        try:
            choice = int(choice)
        except ValueError:
            print("please enter choice as integer")
            continue
        else:
            return choice


def send_a_thankyou():
    """ Sends thank you message for the donors
    """
    donor_names = donor_data.keys()
    while True:
        choice = str(input("Please enter donor name (enter list to show list of donor names, enter q to quit)"))
        print("hey choice is", choice)
        if choice =="q":
            return
        if choice == "list":
            print(("{}\n" * len(donor_data)).format(*donor_data.keys()))
            continue
        else:
            print("coming here {} {}".format(choice, len(choice.split())))
            name = choice.split()
            print("hey name is", name)
            if len(name) == 0:
                print("name can not be empty")
            elif choice in donor_names:
                print("Donor already in the donor names list.. using existing donor name")
            elif len(name) > 0:
                first_name = name[:1]
                last_name = name[1:]
                donor_data[choice] = {"first_name": first_name, "last_name": last_name, "donations": []}

        break

    while True:
        try:
            amount = input("Please enter donation amount")
            if float(amount) <= 0:
                print("amount donated must be a +ve number")
            else:
                break
        except ValueError:
            print("Enter positive number")

    donor_data[choice]['donations'].append(float(amount))
    print("Dear {}\n".format(choice))
    print("\nThank you for your generous donation {}".format(amount))
    print("\nSincerely,\nLocal Charity")


def create_a_report():
    """ Prints donor information for all donors
    """
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    for donor in donor_data:
        print(f"{donor:26} $ {sum(donor_data[donor]['donations']):>10.2f}   {len(donor_data[donor]['donations']):9} "
              f"${sum(donor_data[donor]['donations'])/len(donor_data[donor]['donations']):>12.2f}")


def send_letters():
    """ Send letters to every one, the letters will be stored as text files on disk """
    format_string = "Dear {first_name} {last_name},\n\n\tThank you for your generous donation ${donation:.2f}" \
                    "\n \n\t\tSincerely,\n\t\tLocal Charity\n"
    for donor in donor_data:
        with open(donor + ".txt", "w") as f:
            f.write(format_string.format(donation=donor_data[donor]['donations'][-1], **donor_data[donor]))


if __name__ == "__main__":
    choice_dict = {1: send_a_thankyou, 2: create_a_report, 3: send_letters, 4: sys.exit}
    while True:
        try:
            choice_dict[menu()]()
        except TypeError:
            continue
        except ValueError:
            continue

