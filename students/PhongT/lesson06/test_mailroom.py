"""
Lesson 06: Assignment Mailroom Unit test
- Unit test
"""

import mailroom as mr
import unittest
import os
import io
import fnmatch
from contextlib import redirect_stdout


class MailRoomUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        setUpClass is called only once for all tests. So
        it is good to put all common setup in this def
        """
        print('init all once ...\n')
        self.donors_data = mr.get_donor_data()

    def test_init(self):
        self.assertEqual(self.donors_data[0]['name'], 'Ken Lenning')
        self.assertEqual(self.donors_data[4]['name'], 'Ben Cormack')

    def test_print_report(self):
        """ test print list of your donors to console """
        out = io.StringIO()
        with redirect_stdout(out):
            mr.print_report()
        output = out.getvalue().strip()
        self.assertIn("--------------------------------------------------------------------", output)
        self.assertIn("Donor Name           | Total Given     | Num Gifts  | Average Gift", output)
        self.assertIn("Ken Lenning            $   18,882.74            3     $    6,294.25", output)
        self.assertIn("Lucy Nguyen            $    5,253.82            1     $    5,253.82", output)
        self.assertIn("Ben Cormack            $  157,788.05            3     $   52,596.02", output)
        out.close()

    def test_write_letters_to_file(self):
        """ test whether all thank you letter (files) are generated """
        # first delete all existing thank you files in current directory
        [os.remove(f) for f in os.listdir(".") if f.endswith(".rpt")]
        num_file = len(fnmatch.filter(os.listdir("."), '*.rpt'))
        self.assertEqual(num_file, 0)

        # write thank_you files to current dir
        mr.write_letters_to_file()

        # test valid file
        self.assertTrue(os.path.isfile('Ken_Lenning.rpt'))
        self.assertTrue(os.path.isfile('Thomas_Timmy.rpt'))
        self.assertTrue(os.path.isfile('Jane_Chung.rpt'))
        self.assertTrue(os.path.isfile('Lucy_Nguyen.rpt'))
        self.assertTrue(os.path.isfile('Ben_Cormack.rpt'))

        # test invalid file
        self.assertFalse(os.path.isfile('NO_WAY.rpt'))

    def test_find_existing_donor_id(self):
        """ test record id in db """
        self.assertEqual(mr.find_donor_id("KEN LeNniNG"), 0)
        self.assertEqual(mr.find_donor_id("kEn LENning"), 0)
        self.assertEqual(mr.find_donor_id("Thomas Timmy"), 1)
        self.assertEqual(mr.find_donor_id("jane chung"), 2)
        self.assertEqual(mr.find_donor_id("LucY NguyeN"), 3)
        self.assertEqual(mr.find_donor_id("BEN cormack"), 4)
        self.assertEqual(mr.find_donor_id("NEW NAME"), None)  # new entry record without record id

    def test_add_donor_to_db(self):
        # test Add an existing record to db
        donor = mr.add_donor_to_db("thomas timmy", 100.5, 1)
        self.assertEqual(len(self.donors_data), 5)
        self.assertEqual(donor['donations'][0], 521.3)
        self.assertEqual(donor['donations'][1], 869.14)
        self.assertEqual(donor['donations'][2], 100.5)

        # test Add a new record to db
        donor = mr.add_donor_to_db("new donor", 12.3, None)
        self.assertEqual(donor['donations'][0], 12.3)

    def test_get_thankyou_message(self):
        """ test if generated thank you message as expected """
        donor = self.donors_data[0]
        expected_message = '''Dear Ken Lenning, 
            Thank you so much for your generosity with your most recent donation of $16325.5. 
            It will be put to very good use.
            Sincerely.'''
        self.assertEqual(mr.get_thankyou_message(donor), expected_message)


if __name__ == '__main__':
    unittest.main()
