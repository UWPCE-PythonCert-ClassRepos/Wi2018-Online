import unittest
import mailtest

class Testmail(unittest.TestCase):

    def test_report(self):
        mailtest.fmenureport


    def test_menu(self):
       mailtest.menuprint


    def test_thankmail(self):
        mailtest.thankmail

    def test_menuexit(self):
        mailtest.fmenu3


    def test_nodonation(self):
        mailtest.fask
        print("test 1 print the  report")
        print("test 2 print the menu")
        print("test 3 send thankyou mail")
        print("test 4 user enter no donation")
        print("test 5 menu exit")

if __name__ == '__main__':
    unittest.main()
