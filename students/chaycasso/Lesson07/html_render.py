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
            for key in self.kwarg_dict:
                print(key, self.kwarg_dict[key])
                file_out.write(key + '="' + self.kwarg_dict[key] + '"')
            file_out.write(">\n")
        elif self.tag:
            file_out.write("<" + self.tag + ">\n")
        for element in self.content:
            try:
                element.render(file_out, "")
            except AttributeError:
                file_out.write(cur_ind + str(element) + "\n")
        if self.tag: file_out.write("</" + self.tag + ">\n")
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
    def render(self, file_out, cur_ind=""):
        if self.tag: file_out.write("<" + self.tag + "> ")
        for element in self.content:
            try:
                element.render(file_out, "")
            except AttributeError:
                file_out.write(cur_ind + str(element))
        if self.tag: file_out.write(" </" + self.tag + ">\n")
        return file_out


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    tag = ""

    def render(self, file_out, cur_ind=""):
        if self.tag: file_out.write("<" + self.tag + " />\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"