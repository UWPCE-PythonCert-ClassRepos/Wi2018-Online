#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)

# This is the framework for the base class
class Element(object):
    tag_start = '<html>'
    tag_end = '</html>'

    def __init__(self, content=None):
        self.content = content
        if self.content is None:
            self.content = ''

    def append(self, new_content):
        self.new_content = new_content
        self.content = self.content + ' ' + self.new_content

    def render(self, file_out, cur_ind=""):

        element_render = self.tag_start + '\n' + cur_ind + self.content + '\n' + self.tag_end

        file_out.write(element_render)

class Html(Element):
    """ html class"""
    tag_start = '<html>'
    tag_end = '</html>'

class Body(Element):
    """ body class"""
    tag_start = '<body>'
    tag_end = '</body>'
    def __init__(self, content = None):
        self.content = content
        if self.content is None:
            self.content = ''

class P(Element):
    """ body class"""
    tag_start = '<p>'
    tag_end = '</p>'
    def __init__(self, content = None):
        self.content = content
        if self.content is None:
            self.content = ''
    def append(self, new_content):
        if isinstance(self.content, Element):
            self.content.append(self.content)
        else:
            self.content.append(TextWrapper(self.content))
