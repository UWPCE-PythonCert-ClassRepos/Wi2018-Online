#!/usr/bin/env python3
#
# HTML Render testing script
# Chay Casso
# 3/4/2018
# Testing a script that Renders a given set of text into pretty HTML.

import html_render as hr
import unittest

class htmltest(unittest.TestCase):

    def test_main_append(self):
        """Test that method has an append function that works."""
        e = hr.Element("1")
        e.append("2")
        assert e.content == ["1", "2"]

    def test_render(self):
        """Test that render method works."""
        e = hr.Element("1")
        with open("outfile.html", "w") as outfile:
            e.render(outfile, cur_ind="")
        with open("outfile.html", "r") as infile:
            content = infile.read()
            assert content == "<html>\n1\n</html>"

    def

if __name__ == '__main__':
    unittest.main()
