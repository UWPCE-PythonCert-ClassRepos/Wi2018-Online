
#import mailroom_part4
from mailroom_part4 import *
import unittest
import pytest

#Every function is called by the test

def test_donation_numbers():
    """Test accuracy of report statistics"""
    total_donation, count_donation, average_donation = donation_numbers()
    assert total_donation['Shayna Hill'] == 150
    assert total_donation['Shayna Hill'] == 150
    assert count_donation['Lisa Rodriguez'] == 2
    assert count_donation['Charlie Smith'] == 1
    assert average_donation['Lisa Rodriguez'] == 15   
    assert average_donation['Marge Simpson'] == 100

    #def test_report_generation():
    #    """Test that the report is complete and accurate."""


def test_thank_you():
    thank_you()



