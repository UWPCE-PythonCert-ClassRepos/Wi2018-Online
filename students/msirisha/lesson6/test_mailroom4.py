### Tests for mailroom4 ###
import unittest
import mailroom4 as mr
import os
import io
import sys

class MailroomTest(unittest.TestCase):

    def setUp(self):
        mr.donor_data = {"sai emani": [20.23, 30.456, 50.786],
                      "sirisha marthy": [67.89, 45.89],
                      "ani emani": [12.789, 5.456],
                      "charles dickens": [15.89, 89.20, 345.67],
                      "mark twain": [678.986]
                      }

    def test_donor_count(self):
        self.assertEqual(5, len(mr.donor_data))

    def test_generate_letter(self):
        donor = list(mr.donor_data.keys())[0]
        self.expected_text = "Dear {},\n \nThank you for your generous donation {}.\n \n\n\t\tSincerely, \n\t\tLocal Charity". \
            format(donor, mr.donor_data[donor][-1])
        self.assertEqual(self.expected_text, mr.generate_letter(donor))

    def test_send_letters(self):
        mr.send_letters()
        for donor in mr.donor_data.keys():
            assert os.path.isfile(donor + ".txt")

    def test_create_report(self):
        expected_report = \
'''
Donor Name                | Total Given | Num Gifts | Average Gift
sai emani                  $     101.47           3 $       33.82
sirisha marthy             $     113.78           2 $       56.89
ani emani                  $      18.25           2 $        9.12
charles dickens            $     450.76           3 $      150.25
mark twain                 $     678.99           1 $      678.99
'''
        capture_print = io.StringIO()
        sys.stdout = capture_print
        mr.create_a_report()
        sys.stdout = sys.__stdout__

        self.assertEqual(capture_print.getvalue().strip(), expected_report.strip())

    def tearDown(self):
        for filename  in os.listdir("."):
            if filename.endswith(".txt"):
                if filename[:-4] in mr.donor_data.keys():
                    os.remove(filename)


if __name__ == "__main__":
    unittest.main()

