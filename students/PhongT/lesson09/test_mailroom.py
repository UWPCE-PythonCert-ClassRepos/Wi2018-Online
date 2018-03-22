"""
Lesson 09 Assignment
Object Oriented Mailroom - Unit Test
"""

import unittest
import mailroom as mr
import os
import io
import fnmatch
from contextlib import redirect_stdout


class MyTestCase(unittest.TestCase):

    def test_donor_name(self):
        name = "Ted Inger"
        d = mr.Donor(name)
        self.assertEqual(d.name, name)
        self.assertEqual(d.donations, [])

    def test_add_donation(self):
        name = "Ted Inger"
        amount = 123.45
        d = mr.Donor(name)
        d.add_donation(amount)
        self.assertEqual(d.name, name)
        self.assertEqual(d.donations, [amount])
        self.assertEqual(d.latest_donation, amount)

    def test_add_donations(self):
        name1 = "Adam Lee"
        amt1 = 100
        d = mr.Donor(name1)
        d.add_donation(amt1)
        amt2 = 400
        d.add_donation(amt2)
        self.assertEqual(d.count_donations, 2)
        self.assertEqual(d.total_donations, 500)
        self.assertEqual(d.average_donations, 250)

    def test_add_donors(self):
        name1 = "Adam Lee"
        amt1 = 1.23
        d = mr.DonorDB()
        d.add_donor(name1, amt1)
        self.assertEqual(d.get_donor(name1).name, name1)
        self.assertEqual(d.donors_container[0].latest_donation, 1.23)

        name2 = "Henry Chung"
        amt2  = 123.456
        d.add_donor(name2, amt2)
        self.assertEqual(d.get_donor(name2).name, name2)
        self.assertEqual(d.donors_container[1].latest_donation, amt2)

    def test_print_donor_list(self):
        d = mr.DonorDB()
        name1 = "Adam Lee"
        amt1 = 1.23
        d = mr.DonorDB()
        d.add_donor(name1, amt1)

        name2 = "Henry Chung"
        amt2 = 123.456
        d.add_donor(name2, amt2)

        out = io.StringIO()
        with redirect_stdout(out):
            d.print_donor_list()
        output = out.getvalue().strip()
        self.assertIn("Below are the existing donors:", output)
        self.assertIn("-  Adam Lee   [1.23]", output)
        self.assertIn("-  Henry Chung   [123.456]", output)
        out.close()

    def test_get_thankyou_message(self):
        d = mr.DonorDB()
        name = "Adam Lee"
        amt = 1.23
        d = mr.DonorDB()
        d.add_donor(name, amt)
        expected_message = '''Dear Adam Lee, 
                Thank you so much for your generosity with your most recent donation of $1.23. 
                It will be put to very good use.
                Sincerely.'''
        self.assertEqual(d.get_thankyou_message(d.find_donor(name)), expected_message)

    def test_print_report(self):
        name = "Adam Lee"
        amt = 1.23
        d = mr.DonorDB()
        d.add_donor(name, amt)

        name2 = "Henry Chung"
        amt2 = 100.55
        d.add_donor(name2, amt2)

        out = io.StringIO()
        with redirect_stdout(out):
            d.print_report()
        output = out.getvalue().strip()
        self.assertIn("--------------------------------------------------------------------", output)
        self.assertIn("Donor Name           | Total Given     | Num Gifts  | Average Gift", output)
        self.assertIn("Adam Lee               $        1.23            1     $        1.23", output)
        self.assertIn("Henry Chung            $      100.55            1     $      100.55", output)
        out.close()

    def test_write_letters_to_file(self):
        name = "Adam Lee"
        amt = 1.23
        d = mr.DonorDB()
        d.add_donor(name, amt)

        name2 = "Henry Chung"
        amt2 = 100.55
        d.add_donor(name2, amt2)

        # first delete all existing thank you files in current directory
        [os.remove(f) for f in os.listdir(".") if f.endswith(".rpt")]
        num_file = len(fnmatch.filter(os.listdir("."), '*.rpt'))
        self.assertEqual(num_file, 0)

        # write thank_you letter files to current directory
        d.write_letters_to_file()

        # test thank_you letter files get generated
        self.assertTrue(os.path.isfile('Adam_Lee.rpt'))
        self.assertTrue(os.path.isfile('Henry_Chung.rpt'))
        num_file = len(fnmatch.filter(os.listdir("."), '*.rpt'))
        self.assertEqual(num_file, 2)


if __name__ == '__main__':
    unittest.main()
