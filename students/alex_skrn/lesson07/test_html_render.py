"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes some sense for testing.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    element.render(outfile, ind)
    return outfile.getvalue()

########
# Step 1
########

def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    e = Element()

    e = Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Element("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    <\html>

#     More complex indentation should be tested later.
    """
    e = Element("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # break into lines to check indentation
    lines = file_contents.split('\n')
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[1].startswith(Element.indent + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")

# ########
# # Step 2
# ########


# # tests for the new tags
def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents


# #####################
# # indentation testing
# #####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_result(html, ind="   ")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith("   <")
    assert lines[-1].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * Element.indent + "<")

    assert lines[4].startswith(3 * Element.indent + "some")


########
# Step 3
########

# Add your tests here!

def test_head():
    """Test for a new tag <head>."""
    e = Head("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</head>")


def test_one_line_tag():
    """Test whether OneLineTag() can render two pieces of text on one line."""
    e = OneLineTag("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    lines = file_contents.split("\n")
    # make sure everything is on one line
    assert len(lines) == 1

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")


def test_title():
    """Test for a new tag <title>."""
    e = Title("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</title>")


########
# Step 4
########

# Test new functionality, i.e. keyword attributes, in all render methods
def test_kwargs_to_str():
    """Test that helper function used in the render method."""
    e = Element()
    args = {"id": 125, "style": "red %"}
    assert e.kwargs_to_str(**args) == 'id="125" style="red %"'
    assert e.kwargs_to_str(id="TheList") == 'id="TheList"'


def test_render_opening_tag_no_attr():
    """Test render_opening_attr() w/out attributes."""
    e = Element()

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


def test_render_opening_tag_do_attr():
    """Test render_opening_attr() with attributes."""
    e = Element(id="TheList")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the opening and closing tags are right.
    assert file_contents.startswith('<html id="TheList">')
    assert file_contents.endswith("</html>")


def test_render_element_attr():
    """Test whether the Element can take attributes."""
    e = Element("this is some text", id="TheList", style="line-height:200%")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # making sure the attributes got in there.
    assert('id="TheList"') in file_contents
    assert('style="line-height:200%"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html ")
    assert file_contents.endswith("</html>")


def test_render_element_attr_dict():
    """Test whether the Element can take a dict with attributes."""
    attrs = {"class": "intro"}
    e = Element("this is some text", **attrs)

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # making sure the attributes got in there.
    assert('<html class="intro"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html ")
    assert file_contents.endswith("</html>")


def test_render_html_attr():
    """Test whether the Html can take attributes."""
    e = Element("this is some text", lang="English")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # making sure the attribute got in there.
    assert('lang="English"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html ")
    assert file_contents.endswith("</html>")


def test_render_html_attr_dict():
    """Test whether the Html can take a dict with attributes."""
    attrs = {"class": "intro"}
    e = Element("this is some text", **attrs)

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # making sure the attributes got in there.
    assert('<html class="intro"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html ")
    assert file_contents.endswith("</html>")


def test_render_one_line_tag_attr():
    """Test whether the OneLineTag can take attributes."""
    e = OneLineTag("this is some text", id="TheList", style="line-height:200%")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # making sure the attributes got in there.
    assert('id="TheList"') in file_contents
    assert('style="line-height:200%"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<title ")
    assert file_contents.endswith("</title>")


def test_render_one_line_tag_attr_dict():
    """Test whether the OneLineTag can take a dict with attributes."""
    attrs = {"class": "intro"}
    e = OneLineTag("this is some text", **attrs)

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # making sure the attributes got in there.
    assert('<title class="intro"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<title ")
    assert file_contents.endswith("</title>")


def test_render_title_attr_dict():
    """Test whether the OneLineTag can take a dict with attributes."""
    # Also tests the render method
    attrs = {"class": "intro"}
    e = Title("this is some text", **attrs)

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # making sure the attributes got in there.
    assert('<title class="intro"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<title ")
    assert file_contents.endswith("</title>")


########
# Step 5
########
def test_self_closing_tag():
    """Test whether SelfClosingTag - on one line, attrs, no content."""
    # Test that it raises an exception if any content is passed to it
    with pytest.raises(TypeError):
        e = SelfClosingTag("this is some text", style="text-align:")
    with pytest.raises(TypeError):
        e = SelfClosingTag()
        e.append("and this is some more text")

    e = SelfClosingTag(style="height:30px")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    lines = file_contents.split("\n")
    # make sure everything is on one line
    assert len(lines) == 1

    # making sure the attributes got in there.
    assert('style="height:30px"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<hr ")
    assert file_contents.endswith("/>")

def test_hr_tag():
    """Test hr tag - on one line, attrs, no content."""
    # Test that it raises an exception if any content is passed to it
    with pytest.raises(TypeError):
        e = Hr("this is some text")
    with pytest.raises(TypeError):
        e = Hr()
        e.append("and this is some more text")

    e = Hr(style="height:30px")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    lines = file_contents.split("\n")
    # make sure everything is on one line
    assert len(lines) == 1

    # making sure the attributes got in there.
    assert('style="height:30px"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<hr ")
    assert file_contents.endswith(" />")


def test_br_tag():
    """Test br tag - on one line, attrs, no content."""
    # Test that it raises an exception if any content is passed to it
    with pytest.raises(TypeError):
        e = Br("this is some text")
    with pytest.raises(TypeError):
        e = Br()
        e.append("and this is some more text")

    e = Br(style="height:30px")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    lines = file_contents.split("\n")
    # make sure everything is on one line
    assert len(lines) == 1

    # making sure the attributes got in there.
    assert('style="height:30px"') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<br ")
    assert file_contents.endswith(" />")

########
# Step 6
########
def test_a_link():
    """Test A class for links."""
    e = A("https://www.google.com", "link to google")
    file_contents = render_result(e).strip()
    assert file_contents == '<a href="https://www.google.com">link to google</a>'

def test_a_link_2():
    """Test A class for links in a wider context."""
    parag = P("This is the")
    parag.append(A("https://www.google.com", "link to google"))
    file_contents = render_result(parag).strip()

    # making sure the tag with its attributes got in there.
    assert('<a href="https://www.google.com">link to google</a>') in file_contents

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


########
# Step 7
########
def test_ul():
    """Test unordered list class."""
    e = Ul(id="TheList", style="line-height:200%")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    file_contents = render_result(e).strip()

    assert file_contents.startswith("<ul ")
    assert file_contents.endswith("</ul>")

    # making sure the attributes got in there.
    assert('id="TheList"') in file_contents
    assert('style="line-height:200%"') in file_contents


def test_li():
    """Test list item class."""
    e = Li("One list item", style="color: blue")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("One list item") in file_contents

    assert file_contents.startswith("<li ")
    assert file_contents.endswith("</li>")

    # making sure the attributes got in there.
    assert('style="color: blue"') in file_contents


def test_header():
    """Test header class."""
    e = H(2, "The header text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    file_contents = render_result(e).strip()

    lines = file_contents.split("\n")
    # make sure everything is on one line
    assert len(lines) == 1

    # making sure the content got in there.
    assert("The header text") in file_contents

    assert file_contents.startswith("<h2>")
    assert file_contents.endswith("</h2>")


def test_header_attr():
    """Can header take attributes?."""
    e = H(2, "The header text", style="color: blue")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    file_contents = render_result(e).strip()

    lines = file_contents.split("\n")
    # make sure everything is on one line
    assert len(lines) == 1

    # making sure the content got in there.
    assert("The header text") in file_contents

    assert file_contents.startswith("<h2 ")
    assert file_contents.endswith("</h2>")

    # making sure the attributes got in there.
    assert('style="color: blue"') in file_contents


########
# Step 8
########
def test_html_doctype():
    """Test if Doctype html is at the head of the page."""
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert file_contents.startswith("<!DOCTYPE html>\n")


def test_meta():
        """Test meta charset tag - on one line, attrs, no content."""
        e = Meta(charset="UTF-8")

        # This uses the render_results utility above
        file_contents = render_result(e).strip()

        lines = file_contents.split("\n")
        # make sure everything is on one line
        assert len(lines) == 1

        # making sure the attributes got in there.
        assert('charset="UTF-8"') in file_contents

        # making sure the opening and closing tags are right.
        assert file_contents.startswith("<meta ")
        assert file_contents.endswith("/>")
