"""
Lesson 07 Assignment
The goal is to create a set of classes to render html pages – in a
"pretty printed" way, i.e. nicely indented and human readable.
"""


class TextWrapper:
    """ simple wrapper that creates a class with a render method for simple text """
    def __init__(self, text):
        self.text = text

    def render(self, outfile, cur_ind=""):
        outfile.write(cur_ind + self.text)


class Element():
    tag = 'html'
    indent = 4 * ' '

    def __init__(self, content=None, **kwargs):

        self.content = []
        self.attributes = kwargs  # dictionary for all keyword args
        if content:
            self.content.append(content)

    def append(self, content):
        """ append content to the object """
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render(self, outfile, cur_ind=""):
        self.write_open_tag(outfile, cur_ind)
        outfile.write('\n')
        for item in self.content:
            try:
                item.render(outfile, cur_ind + self.indent)
                outfile.write("\n")
            except AttributeError:
                outfile.write(cur_ind + self.indent + str(item) + "\n")
        self.write_close_tag(outfile, cur_ind)

    def write_open_tag(self, outfile, cur_ind):
        """ open tag with optional attributes dictionary """
        outfile.write('{}<{}'.format(cur_ind, self.tag))
        if self.attributes != {}:
            for key, value in self.attributes.items():
                outfile.write(' {}="{}"'.format(key, value))
        outfile.write('>')

    def write_close_tag(self, outfile, cur_ind):
        """ close tag """
        outfile.write("{}</{}>".format(cur_ind, self.tag))  # html close tag


class Html(Element):
    """ Subclass of Element for the Html tag"""
    tag = 'html'


class Body(Element):
    """Subclass of Element for the Body tag"""
    tag = 'body'


class P(Element):
    """Subclass of Element for the Paragraph tag"""
    tag = 'p'


class Head(Element):
    """ Subclass of Element for the Head tag"""
    tag = 'head'


class OneLineTag(Element):
    """ Subclass of Element to override Element.render to write all on one line"""
    def render(self, outfile, cur_ind=""):
        self.write_open_tag(outfile, cur_ind)
        for item in self.content:
            outfile.write(str(item))
        outfile.write("</{}>".format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    """subclass of Element, to render tags like: <hr /> and <br />"""
    def render(self, outfile, cur_ind=""):
        # Render just a tag and any attributes, ignore contents
        self.write_open_tag(outfile, cur_ind)

    def write_open_tag(self, outfile, cur_ind):
        """ override write open tag with optional attributes dictionary """
        outfile.write('{}<{}'.format(cur_ind, self.tag))
        if self.attributes != {}:
            for key, value in self.attributes.items():
                outfile.write(' {}="{}"'.format(key, value))
        outfile.write(' /> ')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    """
    class for an anchor (link) element. Its constructor should look like:A(self, link, content)
    where link is the link, and content is what you see. It can be called like so:
    A("http://google.com", "link to google")
    """
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        self.kwargs = kwargs
        self.kwargs.update({'href': link})
        Element.__init__(self, content, **self.kwargs)


class Ul(Element):
    """Subclass of Element for the Un-order list tag"""
    tag = 'ul'


class Li(Element):
    """ Subclass of Element for the order list tag"""
    tag = 'li'


class H(OneLineTag):
    """
    A Header class – this one should take an integer argument
    for the header level. i.e <h1>, <h2>, <h3>,
    """
    tag = 'h'

    def __init__(self, h_level, content=None, **kwargs):
        # include h_level for different header levels eg <h2>
        self.tag = 'h' + str(h_level)
        Element.__init__(self, content, **kwargs)


class Meta(SelfClosingTag):
    """ subclass of SelfClosingTag for Metadata tag """
    tag = 'meta'

