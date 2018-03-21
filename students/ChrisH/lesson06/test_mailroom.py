#!/usr/bin/env python3
# -----------------------------------------------------------
# test_mailroom.py
#  uses unittest module to test mailroom.py program
# -----------------------------------------------------------

import io
import os
import sys
import unittest

import mailroom as mr


class MailroomTest(unittest.TestCase):

    def setUp(self):
        mr.donor_data = \
            {mr.Donor('Al', 'Donor1'): [10.00, 20.00, 30.00, 40.00, 50.00],
             mr.Donor('Bert', 'Donor2'): [10.00],
             mr.Donor('Connie', 'Donor3'): [10.00, 10.00, 10.01],
             mr.Donor('Dennis', 'Donor4'): [10.00, 20.00, 20.00],
             mr.Donor('Egbert', 'Donor5'): [10.39, 20.21, 10.59, 4000.40],
             mr.Donor('TESTME', 'TESTME'): [11.39, 22.21, 11.59, 4001.40],
             }

    def test_donor_count(self):
        self.assertEqual(6, len(mr.donor_data))

    def test_get_donor_fullname(self):
        self.assertEqual(mr.get_donor_fullname(mr.Donor('X', 'Y')), 'X Y')
        self.assertEqual(mr.get_donor_fullname(mr.Donor('   THREE', 'THREE   ')), 'THREE THREE')

    def test_print_report(self):
        report_text = \
            '''
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
Al Donor1                  $     150.00           5  $       30.00
Bert Donor2                $      10.00           1  $       10.00
Connie Donor3              $      30.01           3  $       10.00
Dennis Donor4              $      50.00           3  $       16.67
Egbert Donor5              $    4041.59           4  $     1010.40
TESTME TESTME              $    4046.59           4  $     1011.65
'''

        capturedprint = io.StringIO()           # Redirect stdout to a stringIO object
        sys.stdout = capturedprint
        mr.print_report()                       # Execute function that uses stdout
        sys.stdout = sys.__stdout__             # Reset stdout back to normal
        self.assertEqual(capturedprint.getvalue().strip(), report_text.strip())

    def test_generate_letter(self):
        for donor in mr.donor_data:
            format_string = mr.generate_letter(donor)
            self.assertIn(donor.first, format_string)
            self.assertIn(donor.last, format_string)
            self.assertIn(str(mr.donor_data[donor][-1]), format_string)  # Test donor's last donation is in letter

    def test_send_letters_all(self):
        capturedprint = io.StringIO()  # Redirect stdout to a stringIO object
        sys.stdout = capturedprint
        mr.send_letters_all()
        sys.stdout = sys.__stdout__
        for filename in os.listdir('.'):
            if filename.endswith('.txt'):
                donorname = ((filename[9:-4]).replace("_", " ")).split()
                self.assertIn(mr.Donor(donorname[0], ' '.join(donorname[1:])), mr.donor_data.keys())

    def test_get_donor(self):
        self.assertIsNone(mr.get_donor(''))
        self.assertIsNotNone(mr.get_donor('Al Donor1'))
        self.assertIsNotNone(mr.get_donor('NEW DONOR'))

    def tearDown(self):
        # Removes files created by test_send_letters_all
        for filename in os.listdir('.'):
            if filename.endswith('.txt'):
                donorname = ((filename[9:-4]).replace("_", " ")).split()
                if mr.Donor(donorname[0], ' '.join(donorname[1:])) in mr.donor_data.keys():
                    os.remove(filename)


if __name__ == "__main__":
    unittest.main()

