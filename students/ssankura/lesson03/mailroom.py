'''
Lesson03 - Assignment 04 - Mailrom.py
Implementation of the Mailroom functionalities 
- Send a Thank You
- Create a Report
- Quit
'''

#!/usr/bin/env python3


''' Global List variables which store the donor names in a donorsList and the (donor,amount) as a tuple into the donorsAmountList'''
donorsList = []
donorsAmountList = []

'''
Function to display the Main Menu
Takes input from user and the response is not valid - prompts the user to enter a valid response
Returns the response from the user to the calling function
'''
def displayMainUserPrompt():
	print ("********** MAIN MENU **********")
	print ("1. Send a Thank You")
	print ("2. Create a Report")
	print ("3. Quit")
	while (True):
		response = input ("Enter 1 or 2 or 3 to select a Menu item > ")
		if (response != "") and  not(response in ("1","2","3")):
			print ("Enter non empty and valid response - 1 or 2 or 3")
		else:
			return response
			break


'''
Function which implements the send Thank You functionality
Use a while True loop 
	- condition to break from the while loop is once the Thank you note is printed
	- take user input for the name of the Donor
	- If the donor doesn't exist, add the donor to the Donor's list
	- Use the donor and ask user to enter Donation amount and add it to the Donation amounts list
	- If the user enters "list" , display all the donors 
'''
def sendThankYou():
	loop = True
	while (loop):		
		response = input("Enter the Full Name of the Donor > ")
		if (response != "") and (response != "list"):
			if not(response in donorsList):
				#Add the new donor to the Donors List
				donorsList.append(response)
				#do something and break from the While loop
			donor = response
			response = input("Enter the donation amount > ")
			amount = float(response)
			donorsAmountList.append((donor, amount))
			print (f"Hello {donor}, \n \t Thank You for the generous donation of ${amount}. We appreciate your effort to help out with the cause that we have been supporting. \n From, \n ABC Charity")
			loop = False
		else:
			print ("List of Donors:")
			print (("{:30} "*len(donorsList)).format(*donorsList))


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
def createReport():
	donorInfoList = []
	for donor in donorsList:
		total = 0 
		numGifts = 0
		for item in donorsAmountList:
			donorNameInItem = item[0]
			if donorNameInItem == donor:
				total  = total + int(item[1])
				numGifts = numGifts + 1
		averageAmount = total/numGifts
		donorInfoList.append ((donor,total,numGifts,averageAmount))
	sp1 = " " * 19
	strHeader = "Donor Name " + sp1 + " | Total Given  | Num Gifts | Average Gift"
	print (strHeader)
	strDash = "-" * len(strHeader)
	print (strDash)
	for tmpitem in donorInfoList:
		print(f"{tmpitem[0]:30}  ${tmpitem[1]:10.2f}  {tmpitem[2]:10}    ${tmpitem[3]:10.2f}")


'''
Populate data in the global variables - donorsList and donorsAmountList
'''
def populateData():
	donorsList.append("Mark Zuckerberg")
	donorsList.append("Jeff Bezos")
	donorsList.append("Paul Allen")
	donorsList.append("Joanne K Rowling")
	donorsAmountList.append(("Mark Zuckerberg",5000.50))
	donorsAmountList.append(("Jeff Bezos",700.90))
	donorsAmountList.append(("Mark Zuckerberg",1089.90))
	donorsAmountList.append(("Joanne K Rowling",9878.12))
	donorsAmountList.append(("Jeff Bezos",900.99))
	donorsAmountList.append(("Mark Zuckerberg",750.45))
	donorsAmountList.append(("Joanne K Rowling",910.75))
	donorsAmountList.append(("Paul Allen",11100.80))
	donorsAmountList.append(("Joanne K Rowling",1100.80))

'''
Prints the Donors list
'''
def printDonors():
	print("Printing Global variables")
	print (("{:20} "*len(donorsList)).format(*donorsList))
	for item in donorsAmountList:
		print (("{:20} {:8.2f}").format(*item))

'''
Read the user input and invoke the appropriate function accordingly
'''	
def readUserInput(userInput):
	if (userInput == "1"):
		sendThankYou()
	elif (userInput == "2"):
		print("createReport")
		createReport()
	elif (userInput == "3"):
		quit()


'''Main Method'''
if __name__ == "__main__":
	populateData()
	#When the user selects Option 3, the program will Quit
	while (True):
		userInput = displayMainUserPrompt()
		readUserInput(userInput)
	

