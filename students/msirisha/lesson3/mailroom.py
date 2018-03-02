# Mailroom script
# part1. send a thank you note to donors.
# Use the concepts learned so far.

#global data structure
donor_data = [("sai", [20.23, 30.456, 50.786]),
              ("sirisha", [67.89, 45.89]),
              ("ani", [12.789, 5.456]),
              ("mary", [15.89, 89.20, 345.67]),
              ("tom", [678.986])]

def get_donor_names():
    donor_names = []
    for donor_info in donor_data:
        donor_names.append(donor_info[0])
    return donor_names

def menu():
    """ Select one of the three items in the menu
        And returns the number """
    print("1) send a thank you")
    print("2) create a report")
    print("3) quit")
    return int(input("Please enter your choice(1/2/3) >"))

def send_a_thankyou():
    """ Sends thank you message for the donors
    """
    donor_names = get_donor_names()
    while True:
        choice = str(input("Please enter donor name"))
        if choice == "list":
            print(donor_names)
            continue
        elif choice not in donor_names:
            donor_data.append((choice, []))
        elif choice in donor_names:
            print("Donor already in the donor names list.. using existing donor name")
        break

    amount = float(input("Please enter donation amount"))
    for donor in donor_data:
        if donor[0] == choice:
            donor[1].append(amount)

            print("Hi {}\n".format(choice))
            print("\nThank you for your generous donation {}".format(amount))
            print("\nSincerly,\nLocal Charity")


def create_a_report():
    """ Prints donor information
    """
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    for donor_info in donor_data:
        print(f"{donor_info[0]:26} $ {sum(donor_info[1]):>10.2f}   {len(donor_info[1]):9}  ${sum(donor_info[1])/len(donor_info[1]):>12.2f}")

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 1:
            send_a_thankyou()
        elif choice == 2:
            create_a_report()
        elif choice == 3:
            quit(0)
