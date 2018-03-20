import mailroom_3 as mailroom
import unittest


class MailRoomUnittest(unittest.TestCase):

    def test_print_donor_list(self):
        print("I'm here")
        self.donate_list = mailroom.donor_names()
        print(self.donate_list)

    def test_create_report_files(self):
        mailroom.create_report()
        mailroom.create_report_files()

    def test_thank_note(self):
        self.donate_list = mailroom.donor_names()
        mailroom.thank_note("all donors")
        mailroom.thank_note(self.donate_list[0], "single")


if __name__ == '__main__':
    unittest.main()