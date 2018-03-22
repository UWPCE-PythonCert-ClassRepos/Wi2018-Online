class Donor(object):
    """class used to create single donor"""

    def __init__(self, name, donations=None):

        self._name = name
        if donations is None:
            self._donations = []
        else:
            self._donations = list(donations)

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    @property
    def last_donation(self):
        try:
            return self._donations[-1]
        except IndexError:
            return None

    @property
    def total_donations(self):
        return sum(self._donations)

    @property
    def avg_donation(self):
        return self.total_donations / len(self._donations)

    def donate(self, contribution):
        self._donations.append(float(contribution))