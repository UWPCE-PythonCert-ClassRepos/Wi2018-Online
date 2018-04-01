'''
Lesson04 - Assignment 01 - Mailrom.py
Implementation of the Mailroom functionalities 
- 1 - Send a Thank You
- 2 - Create a Report
- 3 - Send letters to everyone
- 4 - Quit
'''

#!/usr/bin/env python3


''' Global donor data dictionary'''
donor_data = {}

'''
Populate data in the global - donor_data dictionary
'''
def populate_data():
	global donor_data
	donor_data = \
		{'Mark Zuckerberg':[5000.50,1089.90,750.45], 
		 'Jeff Bezos':[700.90,900.99],
		  'Paul Allen':[11100.80],
		  'Joanne K Rowling':[1199.90,9878.12]}


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
			donor_data[response_donor] = [] #add item to Dict
			#Add the new donor to the Donors List
			
		response_amount = input("Enter the Amount of donation > ")
		#update value
		donor_data[response_donor].append(float(response_amount))		
		print (generate_letter(response_donor))
		break

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
		if (response != "") and  (response not in ("1","2","3","4")):
			print ("Enter non empty and valid response - 1 or 2 or 3 or 4")
		else:
			return response


'''Main Method'''
if __name__ == "__main__":
	populate_data()
	#When the user selects Option 4, the program will Quit
	while True:
		dict_menu[main_menu()]()
	

