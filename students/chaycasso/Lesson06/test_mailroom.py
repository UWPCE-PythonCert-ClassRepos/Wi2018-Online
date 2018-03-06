#!/usr/bin/env python3
#
# Test Mailroom script
# Chay Casso
# 3/4/2018

import unittest
from mailroom4 import Mailroom

class MailroomTest(unittest.TestCase):

    def test_thank_you_quit_1(self):
        """Test use of 'quit' statement in full_name does nothing."""
        donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                            "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                            "Steve Ballmer": [5198.96, 654.98]}
        m = Mailroom()
        new_dict, output_string = m.thank_you(donor_table_dict, "quit", "Test String")
        assert output_string == ""
        self.assertDictEqual(donor_table_dict, new_dict)

    def test_thank_you_quit_2(self):
        """Test use of 'quit' statement in donation_amount does nothing."""
        donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                            "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                            "Steve Ballmer": [5198.96, 654.98]}
        m = Mailroom()
        new_dict, output_string = m.thank_you(donor_table_dict, "Test String", "quit")
        assert output_string == ""
        self.assertDictEqual(donor_table_dict, new_dict)

    def test_thank_you_list(self):
        """Test use of 'list' statement in donation_amount outputs list of names."""
        donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                            "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                            "Steve Ballmer": [5198.96, 654.98]}
        m = Mailroom()
        new_dict, output_string = m.thank_you(donor_table_dict, "list", "Test String")
        assert output_string == """Donor list:
William Gates, III
Mark Zuckerberg
Jeff Bezos
Paul Allen
Steve Ballmer
"""
        self.assertDictEqual(donor_table_dict, new_dict)

    def test_thank_you_donation_is_string(self):
        """Test value not entered when donation_value is not a float."""
        donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                            "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                            "Steve Ballmer": [5198.96, 654.98]}
        m = Mailroom()
        new_dict, output_string = m.thank_you(donor_table_dict, "Test String", "Bad Value")
        assert output_string == "Not entered. Please enter a positive number value for the donation amount."
        self.assertDictEqual(donor_table_dict, new_dict)

    def test_thank_you_donation_is_nonpositive(self):
        """Test value not entered when donation_value is not a positive number."""
        donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                            "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                            "Steve Ballmer": [5198.96, 654.98]}
        m = Mailroom()
        new_dict, output_string = m.thank_you(donor_table_dict, "Test String", "-1")
        assert output_string == "Not entered. Please enter a positive number value for the donation amount."
        self.assertDictEqual(donor_table_dict, new_dict)

    def test_thank_you_success_existing_name(self):
        """Test value entered into dictionary and output created for existing name."""
        donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                            "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                            "Steve Ballmer": [5198.96, 654.98]}
        target_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                            "Jeff Bezos": [877.33, 910.21], "Paul Allen": [152.42, 30.54, 825.21],
                            "Steve Ballmer": [5198.96, 654.98]}
        m = Mailroom()
        new_dict, output_string = m.thank_you(donor_table_dict, "Jeff Bezos", "910.21")
        assert output_string == """
Dear Jeff Bezos:
    Thank you for your generous donation of $910.21 to Save the Kids.
                    
-------------
Save the Kids
save@kids.org
                    """
        self.assertDictEqual(target_table_dict, new_dict)

    def test_thank_you_success_new_name(self):
        """Test value entered into dictionary and output created for new name."""
        donor_table_dict = {"William Gates, III": [401321.52, 201342.71], "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                            "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                            "Steve Ballmer": [5198.96, 654.98]}
        target_table_dict = {"William Gates, III": [401321.52, 201342.71],
                             "Mark Zuckerberg": [123.45, 5123.21, 8213.11],
                             "Jeff Bezos": [877.33], "Paul Allen": [152.42, 30.54, 825.21],
                             "Steve Ballmer": [5198.96, 654.98], "New Guy": [910.21]}
        m = Mailroom()
        new_dict, output_string = m.thank_you(donor_table_dict, "New Guy", "910.21")
        assert output_string == """
Dear New Guy:
    Thank you for your generous donation of $910.21 to Save the Kids.
                    
-------------
Save the Kids
save@kids.org
                    """
        self.assertDictEqual(target_table_dict, new_dict)



if __name__ == '__main__':
    unittest.main()
