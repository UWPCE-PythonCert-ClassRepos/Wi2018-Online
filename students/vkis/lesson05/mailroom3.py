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
dict_data = {}


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
    length = len(names)
    # initialize dict with names and an empty list-values, value = [money, gifts]
    dict_data.update({names[i]: [0, 0] for i in range(length)})
    # concatenate data
    for i in range(length):
        dict_data.update({names[i]: \
        [dict_data[names[i]][0] + money[i], dict_data[names[i]][1] + gifts[i]]})
                

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
            print("[OUT]: ", list(dict_data.keys()))
        if options == "2":
            email_name = input("\n[IN]: Enter donor name: ")
            try:
                # check if the input name already exists
                dict_data[email_name]
            except KeyError:
                # name is not in dict, add it and ask for donation
                print("\n[OUT]: Donor name is not on record. Adding new Donor name")
                email_money = input("[IN]: Enter new donor's donation amount = ")
                dict_data.update({email_name: [float(email_money),1]})
            finally:
                print("[OUT]: Thank you {}, for donating ${}. - PydPiper".format( \
                email_name, dict_data[email_name][0]))
        if options == "3": break




# ======== Create a Report ========
def report():
    print("{:<20}|{:>15}|{:>10}|{:>15}".format( \
    "Donor Name", "Total Given", "Num Gifts", "Avg Gift"))
    print("_"*60)
    length = len(list(dict_data.keys()))
    for i in range(length):
        name = list(dict_data.items())[i][0]
        money = list(dict_data.items())[i][1][0]
        gift = list(dict_data.items())[i][1][1]
        print("{:<20} ${:>14} {:>10} ${:>14}".format( \
        name, money, gift, money/gift))



# ======== Write All Emails to Files ========        
def all_emails():
    length = len(list(dict_data.keys()))
    for i in range(length):
        name = list(dict_data.items())[i][0]
        money = list(dict_data.items())[i][1][0]
        file_name = name.replace(" ","_") + ".txt"
        with open(file_name, "w") as f:
            content = "Thank you {}, for donating ${}. - PydPiper".format( \
                name, money)
            f.write(content)
            f.close()

    
# ======== Exiting ========
def exiting():
    return "exiting"

# ======== Main ========
main_prompt = \
"""
[OUT]: Menu: Main
    1) Create Thank You Note
    2) Create a Report
    3) Write out all emails
    4) Quit
    
[IN]: """

main_dict = {"1": email_thx, "2": report,"3": all_emails, "4": exiting}



if __name__ == "__main__":
    print("\n[OUT]: Mailroom A1 v1")
    # process raw data
    data_sort()
    while True:
        options = input(main_prompt)
        try:
            # returns a function name from dict, then () calls it
            if main_dict[options]() == "exiting":
                break
        except KeyError:
            print("Invalid Menu Key Entered. Try again")
            continue

            
            

