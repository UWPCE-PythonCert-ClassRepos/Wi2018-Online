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
            assert content == "1\n"

    def test_render_html(self):
        """Test that render renders html tag."""
        e = hr.Html("1")
        with open("outfile.html", "w") as outfile:
            e.render(outfile, cur_ind="")
        with open("outfile.html", "r") as infile:
            content = infile.read()
            assert content == "<html>\n1\n</html>\n"

    def test_render_body(self):
        """Test that render renders body tag."""
        e = hr.Body("1")
        e.append("2")
        with open("outfile.html", "w") as outfile:
            e.render(outfile, cur_ind="")
        with open("outfile.html", "r") as infile:
            content = infile.read()
            assert content == "<body>\n1\n2\n</body>\n"

    def test_render_p(self):
        """Test that render renders p tag."""
        e = hr.P("1")
        e.append("2")
        with open("outfile.html", "w") as outfile:
            e.render(outfile, cur_ind="")
        with open("outfile.html", "r") as infile:
            content = infile.read()
            assert content == "<p>\n1\n2\n</p>\n"

    def test_render_body_2(self):
        """Test that render renders paragraph appended inside body."""
        e = hr.Body("1")
        e.append(hr.P("2"))
        with open("outfile.html", "w") as outfile:
            e.render(outfile, cur_ind="")
        with open("outfile.html", "r") as infile:
            content = infile.read()
            assert content == """<body>
1
<p>
2
</p>
</body>
"""

    def test_render_head(self):
        """Test that render renders head tag."""
        e = hr.Head("1")
        e.append("2")
        with open("outfile.html", "w") as outfile:
            e.render(outfile, cur_ind="")
        with open("outfile.html", "r") as infile:
            content = infile.read()
            assert content == "<head>\n1\n2\n</head>\n"

    def test_title(self):
        """Test that renders single line title."""
        e = hr.Title("1")
        e.append("2")
        with open("outfile.html", "w") as outfile:
            e.render(outfile, cur_ind="")
        with open("outfile.html", "r") as infile:
            content = infile.read()
            assert content == "<title> 12 </title>\n"

    def test_attributes(self):
        """Test that renders title with extended attributes."""
        body = hr.Body()
        body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                         "but this is enough  to show that we can do some text",
                         style="text-align: center; font-style: oblique;"))
        with open("outfile3.html", "w") as outfile:
            body.render(outfile, cur_ind="")
        with open("outfile3.html", "r") as infile:
            content = infile.read()
            assert content == '''<body>
<p style="text-align: center; font-style: oblique;">
Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
</p>
</body>
'''


if __name__ == '__main__':
    unittest.main()
