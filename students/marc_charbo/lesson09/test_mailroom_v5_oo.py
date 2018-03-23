from unittest import TestCase
import mailroom_v5_oo as mailroom
import donor as Donor
import donors_data as DonorData
from textwrap import dedent

class DonorTest(TestCase):
    def test_donor_name(self):
        donor = Donor.Donor('MoneyMan',[1000000000, 2000000000])
        self.assertEqual(donor.name, 'MoneyMan')

    def test_donor_total_donnation(self):
        donor = Donor.Donor('MoneyMan',[1000000000, 2000000000])
        self.assertEqual(donor.total_donations, 3000000000)

    def test_donor_avg_donnation(self):
        donnor = Donor.Donor('MoneyMan',[1000000000, 2000000000])
        self.assertEqual(donnor.avg_donation, 1500000000)

class DonorDataTest(TestCase):
    def test_donor_letter(self):
        donor_set = DonorData.DonorData([Donor.Donor('MoneyMan', [25.00, 150.00, 2000.00, 100000.00])])
        donor_set.save_letters()
        with open('MoneyMan.txt', 'r') as myfile:
            letter_txt = myfile.read()
        with open('MoneyMan_test.txt', 'r') as myfile:
            letter_test = myfile.read()

        self.assertEqual(letter_txt, letter_test)


