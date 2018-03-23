data = {'John Smith': [400],
        'Bill Wilmer': [8000, 10000, 3000],
        'George Guy': [50],
        'Elizabeth Jones': [2000, 1000, 2000],
        'Nathan Star': [250.50, 100]}


def menu():
    ''' Creates the user selection menu '''
    while True:
        print("\nPlease select an option:")
        print("1. Send a Thank You   |   2. Create a Report   |   3. Send letters to everyone   |   4. Quit")
        try:
            menu_selection = int(input())
        except ValueError as e:
            print("Exception occurs in menu_selection: {}".format(e))
            break
        else:
            return menu_selection


def thank_you():
    '''
    Sends a Thank You: Asks for a full name, Lists the donors, Asks for donation amount,
    Converts the donation to an integer, Adds donation amount to associated donor in list
    '''
    while True:
        input_key = input("Please enter a Full Name or type 'list' to see a list of donors: ")
        if input_key == 'list':
            print("\nHere is a list of the current donors:\n")
            for key, val in data.items():
                print(f"{key:20} $  {val}")

        elif input_key in data.keys():
            while True:
                try:
                    input_value = float(input("Enter a donation amount for {} : ".format(input_key)))
                except ValueError as e:
                    print("Exception occurs in donation amount entered: {} \n".format(e))
                    continue
                else:
                    data[input_key].append(input_value)
                    print("\nDear {},\n\nThank You for the generous donation of ${}."
                          "\n\nThe Donation Center :^)".format(input_key, input_value))
                    break

        elif input_key not in data.keys():
            while True:
                try:
                    input_value = float(input("Enter a donation amount for {} : ".format(input_key)))
                except ValueError as e:
                    print("Exception occurs in donation amount entered: {} \n".format(e))
                    continue
                else:
                    data[input_key] = [input_value]
                    print("\nDear {},\n\nThank You for the generous donation of ${}."
                          "\n\nThe Donation Center :^)".format(input_key, input_value))
                    break
        break


def report():
    """ Prints a report with the Donor Name, Total Given, Number of Gifts, and Average Gift. """
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("------------------------------------------------------------------")
    for key, val in data.items():
        print(f"{key:25} $ {float(sum(val)):>12.2f}  {len(val):>8}  $ {float(sum(val))/len(val):>11.2f}")


def letters():
    for key, val in data.items():
        file = open('{}.txt'.format(key), 'w')
        with open('{}.txt'.format(key), 'w') as f:
            f.write("Dear {},\n\nThank You for donating a total of ${}. We look forward to hearing from you again."
                    "\n\nThe Donation Center ;^)".format(key, sum(val)))
        file.close()
    print("\n*** Text files have been created ***\n")


if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 1:
            thank_you()
        elif choice == 2:
            report()
        elif choice == 3:
            letters()
        elif choice == 4:
            print("\n***\nYou have chosen to Exit the program. Goodbye!\n***")
            quit(0)

