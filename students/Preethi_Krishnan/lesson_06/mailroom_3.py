import sys
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
            try:
                amount = input("You have entered a New Donor \n Please enter the donation amount to be added to donor {}:".format(donor_name))
                amount = float(amount)
                donate_list.append([donor_name, amount])
                thank_note(donor_name)
            except NameError:
                amount = input("Enter a valid amount")
                amount = float(amount)
                donate_list.append([donor_name, amount])
                thank_note(donor_name)
        elif donor_name in donor_names():
            thank_note(donor_name)


def thank_note(donor_name, choice="single"):
    space = " "*40
    #"Dear  {}, \n Thank you for your very kind donation of ${}. \n It will be put to very good use. \n {} Sincerely, {}-The Charity Team".format(donor_name, space, space)
    if choice in "single":
        thank_note = "Dear  {}, \n Thank you very much for your recent donation! \n {} Thank You, \n {} Charity A".format(donor_name, space, space)
        print(thank_note)
        return thank_note
    elif choice in "all donors":
        for sub_list in donate_list:
            if sub_list[0] == donor_name:
                total = sum(sub_list[1:])
        thank_note = "Dear  {}, \n Thank you for your very kind donation of ${}. \n It will be put to very good use. \n {} Sincerely, \n {}-The Charity Team \n".format(donor_name, total, space, space)
        return thank_note

def create_report():
    print("{: <23s} | {: <15s} | {: <10s} | {: <18s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))

    print("-" * 75)
    for each_donation in donate_list:
        total = sum(each_donation[1:])
        no_of_gifts = len(each_donation[1:])
        average = total / no_of_gifts
        print("{:20s}    $  {:13.5f} {:10d}    $  {:13.5f}".format(each_donation[0], total, no_of_gifts, average))
        report_note = "{:20s}    $  {:13.5f} {:10d}    $  {:13.5f}".format(each_donation[0], total, no_of_gifts, average)
        return report_note

def create_report_files():
    global send_file_name
    for name in donor_names():
        send_file = name.split()
        send_file_name = send_file[0] + "_" + send_file[1] + ".txt"
        with open(send_file_name, 'w') as f:
            f.writelines(thank_note(name, "all donors"))

def main_menu():
    print("Enter 0 at any point to return to Main Menu")
    print("Enter 1 to Send a Thank You note")
    print("Enter 2 to Create a report of all the donors")
    print("Enter 3 to Create files to send thank you note to all donors")
    print("Enter 4 to Quit")

if __name__ == "__main__":
    response_dict = {"1": thank_you_note, "2": create_report, "3": create_report_files, "4": sys.exit}
    while True:
        main_menu()
        response = raw_input("Choose from the above menu: ")
        try:
            response_dict.get(response)()
        except TypeError:
            response = raw_input("Please choose only from 1, 2, 3, 4")
            response_dict.get(response)()

