import sys

#Donor Class
class iterDonor(type):
    def __iter__(cls):
        return iter(cls._allDonors)

class donor(metaclass=iterDonor):
    _allDonors = {}

    def __init__(self, name):
        self._allDonors.append(self)
        self.name = name

        def __init__(self, name):
            self.my_dict = {};

donorList = []
donorDetails = {}

class donorinfo:
    def __init__(self, object, objects):
        name=self.object
        money=self.objects
        #donorList.append(self.object)
        #donorDetails.append(self.objects)


class donor(object):
    def __init__(self, initial_list):
        for key in initial_list:
            setattr(self, key, initial_list[key])


donors = {'Aron': [10000,300, 100], 'Joan':[100, 50, 65], 'Jean':[30,150], 'Scott':[200]}

class DonorInfo2:

    donors = {'Aron': [10000, 300, 100], 'Joan': [100, 50, 65], 'Jean': [30, 150], 'Scott': [20]}

    def __init__(self, name, donations =[]):
        self.name = name
        self.donations = donations
        donors.update(self.name)




