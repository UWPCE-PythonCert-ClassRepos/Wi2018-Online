#!/usr/bin/env python3

'''
 test_mailroom.py
 Unit test cases for the classes in mailroom.py 
'''

import unittest
import io
import os 
import sys
from mailroom import Mailroom
from mailroom import Donor


class TestMailroom(unittest.TestCase):
	def test_create_donor_without_donation(self):
		expected_val = "Sireesha Sankuratripati"
		donor = Donor (expected_val)
		self.assertEqual(expected_val, donor.donor_name)

	def test_create_donor_with_empty_donation(self):
		expected_val = "Sireesha Sankuratripati"
		donor = Donor (expected_val,[])
		self.assertEqual(expected_val, donor.donor_name)
		print (donor.donation_amounts_list)

	def test_create_donor_with_donations(self):
		donor_name = "Sireesha Sankuratripati"
		donations_list = [900.99,1000.90,2010.99]
		donor = Donor (donor_name,donations_list)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(len(donations_list), len(donor.donation_amounts_list))
		#compare the data
		for index in range(0,len(donations_list)):
			self.assertEqual(donations_list[index], donor.donation_amounts_list[index]) #every item should be equal and in the same order

	def test_add_first_donation_to_donor(self):
		donor_name = "Sireesha Sankuratripati"
		donor = Donor (donor_name)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(0, len(donor.donation_amounts_list))
		#add a donation
		donation_val = 1000.90
		donor.add_donation(donation_val)
		self.assertEqual(1, len(donor.donation_amounts_list))
		self.assertEqual(donation_val, donor.donation_amounts_list[0])

	def test_add_multiple_donations_to_donor(self):
		donor_name = "Sireesha Sankuratripati"
		donor = Donor (donor_name)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(0, len(donor.donation_amounts_list))
		#add a donation
		donation_val = 2000.90
		donor.add_donation(donation_val)
		self.assertEqual(1, len(donor.donation_amounts_list))
		self.assertEqual(donation_val, donor.donation_amounts_list[0])

		donation_val = 12000.00
		donor.add_donation(donation_val)
		self.assertEqual(2, len(donor.donation_amounts_list))
		self.assertEqual(donation_val, donor.donation_amounts_list[1])

	def test_add_invalid_amount(self):
		donor_name = "Sireesha Sankuratripati"
		donor = Donor (donor_name)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(0, len(donor.donation_amounts_list))
		#add a donation
		donation_val = 'i am not a number'
		with self.assertRaises(TypeError):
			donor.add_donation(donation_val)
		donation_val = -1000
		with self.assertRaises(ValueError):
			donor.add_donation(donation_val)

	def test_get_last_donation_amount(self):
		donor_name = "Sireesha Sankuratripati"
		donations_list = [900.99,1000.90,2010.99]
		donor = Donor (donor_name,donations_list)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(len(donations_list), len(donor.donation_amounts_list))
		#compare the data
		self.assertEqual(2010.99, donor.last_donation_amount)
	
	def test_donations_count(self):
		donor_name = "Sireesha Sankuratripati"
		donations_list = [900.99,1000.90,2010.99]
		donor = Donor (donor_name,donations_list)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(len(donations_list), len(donor.donation_amounts_list))

		#compare the data
		self.assertEqual(3, donor.donations_count)


	def test_total_donations_amount(self):
		donor_name = "Sireesha Sankuratripati"
		donations_list = [900,1000,2100]
		donor = Donor (donor_name,donations_list)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(len(donations_list), len(donor.donation_amounts_list))
		#compare the data
		self.assertEqual(4000, donor.total_donation_amount)

	def test_letter_for_donor(self):
		donor_name = "Sireesha Sankuratripati"
		donations_list = [900,1000,2100]
		donor = Donor (donor_name,donations_list)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(len(donations_list), len(donor.donation_amounts_list))
		#compare the data
		expected_letter = "Dear Sireesha Sankuratripati, \n \t Thank You for your very kind donation of $2100.0. It will be put to very good use. \n \t \t Sincerely, \n \t \t \t The Team"
		self.assertEqual(expected_letter, donor.letter_for_donor)

	def test_letter_for_donor(self):
		donor_name = "Sireesha Sankuratripati"
		donations_list = [900,1000,1100]
		donor = Donor (donor_name,donations_list)
		self.assertEqual(donor_name, donor.donor_name)
		self.assertEqual(len(donations_list), len(donor.donation_amounts_list))
		#compare the data
		self.assertEqual(1000, donor.donations_average_amount)

	def test_create_empty_mailroom(self):
		mailroom = Mailroom()
		self.assertEqual(0, mailroom.donor_count)

	def test_create_mailroom_populate_donors_from_dict(self):
		mailroom = Mailroom()
		sample_donor_data = \
		{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
		 'Jeff Bezos':[700.90,900.99],
		  'Paul Allen':[11100.80],
		  'Joanne K Rowling':[1199.90,9878.12]}
		mailroom.populate_donors_from_dict(sample_donor_data)
		self.assertEqual(4,mailroom.donor_count)
		donors = ['Mark Zuckerberg','Jeff Bezos','Paul Allen','Joanne K Rowling']
		for index,name in enumerate(mailroom.donor_names):
			self.assertEqual(name,donors[index])

	def test_populate_donors_from_invalid_data_dict(self):
		mailroom = Mailroom()
		sample_donor_data = \
		{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
		 'Jeff Bezos':[700.90,'not  a number'],
		  'Paul Allen':[11100.80],
		  'Joanne K Rowling':[1199.90,9878.12]}
		with self.assertRaises(ValueError): 
			mailroom.populate_donors_from_dict(sample_donor_data)
		
	def test_mailroom_get_donations_for_donor(self):
		mailroom = Mailroom()
		sample_donor_data = \
		{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
		 'Jeff Bezos':[700.90,900.99],
		  'Paul Allen':[11100.80],
		  'Joanne K Rowling':[1199.90,9878.12]}

		mailroom.populate_donors_from_dict(sample_donor_data)
		self.assertEqual(4,mailroom.donor_count)
		donors = ['Mark Zuckerberg','Jeff Bezos','Paul Allen','Joanne K Rowling']
		for index,name in enumerate(mailroom.donor_names):
			self.assertEqual(name,donors[index])

		donations_list = mailroom.donations_for_donor('Mark Zuckerberg')
		expected_donations = [5000.50,1089.90,750.45]
		self.assertEqual(len(donations_list), len(expected_donations))
		for index in range(0,len(donations_list)):
			self.assertEqual(donations_list[index], expected_donations[index])
		
	def test_send_letters_to_everyone(self):
		mailroom = Mailroom()
		sample_donor_data = \
		{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
		 'Jeff Bezos':[700.90,900.99],
		  'Paul Allen':[11100.80],
		  'Joanne K Rowling':[1199.90,9878.12]}

		mailroom.populate_donors_from_dict(sample_donor_data)
		self.assertEqual(4,mailroom.donor_count)
		donors = ['Mark Zuckerberg','Jeff Bezos','Paul Allen','Joanne K Rowling']
		for index,name in enumerate(mailroom.donor_names):
			self.assertEqual(name,donors[index])

		mailroom.send_letters_to_everyone()
		for filename in os.listdir('.'):
			if filename.endswith('.txt'):
				donorname = filename[:-4]
				self.assertIn(donorname, mailroom.donor_data_dict.keys())

	def test_print_report(self):
		mailroom = Mailroom()
		sample_donor_data = \
		{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
		 'Jeff Bezos':[700.90,900.99],
		  'Paul Allen':[11100.80],
		  'Joanne K Rowling':[1199.90,9878.12]}

		mailroom.populate_donors_from_dict(sample_donor_data)
		self.assertEqual(4,mailroom.donor_count)
		donors = ['Mark Zuckerberg','Jeff Bezos','Paul Allen','Joanne K Rowling']
		for index,name in enumerate(mailroom.donor_names):
			self.assertEqual(name,donors[index])
		capturedOutput = io.StringIO() 	# Create StringIO object
		sys.stdout = capturedOutput           	#  and redirect stdout.
		mailroom.create_report()
		sys.stdout = sys.__stdout__				#Reset Redirect
		report_text = \
			'''Donor Name                     | Total Given  | Num Gifts | Average Gift\n------------------------------------------------------------------------\nMark Zuckerberg                 $   6840.85           3    $   2280.28\nJeff Bezos                      $   1601.89           2    $    800.94\nPaul Allen                      $  11100.80           1    $  11100.80\nJoanne K Rowling                $  11078.02           2    $   5539.01'''
		self.assertEqual(capturedOutput.getvalue().strip(), report_text.strip())
		#Remove all the donor name text files created
		for filename in os.listdir('.'):
			if filename.endswith('.txt'):
				donorname = filename[:-4]
				if donorname in mailroom.donor_data_dict.keys():
					os.remove(filename)
		

	


