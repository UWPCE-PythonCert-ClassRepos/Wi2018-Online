class Element(object):
    """
    class for rendering an html element (xml element).

    attributes: tag, indent
    """
    # Class atributes
    tag = "html"
    indent = '    '

    def __init__(self, content=None, **kwargs):
        """initializer signature where content is expected to be a string – and defaults to Nothing"""
        if content == None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs


    def append(self, content):
        """Add more strings to the content"""
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        """Renders the tag and the strings in the content."""
        file_out.write("{}<{}>\n".format(cur_ind, self.tag))
        for con in self.content:
            if hasattr(con, 'render'):
                con.render(file_out, (cur_ind + self.indent))
            else:
                file_out.write((cur_ind + self.indent) + con + '\n')
        file_out.write("{}</{}>".format(cur_ind, self.tag))

    def __repr__(self):
        return '{self.__class__.__name__}{self.tag}{self.indent}'


class Html(Element):
    """Subclass of Element for html tag."""
    tag = "html"


class Body(Element):
    """Subclass of Element for body."""
    tag = "body"


class P(Element):
    """Subclass of Element for p tag."""
    tag = "p"


class Head(Element):
    """Subclass of Element for head tag."""
    tag = "head"


class OneLineTag(Element):
    """Override the render method, to render everything on one line."""

    def render(self, file_out, cur_ind=""):
        """Override the Element class render method so that
        everything is rendered on one line.
        """
        file_out.write('{}<{}>'.format(cur_ind, self.tag))
        for con in self.content:
            file_out.write(con)
        file_out.write('</{}>\n'.format(self.tag))


class Title(OneLineTag):
    """Subclass of OneLineTag class for the title."""
    tag = "title"


class SelfClosingTag(Element):
    """Sublcass for rendering a self closing tag such as <hr />."""
    def render(self, file_out, cur_ind=""):
        """Render self closing tags."""
        pass
