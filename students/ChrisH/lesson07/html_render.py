#!/usr/bin/env python3
# -----------------------------------------------------------
# html_render.py
#  Render an html page in a 'pretty printed' way, indented
#  and human readable.
# -----------------------------------------------------------


class Element(object):
    """
    Base Class for elements in an HTML document.
    Init takes for content, either strings or other Element objects
    as well as a list of keyword arguments for HTML Element attributes.
    """

    tag = 'html'

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.indent = '    '
        self.attribs = kwargs

    def append(self, new_content):
        """
        Appends another string to the content.
        :return: None
        """
        self.content.append(new_content)

    def render(self, file_out, cur_ind=''):
        """
        Renders the tag and strings in the content.
        :param file_out: any open, writeable file-like object
        :param cur_ind: a string with the current indentation level
                        this is the amount that the element should already be indented
        :return: None
        """
        self.g_render(file_out, cur_ind,
                      cur_ind + '<' + self.tag,
                      '>\n',
                      cur_ind + '</' + self.tag + '>')

    def g_render(self, file_out, cur_ind, tag_start, tag_end, tag_close):

        file_out.write(tag_start)

        for k, v in self.attribs.items():
            file_out.write(f' {k}="{v}"')

        file_out.write(tag_end)

        if self.content:
            for item in self.content:
                try:
                    item.render(file_out, cur_ind + self.indent)
                except AttributeError:
                    file_out.write(cur_ind + self.indent + str(item))
                    if not issubclass(type(self), OneLineTag):          # Test for OneLineTag class type
                        file_out.write('\n')

        file_out.write(tag_close + '\n')


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=''):
        file_out.write(self.indent + '<!DOCTYPE html>\n')
        super().render(file_out, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    """
    Subclass of Element, overrides Element.render to print html text on one line.
    """
    def render(self, file_out, cur_ind=''):
        self.indent = ''                        # Reset indent for this type to prevent unnecessary spaces
        self.g_render(file_out,
                      '',
                      cur_ind + '<' + self.tag,
                      '>',
                      '</' + self.tag + '>')


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.content = None

    def render(self, file_out, cur_ind=''):
        self.g_render(file_out, cur_ind,
                      cur_ind + '<' + self.tag,
                      '',
                      ' />')

    def append(self, new_content):
        raise TypeError


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content):
        super(A, self).__init__(content, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, header_text):
        super().__init__(content=header_text)
        self.tag = 'h' + str(level)


class Meta(SelfClosingTag):
    tag = 'meta'
