
donate_list = [['William Gates', 500, 500.5], ['Mark Zuckerberg', 300, 300.6, 500, 600], ['Jeff Bezos', 800, 970.44], ['Paul Allen', 1, 1000, 780.5]]


def donor_names():
    donor_name = []
    for name in donate_list:
        donor_name.append(name[0])
    return donor_name


def thank_you_note():
    donor_name = raw_input("Please enter the Full Name of the donor to send thank you note or enter \"list donors\" to see the list of donors:")
    if donor_name == '0':
        return
    else:
        if donor_name == 'list donors':
            print("List of Donors are:{}".format(donor_names()))
            thank_you_note()
        elif donor_name not in donor_names():
            amount = raw_input("You have entered a New Donor \n Please enter the donation amount to be added to donor {}:".format(donor_name))
            amount = float(amount)
            donate_list.append([donor_name, amount])
            thank_note(donor_name)
        elif donor_name in donor_names():
            thank_note(donor_name)


def thank_note(donor_name):
    space = " "*40
    thank_note = "Dear  {}, \n Thank you very much for your recent donation! \n {} Thank You, \n {} Charity A".format(donor_name, space, space)
    print(thank_note)


def create_report():
    print("{: <23s} | {: <15s} | {: <10s} | {: <18s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))

    print("-" * 75)
    for each_donation in donate_list:
        total = sum(each_donation[1:])
        no_of_gifts = len(each_donation[1:])
        average = total / no_of_gifts
        print("{:20s}    $  {:13.5f} {:10d}    $  {:13.5f}".format(each_donation[0], total, no_of_gifts, average))


def main_menu():
    print("Enter 1 to send a Thank You note")
    print("Enter 2 to create a report of all the donors")
    print("Enter 0 at any point to return to main menu")
    print("Enter any other number to quit")

if __name__ == "__main__":
    while True:
        main_menu()
        response = raw_input("Choose from the above menu: ")
        if response == "1":
            thank_you_note()
        elif response == "2":
            create_report()
        else:
            print("Entered a choice to QUIT... ")
            break