# Lession 03 - Mailroom v1
# =================================================================

# Existing Data (format: 15 char names, 15 char numbers per line)
rawtext =  """Tony Stark             $453.02
              Captain America      $1,250.00
              Daisy Johnson            $1.99
              Melinda May            $500.01
              Phil Coulson         $9,999.99
              Daisy Johnson            $1.99
              Daisy Johnson           $10.99
              Melinda May             $55.01
              Tony Stark             $453.02
              Captain America      $3,250.00"""

# ======== Text to Lists ========
# split by returns
textlines = rawtext.split("\n")
rawlength = len(textlines)
# initialize list variables
names = []
money = []
gifts = []
for lines in range(rawlength):
    # clean the start and ends of lines
    textlines[lines] = textlines[lines].strip() 

    # pull out a line to a list for editing
    # cut last 15 chars that are for numbers
    rawname = textlines[lines]
    names.append(rawname[:-15].strip())
    
    rawmoney = textlines[lines]
    money.append((rawmoney[15:].strip()).strip("$").replace(",",""))
    money[lines] = float(money[lines])
    
    # log total gifts
    gifts.append(1)

    
# ======== Data Sorting ========
def data_sort():
    for i1 in range(rawlength):
        # i1 dynamic len(names) check after multiple del
        if i1 <= (len(names)-1):
            # matching loop [0]=[0],[0]=[1]...
            for i2 in range(0,rawlength):
                # first pass no deleting [0] == [0]
                # i2 dynamic len(names) check after previous name del
                # i1 dynamic len(names) check after multiple del
                # match names
                if i1 != i2 and \
                i2 <= (len(names)-1) and \
                i1 <= (len(names)-1) and \
                names[i1] == names[i2]:         
                    del names[i2]
                    money[i1] += money[i2]
                    del money[i2]
                    gifts[i1] += gifts[i2]
                    del gifts[i2]
                

# ======== Send a Thank You ========

email_thx_prompt = \
"""
[OUT]: Menu: Create Thank You Note:
    1) View Donor Names
    2) Create Thank You Note
    3) Main Menu

[IN]: """
def email_thx():
    while True:
        options = input(email_thx_prompt)
        if options == "1":
            print(names)
        if options == "2":
            email_name = input("\n[IN]: Enter donor name: ")
            try:
                # check if the input name has a index in names (ie, does it exist?)
                names.index(email_name)
            except ValueError:
                #name is not in list, add it and ask for donation
                print("\n[OUT]: Donor name is not on record. New Donor name added")
                names.append(email_name)
                email_money = input("[IN]: Enter new donor's donation amount = ")
                money.append(float(email_money))
                # add 1 tally to new donor
                gifts.append(1)
            finally:
                print("[OUT]: Thank you {}, for donating ${}. - PydPiper".format( \
                names[names.index(email_name)], money[names.index(email_name)]))
        if options == "3": break




# ======== Create a Report ========
def report():
    print("{:<20}|{:>15}|{:>10}|{:>15}".format( \
    "Donor Name", "Total Given", "Num Gifts", "Avg Gift"))
    print("_"*60)
    for index in range(len(names)):
        print("{:<20} ${:>14} {:>10} ${:>14}".format( \
        names[index], money[index], gifts[index], money[index]/gifts[index]))




# ======== Main ========
main_prompt = \
"""
[OUT]: Menu: Main
    1) Create Thank You Note
    2) Create a Report
    3) Quit
    
[IN]: """

if __name__ == "__main__":
    print("\n[OUT]: Mailroom A1 v1")
    # process raw data
    data_sort()
    while True:
        options = input(main_prompt)
        if options == "1": email_thx()
        if options == "2": report()
        if options == "3": break
