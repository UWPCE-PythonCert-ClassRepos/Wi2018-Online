class Donor():
    """
    Not sure the Donor class is necessary.  Seemed
    like a good idea at the time :-)
    """
    total_donors = 0

    def __init__(self, fname, lname, donations=None):
        self.fname = fname
        self.lname = lname
        if donations is not None:
            self.donations = donations
        else:
            self.donations = []

        Donor.total_donors += 1

    @property
    def fullname(self):
        return f'{self.fname} {self.lname}'



class Mailroom(object):
    """
    The Donor objects are placed into a dictionary in the Mailroom.
    The Donor objects are accessed using fname as the key to locate the
    object.
    """
    def __init__(self):
        self.donor_collection = {}

    def add_new_donor(self,fname, lname, initial_donations=[]):
        self.donor_collection[fname] = Donor(fname, lname, initial_donations)

    def list_donors(self):
        return "\n".join(self.donor_collection.keys())

    def add_donation(self, fname, donation):
        if fname in self.donor_collection.keys():
            self.donor_collection[fname].donations.append(donation)
        else:
            raise ValueError('Donor not found')

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

    from seed_data import initial_data

    mailroom = Mailroom()

    # load intial donors as objects into dictionary
    for k, v in initial_data.items():
        mailroom.donor_collection[k] = Donor(k, v['lname'], v['donations'])

    print(mailroom.donor_collection)








