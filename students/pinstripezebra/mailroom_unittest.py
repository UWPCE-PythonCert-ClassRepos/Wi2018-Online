# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:54:52 2018

@author: seelc
"""

import mailroomP3
import unittest
import os
import datetime

class mailroomTest(unittest.TestCase):
    
    #Runs before each test, gives access to donationHistory
    def setup(self):
        donationHistory = mailroomP3.donationHistory
        
    def tearDown(self):
        self.doationHistory = None
        
    #Tests report function     
    def test_printReport(self):
        donationHistory = mailroomP3.donationHistory
        report = mailroomP3.printReport(donationHistory)
        assert report == list(donationHistory.keys())
    
    #Tests thankYou function with new and existing names
    def test_thankYou(self):
        print("thank you")
        
        #Testing with an existing name
        assert mailroomP3.thankYou("Jeff Bezos", 1000)["Jeff Bezos"] == [10432, 3]
        
        #Testing with a new name
        assert mailroomP3.thankYou("Obama", 1000)["Obama"] == [1000, 1]
        assert mailroomP3.thankYou("Obama", 1000)["Obama"] == [2000, 2]
       
       
    #Tests the thankYou function with invalid donation amounts, checks for
    #Errors being thrown    
    def test_Donation_Amount(self):
        #Testing assertions with existing name
        assert mailroomP3.thankYou("Elon Musk", -100) == mailroomP3.thankYou("Elon Musk", 0)
        assert mailroomP3.thankYou("Elon Musk", "asdfs") == mailroomP3.thankYou("Elon Musk", 0)
        
        #Testing assertions with new name
        assert mailroomP3.thankYou("Joe Dirt", -100) == mailroomP3.thankYou("Joe Dirt", 0)
        assert mailroomP3.thankYou("Trump", "asdf")== mailroomP3.thankYou("Trump", "asdf")
        
    
    #Running groupThanks and checkinbg that all the files supposed to
    #be generated actually exist in the directory    
    def test_groupThanks(self):
        donationHistory = mailroomP3.donationHistory
        mailroomP3.groupThanks(donationHistory)
        names = list(donationHistory.keys())
        for i in range(len(names)):
            dateSent = str(datetime.date.today())
            assert(os.path.isfile("{}_{}".format(names[i], dateSent)))
            
        
if __name__ == '__main__':
    unittest.main()