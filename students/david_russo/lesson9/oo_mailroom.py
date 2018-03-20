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
		recipient = str(input("To whom would you like to send a thank you? > "))
		while recipient == "list":
			print(self.donor_list)
			print("\n")
			recipient = str(input("To whom would you like to send a thank you? > "))
		return(recipient)

	def receive_donation_amount(self):
		while True:
			donation_amount = input("How much would you like to donate? > ")
			try:
				donation_amount = float(donation_amount)
				if donation_amount < 0.00:
					print("You must enter a positive number to donate. ")
					continue
				break
			except ValueError:
				print("You must enter a numeric value. > ")
		return(donation_amount)

	def send_a_thank_you(self):
		recipient = self.receive_thank_you_card_recepient_input()
		donation_amount = self.receive_donation_amount()
		self.donors.setdefault(recipient, Donor(recipient)).add_donation(donation_amount)
		print("Dear {:s},".format(recipient))
		print("Thank you for your generous donations totaling ${:.2f}".format(*[x.total_donations for i,x in enumerate(self.donors.values()) if x.name == recipient]))
		print("Best, The Donation Foundation.")




		












