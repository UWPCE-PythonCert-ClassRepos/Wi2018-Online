import sys
import os

class MailRoom(object):
    def __init__(self):
        self.donation_dict= {"William Gates": [500, 500.5],
                          'Mark Zuckerberg': [300, 300.6, 500, 600],
                          'Jeff Bezos': [800, 970.44],
                          'Paul Allen': [1, 1000, 780.5]
                        }

    def add_new_donor(self, new_name, new_donation):
        self.donation_dict[new_name] = [new_donation]

    def check_donor(self, check_donor):
        return check_donor in self.donation_dict.keys()

    def get_donor_names(self):
        donors_list = list(self.donation_dict.keys())
        return donors_list

    def create_report(self):
        print("{: <23s} | {: <15s} | {: <10s} | {: <18s}".format("Donor Name", "Total Given", "Num Gifts",
                                                                 "Average Gift"))
        print("-" * 75)
        donors = self.get_donor_names()
        #print(donors)
        for every_donor in donors:
            total_each_donation = []
            total_each_donation.append(self.donation_dict[every_donor])
            total_donation_list = [sum(i) for i in zip(*total_each_donation)]
            total_donation = sum(total_donation_list)
            total_gifts = len(total_donation_list)
            average = total_donation / total_gifts
            print("{:20s}    $  {:13.5f} {:10d}    $  {:13.5f}".format(every_donor, total_donation, total_gifts, average))
            report_note = "{:20s}    $  {:13.5f} {:10d}    $  {:13.5f}".format(every_donor, total_donation, total_gifts,
                                                                               average)
            #return report_note

    def create_report_files(self):
        print("{: <23s} | {: <15s} | {: <10s} | {: <18s}".format("Donor Name", "Total Given", "Num Gifts",
                                                                 "Average Gift"))
        print("-" * 75)
        donors = self.get_donor_names()
        for every_donor in donors:
            total_each_donation = []
            total_each_donation.append(self.donation_dict[every_donor])
            total_donation_list = [sum(i) for i in zip(*total_each_donation)]
            total_donation = sum(total_donation_list)
            total_gifts = len(total_donation_list)
            average = total_donation / total_gifts
            #print("{:20s}    $  {:13.5f} {:10d}    $  {:13.5f}".format(every_donor, total_donation, total_gifts, average))
            report_note = "{:20s}    $  {:13.5f} {:10d}    $  {:13.5f}".format(every_donor, total_donation, total_gifts,
                                                                               average)
            report_file = every_donor.split()
            report_file_name = report_file[0] + "_" + report_file[1] + "_report" + ".txt"
            with open(report_file_name, "w") as f:
                f.writelines(report_note)
        files = [f for f in os.listdir('.') if os.path.isfile(report_file_name)]
        print(files)


    def create_thank_files(self):
        global send_file_name
        donors = self.get_donor_names()
        for every_donor in donors:
            send_file = every_donor.split()
            send_file_name = send_file[0] + "_" + send_file[1] + ".txt"
            with open(send_file_name, 'w') as f:
                f.writelines(self.thank_note(every_donor))
        files = [f for f in os.listdir('.') if os.path.isfile(send_file_name)]
        print(files)

    def thank_note(self):
        donor_name = input("Please give the donor name")
        space = " " * 40
        if self.check_donor(donor_name):
            note = "Dear  {}, \n Thank you very much for your recent donation! \n {} Thank You, \n {} Charity A".format(
                donor_name, space, space)
            print(note)
            return note
        else:
            print("You have entered a new donor: {}".format(donor_name))
            print("Adding Donor to the existing list")
            new_donor_name = donor_name
            new_donation = input("Please enter the donation amount")
            self.add_new_donor(new_donor_name, new_donation)
            print("The new list of donors are: {}".format(self.get_donor_names()))
            note = "Dear  {}, \n Thank you very much for your recent donation! \n {} Thank You, \n {} Charity A".format(
                donor_name, space, space)
            return note


    def thank_note_all(self):
        donors = self.get_donor_names()
        space = " " * 40
        for every_donor in donors:
            note = "Dear  {}, \n Thank you very much for your recent donation! \n {} Thank You, \n {} Charity A".format(
                every_donor, space, space)
            print(note)

def main_menu():
    print("Choose from one of the following options: ")
    print("1. Send a Thank You Note")
    print("2. Create a Report")
    print("3. Send Thank You Note to all Donors")
    print("4. Create Report files for all")
    print("5. Quit")

if __name__ == '__main__':

    mailroom = MailRoom()
    choice = {1: mailroom.thank_note,
              2: mailroom.create_report,
              3: mailroom.thank_note_all,
              4: mailroom.create_report_files,
              5: sys.exit}

    while True:
        main_menu()
        option_chosen = int(input("Choose from one of the following: "))
        choice.get(option_chosen)()
