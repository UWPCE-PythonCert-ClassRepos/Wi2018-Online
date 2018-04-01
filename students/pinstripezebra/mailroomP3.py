# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 08:23:07 2018

@author: seelc
"""
import datetime

#Dictionary containing all donor data
donationHistory = {'William Gates, III':[10312.3, 3],
                   'Mark Zuckerberg':[31245.24, 3],
                   'Jeff Bezos':[9432.01, 2],
                   'Paul Alan':[7244.35, 2],
                   'Elon Musk':[13148.94, 1],
        }

def main():
    #promting the user to choose a main action
    userAction = ""
    while userAction !="4":
        userAction = input( "Choose an action: \n1- Send a thank you\n2-Create a Report\n3-Send a thank you to everyone\n4-Quit\n")
        #Attempting to throw an exception if userAction isnt 1, 2, or 3
        try:
            assert userAction in ["1", "2", "3", "4"]
            #if the user chooses to send a thank you
            if userAction == "1":
                nameRequest = input("Please select a name: ")
                #0 stands in for donationAmount, purpose of having second input
                #is to make the thankYou function easier to test
                thankYou(nameRequest, 0)
        
            #if the user chooses to create a report
            elif userAction == "2":
                printReport(donationHistory)
        
            #if the user chooses to send a thank you to everyone
            elif userAction == "3":
                groupThanks(donationHistory)
            #if none of the above options are chosen quits the program
            elif userAction == 4:
                print("Quiting program")
                break
        except ValueError:
            print("The value entered must be 1, 2, 3, or 4")
    
              
    
#If the user selects to send a thank you letter to a single donor   
def thankYou(nameRequest, donationAmount=0):
    names = donationHistory.keys()    
    
    #Prompts the user to select a name if they enter "list"
    while nameRequest == "list":
        for i in range(len(list(names))):
            print(list(names)[i])
        nameRequest = input( "Please select a name: ")
        
    #If the user enters a name that exists 
    if nameRequest in names:
        try:
            #Optional parameter donationAmount can be passed in for testing
            #If it has not been passed in for testing asks user for it here
            if donationAmount == 0:
                donationAmount = int(input( "Please input a donation amount: "))
                
            donationHistory[nameRequest][0] = round(int(donationHistory[nameRequest][0]) + donationAmount, 2)
            donationHistory[nameRequest][1] += 1
            
        #If the donation amount entered isnt valid
        except TypeError:
            print("Value entered must be an integer")
            
        except ValueError:
            print("Value entered must be greater than 0")
        
    #If the user enters a name that doesnt exist
    else:
        try:
            #If the code isnt being ran through testing code
            if donationAmount == 0:
                donationAmount = int(input("Please input a donation amount: "))
                
            donationHistory[nameRequest] = [donationAmount, 1]
            
        except TypeError:  
            print("value entered must be an integer")
        
        except ValueError:
            print("Value entered must be greater than 0")
            
    print('Dear {},\n\n Thank you for your generous donation of ${}, it will be put to good use. \n\nThe team'.format(nameRequest, donationAmount))
    return donationHistory

#If the user wants to print a report of the current donor information    
def printReport(donationHistory):
    #Have to expilicitly declare names as list, otherwise get 'dict_keys' object
    names = list(donationHistory.keys())
    firstColumn = len(max(names, key=len))
    #The length of the string "Donor Name
    secondColumn = 10
    header = "Donor Name"+' '*max(firstColumn - 10,0)+ "|" +"Total Given" + "  |" + "Num Gifts" + "|" + "Average Gift"
    print(header)
    print("-"*len(header))
    
    #Loops over all the donors and prints one line for each
    for i in range(len(names)):
        currentDonor = names[i]
        #number of spaces required for each line between name and total given
        spaces = (max(0, firstColumn - len(names[i])))+ secondColumn - len(str(donationHistory[currentDonor][0]))
        numGifts = donationHistory[currentDonor][1]
        avgGift = round(donationHistory[currentDonor][0]/donationHistory[currentDonor][1], 2)
        print(names[i], ' '*spaces,'$', donationHistory[names[i]][0], ' ' *5, numGifts, ' '*5, '$ ', avgGift)
    return names

#Creates a response email in a separate file for each donor            
def groupThanks(donationHistory):     
    names = list(donationHistory.keys())  
    
    #Running through the list of names and writing a thank you letter for each donor
    for i in range(len(names)):
        #Creating a new text file   
        dateSent = str(datetime.date.today())
        group_Thanks = open("{}_{}".format(names[i], dateSent), "w")
        group_Thanks.write("Dear {},\n\nThank you for your generous donation of ${}, it will be put to good use.\n\n-Sincerely, the team\n\n".format(names[i], donationHistory[names[i]][0] ))
        
if __name__ == '__main__':
    main()           