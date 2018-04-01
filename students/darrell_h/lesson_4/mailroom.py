#!/usr/local/bin/python3

d = {'jack': [100, 200, 300, 400],
     'mary': [3000, 5000],
     'frank': [29.50, 31],
     'jane': [3000, 5000],
     'scrouge': [1, 2, 3],
     'bob': [60000, 70000, 7668, 4]}


#####################
#  HELPER FUNCTIONS #
#####################

def seperator(str):
    # return line that equals string length ignoring newline.
    return "-" * (len(str) - str.count('\n'))


def add_donation(donor_name, exsting_donor):
    while True:
        donation = input(
            f"\nEnter a donation amount for {donor_name.capitalize()}: ")
        if donation.isnumeric() and exsting_donor:
            d[donor_name].append(int(donation))
            break
        elif donation.isnumeric() and not exsting_donor:
            d[donor_name] = [int(donation)]
            break


###################
#  MAIN FUNCTIONS #
###################

def send_thank_you():
    # donor_names = get_names()  # create a list of names only
    while True:
        response = input("\nEnter the name of a donor "
                         "('list' -> list of donors | 'main' -> "
                         "main menu)\n")
        if response == 'list':
            print("\nExisting donors\n-" + "\n-".join(d.keys()))
        elif response == 'main':
            init()
        elif response in d.keys():  # i.e. existing donor
            add_donation(response, exsting_donor=True)
            break
        elif response.isalpha():  # new donor
            add_donation(response, exsting_donor=False)
            break
    init()


def create_report():
    heading = "Donor Name | Total Given | Num Gifts | Average Gift\n"
    print(heading + seperator(heading))
    for k, v in d.items():
        print("{:10} ${:10.2f} {:10} {:15.2f}".format(k,
                                                      sum(v),
                                                      len(v),
                                                      (sum(v) / len(v))))
    init()  # return to main menu


def init():
    while True:
        heading = "\nMain Menu\n"
        print(heading + seperator(heading))
        choice = input("1 - Send a Thank You\n"
                       "2 - Create a Report\n"
                       "3 - Quit\n")
        if choice == '1':
            send_thank_you()
            break
        elif choice == '2':
            create_report()
            break
        elif choice == '3':
            print('Exiting...')
            quit()
            break


if __name__ == "__main__":
    init()
