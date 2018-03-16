#!/usr/bin/env python3

import unittest
from mailroom4 import user_selection, write_letters, send_email

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_user_selection(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = user_selection
        self.assert



if __name__ == '__main__':
    unittest.main()