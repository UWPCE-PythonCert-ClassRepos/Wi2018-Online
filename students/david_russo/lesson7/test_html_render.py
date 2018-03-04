#!/usr/bin/env python

import unittest
from io import StringIO
import html_render as hr

class html_render_TestCase(unittest.TestCase):
	
	def test_tag_is_html(self):
		elem = hr.Element()
		self.assertEqual(elem.tag, "html")
	
	def test_append(self):
		elem = hr.Element("this")
		elem.append("that")
		self.assertEqual(elem.content, ["this", "that"])

if __name__ == '__main__':
    unittest.main()

		
