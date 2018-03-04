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

	def __init__(self, content=None):
		self.content = []
		if content != None:
			self.content.append(content)

	def append(self, extra_content):
		self.content.append(extra_content)

	def render(self, file_out, cur_ind = ""):
		file_out.write('<{}>\n'.format(self.tag))
		for stuff in self.content:
			file_out.write(cur_ind + self.indentation + stuff + '\n')
		file_out.write('<\{}>'.format(self.tag))



class Html(Element):
	"""
	Subclass of Element class, specifically for elements of type 'HTML'
	"""
	tag = "html"

class Body(Element):
	"""
	Subclass of Element class, specifically for elements of type 'body'
	"""
	tag = "body"

class P(Element):
	"""
	Subclass of Element class, specifically for element of type 'p'
	"""
	tag = "p"




	
