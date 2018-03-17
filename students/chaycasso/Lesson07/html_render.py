#!/usr/bin/env python3
#
# HTML Render script
# Chay Casso
# 3/4/2018
# Renders a given set of text into pretty HTML.


class Element(object):

    indent = ""
    tag = ""

    def __init__(self, content=None, **kwargs):
        """Creates Element content value."""
        if content is None:
            self.content = []
        else:
            if isinstance(content, SelfClosingTag): raise TypeError
            self.content = [content]
        self.kwarg_dict = kwargs

    def append(self, append_text):
        self.content.append(append_text)

    def render(self, file_out, cur_ind=""):
        if self.kwarg_dict:
            file_out.write("<" + self.tag + " ")
            kwarg_string = ""
            for key in self.kwarg_dict:
                kwarg_string += (key + '="' + self.kwarg_dict[key] + '"' + ", ")
            kwarg_string = kwarg_string[:-2]
            file_out.write(kwarg_string)
            file_out.write(">\n")

        # If this is a member of SelfClosingTag, we want only limited functionality.
        elif isinstance(self, SelfClosingTag):
            if self.tag: file_out.write("<" + self.tag + " />\n")
            return file_out
        # If this is a member of OneLineTag, we don't want any carriage returns.
        elif isinstance(self, OneLineTag):
            file_out.write("<" + self.tag + "> ")
        elif self.tag:
            file_out.write("<" + self.tag + ">\n")

        for element in self.content:
            try:
                element.render(file_out, "")
            except AttributeError:
                if isinstance(self, OneLineTag):
                    file_out.write(cur_ind + str(element))
                else:
                    file_out.write(cur_ind + str(element) + "\n")

        if isinstance(self, OneLineTag):
            file_out.write(" </" + self.tag + ">\n")
        elif self.tag:
            file_out.write("</" + self.tag + ">\n")
        return file_out


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    tag = ""


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    tag = ""


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(Element):
    """add hyperlink"""
    tag = "a"

    def __init__(self, link=None, content=None):
        super().__init__(content, **{"href": link})


class Ul(Element):
    """add unordered list"""
    tag="ul"


class Li(Element):
    """add list item"""
    tag="li"

class H(OneLineTag):
    """add header tag"""

    def __init__(self, level=1, content=None):
        self.tag = "h" + str(level)
        super().__init__(content)