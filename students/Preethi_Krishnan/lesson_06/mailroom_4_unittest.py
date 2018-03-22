import mailroom_3 as mailroom
import unittest
import os


class MailRoomUnittest(unittest.TestCase):
    def setUp(self):
        self.donate_unit_list = [['William Gates', 500, 500.5], ['Mark Zuckerberg', 300, 300.6, 500, 600], ['Jeff Bezos', 800, 970.44], ['Paul Allen', 1, 1000, 780.5]]
        self.file_names = ["William_Gates.txt", "Mark_Zuckerberg.txt", "Jeff_Bezos.txt", "Paul_Allen.txt"]

    def test_check_donor_list(self):
        total_donors = len(self.donate_unit_list)
        i = 0
        while i < total_donors:
            assert(self.donate_unit_list[i][0] in mailroom.donor_names())
            print(self.donate_unit_list[i][0])
            i = i+1

    def test_create_report_files(self):
        mailroom.create_report_files()
        for file in self.file_names:
            if os.path.exists(file):
                print("File name is created and exists: {}".format(file))
                with open(file, 'r') as f:
                    line = f.readline()
                    #print(line)
                    assert("Dear " in line)

    def test_thank_you_note(self):
        donor_complete_list = mailroom.donor_names()
        for one_donor in donor_complete_list:
            note = mailroom.thank_note(one_donor)
            assert("Thank you very much for your recent donation!" in note)
        note1 = mailroom.thank_note(donor_complete_list)
        for one_donor in donor_complete_list:
            assert(one_donor in note1)

if __name__ == '__main__':
    unittest.main()