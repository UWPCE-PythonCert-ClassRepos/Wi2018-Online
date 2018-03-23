#!/usr/bin/env python

from unittest.mock import patch
import unittest
import mailroom_lesson06
import random
import io
import sys

# construct list of donors with a frozen set, to later be used as keys in the dictionary
donor_names = frozenset(("Daniel Ocean", "Rusty Ryan", "Linus Caldwell", "Ruben Tishkoff", "Basher Tarr"))

# create donors with dict comprehension 
donors = {donor: [1000, 2000] for donor in donor_names}

class MailroomTestCase(unittest.TestCase):

    @patch('builtins.input', return_value = '1')
    def test_prompt_user_string_1(self, input):
    	self.assertEqual(mailroom_lesson06.prompt_user(), 1)

    @patch('builtins.input', return_value = '2')
    def test_prompt_user_string_2(self, input):
    	self.assertEqual(mailroom_lesson06.prompt_user(), 2)

    @patch('builtins.input', return_value = 4)
    def test_prompt_user_numeric_1(self, input):
    	self.assertEqual(mailroom_lesson06.prompt_user(), 4)    

    # I cannot get this unit test to pass. The formatting of the strings is not lining up. 
    @unittest.mock.patch('mailroom_lesson06.input', create = True)
    def test_send_a_thank_you(self, mocked_input):
    	captured_output = io.StringIO()
    	sys.stdout = captured_output
    	mocked_input.side_effect = ['Rusty Ryan', '500']
    	mailroom_lesson06.send_a_thank_you()
    	total_donations = sum(donors['Rusty Ryan'])
    	sys.stdout = sys.__stdout__
    	print(captured_output.getvalue())
    	expected_output = """Dear Rusty Ryan,
    	Thank you for your generous donations totaling $3500.00.
    	Best,
    	The Donation Foundation."""
    	self.assertEqual(captured_output.getvalue(), expected_output)
    	    

    

if __name__ == '__main__':
    unittest.main()



