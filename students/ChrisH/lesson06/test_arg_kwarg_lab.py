#!/usr/bin/env python3
# -----------------------------------------------------------
# test_arg_kwarg_lab.py
#  uses unittest module to test arg_kwarg_lab.py program
# -----------------------------------------------------------

import unittest

from arg_kwarg_lab import func, newfunc


class ArgKwargTest(unittest.TestCase):

    # Default values for arguments:
    # (fore_color='black', back_color='white', link_color='green', visited_color='gray')

    def test_func(self):

        self.assertEqual(
            func(),
            ('black', 'white', 'green', 'gray')
        )

        self.assertEqual(
            func('red', 'blue', 'yellow', 'chartreuse'),
            ('red', 'blue', 'yellow', 'chartreuse')
        )

        self.assertEqual(
            func(link_color='red', back_color='blue'),
            ('black', 'blue', 'red', 'gray')
        )

        self.assertEqual(
            func('purple', link_color='red', back_color='blue'),
            ('purple', 'blue', 'red', 'gray')
        )

        regular = ('red', 'blue')
        links = {'link_color': 'chartreuse'}
        self.assertEqual(
            func(*regular, **links),
            ('red', 'blue', 'chartreuse', 'gray')
        )

    def test_newfunc(self):

        # Test default, no args given
        self.assertEqual(
            newfunc(),
            ('black', 'white', 'green', 'gray')
        )

        # Test that function raises a TypeError (fore_color already assigned by positional arg)
        with self.assertRaises(TypeError):
            newfunc('green', 'yellow', link_color='red', fore_color='blue')

        self.assertEqual(
            newfunc('green', 'yellow', link_color='red', visited_color='blue', ima_camel='NoPe'),
            ('green', 'yellow', 'red', 'blue')
        )


if __name__ == "__main__":
    unittest.main()
