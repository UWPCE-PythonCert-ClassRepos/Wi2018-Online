#!/usr/bin/env python3

# Lesson09
# Mailroom Assignment Testing - Part 5 - OOP
# Perform testing on the object oriented version of mailroom_oo.py
import sys
import pytest
import mailroom_oo as mailroom




def test_list_donor():
    """Test that the list of donors is returned correctly."""
    d1 = mailroom.Donor()
    listing = d1.show_donor_names()
    assert "Jimmy Nguyen" in listing
    assert "Elizabeth McBath" in listing



# def test_donor_lookup():
#     """Checks a donor that is there, but with odd case and spaces"""
#     d1 = mailroom.Donor()
#     donor = d1.donor_lookup("Jimmy Nguyen")
#     assert donor[0] == "Jimmy Nguyen"
#
#
# def test_find_donor_not():
#     """test one that's not there."""
#     d1 = mailroom.Donor()
#     donor = d1.find_donor("Jimmy Nguyen")
#     assert donor is None
#
#
# def test_gen_letter():
#     """Test the donor letter"""
#     d1 = mailroom.Donor()
#     donor = ("Daniel Grubbs", [432.45, 65.45, 230.0])
#     letter = d1.gen_letter(donor)
#     assert letter.startswith("Dear Daniel Grubbs")
#     assert letter.endswith("-The Team\n")
#     assert "donation of $230.00" in letter
#
#
# def test_add_donor():
#     d1 = mailroom.Donor()
#     name = "    Daniel Grubbs    "
#     donor = d1.add_donor(name)
#     donor[1].append(1500)
#     assert donor[0] == "Daniel Grubbs"
#     assert donor[1] == [300]
#     assert d1.find_donor(name) == donor
#
#
# def test_create_donor_report():
#     d1 = mailroom.Donor()
#     report = d1.create_donor_report()
#     print(report)
#
#     assert report.startswith(
#         "Donor Name")
#
#     assert "Jimmy Nguyen                  $    1505           3   $     1505" in report
#
#
#
# def test_save_letters_to_disk():
#     """Test for file creation. Verify that one of the files created is not empty."""
#     d1 = mailroom.Donor()
#     d1.send_letter_file()
#
#     assert os.path.isfile('Jimmy Nguyen.txt')
#     assert os.path.isfile('Elizabeth McBath.txt')
#
#     # Verify that the file has some content
#     with open('Jimmy Nguyen.txt') as f:
#         size = len(f.read())
#     assert size > 0
