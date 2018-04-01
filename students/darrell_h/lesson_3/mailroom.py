#!/usr/local/bin/python3

donors = [['jack', [100, 200, 300, 400]],
          ['mary', [3000, 5000]],
          ['frank', [29.50, 31]],
          ['jane', [3000, 5000]],
          ['scrouge', [1, 2, 3]],
          ['bob', [60000, 70000, 80000]]]


#####################
#  HELPER FUNCTIONS #
#####################

def seperator(str):
    # return line that equals string length ignoring newline.
    return "-" * (len(str) - str.count('\n'))


def get_summary():
    summary = []
    for donor in donors:
        summary.append([donor[0],  # name
                        sum(donor[1]),  # total donation
                        len(donor[1]),  # number of donations
                        sum(donor[1]) / len(donor[1])])  # average donation
    return summary


def get_names():
    names = []
    for donor in donors:
        names.append(donor[0])
    return names


def add_donation(donor_name, exsting_donor):
    while True:
        donation = input(
            f"\nEnter a donation amount for {donor_name.capitalize()}: ")
        if donation.isnumeric() and exsting_donor:
            for index, donor in enumerate(donors):
                if donor[0] == donor_name:  # existing donor
                    donors[index][1].append(int(donation))
            break
        elif donation.isnumeric() and not exsting_donor:
            donors.append([donor_name, [int(donation)]])
            break


###################
#  MAIN FUNCTIONS #
###################

def send_thank_you():
    donor_names = get_names()  # create a list of names only
    while True:
        response = input("\nEnter the name of a donor "
                         "('list' -> list of donors | 'main' -> "
                         "main menu)\n")
        if response == 'list':
            print("\nExisting donors\n - " + "\n - ".join(donor_names))
        elif response == 'main':
            init()
        elif response in donor_names:  # i.e. existing donor
            add_donation(response, exsting_donor=True)
            break
        elif response.isalpha():  # new donor
            add_donation(response, exsting_donor=False)
            break
    init()


def create_report():
    donor_data = []
    donor_data = get_summary()
    heading = "Donor Name | Total Given | Num Gifts | Average Gift\n"
    print(heading + seperator(heading))
    for item in donor_data:
        print("{:10} ${:10.2f} {:10} {:15.2f}".format(item[0],
                                                      item[1],
                                                      item[2],
                                                      item[3]))
    init()


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
