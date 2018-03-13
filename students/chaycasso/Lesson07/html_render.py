#!/usr/bin/env python3
#
# HTML Render script
# Chay Casso
# 3/4/2018
# Renders a given set of text into pretty HTML.


class Element(object):

    indent = ""
    tag = ""

    def __init__(self, content=None):
        """Creates Element content value."""
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, append_text):
        self.content.append(append_text)

    def render(self, file_out="", cur_ind=" "):
        if self.tag: file_out.write("<" + self.tag + ">\n")
        for element in self.content:
            if element is str:
                file_out.write(cur_ind + element + "\n")
            else:
                file_out.write(cur_ind + element.render(file_out, cur_ind) + "\n")
        if self.tag: file_out.write("</" + self.tag + ">")
        return file_out


class Html(Element):

    tag = "html"

class Body(Element):

    tag = "body"

class P(Element):

    tag = "p"