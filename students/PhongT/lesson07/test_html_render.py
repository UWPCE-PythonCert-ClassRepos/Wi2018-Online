"""
Lesson 07 Assignment: HTML render Unit test
"""
import unittest
import io
import html_render as html


class MyTestCase(unittest.TestCase):
    @staticmethod
    def render_element(element, cur_ind=""):
        out_io = io.StringIO()
        element.render(out_io, cur_ind=cur_ind)
        return out_io.getvalue()

    def test_html_tag(self):
        self.assertEqual(html.Element.tag, 'html')
        obj = html.Element('more text')
        self.assertEqual(obj.tag, 'html')

    def test_element_init(self):
        element = html.Element()
        self.assertEqual(element.content, [])
        element = html.Element('content')
        self.assertEqual(element.content, ['content'])

    def test_one_line_tag(self):
        title = html.Title('Title Text')
        outfile = io.StringIO()
        title.render(outfile)
        self.assertEqual(outfile.getvalue(), '<title>Title Text</title>')

    def test_meta_tag(self):
        head = html.Head()
        head.append(html.Meta(charset="UTF-8"))
        outfile = io.StringIO()
        head.render(outfile)
        output = outfile.getvalue().strip().split('\n')
        print(output)
        self.assertEqual(output[0].strip(), '<head>')
        self.assertEqual(output[1].strip(), '<meta charset="UTF-8" />')
        self.assertEqual(output[-1].strip(), '</head>')

    def test_body_tag(self):
        body = html.Body()
        self.assertTrue(body.tag, 'body')

    def test_body_content(self):
        body = html.Body()
        body.append(html.H(2, "PythonClass - Example"))
        content = MyTestCase.render_element(body)
        self.assertTrue(content.startswith('<body>'))
        self.assertIn('<h2>PythonClass - Example</h2>', content)
        self.assertTrue(content.endswith('</body>'))
        print(content)

    def test_header_tag(self):
        h1 = html.H(5, 'header text', style="bold")
        outfile = io.StringIO()
        h1.render(outfile)
        self.assertIn(outfile.getvalue(), '<h5 style="bold">header text</h5>')

    def test_attribute(self):
        p = html.P("Here is a sample text", style="text-align: left;")
        content = MyTestCase.render_element(p)
        print(content)
        self.assertTrue(content.startswith('<p style="text-align: left;">'))
        # assert results.startswith('<p style="text-align: left;">')


if __name__ == '__main__':
    unittest.main()
