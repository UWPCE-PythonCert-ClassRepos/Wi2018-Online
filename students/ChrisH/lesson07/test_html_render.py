#!/usr/bin/env python3
# -----------------------------------------------------------
# test_html_render.py
#  uses unittest module to test html_render.py module
# -----------------------------------------------------------


import unittest
from io import StringIO
# from contextlib import redirect_stdout
import html_render as hr


class HtmlRenderTest(unittest.TestCase):

    @staticmethod
    def rendercap(element):
        f = StringIO()
        element.render(f, '')
        return f.getvalue()

    def test_element_init(self):                # default init
        page = hr.Element()
        self.assertEqual(page.content, [])

        page = hr.Element('test content')       # init with content
        self.assertEqual(page.content, ['test content'])

    def test_element_render(self):
        page = hr.Element()
        self.assertIn('<html>', self.rendercap(page))

        page = hr.Element('test content')
        self.assertIn('test content', self.rendercap(page))

    def test_element_append(self):
        page = hr.Element()
        page.append("Test append, text.")
        self.assertIn('Test append, text.', self.rendercap(page))

    def test_SelfClosingTag_init(self):
        el = hr.SelfClosingTag()
        self.assertIsNone(el.content)

    def test_SelfClosingTag_append(self):
        el = hr.SelfClosingTag()
        with self.assertRaises(TypeError):
            el.append('new content')

    def test_hr(self):
        hzr = hr.Hr()
        self.assertEqual(self.rendercap(hzr), '<hr />\n')

        hzr = hr.Hr('', style='text-align: center;')
        self.assertEqual(self.rendercap(hzr), '<hr style="text-align: center;" />\n')

    def test_br(self):
        br = hr.Br('', style='text-align: center;')
        self.assertEqual(self.rendercap(br), '<br style="text-align: center;" />\n')

    def test_A(self):
        a = hr.A('http://www.google.com', 'Google')

        self.assertEqual(self.rendercap(a), '<a href="http://www.google.com">Google</a>\n')

    def test_Ul_empty(self):
        ul = hr.Ul(id="TheList", style="line-height:200%")
        self.assertEqual(self.rendercap(ul), '<ul id="TheList" style="line-height:200%">\n</ul>\n')

    def test_Li_single(self):
        li = hr.Li("Single item", style="color: green")
        self.assertEqual(self.rendercap(li), '<li style="color: green">\n    Single item\n</li>\n')

    def test_Header(self):
        h = hr.H(6, "This is a header.")
        self.assertEqual(self.rendercap(h), '<h6>This is a header.</h6>\n')

    def test_doctype(self):
        h = hr.Html()
        self.assertIn('<!DOCTYPE html>', self.rendercap(h))

    def test_Meta_Class(self):
        mc = hr.Meta(charset="UTF-8")
        self.assertEqual(self.rendercap(mc), '<meta charset="UTF-8" />\n')

    def test_Body(self):
        b = hr.Body()
        self.assertEqual(self.rendercap(b), '<body>\n</body>\n')


if __name__ == "__main__":
    unittest.main()
