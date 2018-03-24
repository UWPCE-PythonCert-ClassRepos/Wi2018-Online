#!/usr/bin/env python3
"""
Unit Tests to test the Mail Room Program
__author__ = "Padmaja Peri"
"""

import mailroom_part3 as mailroom
import unittest


class TestMailRoom(unittest.TestCase):

    def test_donor_names(self):
        """ Method to verify the donor names returned"""
        actual_donor_names = list(mailroom.donor_names())
        expected_donor_names = ['William Gates III', 'Mark Zuckerberg',
                                       'Jeff Bezos', 'Larry Page',
                                'Steve Jobs']
        self.assertEqual(actual_donor_names, expected_donor_names,
                         "Pre-populated donor names in mailroom program does "
                         "not match expected list. Expected is:{} and Actual "
                         "is:{}".format(expected_donor_names,
                                        actual_donor_names))

    def test_thank_you(self):
        """ Method to verify the thank you text generated """
        expected_thankyou_text = "Dear  {} , \nThank you very much for your " \
                               "recent donation" \
                 " to XYZ Charity for an amount of {}. \n" \
                 "The funds raised will go towards X, Y and Z. Thank You " \
                 "again for your kindness.\nSincerely,\nThe Team\n".\
                format("Steve Jobs", 60000)
        actual_thankyou_text = mailroom.print_thank_you('Steve Jobs')
        self.assertEqual(expected_thankyou_text, actual_thankyou_text,
                         "Expected and Actual Thank You notes do not match. "
                         "Expected is:{} and Actual is:{}".
                          format(expected_thankyou_text, actual_thankyou_text))

    def test_write_to_file(self):
        """ Method to verify if the file is getting generated """
        mailroom.print_thank_you('Steve Jobs', write_to_file=1)
        try:
            with open('Steve_Jobs.txt', 'r') as fd:
                pass
        except FileNotFoundError:
            raise self.fail("Expected Thank You File not found in the "
                            "location.")

    def test_send_thanks_to_all_donors(self):
        """ Method to verify if the file are getting generated for all users"""
        donors = ['William Gates III', 'Mark Zuckerberg',
                 'Jeff Bezos', 'Larry Page', 'Steve Jobs']
        for donor in donors:
            mailroom.print_thank_you(donor, write_to_file=1)
            file_name = "_".join(donor.split()) + '.txt'
            try:
                with open(file_name, 'r') as fd:
                    pass
            except FileNotFoundError:
                raise self.fail("Expected File {} not found in the "
                                "location.".format(file_name))


if __name__ == '__main__':
    unittest.main()
