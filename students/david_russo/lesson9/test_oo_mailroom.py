#!/usr/bin/env python

import oo_mailroom as oo_mr
import unittest
from unittest.mock import patch

class oo_mailroom_test(unittest.TestCase):

	# test 1
	def test_name(self):
		donor1 = oo_mr.Donor("the cat")
		self.assertEqual(donor1.name, "the cat")

	# test 2
	def test_donation_append(self):
		donor2 = oo_mr.Donor("Rusty Ryan")
		donor2.add_donation(100)
		self.assertEqual(donor2.donations, [100.0])

	# test 3
	def test_total_donations(self):
		donor3 = oo_mr.Donor("Mathew Richter")
		donor3.add_donation("450")
		donor3.add_donation(550)
		self.assertEqual(donor3.total_donations, 1000.00)

	# test 4
	def test_number_of_donations(self):
		donor4 = oo_mr.Donor("Daniel Ocean")
		donor4.add_donation("300")
		donor4.add_donation(600)
		donor4.add_donation(0.01)
		self.assertEqual(donor4.number_of_donations, 3)
	
	# test 5
	def test_average_donation_size(self):
		donor5 = oo_mr.Donor("Thomas Graham")
		donor5.add_donation(500)
		donor5.add_donation("1000")
		donor5.add_donation(1500)
		self.assertEqual(donor5.average_donation_size, 1000.0)

	# test 6
	def test_empty_dict(self):
		donor_list1 = oo_mr.DonorList()
		self.assertEqual(donor_list1.donors, {})

	# test 7
	def test_add_donor_to_donorList(self):
		donor6 = oo_mr.Donor("Sherm")
		donor_list2 = oo_mr.DonorList()
		donor_list2.add_donor(donor6)
		self.assertEqual(donor_list2.donor_list, ["Sherm"])

	# test 8
	@patch()
	def test_receive_input(self):
		with mock.patch('__builtin__.input', return_value = 'Earl'):
			donor_7a = oo_mr.Donor("Earl")
			donor_7b = oo_mr.Donor("Thomas")
			donor_7c = oo_mr.Donor("Wagner")
			donor_list3 = oo_mr.DonorList()
			donor_list3.add_donor(donor_7a)
			donor_list3.add_donor(donor_7b)
			donor_list3.add_donor(donor_7c)
			self.assertEqual(donor_list3.receive_thank_you_card_recepient_input(), "Earl")







if __name__ == '__main__':
    unittest.main()  
