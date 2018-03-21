#!/usr/bin/env python

import fp_mailroom as fp_mr
import unittest
from unittest.mock import patch
from unittest import mock
import io
import sys
import os

class oo_mailroom_test(unittest.TestCase):

	# test 1
	def test_name(self):
		donor1 = fp_mr.Donor("the cat")
		self.assertEqual(donor1.name, "the cat")

	# test 2
	def test_donation_append(self):
		donor2 = fp_mr.Donor("Rusty Ryan")
		donor2.add_donation(100)
		self.assertEqual(donor2.donations, [100.0])

	# test 3
	def test_total_donations(self):
		donor3 = fp_mr.Donor("Mathew Richter")
		donor3.add_donation("450")
		donor3.add_donation(550)
		self.assertEqual(donor3.total_donations, 1000.00)

	# test 4
	def test_number_of_donations(self):
		donor4 = fp_mr.Donor("Daniel Ocean")
		donor4.add_donation("300")
		donor4.add_donation(600)
		donor4.add_donation(0.01)
		self.assertEqual(donor4.number_of_donations, 3)
	
	# test 5
	def test_average_donation_size(self):
		donor5 = fp_mr.Donor("Thomas Graham")
		donor5.add_donation(500)
		donor5.add_donation("1000")
		donor5.add_donation(1500)
		self.assertEqual(donor5.average_donation_size, 1000.0)

	# test 6
	def test_empty_dict(self):
		donor_list1 = fp_mr.DonorList()
		self.assertEqual(donor_list1.donors, {})

	# test 7
	def test_add_donor_to_donorList(self):
		donor6 = fp_mr.Donor("Sherm")
		donor_list2 = fp_mr.DonorList()
		donor_list2.add_donor(donor6)
		self.assertEqual(donor_list2.donor_list, ["Sherm"])

	# test 8
	@patch('builtins.input', return_value = "Earl")
	def test_receive_input(self, input):
		donor_list3 = fp_mr.DonorList()
		answer = donor_list3.receive_thank_you_card_recepient_input()
		self.assertEqual(answer, "Earl")

	# test 9
	@patch('builtins.input', create = True)
	def test_send_a_thank_you(self, mocked_input):
		mocked_input.side_effect = ['Earl', 400]
		donor_list4 = fp_mr.DonorList()
		donor_list4.add_donor(fp_mr.Donor("Earl"))
		out = io.StringIO()
		donor_list4.send_a_thank_you(out=out)
		output = out.getvalue().strip()
		self.assertEqual("Dear Earl, \nThank you for your generous donations totaling $400.00. \nBest, The Donation Foundation", output)

	# test 10
	def test_send_letters_to_everyone(self):		
		# create cat and dog donors
		cat = fp_mr.Donor("cat")
		cat.add_donation(50)
		cat.add_donation(50)

		dog = fp_mr.Donor("dog")
		# it's been a ruff year, only $2 in donations
		dog.add_donation(1)
		dog.add_donation(1)

		# create a donor list and add the cat and dog donors
		animal_donors = fp_mr.DonorList()
		animal_donors.add_donor(cat)
		animal_donors.add_donor(dog)

		if(os.path.isfile("thank_you_cat.txt")):
			os.remove("thank_you_cat.txt")
		if(os.path.isfile("thank_you_dog.txt")):
			os.remove("thank_you_dog.txt")

		animal_donors.send_letters_to_everyone()

		self.assertEqual(os.path.isfile("thank_you_cat.txt") & os.path.isfile("thank_you_dog.txt"), True)

	# test 11
	def test_challenge_donor(self):
		# create a donor object and add some donations
		ray = fp_mr.Donor("Ray")
		ray.add_donation(50)
		ray.add_donation(100)
		ray.add_donation(500)

		# inflate the donations by a factor of 2
		ray_post_challenge = ray.challenge(inflation_factor = 1.5)
		self.assertEqual(ray_post_challenge.donations, [75.0, 150.0, 750.0])

	# test 12
	def test_challenge_donor_db(self):
		# create two donors with some donations		
		the_cb = fp_mr.Donor("Griffin")
		the_cb.add_donation(100)
		the_cb.add_donation(200)

		the_lb = fp_mr.Donor("Wagner")
		the_lb.add_donation(5000)
		the_lb.add_donation(10000)

		# create a DonorList() and add the donors
		defense = fp_mr.DonorList()
		defense.add_donor(the_cb)
		defense.add_donor(the_lb)

		# inflate the donations by 10
		defense_post_challenge = defense.challenge_donors(inflation_factor = 10)

		# get new donation lists
		the_cb_post = defense_post_challenge.donors['Griffin'].donations
		the_lb_post = defense_post_challenge.donors['Wagner'].donations

		self.assertEqual([the_cb_post, the_lb_post], [[1000.0, 2000.0], [50000.0, 100000.0]])




if __name__ == '__main__':
    unittest.main()  
