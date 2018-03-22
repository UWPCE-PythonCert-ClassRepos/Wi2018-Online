class Donor():
    """
    Not sure the Donor class is necessary.  Seemed
    like a good idea at the time :-)
    """
    total_donors = 0

    def __init__(self, fname, donations=[]):
        self.fname = fname
        self.donations = donations
        Donor.total_donors +=1

class Mailroom(object):
    """
    The Donor objects are placed into a dictionary in the Mailroom.
    The Donor objects are accessed using fname as the key to locate the
    object.
    """
    def __init__(self):
        self.donor_collection = {}

    def add_new_donor(self,fname, initial_donations=[]):
        self.donor_collection[fname] = Donor(fname, initial_donations)

    def list_donors(self):
        return "\n".join(self.donor_collection.keys())

    def add_donation(self, fname, donation):
        if fname in self.donor_collection.keys():
            self.donor_collection[fname].donations.append(donation)
        else:
            self.add_new_donor(fname, donation)

    def sum_donations(self, fname):
        return sum(self.donor_collection.get(fname).donations)

    def total_number_of_donors(self):
        return Donor.total_donors

    def seperator(self,str):
        """return line that equals string length ignoring newline."""
        return "-" * (len(str) - str.count('\n'))

    def create_report(self):
        heading = "Donor Name | Total Given | Num Gifts | Average Gift\n"
        heading += self.seperator(heading)
        result = ''
        for k, v in self.donor_collection.items():
            result += "{:10} ${:10.2f} {:10} {:15.2f}\n".format(k,
                                                                sum(v.donations),
                                                                len(v.donations),
                                                                (sum(v.donations) / len(v.donations)))
        return(f"{heading}\n{result}")


if __name__ == "__main__":
    # should probably uses this for testing only and load as
    # a module.
    intial_data = {'jack': [100, 200, 300, 400],
                   'mary': [3000, 5000],
                   'frank': [29.50, 31],
                   'jane': [3000, 5000],
                   'scrouge': [1, 2, 3],
                   'bob': [60000, 70000, 7668, 4]}

    mailroom = Mailroom()

    # load intial donors as objects into dictionary
    for k,v in intial_data.items():
        mailroom.donor_collection[k] = Donor(k,v)








