#!/usr/bin/python

"""
Lession 10 - Mailroom v6
=================================================================
1) Add mapping, so that each donation on record can be multiplied by a num
   returns new donor database with new data
2) Add filter so donations either above or below a specified $ are included
   in the map (filter before mapping)
3) Add another menu item for multiplying donations under or over a certain
   amount based on current data from company matching program
=================================================================
"""

# imports
from functools import reduce


# initialize list variables
donor1 = ["Tony Stark", 25.01, 150.99]
donor2 = ["Captain America", 50.00, 1000.00]
donor3 = ["Daisy Johnson", 51.00, 500.00, 1200.00]
donor4 = ["Melinda May", 1.99, 5.00, 15.01]
donor5 = ["Phil Coulson", 5000.00]

donors = [donor1, donor2, donor3, donor4, donor5]

# load donors to database
database = {}
for donor in donors:
    name = donor[0]
    donations = donor[1:]
    database.update({name: {"donations": donations, "gifts": len(donations)}})

# ======== MAPPING/FILTERING ========

temp_database = {}
def mymap(multi, lwr_bound, upr_bound):
    """mymap(dictionary, int) returns temp_database
       Takes in a int and multiplies all donations inside database by val"""
    for name in database.keys():
        # my version of filter
        def fmulti(x, lb = lwr_bound, ub = upr_bound, multi=multi):
            if lb is None:
                if ub is None or x <= ub:
                    return x * multi
                else:
                    return x
            elif x >= lb:
                if ub is None or x <= ub:
                    return x * multi
                else:
                    return x
            else:
                return x

        l_donations = list(map(fmulti, database[name]["donations"]))
        temp_database.update({name: {"donations": l_donations, "gifts": database[name]["gifts"]}})



# RUNTIME LOGIC
# ======== Single Entry/Report ========
menu_sigle_prompt = \
"""
[OUT]: Menu: Single Entry/Report:
    1) View Donor Names
    2) Print Thank You Note or Add new Entry
    3) Main Menu

[IN]: """


def menu_single():
    while True:
        options = input(menu_sigle_prompt)
        if options == "1":
            print("[OUT]: ", [names for names in iter(database.keys())])
        if options == "2":
            Iname = input("\n[IN]: Enter donor name: ")
            try:
                # check if the input name already exists
                database[name]
            except KeyError:
                # name is not in dict, add it and ask for donation
                print("\n[OUT]: Donor name is not on record. Adding new Donor name")
                donation = input("[IN]: Enter new donor's donation amount (single int, or list) = ")
                database.update({name: {"donations": donation, "gifts": len(donation)}})
            finally:
                print("[OUT]: Thank you {}, for donating ${}. - PydPiper".format(
                    name, reduce(lambda x, y=0: x+y, database[name]["donations"])))
        if options == "3": break

# ======== Database ========
menu_database_promt = \
"""
[OUT]: Menu: Database:
    1) Create Summary Report
    2) Modify All Donations
    3) Main Menu

[IN]: """
def menu_database():
    while True:
        options = input(menu_database_promt)
        if options == "1": report(database)
        if options == "2":
            multi = int(input("Enter value to multiply all donations by (type=int) = "))
            lwr_bound = input("Enter lower bound filter (none or float) = ")
            if lwr_bound == "none": lwr_bound = None
            else: lwr_bound = float(lwr_bound)
            upr_bound = input("Enter upper bound filter (none or float) = ")
            if upr_bound == "none": upr_bound = None
            else: upr_bound = float(upr_bound)

            mymap(multi, lwr_bound, upr_bound)

            report(temp_database)
            keeper = input("Update database with newly multiplied donations? (yes,no)")
            if keeper == "yes":
                # wipe existing data and replace
                database.update({})
                database.update(temp_database)
            else:
                # cleanup temp database
                temp_database.update({})
        if options == "3": break

# ======== Create a Report ========
def report(db):
    print("{:<20}|{:>15}|{:>10}|{:>15}".format(
        "Donor Name", "Total Given", "Num Gifts", "Avg Gift"))
    print("_"*60)
    length = len(list(db.keys()))
    for i in range(length):
        name = [names for names in iter(db.keys())][i]
        donations = reduce(lambda x, y: x+y, db[name]["donations"])
        gifts = db[name]["gifts"]
        print("{:<20} ${:>14.2f} {:>10d} ${:>14.2f}".format(
            name, donations, gifts, donations/gifts))


# ======== Write All Emails to Files ========        
def menu_emailALL():
    length = len(list(database.keys()))
    for i in range(length):
        name = [names for names in iter(database.keys())][i]
        donations = reduce(lambda x, y: x+y, database[name]["donations"])
        file_name = name.replace(" ","_") + ".txt"
        with open(file_name, "w") as f:
            content = "Thank you {}, for donating ${}. - PydPiper".format(
                name, donations)
            f.write(content)
            f.close()


# ======== Exiting ========
def exiting():
    return "exiting"

# ======== Main ========
main_prompt = \
"""
[OUT]: Menu: Main
    1) Single Entry/Report
    2) Database
    3) Write out all emails
    4) Quit
    
[IN]: """

main_dict = {"1": menu_single, "2": menu_database,"3": menu_emailALL, "4": exiting}



if __name__ == "__main__":
    print("\n[OUT]: Mailroom A10 v6")
    while True:
        options = input(main_prompt)
        try:
            # returns a function name from dict, then () calls it
            if main_dict[options]() == "exiting":
                break
        except KeyError:
            print("Invalid Menu Key Entered. Try again")
            continue





