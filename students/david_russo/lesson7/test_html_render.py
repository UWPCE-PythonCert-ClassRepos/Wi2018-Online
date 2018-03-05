#!/usr/bin/env python

import unittest
from io import StringIO
import html_render as hr

class html_render_TestCase(unittest.TestCase):
	
	def test_tag_is_html(self):
		elem = hr.Element()
		self.assertEqual(elem.tag, "html")

	def test_html_tag_is_html(self):
		elem = hr.Html()
		self.assertEqual(elem.tag, "html")

	def test_body_tag_is_body(self):
		elem = hr.Body()
		self.assertEqual(elem.tag, "body")

	def test_p_tag_is_p(self):
		elem = hr.P()
		self.assertEqual(elem.tag, "p")
	
	def test_title_tag_is_title(self):
		elem = hr.Title()
		self.assertEqual(elem.tag, "title")

if __name__ == '__main__':
    unittest.main()

		
