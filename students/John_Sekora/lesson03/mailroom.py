data = [('John Smith', [400]),
        ('Bill Wilmer', [8000, 10000, 3000]),
        ('George Guy', [50]),
        ('Elizabeth Jones', [2000, 1000, 2000]),
        ('Nathan Star', [250.50, 100])]


def menu():
    ''' Creates the user selection menu '''
    print("\nPlease select an option:")
    print("1. Send a Thank You   |   2. Create a Report   |   3. Quit")
    return int(input())


def people():
    ''' Creates a list of donor names '''
    names = []
    for person in data:
        names.append(person[0])
    return names


def thank_you():
    '''
    Sends a Thank You: Asks for a full name, Lists the donors, Asks for donation amount,
    Converts the donation to an integer, Adds donation amount to associated donor in list
    '''
    people_list = people()
    while True:
        input_name = input("Please enter a Full Name or type 'list' to see a list of donors: ")
        if input_name == 'list':
            print(("{}\n" * len(people_list)).format(*people_list))
        if input_name not in people_list:
            data.append((input_name, []))
        break
    donation = input("Enter a donation amount for {} : ".format(input_name))
    for person in data:
        if input_name in person[0]:
            person[1].append(float(donation))
            print("\nDear {},\n\nThank You for the generous donation of ${}."
                  "\n\nThe Donation Center :^)".format(input_name, donation))


def report():
    """ Prints a report with the Donor Name, Total Given, Number of Gifts, and Average Gift. """
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("------------------------------------------------------------------")
    for person in data:
        print(f"{person[0]:25} $ {sum(person[1]):>12.2f}  {len(person[1]):>8}  $ {sum(person[1])/len(person[1]):>11.2f}")


if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 1:
            thank_you()
        elif choice == 2:
            report()
        elif choice == 3:
            print("\n***\nYou have chosen to Exit the program. Goodbye!\n***")
            quit(0)

