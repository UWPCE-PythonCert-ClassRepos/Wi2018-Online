import numbers
'''
Lesson09 - Mailrom.py - Object Oriented Mailroom
Implementation of the Mailroom functionalities 
- 1 - Send a Thank You
- 2 - Create a Report
- 3 - Send letters to everyone
- 4 - Quit

Implemented Exception Handling for User Input - Entering donation amount and entering menu selection
Re-factored methods in the mailroom to enable being called from test cases
Implemented Object Oriented Mailroom with 2 classes - Donor and Mailroom
'''

#!/usr/bin/env python3


class Donor(object):
	def __init__(self,donor_name, donation_amounts_list = None):
		''' Constructor for Donor class'''
		self.donor_name = donor_name
		if donation_amounts_list == None:
			self.donation_amounts_list =[]
		else:
			self.donation_amounts_list = list(donation_amounts_list)

	def add_donation(self, val):
		'''adds a donation to the donation_amounts_list for the donor'''
		if isinstance (val, numbers.Number):
			if val >=0 :
				self.donation_amounts_list.append(val)
			else:
				raise ValueError
		else:
			raise TypeError

	@property
	def last_donation_amount(self):
		'''returns the most recent donation amount'''
		return (self.donation_amounts_list[-1])

	@property
	def letter_for_donor(self):
		'''generates a letter in the specified format'''
		amount = self.last_donation_amount
		lettercontent = f"Dear {self.donor_name}, \n \t Thank You for your very kind donation of ${amount}. It will be put to very good use. \n \t \t Sincerely, \n \t \t \t The Team"
		return (lettercontent)

	@property
	def total_donation_amount(self):
		'''gets the total donation amount for a donor'''
		total_donation = 0.0
		for amount in self.donation_amounts_list:
			total_donation += amount
		return (total_donation)

	@property
	def donations_count(self):
		return len(self.donation_amounts_list)

	@property
	def donations_average_amount(self):
		if len(self.donation_amounts_list) == 0:
			return 0
		avg_amount = self.total_donation_amount/len(self.donation_amounts_list)
		return (avg_amount)


