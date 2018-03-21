#!/usr/bin/env python3

# Week 6
# Mailroom Assignment testing - Part 4
import os
import sys
import pytest
import mailroom4


def test_print_donor_list():
    """Test printing the donor list."""
    donor = mailroom4.print_donor_list()
    assert donor[0] == 'Jimmy Nguyen'
    assert donor[1] == 'Steve Smith'


def test_get_donor():
    """Testing that the name is pulled correctly."""
    name_one = "Jimmy Nguyen"
    name_two = "Elizabeth McBath"

    assert name_one in mailroom4.donors.keys()
    assert name_two in mailroom4.donors.keys()


def test_create_report():
    """Test for creating a report of donors with donation amounts."""

    report_keys = mailroom4.donors.keys()
    report_values = list(mailroom4.donors.values())

    assert "Jimmy Nguyen" in report_keys
    assert report_values[0][1] == 1350


def test_letter():
    """Test the letter function."""
    letter = """Dear {},\nThank you for your very kind donation of {:.2f}.\n\nIt will be put to very good use.\n\n \t\tSincerely,\n\t\t\t-The Team"""
    donor_list = list(mailroom4.donors.keys())
    donor = donor_list[0]
    result = mailroom4.letter(donor)
    assert result == letter.format(donor, mailroom4.donors[donor][-1])


def test_send_letter_file():
    """Test for writing a letter to a donor."""
    # pytest.set_trace()  # invoke PDB debugger and tracing
    mailroom4.send_letter_file()

    assert os.path.isfile("Jimmy Nguyen.txt")
    assert os.path.isfile("Elizabeth McBath.txt")
