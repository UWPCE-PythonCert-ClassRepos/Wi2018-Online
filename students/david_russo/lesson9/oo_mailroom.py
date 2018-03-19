#!/usr/bin/env python

class Donor():

	def __init__(self, name):
		self.name = name
		self.donations = []

	@property
	def total_donations(self):
		return sum(self.donations)

	@property
	def number_of_donations(self):
		return(len(self.donations))

	@property
	def average_donation_size(self):
		return(self.total_donations/self.number_of_donations)

	def add_donation(self, amount):
		try:
			self.donations.append(float(amount))
		except ValueError:
			print("You must enter a numeric donation amount. ")



class DonorList():

	def __init__(self):
		self.donors = {}

	@property
	def donor_list(self):
		return(list(self.donors.keys()))

	def add_donor(self, new_donor):
		self.donors[new_donor.name] = new_donor

	def receive_thank_you_card_recepient_input(self):
		return(str(input("To whom would you like to send a thank you? > \n")))

	def send_a_thank_you(self):
		recipient = receive_thank_you_card_recepient_input()












