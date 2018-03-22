import mailroom_3 as mailroom
import unittest
import os


class MailRoomUnittest(unittest.TestCase):

    def test_print_donor_list(self):
        self.donate_list = mailroom.donor_names()
        try:
            if self.donate_list is not None:
                print(self.donate_list)
        except ValueError:
            print("Not Donor Names")

    def test_create_report_files(self):
        text = mailroom.create_report()
        try:
            if text is not None:
                print(text)
        except ValueError:
            print("Not Donor Names")

        mailroom.create_report_files()
        file = mailroom.send_file_name
        try:
            print(file, os.path.exists(file))
        except FileNotFoundError:
            print("The file {} is not found".format(file))

    def test_thank_note(self):
        self.donate_list = mailroom.donor_names()
        text_1 = mailroom.thank_note("all donors")
        try:
            if "Thank" in text_1:
                print(text_1)
        except ValueError:
            print("No Thank you Note found")

        text_2 =mailroom.thank_note(self.donate_list[0], "single")
        try:
            if "Thank" in text_2:
                print(text_2)
        except ValueError:
            print("No Thank you Note found")


if __name__ == '__main__':
    unittest.main()