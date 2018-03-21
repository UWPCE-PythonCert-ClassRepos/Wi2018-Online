#!/usr/bin/env python

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    """Base element class."""

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        """content: str or objects subclassed from Element; kwargs: attrs."""
        if content is not None:
            self.content = [content]
        else:
            self.content = []

        # this will be used by the render method to render the opening tag
        self.attrs = self.kwargs_to_str(**kwargs)

    def append(self, new_content):
        """Add str or other objects to content."""
        self.content.append(new_content)

    def kwargs_to_str(self, **kwargs):
        """Convert kwargs to a string to be used in the render method."""
        a_list = []
        for k, v in zip(kwargs.keys(), kwargs.values()):
            a_list.append(k)
            a_list.append(v)
        return " ".join(['{}="{}"'] * len(kwargs)).format(*tuple(a_list))

    def render_opening_attr(self, file_out, cur_ind, no_attrs, do_attrs):
        """Render the opening tag with or w/o attributes."""
        # no_attrs, do_attrs: formatting templates
        if not self.attrs:
            file_out.write(no_attrs.format(cur_ind, self.tag))
        else:
            file_out.write(do_attrs.format(cur_ind, self.tag, self.attrs))

    def render(self, file_out, cur_ind="", closing_newline=True):
        """Write tags and content to a file-like object with a write method."""
        # opening tag with or w/out attributes -- followed by newline char "\n"
        no_attrs = "{}<{}>\n"
        do_attrs = "{}<{} {}>\n"
        self.render_opening_attr(file_out, cur_ind, no_attrs, do_attrs)

        # the content goes here -- followed by newline char "\n"
        for elem in self.content:
            try:
                elem.render(file_out, Element.indent + cur_ind)
            except AttributeError:
                file_out.write("{}{}\n".format(Element.indent + cur_ind, str(elem)))

        # closing tag ...
        file_out.write("{}</{}>".format(cur_ind, self.tag))

        # ... followed by newline char "\n" -- except in case of the html tag
        if closing_newline:
            file_out.write("\n")


class Html(Element):
    """Subclass Html from Element."""

    tag = "html"

    def render(self, file_out, cur_ind=""):
        """Write tags and content to a file-like object with a write method."""
        # write this at the head of the page, before the html element
        file_out.write("{}<!DOCTYPE html>\n".format(cur_ind))

        Element.render(self, file_out, cur_ind, closing_newline=False)


class Body(Element):
    """Subclass Body from Element."""

    tag = "body"


class P(Element):
    """Subclass P for paragraph from Element."""

    tag = "p"


class Head(Element):
    """Subclass Head from Element."""

    tag = "head"


class OneLineTag(Element):
    """Base class for one-line tags subclassed from Element."""

    tag = "title"

    def render(self, file_out, cur_ind=""):
        """Write tags and content to a file-like object with a write method."""
        # opening tag with or w/out attributes -- no "\n" at the end
        no_attrs = "{}<{}>"
        do_attrs = "{}<{} {}>"
        Element.render_opening_attr(self, file_out, cur_ind, no_attrs, do_attrs)

        # the content goes here -- there is NO "\n" at the end
        # also there is no indentation among arguments passed to format()
        for elem in self.content:
            try:
                elem.render(file_out, Element.indent + cur_ind)
            except AttributeError:
                file_out.write("{}".format(str(elem)))

        # closing tag -- followed by "\n"
        file_out.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    """Subclass Title from OneLineTag."""

    tag = "title"


class SelfClosingTag(Element):
    """Base class for self-closing tags subclassed from Element; no content."""

    tag = "hr"
    try:
        def __init__(self, **kwargs):
            self.attrs = self.kwargs_to_str(**kwargs)
    except TypeError:
        print("SelfClosingTag accepts no content")
        raise

    def append(self):
        """Raise TypeError on attempt to add content."""
        print("SelfClosingTag accepts no content")
        raise TypeError

    def render(self, file_out, cur_ind=""):
        """Render a self-closing tag w/ or w/o attributes."""
        # opening < and closing /> on one line, with optional attrs
        no_attrs = "{}<{} />\n"
        do_attrs = "{}<{} {} />\n"
        Element.render_opening_attr(self, file_out, cur_ind, no_attrs, do_attrs)


class Hr(SelfClosingTag):
    """Subclass Hr for horizontal ruler from SelfClosingTag."""

    tag = "hr"


class Br(SelfClosingTag):
    """Subclass Br for line break from SelfClosingTag."""

    tag = "br"


class A(OneLineTag):
    """A subclass for anchor (link)."""

    # The assignment asks for it to be a subclass of Element ...
    # ... but in my case it seemed to be easier to subclass from OneLineTag
    # ... because A is also a one-line-tag.
    # Otherwise I'd need to override Element.render ...
    # ... which writes tags and content on multiple lines.
    tag = "a"

    def __init__(self, link, content):
        """Accept link for an internet address; content for a str to show."""
        OneLineTag.__init__(self, content, href=link)


class Ul(Element):
    """Subclass Ul for unordered list from Element."""

    tag = "ul"


class Li(Element):
    """Subclass Li for list item from Element."""

    tag = "li"


class H(OneLineTag):
    """Subclass H for header from OneLineTag."""

    tag = "h"

    def __init__(self, level_num, content, **kwargs):
        """Accept int for the header level, str for content, and attributes."""
        self.tag = self.tag + str(level_num)
        OneLineTag.__init__(self, content, **kwargs)


class Meta(SelfClosingTag):
    """Subclass Meta from SelfClosingTag."""

    tag = "meta"
