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

	# test 13
	def test_challenge_donor_with_filter(self):
		# create a donor object and add some donations
		walt = fp_mr.Donor("Walt")
		walt.add_donation(99)
		walt.add_donation(150)
		walt.add_donation(201)

		# filter out all donations less than 100 and greater than 200
		walt_post_filter = walt.challenge(inflation_factor = 1, min_donations = 100, max_donations = 200)
		self.assertEqual(walt_post_filter.donations, [150.00])

	# test 14
	def test_challenge_donor_with_filter_db(self):
		# create two donors with some donations		
		the_cb = fp_mr.Donor("Griffin")
		the_cb.add_donation(2000)
		the_cb.add_donation(5000)

		the_lb = fp_mr.Donor("Wagner")
		the_lb.add_donation(10000)
		the_lb.add_donation(100)

		# create a DonorList() and add the donors
		defense = fp_mr.DonorList()
		defense.add_donor(the_cb)
		defense.add_donor(the_lb)

		# filter out donations less than 1000 and greater than 6000
		defense_post_challenge = defense.challenge_donors(inflation_factor = 1, min_donations = 1000, max_donations = 6000)

		# get new donation lists
		the_cb_post = list(defense_post_challenge.donors['Griffin'].donations)
		the_lb_post = list(defense_post_challenge.donors['Wagner'].donations)

		self.assertEqual([the_cb_post, the_lb_post], [[2000.0, 5000.0], []])

	# test 15
	def test_challenge_donor_with_projection_under100(self):
		# create a donor with some donations		
		the_cb = fp_mr.Donor("Griffin")
		the_cb.add_donation(50)
		the_cb.add_donation(75)
		the_cb.add_donation(787)
		the_cb.add_donation(797)

		# double contributions under 100
		the_cb_projected = the_cb.challenge(inflation_factor = 2, max_donations = 100, projection = True)

		self.assertEqual(the_cb_projected.donations, [100.0, 150.0, 787.0, 797.0])

	# test 16
	def test_challenge_donor_with_projection_over50(self):
		# create a donor with some donations		

		the_lb = fp_mr.Donor("Wagner")
		the_lb.add_donation(25)
		the_lb.add_donation(49)
		the_lb.add_donation(130)
		the_lb.add_donation(155)

		# triple contributions over 50
		the_lb_projected = the_lb.challenge(inflation_factor = 3, min_donations = 50, projection = True)

		self.assertEqual(the_lb_projected.donations, [390.0, 465.0, 25.0, 49.0])

	# test 17
	def test_challenge_donor_db_with_projection_over50(self):
		# create two donors with some donations		
		the_cb = fp_mr.Donor("Griffin")
		the_cb.add_donation(50)
		the_cb.add_donation(75)
		the_cb.add_donation(787)
		the_cb.add_donation(797)

		the_lb = fp_mr.Donor("Wagner")
		the_lb.add_donation(25)
		the_lb.add_donation(49)
		the_lb.add_donation(130)
		the_lb.add_donation(155)

		# create a DonorList() and add the donors
		defense = fp_mr.DonorList()
		defense.add_donor(the_cb)
		defense.add_donor(the_lb)

		# project donor database where all contributions under 100 are doubled
		defense_post_challenge = defense.challenge_donors(inflation_factor = 2, max_donations = 100, projection = True)

		# get new donation lists
		the_cb_post = list(defense_post_challenge.donors['Griffin'].donations)
		the_lb_post = list(defense_post_challenge.donors['Wagner'].donations)

		self.assertEqual([the_cb_post, the_lb_post], [[100.0, 150.0, 787, 797], [50.0, 98.0, 130.0, 155.0]])		







if __name__ == '__main__':
    unittest.main()  
