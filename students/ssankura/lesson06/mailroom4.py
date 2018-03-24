'''
Lesson05 - Mailrom.py - Part 3
Implementation of the Mailroom functionalities 
- 1 - Send a Thank You
- 2 - Create a Report
- 3 - Send letters to everyone
- 4 - Quit

Implemented Exception Handling for User Input - Entering donation amount and entering menu selection
Re-factored methods in the mailroom to enable being called from test cases
'''

#!/usr/bin/env python3


''' Global donor data dictionary'''
donor_data = {}

'''
Populate data in the global - donor_data dictionary
'''	
def populate_donors_from_dict(donor_dict):
	for key, value in donor_dict.items():
		donor_data[key] = value

'''
method checks if the donation amounts are floating point values
'''
def check_donations_list_valid_float_nums(amounts_list):
	for item in amounts_list:
		try:
			valid = float(item)
		except ValueError:
			return False
	return True


'''
adds a donor to the global donor_data
'''
def add_donor(donor_full_name, donation_amounts_list):
	if donor_full_name not in donor_data:
		valid = check_donations_list_valid_float_nums(donation_amounts_list)
		if valid:
			donor_data[donor_full_name] = amt_list
			return True
	return False

'''
adds a donor to the global donor_data without any amount
'''
def add_donor_without_amount(donor_full_name):
	if donor_full_name not in donor_data:
		donor_data[donor_full_name] = []
		return True
	else:
		return False

'''
adds a donation amount to and existing donor in the global donor_data
'''
def add_donation_to_existing_donor(donor_full_name, donation_amt):
	if donor_full_name in donor_data:
		try:
			donor_data[donor_full_name].append(float(donation_amt))
			return True
		except ValueError as e:
			print ("Exception occured in User Input for Menu: {}".format(e))
			print ("Invalid Format for Donation Amount. Enter a valid integer or Floating point number")
	return False

'''
gets last or latest donation amount
'''
def get_last_donation_for_donor(donor_full_name):
	return donor_data[donor_full_name][-1]

'''
gets count of donors
'''
def get_donor_count():
	return len(donor_data)

'''
gets donor names
'''
def get_donor_names():
	return (donor_data.keys())

'''
checks if a donor exists
'''
def check_donor_exists(donor_full_name):
	return (donor_full_name in donor_data)

'''
gets the donation amounts list for a donor
'''
def get_donation_values_for_donor(donor_full_name):
	return (donor_data[donor_full_name])

'''
gets the total donation amount for a donor
'''
def get_total_donation_amount_for_donor(donor_full_name):
	total_donation = 0.0
	if donor_full_name in donor_data:
		for val in donor_data[donor_full_name]:
			total_donation += val 
	return (total_donation)


'''
Generates letters to all the donors in the Donor list with DonorName.txt 
Writes the files to the hard disk 
'''
def send_letters_to_everyone():
	for donor in donor_data.keys():
		total = 0 
		for item in donor_data[donor]:
			total  = total + item
		letter = generate_letter(donor)
		filename = donor + ".txt"
		file = open(filename,"w")
		file.write(letter)
		file.close()
		print ("Generated letter with file name {} for Donor {}".format(filename,donor))


'''
Helper function to generate the letter in the specified format
'''
def generate_letter(donor):
	amount = donor_data[donor][-1] #most recent donation
	lettercontent = f"Dear {donor}, \n \t Thank You for your very kind donation of ${amount}. It will be put to very good use. \n \t \t Sincerely, \n \t \t \t The Team"
	return (lettercontent)


'''
Function which implements the send Thank You functionality
Use a while True loop 
	- condition to break from the while loop is once the Thank you note is printed
	- take user input for the name of the Donor
	- If the donor doesn't exist, add the donor info to the global dictionary
	- Use the donor and ask user to enter Donation amount and add it to the donation amounts in the Dictioary
	- If the user enters "list" , display all the donors 
'''
def send_thankyou():
	while True:		
		response_donor = input("Enter the Full Name of the Donor > ")

		if response_donor == "list":
			print ("List of Donors:")
			print (("{:30} "*len(donor_data.keys())).format(*donor_data.keys()))
			continue 
		if response_donor not in donor_data.keys():
			add_donor_without_amount(response_donor)
			#donor_data[response_donor] = [] #add item to Dict
			#Add the new donor to the Donors List
		
		while True:
			try:
				response_amount = input("Enter the Amount of donation > ")
				#update value
				add_donation_to_existing_donor(response_donor,float(response_amount))
				#donor_data[response_donor].append(float(response_amount))	
				break #Break from while for Donation Amount Entry
			except ValueError as e:
				print ("Exception occured in User Input for Menu: {}".format(e))
				print ("Invalid Format for Donation Amount. Enter a valid integer or Floating point number")

		letter_content = generate_letter(response_donor)
		print (letter_content)
		return letter_content #Break and return from while loop for Donor Name Entry and the method

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
def create_report():
	donorinfolist = []
	for donor in donor_data.keys():
		total = 0 
		numgifts = 0
		for item in donor_data[donor]:
			total  = total + item
			numgifts = numgifts + 1
		avgamount = total/numgifts
		donorinfolist.append ((donor,total,numgifts,avgamount))
	sp1 = " " * 19
	header = "Donor Name " + sp1 + " | Total Given  | Num Gifts | Average Gift"
	print (header)
	dash = "-" * len(header)
	print (dash)
	for tmpitem in donorinfolist:
		print(f"{tmpitem[0]:30}  ${tmpitem[1]:10.2f}  {tmpitem[2]:10}    ${tmpitem[3]:10.2f}")


'''
Method that ends the program
'''
def exit():
	print ("Exiting the program based on User Selection")
	quit()


'''
Global dictionary that stores the menu - key as the option number entered by user
value - is the corresponding method name that needs to be invoked for that menu
'''
dict_menu = {"1": send_thankyou,
			 "2" : create_report,
			 "3" : send_letters_to_everyone,
			 "4" : exit }

'''
Function to display the Main Menu
Takes input from user and the response is not valid - prompts the user to enter a valid response
Returns the response from the user to the calling function
'''
def main_menu():
	print ("********** MAIN MENU **********")	
	print ("1 - Send a Thank You")
	print ("2 - Create a Report")
	print ("3 - Sent letters to everyone")
	print ("4 - Quit")
	while True:		
		response = input ("Enter 1 or 2 or 3 or 4 to select a Menu item > ")
		return response


'''Main Method'''
if __name__ == "__main__":
	donor_dict = \
		{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
		 'Jeff Bezos':[700.90,900.99],
		  'Paul Allen':[11100.80],
		  'Joanne K Rowling':[1199.90,9878.12]}

	populate_donors_from_dict(donor_dict)
	#When the user selects Option 4, the program will Quit
	while True:
		try:
			dict_menu[main_menu()]()
		except KeyError as e:
			print ("Exception occured in User Input for Menu: {}".format(e))
			print ("Enter non empty and valid response - 1 or 2 or 3 or 4")

	