class Mailroom(object):

	def __init__(self):
		'''Constructor for Mailroom'''

		''' Dictionary that stores Key, Value pairs - Key - donor name and Value - donor object '''
		self.donor_data_dict = {}

		'''Dictionary that stores the donor name as the key as the option number entered by user
		value - is the corresponding method name that needs to be invoked for that menu'''
		self.dict_menu = {\
						"1": self.send_thankyou,
						"2" : self.create_report,
				 		"3" : self.send_letters_to_everyone,
				 		"4" : self.exit }

	
	@property
	def donor_count(self):
		'''gets count of donors'''
		return len(self.donor_data_dict)

	@property
	def donor_names(self):
		'''gets donor names'''
		return (self.donor_data_dict.keys())

	@property
	def check_donor_exists(self, donor_full_name):
		'''checks if a donor exists'''
		return (donor_full_name in self.donor_data_dict)

	def donations_for_donor(self, donor_full_name):
		'''gets the donation amounts list for a donor'''
		if donor_full_name in self.donor_data_dict:
			return (self.donor_data_dict[donor_full_name].donation_amounts_list)
		else:
			return None

	def populate_donors_from_dict(self, donor_dict):
		'''Populate data in the donor_data dictionary from the input dictionary'''	
		for key, value in donor_dict.items():
			if self.check_list_for_valid_nums(value):
				donor_obj = Donor (key,list(value))
				self.donor_data_dict[key] = donor_obj
			else:
				raise ValueError

	def check_list_for_valid_nums(self,amounts_list):
		'''method checks if the donation amounts are floating point values'''
		for item in amounts_list:
			try:
				valid = float(item)
			except ValueError:
				return False
		return True

	def add_donor(self, donor_full_name, donation_amounts_list):
		'''adds a donor to the global donor_data'''
		if donor_full_name not in self.donor_data_dict:
			valid = check_donations_list_valid_float_nums(donation_amounts_list)
			if valid:
				donor = Donor(donor_full_name,amt_list)
				self.donor_data_dict[donor_full_name] = donor
				return True
			else:
				raise ValueError
		return False

	def add_donor_without_amount(self, donor_full_name):
		'''adds a donor to the global donor_data without any amount'''
		if donor_full_name not in self.donor_data_dict:
			donor = Donor (donor_full_name)
			self.donor_data_dict[donor_full_name] = donor
			return True
		else:
			return False

	def add_donation_to_existing_donor(self, donor_full_name, donation_amt):
		'''adds a donation amount to and existing donor in the global donor_data'''
		if donor_full_name in self.donor_data_dict:
			try:
				donor = self.donor_data_dict[donor_full_name]
				donor.donation_amounts_list.append(float(donation_amt))
				#donor_data[donor_full_name].append(float(donation_amt))
				return True
			except ValueError as e:
				print ("Exception occured in User Input for Menu: {}".format(e))
				print ("Invalid Format for Donation Amount. Enter a valid integer or Floating point number")
		return False

	@property
	def get_last_donation_for_donor(self, donor_full_name):
		'''gets last or latest donation amount'''
		return self.donor_data_dict[donor_full_name].last_donation_amount


	def send_letters_to_everyone(self):
		'''Generates letters to all the donors in the Donor list with DonorName.txt. Writes the files to the hard disk '''
		for key_donor_name, val_donor_obj in self.donor_data_dict.items():
			letter = val_donor_obj.letter_for_donor
			filename = key_donor_name + ".txt"
			file = open(filename,"w")
			file.write(letter)
			file.close()
			print ("Generated letter with file name {} for Donor {}".format(filename,key_donor_name))

	
	def send_thankyou(self):
		'''
		Function which implements the send Thank You functionality
		Use a while True loop 
			- condition to break from the while loop is once the Thank you note is printed
			- take user input for the name of the Donor
			- If the donor doesn't exist, add the donor info to the global dictionary
			- Use the donor and ask user to enter Donation amount and add it to the donation amounts in the Dictioary
			- If the user enters "list" , display all the donors 
		'''
		while True:		
			response_donor = input("Enter the Full Name of the Donor > ")

			if response_donor == "list":
				print ("List of Donors:")
				print (("{:30} "*len(self.donor_data_dict.keys())).format(*self.donor_data_dict.keys()))
				continue 
			if response_donor not in self.donor_data_dict.keys():
				self.add_donor_without_amount(response_donor)
				
				#donor_data[response_donor] = [] #add item to Dict
				#Add the new donor to the Donors List
			
			while True:
				try:
					response_amount = input("Enter the Amount of donation > ")
					#update value
					self.add_donation_to_existing_donor(response_donor,float(response_amount))
					#donor_data[response_donor].append(float(response_amount))	
					break #Break from while for Donation Amount Entry
				except ValueError as e:
					print ("Exception occured in User Input for Menu: {}".format(e))
					print ("Invalid Format for Donation Amount. Enter a valid integer or Floating point number")

			letter_content = self.donor_data_dict[response_donor].letter_for_donor
			#letter_content = generate_letter(response_donor)
			print (letter_content)
			return letter_content #Break and return from while loop for Donor Name Entry and the method

	
	def create_report(self):
		'''
		Create a report in the format specified in the requirements - as shown below
		Donor Name                | Total Given | Num Gifts | Average Gift
		------------------------------------------------------------------
		William Gates, III         $  653784.49           2  $   326892.24
		Mark Zuckerberg            $   16396.10           3  $     5465.37
		Jeff Bezos                 $     877.33           1  $      877.33
		Paul Allen                 $     708.42           3  $      236.14

		Compute the Donor info along with total donation amount, number of gifts and average amount
			- store the info as tuples in a list - donorInfoList
		Print the Data in the specified format
		'''
		donorinfolist = []
		for key_donor_name, value_donor_obj in self.donor_data_dict.items():
			donorinfolist.append ((key_donor_name, value_donor_obj.total_donation_amount, value_donor_obj.donations_count, value_donor_obj.donations_average_amount))
		sp1 = " " * 19
		header = "Donor Name " + sp1 + " | Total Given  | Num Gifts | Average Gift"
		print (header)
		dash = "-" * len(header)
		print (dash)
		for tmpitem in donorinfolist:
			print(f"{tmpitem[0]:30}  ${tmpitem[1]:10.2f}  {tmpitem[2]:10}    ${tmpitem[3]:10.2f}")


	def exit(self):
		'''Method that ends the program'''
		print ("Exiting the program based on User Selection")
		quit()

	def main_menu(self):
		'''
		Function to display the Main Menu
		Takes input from user and the response is not valid - prompts the user to enter a valid response
		Returns the response from the user to the calling function
		'''
		print ("********** MAIN MENU **********")	
		print ("1 - Send a Thank You")
		print ("2 - Create a Report")
		print ("3 - Sent letters to everyone")
		print ("4 - Quit")
		while True:		
			response = input ("Enter 1 or 2 or 3 or 4 to select a Menu item > ")
			return response


'''****Main Method****'''
if __name__ == "__main__":
	sample_donor_data = \
		{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
		 'Jeff Bezos':[700.90,900.99],
		  'Paul Allen':[11100.80],
		  'Joanne K Rowling':[1199.90,9878.12]}
	mailroom = Mailroom()
	mailroom.populate_donors_from_dict(sample_donor_data)

	#When the user selects Option 4, the program will Quit
	while True:
		try:
			mailroom.dict_menu[mailroom.main_menu()]()
		except KeyError as e:
			print ("Exception occured in User Input for Menu: {}".format(e))
			print ("Enter non empty and valid response - 1 or 2 or 3 or 4")

	

