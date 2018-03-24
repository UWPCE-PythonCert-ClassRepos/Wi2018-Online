import unittest
import mailroom4 as mailroom
import io
import sys
import os

class MailroomTest(unittest.TestCase):		
			
	def setUp(self):
		mailroom.donor_data = \
			{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
			 'Jeff Bezos':[700.90,900.99],
			 'Paul Allen':[11100.80],
			 'Joanne K Rowling':[1199.90,9878.12]
			}

	def test_donors_count(self):
		self.assertEqual(len(mailroom.donor_data),4)

	def test_donors_names(self):
		self.assertEqual(mailroom.check_donor_exists('Mark Zuckerberg'),True)
		self.assertEqual(mailroom.check_donor_exists('Jeff Bezos'),True)
		self.assertEqual(mailroom.check_donor_exists('Paul Allen'),True)
		self.assertEqual(mailroom.check_donor_exists('Joanne K Rowling'),True)

	def test_check_donor_exists(self):
		self.assertEqual(mailroom.check_donor_exists('Jeff Bezos'),True)
		self.assertEqual(mailroom.check_donor_exists('Sireesha Sankuratripati'),False)

	def test_add_donor(self):
		self.assertEqual(mailroom.check_donor_exists('Sireesha Sankuratripati'),False)
		#Add the above donor and test again
		mailroom.add_donor_without_amount('Sireesha Sankuratripati')
		self.assertEqual(mailroom.check_donor_exists('Sireesha Sankuratripati'),True)
		self.assertEqual(len(mailroom.donor_data),5)

	def test_add_invalid_donation_to_donor(self):
		retval = mailroom.add_donor_without_amount('Sireesha Sankuratripati')
		self.assertEqual(retval,True)
		retval = mailroom.add_donation_to_existing_donor('Sireesha Sankuratripati','invalid')
		self.assertEqual(retval,False)

	def test_get_last_donation_amount(self):
		mailroom.add_donation_to_existing_donor('Jeff Bezos',10000.00)
		self.assertEqual(mailroom.get_last_donation_for_donor('Jeff Bezos'),10000.00)
		
	def test_generate_letter(self):
		mailroom.add_donation_to_existing_donor('Jeff Bezos',10000.00)
		letter = mailroom.generate_letter('Jeff Bezos')
		self.assertIn('Jeff Bezos',letter)
		self.assertIn('10000.0',letter)

	def test_send_letters_to_everyone(self):
		mailroom.send_letters_to_everyone()
		for filename in os.listdir('.'):
			if filename.endswith('.txt'):
				donorname = filename[:-4]
				self.assertIn(donorname, mailroom.donor_data.keys())

	def test_print_report(self):
		report_text = \
			'''
Donor Name                     | Total Given  | Num Gifts | Average Gift
------------------------------------------------------------------------
Mark Zuckerberg                 $   6840.85           3    $   2280.28
Jeff Bezos                      $   1601.89           2    $    800.94
Paul Allen                      $  11100.80           1    $  11100.80
Joanne K Rowling                $  11078.02           2    $   5539.01
'''
		capturedOutput = io.StringIO() 	# Create StringIO object
		sys.stdout = capturedOutput           	#  and redirect stdout.
		mailroom.create_report()
		sys.stdout = sys.__stdout__				#Reset Redirect
		self.assertEqual(capturedOutput.getvalue().strip(), report_text.strip())

	def tearDown(self):
		#Remove all the donor name text files created
		for filename in os.listdir('.'):
			if filename.endswith('.txt'):
				donorname = filename[:-4]
				if donorname in mailroom.donor_data.keys():
					os.remove(filename)



if __name__ == "__main__":
	unittest.main()