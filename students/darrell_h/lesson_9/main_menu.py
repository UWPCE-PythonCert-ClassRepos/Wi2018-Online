from mailroom_class_using_composition import Donor, Mailroom

mailroom = Mailroom()

def print_menu():  ## Your menu design here
    print(23 * "-", "Mailroom Main Menu", 23 * "-")
    print("1. Generate Report")
    print("2. List Donors")
    print("q. Quit")
    print(66 * "-")

def process_result(result):
    print(f'\n{result}\n')


def start_menu():
    loop = True
    while loop:  ## While loop which will keep going until loop = False
        print_menu()  ## Displays menu
        choice = input("Enter your choice [1-2]: ")

        if choice == '1':
            process_result(mailroom.create_report())
        elif choice == '2':
            process_result(mailroom.list_donors())
        elif choice == 'q':
            print('\n===============\n'
                  '=== Goodbye ==='
                  '\n===============')
            break
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")


if __name__ == "__main__":

    intial_data = {'jack': [100, 200, 300, 400],
                   'mary': [3000, 5000],
                   'frank': [29.50, 31],
                   'jane': [3000, 5000],
                   'scrouge': [1, 2, 3],
                   'bob': [60000, 70000, 7668, 4]}

    # load intial donors as objects into dictionary
    for k, v in intial_data.items():
        mailroom.donor_collection[k] = Donor(k, v)
    start_menu()