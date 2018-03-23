#!/usr/local/python3

import sys
import weakref

#Initial Donors List
#

donors = {'Aron': [100, 300, 100], 'Joan': [100, 50, 65, 100], 'Jean': [30, 150], 'Scott': [200]}

#Donor Class
class Donor(object):

    _instances = set()

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
        self.name = initial_data
        self.donations=kwargs
        self._instances.add(weakref.ref(self))

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

    @classmethod
    def donor_info(cls):
        return 'Donor: {}'.format(cls.names)

    @classmethod
    def donor_names(cls):
        names = []
        for donor in donors:
            names.append(donor)
            return names

    def __add__(self, object):
        return donor(self.donations + object.donations)

    @classmethod
    def donor_sum(cls):
        summary = []
        for donor in donors:
            summary.append(sum(donors[donor]))
        #    donor_summary.append([donor](summary))
        return summary
