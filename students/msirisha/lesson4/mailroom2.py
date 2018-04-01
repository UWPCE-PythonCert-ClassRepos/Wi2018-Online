# Mailroom script
# part1. send a thank you note to donors.
# Use the concepts learned so far.

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
    return int(input("Please enter your choice(1/2/3/4) >"))

def send_a_thankyou():
    """ Sends thank you message for the donors
    """
    donor_names = donor_data.keys()
    while True:
        choice = str(input("Please enter donor name (enter list to show list of donor names"))
        if choice == "list":
            print(("{}\n" * len(donor_data)).format(*donor_data.keys()))
            continue
        elif choice not in donor_names:
            donor_data[choice] = {"first_name": choice.split(" ")[0], "last_name": choice.split(" ")[1], "donations": []}
        elif choice in donor_names:
            print("Donor already in the donor names list.. using existing donor name")
        break

    amount = float(input("Please enter donation amount"))
    donor_data[choice]['donations'].append(amount)
    print("Dear {}\n".format(choice))
    print("\nThank you for your generous donation {}".format(amount))
    print("\nSincerly,\nLocal Charity")


def create_a_report():
    """ Prints donor information for all donors
    """
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    for donor in donor_data:
        print(f"{donor:26} $ {sum(donor_data[donor]['donations']):>10.2f}   {len(donor_data[donor]['donations']):9}  ${sum(donor_data[donor]['donations'])/len(donor_data[donor]['donations']):>12.2f}")

def send_letters():
    """ Send letters to every one, the letters will be stored as text files on disk """
    format_string = "Dear {first_name} {last_name},\n\n\tThank you for your generous donation ${donation:.2f}\n \n\t\tSincerly,\n\t\tLocal Charity\n"
    for donor in donor_data:
        with open(donor + ".txt", "w") as f:
            f.write(format_string.format(donation=donor_data[donor]['donations'][-1],**donor_data[donor]))

if __name__ == "__main__":
    choice_dict = {1: send_a_thankyou, 2: create_a_report, 3: send_letters, 4: quit}
    while True:
        choice_dict[menu()]()

