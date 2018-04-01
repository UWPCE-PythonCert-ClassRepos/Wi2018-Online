#!/usr/local/python3

import sys
import weakref

#Initial Donors List
#

donors = {'Aron': [100, 300, 100], 'Joan': [100, 50, 65, 100], 'Jean': [30, 150], 'Scott': [200]}

#Donor Class
class Donor:
    donors = {'Aron': [100, 300, 100], 'Joan': [100, 50, 65, 100], 'Jean': [30, 150], 'Scott': [200]}
    summary = []
    names = []

    def __init__(self, name, donation=None):
        self.name=name
        self.donations = donation

    def add_donor(name, donation=None):
        Donor.donors.update({name:[donation]})

    @classmethod
    def donor_names(cls):
        for donor in Donor.donors:
            Donor.names.append(donor)

    def donor_info(cls):
        return 'Donor: {}'.format(cls.name)


    def donor_sum(cls):
        for donor in Donor.donors:
            Donor.summary.append(sum(Donor.donors[donor]))
        #    donor_summary.append([donor](summary))

