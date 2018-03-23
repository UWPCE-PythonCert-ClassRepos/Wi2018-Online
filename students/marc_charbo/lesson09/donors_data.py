import donor as Donor
from textwrap import dedent

class DonorData():
    def __init__(self, donors=None):
        if donors is None:
            self.donor_dict = {}
        else:
            self.donor_dict = {d.name: d for d in donors}

    @property
    def donors(self):
        return self.donor_dict.values()

    def find_donor(self, name):
        print (name)
        return self.donor_dict.get(name)

    def add_donor(self, name):
        donor = Donor.Donor(name)
        self.donor_dict[donor.name] = donor
        return donor

    def gen_letter(self, donor):
        return dedent('''Dear {},

              Thank you for your very kind donation of ${:.2f}.
              It will be put to very good use.

                Sincerely,
                -The Team'''.format(donor.name, donor.last_donation))

    def save_letters(self):
        for donor in self.donor_dict.values():
            with open(donor.name + '.txt', 'w') as file:
                file.write(self.gen_letter(donor))

    def print_report(self):
        line = []
        for donor in self.donor_dict.values():
            name = donor.name
            gift_list = donor.donations
            total_gifts = donor.total_donations
            num_gifts = len(gift_list)
            avg_gift = donor.avg_donation
            line.append((name, total_gifts, num_gifts, avg_gift))

        report = []
        header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        report.append('{:25} |{:^15} |{:^15} |{:^15}'.format(*header))
        report.append("-" * 75)
        for l in line:
            report.append("{:25}   ${:^15.2f}   {:^15d}   ${:^15.2f}".format(*l))
        return "\n".join(report)

    def print_donor_names(self):
       name_list=[]
       for donor in self.donors:
           name_list.append(donor.name)
       return ("\n".join(name_list))
