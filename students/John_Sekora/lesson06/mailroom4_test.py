from unittest import TestCase
from mailroom4 import *


class TestMailroom4(TestCase):

    def test_data(self):
        self.assertEqual(data, {'John Smith': [400],
                                'Bill Wilmer': [8000, 10000, 3000],
                                'George Guy': [50],
                                'Elizabeth Jones': [2000, 1000, 2000],
                                'Nathan Star': [250.50, 100]})


if __name__ == 'main':
    TestCase()






