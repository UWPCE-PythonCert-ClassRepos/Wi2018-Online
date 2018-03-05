#!/usr/bin/env python

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

class Element():
	tag = "html"
	indentation = 4 * " "

	def __init__(self, content=None, **kwargs):
		self.content = []
		self.attributes = kwargs
		if content != None:
			self.content.append(content)

	def append(self, extra_content):
		if hasattr(extra_content, 'render'):
			self.content.append(extra_content)
		else:
			self.content.append(TextWrapper(str(extra_content)))

	def render(self, file_out, cur_ind = ""):
		file_out.write("{}<{}".format(cur_ind, self.tag))

		for key, value in self.attributes.items():
			file_out.write(' {}="{}"'.format(key, value))

		file_out.write(">\n")

		cur_ind = cur_ind + self.indentation

		for stuff in self.content:
			try:
				stuff.render(file_out, cur_ind + self.indentation)
				file_out.write("\n")
			except AttributeError:
			    file_out.write(cur_ind + self.indentation + stuff)
			    file_out.write("\n")
		file_out.write("</{}>".format(self.tag))



class Html(Element):
	"""
	Subclass of Element class, specifically for elements of type 'HTML'
	"""
	tag = "html"

	def render(self, file_out, cur_ind = ""):
		file_out.write("<!DOCTYPE {}>\n".format(self.tag))
		Element.render(self, file_out, cur_ind = "")


class Body(Element):
	"""
	Subclass of Element class, specifically for elements of type 'body'
	"""
	tag = "body"

class P(Element):
	"""
	Subclass of Element class, specifically for elements of type 'p'
	"""
	tag = "p"

class Head(Element):
	"""
	Subclass of Element class, specifically for elements of type 'head'
	"""
	tag = "head"

class OneLineTag(Element):
	"""
	Subclass of Element class, specifically for elements of type 'one line'
	"""
	def render(self, file_out, cur_ind = ""):
		file_out.write("<{}> ".format(self.tag))

		for stuff in self.content:
			file_out.write(str(stuff))

		file_out.write("</{}>".format(self.tag))

class Title(OneLineTag):
	"""
	Subclass of OneLineTag class, specifically for elements of type title
	"""
	tag = "title"

class SelfClosingTag(Element):
	"""
	Subclass of Element class, with a render method just for the tag and attributes
	"""
	def render(self, file_out, cur_ind = ""):

		file_out.write("<{}".format(self.tag))

		for key, value in self.attributes.items():
			file_out.write(' {}="{}"'.format(key, value))

		file_out.write(" />")

class Hr(SelfClosingTag):
	"""
	Subclass of SelfClosingTag specifically for horizontal rules
	"""
	tag = "hr"

class Br(SelfClosingTag):
	"""
	Subclass of SelfClosingTag specifically for line breaks
	"""
	tag = "br"

class A(Element):
	"""
	A is an anchor link, which is  a subclass of Element
	"""
	tag = "a"
	def __init__(self, link, content = None, **kwargs):
		kwargs["href"] = link
		Element.__init__(self, content = content, **kwargs)

class Ul(Element):
	"""
	Subclass of class element, specifically for elements of type "un-ordered list"
	"""
	tag = "ul"

class Li(Element):
	"""
	Subclass of class Element, specifically for elements of type "list"
	"""
	tag = "li"

class H(OneLineTag):
	"""
	Subclass of OneLineTag class
	"""
	def __init__(self, level, content = None, **kwargs):
		self.tag = "h" + str(level)
		Element.__init__(self, content, **kwargs)

class Meta(SelfClosingTag):
	"""
	Subclass of class SelfClosingTag, designed to insert metadata into the html header
	"""
	tag = "meta"












	
